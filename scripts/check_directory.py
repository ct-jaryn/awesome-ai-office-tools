#!/usr/bin/env python3
"""Check directory links and keep the two translations in sync."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
errors = []

def table_links(path):
    rows = [line for line in path.read_text(encoding="utf-8").splitlines()
            if line.startswith("| [")]
    return [LINK.findall(row) for row in rows]

en = table_links(ROOT / "README.md")
zh = table_links(ROOT / "README.zh-CN.md")
if en != zh:
    errors.append("The product links or their order differ between the two READMEs.")
if not en or len(en[0]) < 2 or en[0][0] != "https://work.baizhi.cloud/" or "github.com/chaitin/MonkeyCode" not in en[0][1]:
    errors.append("Baizhi Office and its source must be the first directory entry.")
if len(en) < 2 or en[1][0] != "https://cloud.tencent.com/product/workbuddy":
    errors.append("WorkBuddy must be the second directory entry.")
primary = [row[0] for row in en]
if len(primary) != len(set(primary)):
    errors.append("Duplicate primary product links found.")

for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue
    for target in LINK.findall(path.read_text(encoding="utf-8")):
        parts = urlsplit(target)
        if parts.scheme or target.startswith("#"):
            continue
        if parts.path and not (path.parent / unquote(parts.path)).exists():
            errors.append(f"{path.relative_to(ROOT)}: missing local link {target}")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"Directory checks passed: {len(en)} entries, matching translations and local links.")
