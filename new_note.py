#!/usr/bin/env python3
"""Usage: python new_note.py <number> "<title>" <pattern-folder> <Easy|Medium|Hard>
       python new_note.py index      (rebuild all indexes)"""
import sys, re, datetime, pathlib
ROOT = pathlib.Path(__file__).parent
EMOJI = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}

def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
def pname(folder): return folder.replace("-", " ").title()

def collect():
    pats = {}
    for f in sorted((ROOT / "patterns").glob("*/*.md")):
        if f.name == "README.md": continue
        t = f.read_text(encoding="utf-8")
        m = re.search(r"^# (\d+)\. (.+)$", t, re.M)
        d = re.search(r"\*\*Difficulty:\*\* (\w+)", t)
        if m: pats.setdefault(f.parent.name, []).append((int(m[1]), m[2], d[1] if d else "-", f))
    for v in pats.values(): v.sort(key=lambda r: r[0])
    return pats

def table(rows, base):
    head = "| # | Problem | Level |\n|---|---|---|\n"
    return head + "\n".join(
        f"| {n} | [{t}]({f.relative_to(base).as_posix()}) | {EMOJI.get(lv, '')} {lv} |" for n, t, lv, f in rows)

def put(path, start, end, content):
    txt = path.read_text(encoding="utf-8") if path.exists() else ""
    block = f"{start}\n{content}\n{end}"
    if start in txt:
        txt = re.sub(re.escape(start) + ".*?" + re.escape(end), lambda m: block, txt, flags=re.S)
    else:
        txt = txt.rstrip() + "\n\n" + block + "\n"
    path.write_text(txt, encoding="utf-8")

def build_index():
    pats = collect(); total = sum(len(v) for v in pats.values())
    parts = [f"**{total} problems solved across {len(pats)} patterns**\n"]
    for pat in sorted(pats):
        rows = pats[pat]
        parts.append(f"### {pname(pat)} ({len(rows)})\n📖 [Cheat sheet](patterns/{pat}/README.md)\n\n{table(rows, ROOT)}\n")
        pr = ROOT / "patterns" / pat / "README.md"
        if not pr.exists():
            pr.write_text(f"# {pname(pat)}\n\n## When to use\n\n## Core idea\n\n## Java template\n```java\n\n```\n\n## Checklist\n- [ ] \n", encoding="utf-8")
        put(pr, "<!-- PROBLEMS:START -->", "<!-- PROBLEMS:END -->", "## 📋 Problems solved\n" + table(rows, pr.parent))
    put(ROOT / "README.md", "<!-- INDEX:START -->", "<!-- INDEX:END -->", "\n".join(parts))

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "index": return build_index()
    n, title, pat, lvl = sys.argv[1:5]
    d = ROOT / "patterns" / pat; d.mkdir(parents=True, exist_ok=True)
    out = d / f"{int(n):04d}-{slug(title)}.md"
    body = (ROOT / "templates/problem.md").read_text(encoding="utf-8")
    for k, v in {"{{NUM}}": n, "{{TITLE}}": title, "{{PATTERN}}": pat, "{{LEVEL}}": lvl,
                 "{{DATE}}": str(datetime.date.today())}.items():
        body = body.replace(k, v)
    out.write_text(body, encoding="utf-8"); build_index(); print("Created", out)

main()
