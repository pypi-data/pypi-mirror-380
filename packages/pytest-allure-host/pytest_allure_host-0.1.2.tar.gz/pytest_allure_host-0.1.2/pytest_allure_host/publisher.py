"""Report publishing primitives (generate, upload, atomic latest swap).

Responsible for:
  * Generating Allure report (pulling prior history first)
  * Uploading run report to S3 (run prefix) + atomic promotion to latest/
  * Writing manifest (runs/index.json) + human HTML index + trend viewer
  * Retention (max_keep_runs) + directory placeholder objects
    * Extracting metadata keys from runs

The trend viewer (runs/trend.html) is a small dependency‑free canvas page
visualising passed / failed / broken counts across historical runs using
Allure's history-trend.json.
"""

from __future__ import annotations

import json
import shutil
import subprocess  # nosec B404
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from time import time

import boto3
from botocore.exceptions import ClientError

from .utils import (
    PublishConfig,
    branch_root,
    cache_control_for_key,
    compute_dir_size,
    guess_content_type,
    merge_manifest,
)

# --------------------------------------------------------------------------------------
# Paths helper
# --------------------------------------------------------------------------------------


@dataclass
class Paths:
    """Filesystem layout helper.

    Backwards compatibility: tests (and prior API) may pass explicit
    'report=' and 'results=' paths. If omitted we derive them from base.
    """

    base: Path = Path(".")
    report: Path | None = None
    results: Path | None = None

    def __post_init__(self) -> None:  # derive defaults if not provided
        if self.results is None:
            self.results = self.base / "allure-results"
        if self.report is None:
            self.report = self.base / "allure-report"


def _discover_meta_keys(runs: list[dict]) -> list[str]:
    """Return sorted list of dynamic metadata keys across runs."""
    core_cols = {
        "run_id",
        "time",
        "size",
        "project",
        "branch",
        "passed",
        "failed",
        "broken",
        "context_url",
    }
    keys: list[str] = []
    for r in runs:
        for k in r.keys():
            if k in core_cols or k.endswith("_url"):
                continue
            if k not in keys:
                keys.append(k)
    keys.sort()
    return keys


def _format_meta_cell(val) -> str:
    if val is None:
        return "<td>-</td>"
    esc = str(val).replace("<", "&lt;").replace(">", "&gt;")
    return f"<td>{esc}</td>"


def _s3(cfg: PublishConfig):  # allow custom endpoint (tests / local)
    endpoint = getattr(cfg, "s3_endpoint", None)
    if endpoint:
        return boto3.client("s3", endpoint_url=endpoint)
    return boto3.client("s3")


def list_keys(
    bucket: str,
    prefix: str,
    endpoint: str | None = None,
) -> Iterable[str]:
    s3 = boto3.client("s3", endpoint_url=endpoint) if endpoint else boto3.client("s3")
    paginator = s3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        for obj in page.get("Contents", []) or []:
            key = obj.get("Key")
            if key:
                yield key


def delete_prefix(
    bucket: str,
    prefix: str,
    endpoint: str | None = None,
) -> None:
    keys = list(list_keys(bucket, prefix, endpoint))
    if not keys:
        return
    s3 = boto3.client("s3", endpoint_url=endpoint) if endpoint else boto3.client("s3")
    # Batch delete 1000 at a time
    for i in range(0, len(keys), 1000):
        # Ruff style: remove spaces inside slice
        batch = keys[i : i + 1000]
        if not batch:
            continue
        s3.delete_objects(
            Bucket=bucket,
            Delete={"Objects": [{"Key": k} for k in batch], "Quiet": True},
        )


# --------------------------------------------------------------------------------------
# Report generation & history preservation
# --------------------------------------------------------------------------------------


def pull_history(cfg: PublishConfig, paths: Paths) -> None:
    """Download previous latest/history/ to seed new history for trends."""
    s3 = _s3(cfg)
    root = branch_root(cfg.prefix, cfg.project, cfg.branch)
    history_prefix = f"{root}/latest/history/"
    local_history = paths.results / "history"
    if local_history.exists():
        shutil.rmtree(local_history)
    local_history.mkdir(parents=True, exist_ok=True)

    # List objects and download those under history/
    try:
        for key in list_keys(cfg.bucket, history_prefix):
            rel = key[len(history_prefix) :]
            if not rel:  # skip directory placeholder
                continue
            dest = local_history / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            s3.download_file(cfg.bucket, key, str(dest))
    except ClientError:
        # best‑effort; history absence is fine
        pass


