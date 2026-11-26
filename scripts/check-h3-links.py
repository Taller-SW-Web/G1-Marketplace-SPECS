"""Validate local Markdown targets in this branch's changed documents only."""
import argparse
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote

parser = argparse.ArgumentParser()
parser.add_argument("--base", default="a8c3a7e21482063d71a083fd950dd8fa418b615c")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]


def git(*arguments):
    return subprocess.check_output(["git", *arguments], cwd=root).decode("utf-8")


names = set(git("diff", "--name-only", "-z", "--diff-filter=ACMR", args.base).split("\0"))
names.update(git("ls-files", "-z", "--others", "--exclude-standard").split("\0"))
errors = []
documents = 0
links = 0
for name in sorted(names):
    document = root / name
    if not name.endswith(".md") or not document.is_file():
        continue
    documents += 1
    fence = None
    for line_number, line in enumerate(document.read_text(encoding="utf-8-sig").splitlines(), 1):
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            if fence is None:
                fence = marker[1][0]
            elif marker[1][0] == fence:
                fence = None
            continue
        if fence:
            continue
        for match in re.finditer(r"\[[^\]]*\]\((<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)", line):
            target = unquote(match[1].strip("<>"))
            if target.startswith(("#", "//")) or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            resolved = (root / target.lstrip("/")) if target.startswith("/") else document.parent / target
            links += 1
            if not resolved.exists():
                errors.append(f"{name}:{line_number}: {target}")
print(f"H3 links: {documents} changed Markdown files, {links} local targets, {len(errors)} missing.")
for error in errors:
    print(error)
raise SystemExit(bool(errors))
