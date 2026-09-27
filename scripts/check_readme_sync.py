#!/usr/bin/env python3
"""Check that README.md (English) and README.zh-CN.md (Chinese) stay in sync.

Both files must list exactly the same set of external resource links. Run it
locally before opening a pull request:

    python3 scripts/check_readme_sync.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = {"English": ROOT / "README.md", "Chinese": ROOT / "README.zh-CN.md"}
LINK = re.compile(r"^\s*[-*] \[[^\]]+\]\((https?://[^)\s]+)\)", re.MULTILINE)


def links(path: Path) -> list[str]:
    return LINK.findall(path.read_text(encoding="utf-8"))


def main() -> int:
    found = {lang: links(path) for lang, path in FILES.items()}
    ok = True

    for lang, urls in found.items():
        dupes = sorted({u for u in urls if urls.count(u) > 1})
        if dupes:
            ok = False
            print(f"Duplicate links in the {lang} README:")
            for url in dupes:
                print(f"  {url}")

    en, zh = set(found["English"]), set(found["Chinese"])
    for missing, lang in ((en - zh, "Chinese"), (zh - en, "English")):
        if missing:
            ok = False
            print(f"Links missing from the {lang} README:")
            for url in sorted(missing):
                print(f"  {url}")

    if ok:
        print(f"OK: both READMEs list the same {len(en)} resources.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