def ensure_allure_cli() -> None:
    """Ensure the allure binary is discoverable; raise if not."""
    path = shutil.which("allure")
    if not path:
        raise RuntimeError("Allure CLI not found in PATH (install allure-commandline)")


def generate_report(paths: Paths) -> None:
    if not paths.results.exists() or not any(paths.results.iterdir()):
        raise RuntimeError("allure-results is missing or empty")
    if paths.report.exists():
        shutil.rmtree(paths.report)
    ensure_allure_cli()
    allure_path = shutil.which("allure")
    if not allure_path:  # defensive
        raise RuntimeError("Allure CLI unexpectedly missing")
    # Validate discovered binary path before executing (Bandit B603 mitigation)
    exec_path = Path(allure_path).resolve()
    if not exec_path.is_file() or exec_path.name != "allure":  # pragma: no cover
        raise RuntimeError(
            f"Unexpected allure exec: {exec_path}"  # shorter for line length
        )
    # Safety: allure_path validated above; args are static & derived from
    # controlled paths (no user-provided injection surface).
    cmd = [
        allure_path,
        "generate",
        str(paths.results),
        "--clean",
        "-o",
        str(paths.report),
    ]
    try:
        # Security justification (S603/B603):
        #  * shell=False (no shell interpolation)
        #  * Executable path resolved & filename checked above
        #  * Arguments are constant literals + vetted filesystem paths
        #  * No user-controlled strings reach the command list
        #  * Capturing output allows safe error surfacing without exposing
        #    uncontrolled stderr directly to logs if later sanitized.
        subprocess.run(  # noqa: S603  # nosec B603 - validated binary
            cmd,
            check=True,
            capture_output=True,
            text=True,
        )
        # Optionally could log completed.stdout at debug level elsewhere.
    except subprocess.CalledProcessError as e:  # pragma: no cover - error path
        raise RuntimeError(
            "Allure report generation failed: exit code "
            f"{e.returncode}\nSTDOUT:\n{(e.stdout or '').strip()}\n"
            f"STDERR:\n{(e.stderr or '').strip()}"
        ) from e


# --------------------------------------------------------------------------------------
# Upload primitives
# --------------------------------------------------------------------------------------


def upload_dir(cfg: PublishConfig, root_dir: Path, key_prefix: str) -> None:
    s3 = _s3(cfg)
    for p in root_dir.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(root_dir).as_posix()
        key = f"{key_prefix}{rel}"
        extra: dict[str, str] = {"CacheControl": cache_control_for_key(key)}
        ctype = guess_content_type(p)
        if ctype:
            extra["ContentType"] = ctype
        if cfg.ttl_days is not None:
            extra["Tagging"] = f"ttl-days={cfg.ttl_days}"
        if cfg.sse:
            extra["ServerSideEncryption"] = cfg.sse
            if cfg.sse == "aws:kms" and cfg.sse_kms_key_id:
                extra["SSEKMSKeyId"] = cfg.sse_kms_key_id
        s3.upload_file(str(p), cfg.bucket, key, ExtraArgs=extra)


# --------------------------------------------------------------------------------------
# Two‑phase latest swap
# --------------------------------------------------------------------------------------


def two_phase_update_latest(cfg: PublishConfig, report_dir: Path) -> None:
    root = branch_root(cfg.prefix, cfg.project, cfg.branch)
    tmp_prefix = f"{root}/latest_tmp/"
    latest_prefix = f"{root}/latest/"

    # 1. Upload to tmp
    upload_dir(cfg, report_dir, tmp_prefix)
    # 2. Remove existing latest
    delete_prefix(cfg.bucket, latest_prefix, getattr(cfg, "s3_endpoint", None))
    # 3. Copy tmp → latest
    s3 = _s3(cfg)
    for key in list_keys(
        cfg.bucket,
        tmp_prefix,
        getattr(cfg, "s3_endpoint", None),
    ):
        rel = key[len(tmp_prefix) :]
        dest_key = f"{latest_prefix}{rel}"
        s3.copy({"Bucket": cfg.bucket, "Key": key}, cfg.bucket, dest_key)
    # 4. Validate & repair index if missing
    _validate_and_repair_latest(cfg, report_dir, latest_prefix)
    # 5. Write readiness marker + directory placeholder
    _write_latest_marker(cfg, latest_prefix)
    _ensure_directory_placeholder(cfg, report_dir / "index.html", latest_prefix)
    # 6. Delete tmp
    delete_prefix(cfg.bucket, tmp_prefix, getattr(cfg, "s3_endpoint", None))


