import argparse
import sys
from importlib import resources

from . import __version__


def spec_root():
    return resources.files("aiuml") / "spec"


def iter_files(root):
    # Yield relative Posix paths for all files under root
    for entry in root.rglob("*"):
        if entry.is_file():
            yield entry.relative_to(root).as_posix()


def cmd_spec_files(_args):
    root = spec_root()
    for rel in iter_files(root):
        print(rel)


def cmd_spec_path(_args):
    print(str(spec_root()))


def cmd_spec_show(args):
    root = spec_root()
    target = root / args.name
    if not target.is_file():
        sys.stderr.write(f"Not found in bundled spec: {args.name}\n")
        sys.exit(1)
    data = target.read_text(encoding="utf-8")
    sys.stdout.write(data)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="aiuml", description="AIUML CLI")
    p.add_argument("--version", action="version", version=__version__)
    sub = p.add_subparsers(dest="command")

    sp = sub.add_parser("spec", help="Interact with bundled spec docs")
    ssub = sp.add_subparsers(dest="spec_cmd")

    sp_files = ssub.add_parser("files", help="List bundled spec files")
    sp_files.set_defaults(func=cmd_spec_files)

    sp_path = ssub.add_parser("path", help="Print bundled spec directory path")
    sp_path.set_defaults(func=cmd_spec_path)

    sp_show = ssub.add_parser("show", help="Print a bundled spec file")
    sp_show.add_argument("name", help="Relative path inside spec (e.g., VISION_v0.1.0-alpha.md or docs/FORMAL_GRAMMAR_BNF.md)")
    sp_show.set_defaults(func=cmd_spec_show)

    return p


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if not getattr(args, "command", None):
        parser.print_help()
        return 0
    if args.command == "spec" and not getattr(args, "spec_cmd", None):
        # default to files
        return cmd_spec_files(args)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

