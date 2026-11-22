#!/usr/bin/env python3
"""Scans patterns/*/*.md and writes manifest.json (the site's sidebar)."""
import re, json, pathlib
R = pathlib.Path(__file__).parent

def build():
    pats = []
    for d in sorted((R / "patterns").iterdir()):
        if not d.is_dir(): continue
        ns = []
        for f in sorted(d.glob("*.md")):
            if f.name == "README.md": continue
            t = f.read_text(encoding="utf-8")
            m = re.search(r"^# (\d+)\. (.+)$", t, re.M)
            l = re.search(r"\*\*Difficulty:\*\* (\w+)", t)
            if m: ns.append({"n": int(m[1]), "title": m[2], "level": l[1] if l else "Medium",
                             "path": f.relative_to(R).as_posix()})
        ns.sort(key=lambda x: x["n"])
        c = d / "README.md"
        pats.append({"id": d.name, "name": d.name.replace("-", " ").title(),
                     "cheat": c.relative_to(R).as_posix() if c.exists() else None, "notes": ns})
    (R / "manifest.json").write_text(json.dumps({"patterns": pats}, indent=1), encoding="utf-8")

if __name__ == "__main__": build()
