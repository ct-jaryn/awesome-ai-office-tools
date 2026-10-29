#!/usr/bin/env python3
"""Validate the bilingual directory and local Markdown links without network access.

When adding or renaming a product category, update CATEGORY_HEADINGS below in
both languages. Other tables (for example, quick-start guides) are ignored.
"""

from collections import Counter
from pathlib import Path
import re
import sys
from urllib.parse import parse_qsl, unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
CATEGORY_HEADINGS = (
    ("AI workbenches and agents", "AI 工作台与智能体"),
    ("Writing, documents and presentations", "写作、文档与演示"),
    ("Research and knowledge", "调研与知识管理"),
    ("Meetings and collaboration", "会议与协作"),
    ("Workflow automation", "工作流自动化"),
)
FEATURED_URL = "https://work.baizhi.cloud/"
FEATURED_SOURCE = "https://github.com/chaitin/MonkeyCode"
WORKBUDDY_URL = "https://cloud.tencent.com/product/workbuddy"
LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
BARE_URL = re.compile(r"https?://[^\s<>()|]+", re.IGNORECASE)
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
SEPARATOR = re.compile(r":?-{3,}:?")
# This is a short denylist, not a comprehensive privacy or URL safety scan.
TRACKING_KEYS = {
    "ref", "ref_id", "referral", "referral_code", "affiliate", "affiliate_id",
    "aff", "aff_id", "gclid", "fbclid", "msclkid",
}


def split_row(line):
    """Split a pipe-delimited Markdown row; preserve escaped literal pipes."""
    text = line.strip()
    if not (text.startswith("|") and text.endswith("|")):
        return None
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", text[1:-1])]


def valid_url(url):
    try:
        parts = urlsplit(url)
        if (parts.scheme != "https" or not parts.hostname or "@" in parts.netloc
                or any(c.isspace() for c in url)):
            return False
        # Some sites still use semicolons to separate query parameters.
        params = parse_qsl(parts.query.replace(";", "&"), keep_blank_values=True)
        keys = (key.casefold() for key, _ in params)
        return not any(key.startswith("utm_") or key in TRACKING_KEYS for key in keys)
    except ValueError:
        return False


def normalized_url(url):
    """Normalize common spelling differences without conflating product paths."""
    parts = urlsplit(url)
    return (parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), parts.query)


def product_sections(path, headings, errors):
    """Return ordered URL lists for each named category and report malformed rows."""
    lines = path.read_text(encoding="utf-8").splitlines()
    expected = set(headings)
    sections = {}
    current = None
    for number, line in enumerate(lines, 1):
        match = HEADING.match(line)
        if match and len(match.group(1)) <= 2:
            title = match.group(2)
            current = title if len(match.group(1)) == 2 and title in expected else None
            if current is not None:
                if current in sections:
                    errors.append(f"{path.name}:{number}: duplicate category {current!r}")
                else:
                    sections[current] = []
            continue
        if current is not None and line.strip().startswith("|"):
            sections[current].append((number, line))

    observed = list(sections)
    if observed != list(headings):
        errors.append(f"{path.name}: categories missing, duplicated, or out of order")
    result = []
    for title in headings:
        rows = sections.get(title, [])
        if len(rows) < 3:
            errors.append(f"{path.name}: category {title!r} needs a header, separator, and entries")
            result.append([])
            continue
        for previous, current_row in zip(rows, rows[1:]):
            if current_row[0] != previous[0] + 1:
                errors.append(f"{path.name}:{current_row[0]}: product table must be continuous without blank or non-table lines")
        header = split_row(rows[0][1])
        separator = split_row(rows[1][1])
        if not header or len(header) != 2 or not all(header):
            errors.append(f"{path.name}:{rows[0][0]}: expected a two-column table header")
        if not separator or len(separator) != 2 or not all(SEPARATOR.fullmatch(s) for s in separator):
            errors.append(f"{path.name}:{rows[1][0]}: expected a two-column Markdown table separator")
        entries = []
        for number, line in rows[2:]:
            cells = split_row(line)
            if not cells or len(cells) != 2:
                errors.append(f"{path.name}:{number}: expected a two-column product row")
                continue
            matches = list(LINK.finditer(cells[0]))
            if not matches or matches[0].start() != 0:
                errors.append(f"{path.name}:{number}: product name must begin with a Markdown link")
                continue
            description_links = list(LINK.finditer(cells[1]))
            if any(not match.group(1).strip() for match in matches + description_links):
                errors.append(f"{path.name}:{number}: product links need a name")
                continue
            urls = [match.group(2) for match in matches + description_links]
            urls.extend(BARE_URL.findall(cells[1]))
            if any(not valid_url(url) for url in urls):
                # Do not echo the URL: it might contain credentials or identifiers.
                errors.append(f"{path.name}:{number}: product URLs must use HTTPS without credentials, tracking parameters, or affiliate codes")
                continue
            if not cells[1].strip():
                errors.append(f"{path.name}:{number}: product description is empty")
            entries.append([match.group(2) for match in matches])
        result.append(entries)
    return result


