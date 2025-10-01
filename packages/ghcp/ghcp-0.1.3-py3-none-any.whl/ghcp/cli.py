from __future__ import annotations
import argparse
import sys
from pathlib import Path

from .core import download_url, GHCPError


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="ghcp",
        description="Copy a folder or file from GitHub without cloning.",
    )
    p.add_argument("url", help="GitHub URL (repo, tree/<ref>/<path>, or blob/<ref>/<path>)")
    p.add_argument("-o", "--out", default=".", help="Output directory (default: .)")
    p.add_argument("--ref", help="Branch, tag, or commit SHA to use (default: repo default branch)")
    p.add_argument("--token", help="GitHub token (otherwise uses $GITHUB_TOKEN if set)")
    p.add_argument("--preserve", action="store_true", help="Preserve full folder path inside the repo")
    p.add_argument("-q", "--quiet", action="store_true", help="Reduce output")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        dest = download_url(
            url=args.url,
            outdir=args.out,
            ref=args.ref,
            token=args.token,
            preserve=args.preserve,
            quiet=args.quiet,
        )
        if not args.quiet:
            print(f"✅ Saved to {Path(dest).resolve()}")
        return 0
    except GHCPError as e:
        print(f"ghcp: {e}", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"ghcp: unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())