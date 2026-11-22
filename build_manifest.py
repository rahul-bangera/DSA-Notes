#!/usr/bin/env python3
"""Scans patterns/*/*.md and writes manifest.json (sidebar, menu, dashboard)."""
import re, json, pathlib
R = pathlib.Path(__file__).parent
ROAD = ["two-pointers","sliding-window","prefix-sum","binary-search","stack","linked-list","trees","heap","backtracking","graphs","dp","greedy"]
NAME = {"dp": "Dynamic Programming"}

def build():
    found = {d.name: d for d in (R / "patterns").iterdir() if d.is_dir()}
    pats = []
    for pid in ROAD + sorted(k for k in found if k not in ROAD):
        d = found.get(pid); ns = []; cheat = None
        if d:
            for f in sorted(d.glob("*.md")):
                if f.name == "README.md": continue
                t = f.read_text(encoding="utf-8")
                m = re.search(r"^# (\d+)\. (.+)$", t, re.M)
                if not m: continue
                g = lambda p: (re.search(p, t) or [None, ""])[1]
                st = g(r"\*\*Status:\*\* (.+)")
                ns.append({"n": int(m[1]), "title": m[2], "level": g(r"\*\*Difficulty:\*\* (\w+)") or "Medium",
                           "date": g(r"\*\*Solved:\*\* (\d{4}-\d\d-\d\d)"), "rev": "Revise" in st, "ok": "Mastered" in st,
                           "path": f.relative_to(R).as_posix()})
            ns.sort(key=lambda x: x["n"])
            if (d / "README.md").exists(): cheat = (d / "README.md").relative_to(R).as_posix()
        pats.append({"id": pid, "name": NAME.get(pid, pid.replace("-", " ").title()), "cheat": cheat, "notes": ns, "soon": not ns and not cheat})
    (R / "manifest.json").write_text(json.dumps({"patterns": pats}, indent=1), encoding="utf-8")

if __name__ == "__main__": build()
