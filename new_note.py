#!/usr/bin/env python3
"""Usage: python3 new_note.py <number> "<title>" <pattern-folder> <Easy|Medium|Hard>"""
import sys, re, datetime, pathlib
from build_manifest import build
R = pathlib.Path(__file__).parent
n, title, pat, lvl = sys.argv[1:5]
d = R / "patterns" / pat; d.mkdir(parents=True, exist_ok=True)
out = d / f"{int(n):04d}-{re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')}.md"
b = (R / "templates/problem.md").read_text(encoding="utf-8")
for k, v in {"{{NUM}}": n, "{{TITLE}}": title, "{{PATTERN}}": pat, "{{LEVEL}}": lvl,
             "{{DATE}}": str(datetime.date.today())}.items():
    b = b.replace(k, v)
out.write_text(b, encoding="utf-8")
c = d / "README.md"
if not c.exists():
    c.write_text(f"# {pat.replace('-', ' ').title()}\n\n## When to use\n\n## Core idea\n\n## Java template\n```java\n\n```\n", encoding="utf-8")
build(); print("Created", out)