def _validate_and_repair_latest(
    cfg: PublishConfig,
    report_dir: Path,
    latest_prefix: str,
) -> None:
    s3 = _s3(cfg)
    try:
        s3.head_object(Bucket=cfg.bucket, Key=f"{latest_prefix}index.html")
        return
    except ClientError:
        pass
    idx = report_dir / "index.html"
    if not idx.exists():
        return
    extra = {
        "CacheControl": cache_control_for_key(f"{latest_prefix}index.html"),
        "ContentType": guess_content_type(idx) or "text/html",
    }
    if cfg.ttl_days is not None:
        extra["Tagging"] = f"ttl-days={cfg.ttl_days}"
    s3.upload_file(
        str(idx),
        cfg.bucket,
        f"{latest_prefix}index.html",
        ExtraArgs=extra,
    )


def _write_latest_marker(cfg: PublishConfig, latest_prefix: str) -> None:
    _s3(cfg).put_object(
        Bucket=cfg.bucket,
        Key=f"{latest_prefix}LATEST_READY",
        Body=b"",
        CacheControl="no-cache",
        ContentType="text/plain",
    )


# --------------------------------------------------------------------------------------
# Manifest + HTML index + trend viewer
# --------------------------------------------------------------------------------------


def _extract_summary_counts(report_dir: Path) -> dict | None:
    summary = report_dir / "widgets" / "summary.json"
    if not summary.exists():
        return None
    try:
        data = json.loads(summary.read_text("utf-8"))
    except Exception:
        return None
    stats = data.get("statistic") or {}
    if not isinstance(stats, dict):  # corrupt
        return None
    return {k: stats.get(k) for k in ("passed", "failed", "broken") if k in stats}


def write_manifest(cfg: PublishConfig, paths: Paths) -> None:
    s3 = _s3(cfg)
    root = branch_root(cfg.prefix, cfg.project, cfg.branch)
    manifest_key = f"{root}/runs/index.json"

    existing = None
    try:
        body = s3.get_object(Bucket=cfg.bucket, Key=manifest_key)["Body"].read()
        existing = json.loads(body)
    except Exception:
        existing = None

    entry = {
        "run_id": cfg.run_id,
        "time": int(time()),
        "size": compute_dir_size(paths.report),
        "project": cfg.project,
        "branch": cfg.branch,
    }
    if getattr(cfg, "context_url", None):
        entry["context_url"] = cfg.context_url
    if cfg.metadata:
        for mk, mv in cfg.metadata.items():
            if mk not in entry:
                entry[mk] = mv
    counts = _extract_summary_counts(paths.report)
    if counts:
        entry.update(counts)
    manifest = merge_manifest(existing, entry)
    s3.put_object(
        Bucket=cfg.bucket,
        Key=manifest_key,
        Body=json.dumps(manifest, indent=2).encode("utf-8"),
        ContentType="application/json",
        CacheControl="no-cache",
    )

    latest_payload = {
        "run_id": cfg.run_id,
        "run_url": cfg.url_run(),
        "latest_url": cfg.url_latest(),
        "project": cfg.project,
        "branch": cfg.branch,
    }
    s3.put_object(
        Bucket=cfg.bucket,
        Key=f"{root}/latest.json",
        Body=json.dumps(latest_payload, indent=2).encode("utf-8"),
        ContentType="application/json",
        CacheControl="no-cache",
    )

    # runs/index.html
    index_html = _build_runs_index_html(manifest, latest_payload, cfg)
    s3.put_object(
        Bucket=cfg.bucket,
        Key=f"{root}/runs/index.html",
        Body=index_html,
        ContentType="text/html; charset=utf-8",
        CacheControl="no-cache",
    )

    # runs/trend.html
    trend_html = _build_trend_viewer_html(cfg)
    s3.put_object(
        Bucket=cfg.bucket,
        Key=f"{root}/runs/trend.html",
        Body=trend_html,
        ContentType="text/html; charset=utf-8",
        CacheControl="no-cache",
    )


