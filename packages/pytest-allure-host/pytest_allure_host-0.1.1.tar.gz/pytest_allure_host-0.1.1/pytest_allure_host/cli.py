from __future__ import annotations

import argparse
import os

from .config import load_effective_config
from .publisher import plan_dry_run, preflight, publish
from .utils import PublishConfig, default_run_id


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser("publish-allure")
    p.add_argument("--config", help="Path to YAML config (optional)")
    p.add_argument("--bucket")
    p.add_argument("--prefix", default=None)
    p.add_argument("--project")
    p.add_argument("--branch", default=os.getenv("GIT_BRANCH", "main"))
    p.add_argument(
        "--run-id",
        default=os.getenv("ALLURE_RUN_ID", default_run_id()),
    )
    p.add_argument("--cloudfront", default=os.getenv("ALLURE_CLOUDFRONT"))
    p.add_argument("--results", default="allure-results")
    p.add_argument("--report", default="allure-report")
    p.add_argument("--ttl-days", type=int, default=None)
    p.add_argument("--max-keep-runs", type=int, default=None)
    p.add_argument(
        "--s3-endpoint",
        default=os.getenv("ALLURE_S3_ENDPOINT"),
        help=("Custom S3 endpoint URL (e.g. http://localhost:4566 for LocalStack)"),
    )
    p.add_argument("--summary-json", default=None)
    p.add_argument(
        "--context-url",
        default=os.getenv("ALLURE_CONTEXT_URL"),
        help="Optional hyperlink giving change context (e.g. Jira ticket)",
    )
    p.add_argument("--dry-run", action="store_true", help="Plan only")
    p.add_argument(
        "--check",
        action="store_true",
        help="Run preflight checks (AWS, allure, inputs)",
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()
    cli_overrides = {
        "bucket": args.bucket,
        "prefix": args.prefix,
        "project": args.project,
        "branch": args.branch,
        "cloudfront": args.cloudfront,
        "run_id": args.run_id,
        "ttl_days": args.ttl_days,
        "max_keep_runs": args.max_keep_runs,
        "s3_endpoint": args.s3_endpoint,
        "context_url": args.context_url,
    }
    effective = load_effective_config(cli_overrides, args.config)
    missing = [k for k in ("bucket", "project") if not effective.get(k)]
    if missing:
        raise SystemExit(
            f"Missing required config values: {', '.join(missing)}. Provide via CLI, env, or YAML."  # noqa: E501
        )
    cfg = PublishConfig(
        bucket=effective["bucket"],
        prefix=effective.get("prefix") or "reports",
        project=effective["project"],
        branch=effective.get("branch") or args.branch,
        run_id=effective.get("run_id") or args.run_id,
        cloudfront_domain=effective.get("cloudfront"),
        ttl_days=effective.get("ttl_days"),
        max_keep_runs=effective.get("max_keep_runs"),
        s3_endpoint=effective.get("s3_endpoint"),
        context_url=effective.get("context_url"),
    )
    if args.check:
        checks = preflight(cfg)
        print(checks)
        if not all(checks.values()):
            return 2
    if args.dry_run:
        plan = plan_dry_run(cfg)
        print(plan)
        if args.summary_json:
            import json

            with open(args.summary_json, "w", encoding="utf-8") as f:
                json.dump(plan, f, indent=2)
        return 0
    out = publish(cfg)
    print(out)
    if args.summary_json:
        import json

        with open(args.summary_json, "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
