import argparse
from typing import List

from .types import APP
from .app import Slack


def main(argv: List[str] | None = None):
    parser = argparse.ArgumentParser(prog="alert")
    parser.add_argument("message", type=str, default="alert")
    parser.add_argument("--app", type=str, default=APP.SLACK, choices=list(APP))
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--disable", action="store_true")
    args, _ = parser.parse_known_args(argv)

    if args.app == APP.SLACK:
        caller = Slack(verbose=args.verbose)
    else:
        raise NotImplementedError(
            f"Notice for {args.app} has not been implemented."
        )

    if not args.disable:
        caller(args.message)


if __name__ == "__main__":
    raise SystemExit(main())