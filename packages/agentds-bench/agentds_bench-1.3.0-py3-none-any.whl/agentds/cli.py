"""
Command Line Interface for the AgentDS client.
"""

import argparse
import sys
from typing import Optional

from .client import BenchmarkClient


def _exit(code: int, message: Optional[str] = None) -> None:
    if message:
        print(message)
    sys.exit(code)


def main() -> None:
    parser = argparse.ArgumentParser(prog="agentds", description="AgentDS CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # auth
    auth_parser = subparsers.add_parser("auth", help="Authenticate and save team credentials")
    auth_parser.add_argument("--api-key", required=True)
    auth_parser.add_argument("--team-name", required=True)

    # start
    subparsers.add_parser("start", help="Start competition for the current team")

    # domains
    subparsers.add_parser("domains", help="List available domains")

    # status
    subparsers.add_parser("status", help="Get competition status")

    # submit
    submit_parser = subparsers.add_parser("submit", help="Submit predictions CSV for evaluation")
    submit_parser.add_argument("--domain", required=True)
    submit_parser.add_argument("--task", type=int, required=True)
    submit_parser.add_argument("--file", required=True)
    submit_parser.add_argument("--format", dest="submission_format")
    submit_parser.add_argument("--expected-rows", type=int)
    submit_parser.add_argument("--numeric", action="store_true", help="Expect numeric prediction column")
    submit_parser.add_argument("--prob-range", nargs=2, type=float, metavar=("LOW", "HIGH"))

    # history
    history_parser = subparsers.add_parser("history", help="Show submission history")
    history_parser.add_argument("--domain")
    history_parser.add_argument("--limit", type=int, default=10)

    # leaderboard
    leaderboard_parser = subparsers.add_parser("leaderboard", help="Show leaderboard (optionally set JWT)")
    leaderboard_parser.add_argument("--domain")
    leaderboard_parser.add_argument("--jwt")

    args = parser.parse_args()

    if args.command == "auth":
        client = BenchmarkClient(api_key=args.api_key, team_name=args.team_name)
        try:
            if client.authenticate():
                _exit(0, "Authenticated and saved credentials.")
        except Exception as e:
            _exit(1, f"Authentication failed: {e}")

    client = BenchmarkClient()

    if args.command == "start":
        try:
            ok = client.start_competition()
            _exit(0 if ok else 1, "Competition started." if ok else "Failed to start competition.")
        except Exception as e:
            _exit(1, f"Start failed: {e}")

    if args.command == "domains":
        domains = client.get_domains()
        for d in domains:
            print(d)
        _exit(0)

    if args.command == "status":
        status = client.get_status()
        if "formatted_table" in status:
            print(status["formatted_table"])
        else:
            print(status)
        _exit(0)

    if args.command == "submit":
        prob_range = tuple(args.prob_range) if args.prob_range else None
        result = client.submit_prediction(
            args.domain,
            args.task,
            args.file,
            submission_format=args.submission_format,
            expected_rows=args.expected_rows,
            numeric_prediction=args.numeric,
            probability_range=prob_range,
        )
        if result.get("success", False):
            print(f"Score: {result['score']} ({result['metric_name']})")
            _exit(0)
        else:
            print("Submission failed.")
            if not result.get("validation_passed", True):
                for err in result.get("details", {}).get("validation_errors", []):
                    print(f"- {err}")
            _exit(1)

    if args.command == "history":
        subs = client.get_submission_history(args.domain, args.limit)
        for s in subs:
            print(s)
        _exit(0)

    if args.command == "leaderboard":
        if args.jwt:
            client.set_jwt_token(args.jwt)
        if args.domain:
            data = client.get_domain_leaderboard(args.domain)
        else:
            data = client.get_leaderboard()
        print(data)
        _exit(0)


if __name__ == "__main__":
    main()


