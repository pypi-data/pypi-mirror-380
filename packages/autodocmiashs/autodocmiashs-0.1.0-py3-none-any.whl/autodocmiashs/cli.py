import os
import sys
from pathlib import Path
from typing import List, Optional
from .generator import generate

def main():
    # Usage:
    #   autodocmiashs                -> process all src/**/*.py
    #   autodocmiashs --changed f1.py f2.py
    #   autodocmiashs --env-file .env
    """Processes Python files to generate documentation, with optional filtering for changed files or environment configuration.

Handles command-line arguments for specifying changed files or environment file paths.

Args:
    args: List[str]: Command-line arguments (default: sys.argv[1:])

Raises:
    SystemExit: Exits with status code from generate() or error conditions."""
    args: List[str] = sys.argv[1:]
    only_changed = False
    changed_files: Optional[List[str]] = None

    # minimal --env-file support
    if "--env-file" in args:
        i = args.index("--env-file")
        try:
            env_path = Path(args[i+1])
        except IndexError:
            print("Usage: --env-file <path>")
            sys.exit(2)
        if env_path.is_file():
            for line in env_path.read_text(encoding="utf-8").splitlines():
                if not line.strip() or line.strip().startswith("#"):
                    continue
                if "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip())

    if "--changed" in args:
        only_changed = True
        i = args.index("--changed")
        changed_files = []
        for a in args[i+1:]:
            if a.startswith("-"):
                break
            changed_files.append(a)

    code = generate(only_changed=only_changed, changed_files=changed_files)
    sys.exit(code)
