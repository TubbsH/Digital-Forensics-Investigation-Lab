#!/usr/bin/env python3
"""Calculate MD5 and SHA-256 hashes for a file.

Usage:
    python hash_file.py <path-to-file>
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def calculate_hashes(path: Path, chunk_size: int = 1024 * 1024) -> tuple[str, str]:
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()

    with path.open("rb") as evidence_file:
        while chunk := evidence_file.read(chunk_size):
            md5.update(chunk)
            sha256.update(chunk)

    return md5.hexdigest(), sha256.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate MD5 and SHA-256 file hashes.")
    parser.add_argument("file", type=Path, help="File to hash")
    args = parser.parse_args()

    if not args.file.is_file():
        raise SystemExit(f"File not found: {args.file}")

    md5, sha256 = calculate_hashes(args.file)
    print(f"File:    {args.file}")
    print(f"Size:    {args.file.stat().st_size} bytes")
    print(f"MD5:     {md5}")
    print(f"SHA-256: {sha256}")


if __name__ == "__main__":
    main()
