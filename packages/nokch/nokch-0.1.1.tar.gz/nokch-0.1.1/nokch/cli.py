import argparse
import sys
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from .interpreter import Interpreter


def get_ver():
    try:
        return version("nokch")
    except PackageNotFoundError:
        return "unknown"


def main():
    print("cli")

    parser = argparse.ArgumentParser(description=f"nokch {get_ver()}")
    parser.add_argument("file", type=Path, help="path to target file to interpret")
    args = parser.parse_args()

    if not args.file.exists():
        sys.exit(f"Error: {args.file} does not exist")
    if not args.file.is_file():
        sys.exit(f"Error: {args.file} is not a file")

    print(args.file)

    Interpreter()  # ft: nkch


if __name__ == "__main__":
    main()