def _format_epoch_utc(epoch: int) -> str:
    from datetime import datetime, timezone

    try:
        return datetime.fromtimestamp(epoch, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:  # pragma: no cover - defensive
        return "-"


def _format_bytes(n: int) -> str:
    step = 1024.0
    units = ["B", "KB", "MB", "GB", "TB"]
    v = float(n)
    for u in units:
        if v < step:
            return f"{v:.1f}{u}" if u != "B" else f"{int(v)}B"
        v /= step
    return f"{v:.1f}PB"


def _build_runs_index_html(
    manifest: dict,
    latest_payload: dict,
    cfg: PublishConfig,
    row_cap: int = 500,
) -> bytes:
    runs_list = manifest.get("runs", [])
    runs_sorted = sorted(
        runs_list,
        key=lambda r: r.get("time", 0),
        reverse=True,
    )
    # discover dynamic metadata keys (excluding core + *_url)
    meta_keys = _discover_meta_keys(runs_sorted)
    rows: list[str] = []
    for rinfo in runs_sorted[:row_cap]:
        rid = rinfo.get("run_id", "?")
        size = int(rinfo.get("size") or 0)
        t = int(rinfo.get("time") or 0)
        passed, failed, broken = (
            rinfo.get("passed"),
            rinfo.get("failed"),
            rinfo.get("broken"),
        )
        has_counts = any(v is not None for v in (passed, failed, broken))
        summary = f"{passed or 0}/{failed or 0}/{broken or 0}" if has_counts else "-"
        ctx_url = rinfo.get("context_url")
        ctx_cell = (
            f"<a href='{ctx_url}' target='_blank' rel='noopener'>link</a>" if ctx_url else "-"
        )
        meta_cells = "".join(_format_meta_cell(rinfo.get(mk)) for mk in meta_keys)
        row_html = (
            "\n<tr"
            f" data-passed='{passed or 0}'"
            f" data-failed='{failed or 0}'"
            f" data-broken='{broken or 0}'><td><code>"
            f"{rid}</code></td><td>{t}</td><td>{_format_epoch_utc(t)}</td>"
            f"<td title='{size}'>{_format_bytes(size)}</td><td>{summary}</td>"
            f"<td>{ctx_cell}</td>{meta_cells}"
            f"<td><a href='../{rid}/'>run</a></td>"
            "<td><a href='../latest/'>latest</a></td></tr>"
        )
        rows.append(row_html)
    # colspan accounts for base 8 columns + dynamic metadata count
    empty_cols = 8 + len(meta_keys)
    table_rows = (
        "\n".join(rows) if rows else f"<tr><td colspan='{empty_cols}'>No runs yet</td></tr>"
    )
    title = f"Allure Runs: {cfg.project} / {cfg.branch}"
    nav = (
        "<nav class='quick-links'><strong>Latest:</strong> "
        "<a href='../latest/'>root</a>"
        "<a href='../latest/#/graphs'>graphs</a>"
        "<a href='../latest/#/timeline'>timeline</a>"
        "<a href='../latest/history/history-trend.json'>history-json</a>"
        "<a href='trend.html'>trend-view</a>"
        "</nav>"
    )
    meta_header = "".join(f"<th class='sortable' data-col='meta:{k}'>{k}</th>" for k in meta_keys)
    parts: list[str] = [
        "<!doctype html><html><head><meta charset='utf-8'>",
        f"<title>{title}</title>",
        "<style>",
        "body{font-family:system-ui;margin:1.5rem;}",
        "table{border-collapse:collapse;width:100%;}",
        (
            "th,td{padding:.35rem .55rem;border-bottom:1px solid #ddd;"  # noqa: E501
            "font-size:14px;}"
        ),
        (
            "th{text-align:left;background:#f8f8f8;}"  # noqa: E501
            "tr:hover{background:#f5f5f5;}"
        ),
        "tbody tr:first-child{background:#fffbe6;}",
        "tbody tr:first-child code::before{content:'★ ';color:#d18f00;}",
        "code{background:#f2f2f2;padding:2px 4px;border-radius:3px;}",
        "footer{margin-top:1rem;font-size:12px;color:#666;}",
        (
            "a{color:#0366d6;text-decoration:none;}"  # noqa: E501
            "a:hover{text-decoration:underline;}"
        ),
        "nav.quick-links{margin:.25rem 0 1rem;font-size:14px;}",
        "nav.quick-links a{margin-right:.65rem;}",
        "</style></head><body>",
        f"<h1>{title}</h1>",
        (
            "<div id='controls' style='margin:.5rem 0 1rem;display:flex;"  # noqa: E501
            "gap:1rem;flex-wrap:wrap'>"  # noqa: E501
            "<label style='font-size:14px'>Search: <input id='run-filter'"  # noqa: E501
            " type='text' placeholder='substring (id, context, meta)'"  # noqa: E501
            " style='padding:4px 6px;font-size:14px;border:1px solid #ccc;"  # noqa: E501
            "border-radius:4px'></label>"  # noqa: E501
            "<label style='font-size:14px'>"  # noqa: E501
            "<input type='checkbox' id='only-failing' style='margin-right:4px'>"  # noqa: E501
            "Only failing</label>"  # noqa: E501
            "<span id='stats' style='font-size:12px;color:#666'></span></div>"  # noqa: E501
        ),
        nav,
        "<table id='runs-table'><thead><tr>",
        (
            "<th class='sortable' data-col='run_id'>Run ID</th>"
            "<th class='sortable' data-col='epoch'>Epoch</th>"
            "<th class='sortable' data-col='utc'>UTC Time</th>"
            "<th class='sortable' data-col='size'>Size</th>"
        ),
        (
            "<th class='sortable' data-col='pfb'>P/F/B</th>"
            "<th class='sortable' data-col='context'>Context</th>"
            f"{meta_header}<th>Run</th><th>Latest</th></tr></thead><tbody>"
        ),
        table_rows,
        "</tbody></table>",
        (
            f"<footer>Updated {latest_payload.get('run_id', '?')} • "
            f"{cfg.project}/{cfg.branch}</footer>"
        ),
        (
            "<script>"
            "(function(){"  # IIFE wrapper
            "const tbl=document.getElementById('runs-table');"
            "const filter=document.getElementById('run-filter');"
            "const stats=document.getElementById('stats');"
            "const onlyFail=document.getElementById('only-failing');"
            "function updateStats(){const total=tbl.tBodies[0].rows.length;"
            "const visible=[...tbl.tBodies[0].rows]"  # next line filters
            ".filter(r=>r.style.display!=='none').length;"
            "stats.textContent=visible+' / '+total+' shown';}"
            "function applyFilter(){const q=filter.value.toLowerCase();"
            "const onlyF=onlyFail.checked;"
            "[...tbl.tBodies[0].rows].forEach(r=>{"
            "const txt=r.textContent.toLowerCase();"
            "const hasTxt=!q||txt.indexOf(q)>-1;"
            "const failing=Number(r.getAttribute('data-failed')||'0')>0;"
            "r.style.display=(hasTxt&&(!onlyF||failing))?'':'none';});"
            "updateStats();}"
            "filter.addEventListener('input',applyFilter);"
            "onlyFail.addEventListener('change',applyFilter);"
            "let sortState=null;"
            "function extract(r,col){switch(col){"
            "case 'epoch':return r.cells[1].textContent;"
            "case 'size':return r.cells[3].getAttribute('title');"
            "case 'pfb':return r.cells[4].textContent;"
            "default:return r.textContent;}}"
            "function sortBy(col){const tbody=tbl.tBodies[0];"
            "const rows=[...tbody.rows];let dir=1;"
            "if(sortState&&sortState.col===col){dir=-sortState.dir;}"
            "sortState={col,dir};"
            "const numeric=(col==='epoch'||col==='size');"
            "rows.sort((r1,r2)=>{const a=extract(r1,col);"
            "const b=extract(r2,col);if(numeric){return (("
            "(Number(a)||0)-(Number(b)||0))*dir;}"
            "return a.localeCompare(b)*dir;});"
            "rows.forEach(r=>tbody.appendChild(r));}"
            "tbl.tHead.querySelectorAll('th.sortable')"  # split chain
            ".forEach(th=>{th.addEventListener('click',()=>sortBy(th.dataset.col));});"  # noqa: E501
            "updateStats();})();"
            "</script>"
        ),
        "</body></html>",
    ]
    return "".join(parts).encode("utf-8")


def _build_trend_viewer_html(cfg: PublishConfig) -> bytes:
    title = f"Run History Trend: {cfg.project} / {cfg.branch}"
    json_url = "../latest/history/history-trend.json"
    parts: list[str] = [
        "<!doctype html><html><head><meta charset='utf-8'>",
        f"<title>{title}</title>",
        "<style>",
        "body{font-family:system-ui;margin:1.25rem;}",
        "h1{margin-top:0;}",
        "#meta{font-size:12px;color:#666;margin-bottom:1rem;}",
        "canvas{max-width:100%;border:1px solid #ddd;background:#fff;}",
        "a{color:#0366d6;text-decoration:none;}",
        "a:hover{text-decoration:underline;}",
        "table{border-collapse:collapse;margin-top:1rem;font-size:12px;}",
        "th,td{padding:4px 6px;border:1px solid #ccc;}",
        (
            ".legend-swatch{display:inline-block;width:10px;height:10px;"
            "margin-right:4px;border-radius:2px;}"
        ),
        "</style></head><body>",
        f"<h1>{title}</h1>",
        (
            "<div id='meta'>Data source: <code>latest/history/history-"
            "trend.json</code> · <a href='index.html'>back to runs</a></div>"
        ),
        "<canvas id='trend' width='900' height='300'></canvas>",
        "<div id='legend'></div>",
        (
            "<table id='raw'><thead><tr><th>Label</th><th>Total</th><th>Passed"  # noqa: E501
            "</th><th>Failed</th><th>Broken</th><th>Skipped</th><th>Unknown"  # noqa: E501
            "</th></tr></thead><tbody></tbody></table>"
        ),
        "<script>\n(async function(){\n",
        f"  const resp = await fetch('{json_url}');\n",
        (
            "  if(!resp.ok){document.body.insertAdjacentHTML('beforeend',"  # noqa: E501
            "'<p style=\\'color:red\\'>Failed to fetch trend JSON ('+resp.status+')</p>');return;}\n"  # noqa: E501
        ),
        "  const data = await resp.json();\n",
        (
            "  if(!Array.isArray(data)){document.body.insertAdjacentHTML('beforeend',"  # noqa: E501
            "'<p>No trend data.</p>');return;}\n"  # noqa: E501
        ),
        # Sanitize & enrich: fallback label if reportName/buildOrder missing
        (
            "  const stats = data\n"
            "    .filter(d=>d&&typeof d==='object')\n"
            "    .map((d,i)=>{\n"
            "      const st = (d.statistic && typeof d.statistic==='object') ?"  # noqa: E501
            " d.statistic : {};\n"
            "      const lbl = d.reportName || d.buildOrder || st.name ||"  # noqa: E501
            " (i+1);\n"
            "      return {label: String(lbl), ...st};\n"
            "    });\n"
        ),
        (
            "  if(!stats.length){document.body.insertAdjacentHTML('beforeend','<p>No usable trend entries.</p>');return;}\n"  # noqa: E501
        ),
        "  const cvs=document.getElementById('trend');\n",
        "  const ctx=cvs.getContext('2d');\n",
        (
            "  const colors={passed:'#2e7d32',failed:'#d32f2f',broken:'#ff9800'};\n"  # noqa: E501
        ),
        "  const keys=['passed','failed','broken'];\n",
        (
            "  const max=Math.max(1,...stats.map(s=>Math.max(...keys.map(k=>s[k]||0))));\n"  # noqa: E501
        ),
        (
            "  const pad=30;const w=cvs.width-pad*2;const h=cvs.height-pad*2;\n"  # noqa: E501
        ),
        (
            "  ctx.clearRect(0,0,cvs.width,cvs.height);ctx.font='12px system-ui';ctx.strokeStyle='#999';ctx.beginPath();ctx.moveTo(pad,pad);ctx.lineTo(pad,pad+h);ctx.lineTo(pad+w,pad+h);ctx.stroke();\n"  # noqa: E501
        ),
        "  const stepX = stats.length>1 ? w/(stats.length-1) : 0;\n",
        "  function y(v){return pad + h - (v/max)*h;}\n",
        (
            "  keys.forEach(k=>{ctx.beginPath();ctx.strokeStyle=colors[k];stats.forEach((s,i)=>{const x=pad+i*stepX;const yy=y(s[k]||0);if(i===0)ctx.moveTo(x,yy);else ctx.lineTo(x,yy);});ctx.stroke();});\n"  # noqa: E501
        ),
        (
            "  stats.forEach((s,i)=>{const x=pad+i*stepX;keys.forEach(k=>{const v=s[k]||0;const yy=y(v);ctx.fillStyle=colors[k];ctx.beginPath();ctx.arc(x,yy,3,0,Math.PI*2);ctx.fill();});ctx.fillStyle='#222';ctx.fillText(String(s.label), x-10, pad+h+14);});\n"  # noqa: E501
        ),
        (
            "  const legend=document.getElementById('legend');legend.innerHTML=keys.map(k=>`<span class='legend-swatch' style='background:${colors[k]}'></span>${k}`).join(' &nbsp; ');\n"  # noqa: E501
        ),
        (
            "  const tbody=document.querySelector('#raw tbody');tbody.innerHTML=stats.map(s=>`<tr><td>${s.label}</td><td>${s.total||''}</td><td>${s.passed||''}</td><td>${s.failed||''}</td><td>${s.broken||''}</td><td>${s.skipped||''}</td><td>${s.unknown||''}</td></tr>`).join('');\n"  # noqa: E501
        ),
        "})();\n</script>",
        "</body></html>",
    ]
    return "".join(parts).encode("utf-8")


# --------------------------------------------------------------------------------------
# Retention cleanup & directory placeholder
# --------------------------------------------------------------------------------------


def cleanup_old_runs(cfg: PublishConfig, keep: int) -> None:
    if keep is None or keep <= 0:
        return
    s3 = _s3(cfg)
    root = branch_root(cfg.prefix, cfg.project, cfg.branch)
    # list immediate children (run prefixes)
    paginator = s3.get_paginator("list_objects_v2")
    run_prefixes: list[str] = []
    for page in paginator.paginate(
        Bucket=cfg.bucket,
        Prefix=f"{root}/",
        Delimiter="/",
    ):
        for cp in page.get("CommonPrefixes", []) or []:
            pfx = cp.get("Prefix")
            if not pfx:
                continue
            name = pfx.rsplit("/", 2)[-2]
            if name in {"latest", "runs"}:
                continue
            is_ts = len(name) == 15 and name[8] == "-" and name.replace("-", "").isdigit()
            if is_ts:
                run_prefixes.append(pfx)
    run_prefixes.sort(reverse=True)
    for old in run_prefixes[keep:]:
        delete_prefix(cfg.bucket, old, getattr(cfg, "s3_endpoint", None))


def _ensure_directory_placeholder(
    cfg: PublishConfig,
    index_file: Path,
    dir_prefix: str,
) -> None:
    if not index_file.exists() or not dir_prefix.endswith("/"):
        return
    body = index_file.read_bytes()
    extra = {"CacheControl": "no-cache", "ContentType": "text/html"}
    if cfg.ttl_days is not None:
        extra["Tagging"] = f"ttl-days={cfg.ttl_days}"
    try:
        _s3(cfg).put_object(
            Bucket=cfg.bucket,
            Key=dir_prefix,
            Body=body,
            CacheControl=extra["CacheControl"],
            ContentType=extra["ContentType"],
        )
    except ClientError as e:  # pragma: no cover – best effort
        print(f"Placeholder upload skipped: {e}")


# --------------------------------------------------------------------------------------
# Preflight / Dry run / Publish orchestration
# --------------------------------------------------------------------------------------


def preflight(
    cfg: PublishConfig,
    paths: Paths | None = None,
    check_allure: bool = True,
) -> dict:
    paths = paths or Paths()
    results = {
        "allure_cli": False,
        "allure_results": False,
        "s3_bucket": False,
    }

    if check_allure:
        try:
            ensure_allure_cli()
            results["allure_cli"] = True
        except Exception:
            results["allure_cli"] = False
    else:
        results["allure_cli"] = True

    try:
        results_dir = paths.results
        results["allure_results"] = results_dir.exists() and any(results_dir.iterdir())
    except OSError:
        results["allure_results"] = False

    region_mismatch = False
    bucket_region = None
    try:
        s3 = _s3(cfg)
        head = s3.head_bucket(Bucket=cfg.bucket)
        # region detection (defensive: some stubs may return None)
        if head:
            bucket_region = (
                head.get("ResponseMetadata", {}).get("HTTPHeaders", {}).get("x-amz-bucket-region")
            )
        # Attempt a small list to confirm permissions
        s3.list_objects_v2(
            Bucket=cfg.bucket,
            Prefix=cfg.s3_latest_prefix,
            MaxKeys=1,
        )
        results["s3_bucket"] = True
    except ClientError as e:
        code = getattr(e, "response", {}).get("Error", {}).get("Code")
        if code == "301":  # permanent redirect / region mismatch
            region_mismatch = True
        results["s3_bucket"] = False
    results["bucket_region"] = bucket_region
    results["region_mismatch"] = region_mismatch
    return results


def plan_dry_run(cfg: PublishConfig, paths: Paths | None = None) -> dict:
    paths = paths or Paths()
    samples = []
    if paths.report.exists():
        for i, p in enumerate(paths.report.rglob("*")):
            if i >= 20:
                break
            if p.is_file():
                rel = p.relative_to(paths.report).as_posix()
                key_run = f"{cfg.s3_run_prefix}{rel}"
                samples.append(
                    {
                        "file": rel,
                        "run_key": key_run,
                        "cache": cache_control_for_key(key_run),
                    }
                )
    else:
        samples.append({"note": "Report missing; would run allure generate."})
    root = branch_root(cfg.prefix, cfg.project, cfg.branch)
    latest_tmp = f"{root}/latest_tmp/"
    mapping = {
        "bucket": cfg.bucket,
        "prefix": cfg.prefix,
        "project": cfg.project,
        "branch": cfg.branch,
        "run_id": cfg.run_id,
        "run_prefix": cfg.s3_run_prefix,
        # Backwards compat: historical key name pointed to temp swap area
        "latest_prefix": latest_tmp,
        "latest_tmp_prefix": latest_tmp,
        "latest_final_prefix": cfg.s3_latest_prefix,
    }
    return {
        **mapping,
        "run_url": cfg.url_run(),
        "latest_url": cfg.url_latest(),
        "context_url": getattr(cfg, "context_url", None),
        "metadata": cfg.metadata or {},
        "samples": samples,
        "encryption": {
            "sse": cfg.sse,
            "sse_kms_key_id": cfg.sse_kms_key_id,
        },
    }


def publish(cfg: PublishConfig, paths: Paths | None = None) -> dict:
    paths = paths or Paths()
    pull_history(cfg, paths)
    generate_report(paths)
    upload_dir(cfg, paths.report, cfg.s3_run_prefix)
    _ensure_directory_placeholder(cfg, paths.report / "index.html", cfg.s3_run_prefix)
    two_phase_update_latest(cfg, paths.report)
    try:
        write_manifest(cfg, paths)
    except ClientError as e:  # pragma: no cover – non fatal
        print(f"Manifest write skipped: {e}")
    try:  # retention cleanup
        if getattr(cfg, "max_keep_runs", None):
            cleanup_old_runs(cfg, int(cfg.max_keep_runs))
    except Exception as e:  # pragma: no cover
        print(f"Cleanup skipped: {e}")

    files_count = sum(1 for p in paths.report.rglob("*") if p.is_file())
    return {
        "run_url": cfg.url_run(),
        "latest_url": cfg.url_latest(),
        "bucket": cfg.bucket,
        "run_prefix": cfg.s3_run_prefix,
        "latest_prefix": cfg.s3_latest_prefix,
        "report_size_bytes": compute_dir_size(paths.report),
        "report_files": files_count,
    }


__all__ = [
    "Paths",
    "pull_history",
    "generate_report",
    "upload_dir",
    "two_phase_update_latest",
    "write_manifest",
    "cleanup_old_runs",
    "preflight",
    "plan_dry_run",
    "publish",
]
