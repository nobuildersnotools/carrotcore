#!/usr/bin/env python3
"""Compile this repo into a Minecraft datapack ZIP.

Packages pack.mcmeta and data/ at the root of the archive (the format
Minecraft requires), skipping VCS files, docs, and the output zip itself.
"""
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INCLUDE = ["pack.mcmeta", "data"]


def iter_pack_files():
    for name in INCLUDE:
        path = ROOT / name
        if path.is_file():
            yield path
        elif path.is_dir():
            yield from sorted(p for p in path.rglob("*") if p.is_file())
        else:
            sys.exit(f"error: expected '{name}' in {ROOT}, not found")


def build(output: Path):
    files = list(iter_pack_files())
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            zf.write(path, path.relative_to(ROOT).as_posix())
    print(f"wrote {output.name} ({len(files)} files, {output.stat().st_size:,} bytes)")


if __name__ == "__main__":
    out = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "Carrotcore.zip"
    build(out)