def heading_anchors(path):
    """Approximate GitHub heading slugs, including CJK and duplicate headings."""
    counts = Counter()
    anchors = set()
    fence = None
    for line in path.read_text(encoding="utf-8").splitlines():
        fence_match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence_match:
            marker = fence_match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence:
            continue
        match = HEADING.match(line)
        if not match:
            continue
        title = match.group(2).lower()
        title = re.sub(r"<[^>]+>", "", title)
        title = LINK.sub(lambda m: m.group(1), title)
        slug = re.sub(r"[^\w\- ]", "", title, flags=re.UNICODE).replace(" ", "-")
        suffix = counts[slug]
        counts[slug] += 1
        anchors.add(f"{slug}-{suffix}" if suffix else slug)
    return anchors


def check_local_links(root, errors):
    anchor_cache = {}
    for path in root.rglob("*.md"):
        if ".git" in path.relative_to(root).parts:
            continue
        content = path.read_text(encoding="utf-8")
        for match in LINK.finditer(content):
            target = match.group(2)
            location = f"{path.relative_to(root)}:{content.count(chr(10), 0, match.start()) + 1}"
            try:
                parts = urlsplit(target)
            except ValueError:
                errors.append(f"{location}: invalid link")
                continue
            if parts.scheme or parts.netloc:
                continue
            destination = (path.parent / unquote(parts.path)).resolve() if parts.path else path.resolve()
            if not destination.is_relative_to(root.resolve()) or not destination.exists():
                errors.append(f"{location}: missing or out-of-repository relative link")
                continue
            if parts.fragment and destination.is_file() and destination.suffix.lower() == ".md":
                if destination not in anchor_cache:
                    anchor_cache[destination] = heading_anchors(destination)
                if unquote(parts.fragment) not in anchor_cache[destination]:
                    errors.append(f"{location}: missing heading anchor")


def check_root(root):
    root = Path(root)
    errors = []
    files = (root / "README.md", root / "README.zh-CN.md")
    if not all(path.is_file() for path in files):
        return ["Both README.md and README.zh-CN.md are required"]
    en = product_sections(files[0], [pair[0] for pair in CATEGORY_HEADINGS], errors)
    zh = product_sections(files[1], [pair[1] for pair in CATEGORY_HEADINGS], errors)
    for index, (english, chinese) in enumerate(zip(en, zh)):
        if english != chinese:
            errors.append(f"Category {CATEGORY_HEADINGS[index][0]!r}: product links or order differ between languages")
    all_entries = [row for category in en for row in category]
    if not all_entries or len(all_entries[0]) < 2 or all_entries[0][:2] != [FEATURED_URL, FEATURED_SOURCE]:
        errors.append("Baizhi Office and its source must be the first directory entry")
    if len(all_entries) < 2 or all_entries[1][0] != WORKBUDDY_URL:
        errors.append("WorkBuddy must be the second directory entry")
    primary = [normalized_url(row[0]) for row in all_entries]
    if len(primary) != len(set(primary)):
        errors.append("Duplicate primary product links found")
    check_local_links(root, errors)
    return errors


def main():
    errors = check_root(ROOT)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Directory checks passed: categories, product links and order, and local Markdown links. No network requests made.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
