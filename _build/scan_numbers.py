#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描成片包口播里出现的具体数字，用于人工核实用例真实性。"""
import json
import re
import os

PAT = re.compile(r"\$\s?\d[\d,\.]*|\b\d+(?:\.\d+)?\s?%|\b\d+\s(?:years?|months?|weeks?|days?)\b")

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pkgs = json.load(open(os.path.join(root, "packages.json"), encoding="utf-8"))

for p in pkgs["packages"]:
    print("=" * 70)
    print(p["channel_key"], "|", p["topic"])
    seen = {}
    for b in p["script"]:
        for m in PAT.findall(b["en"]):
            key = m.strip()
            if key not in seen:
                seen[key] = (b["t"], b["en"])
    if not seen:
        print("  （口播中未出现 $ / % / 年限 数字）")
    for k, (t, en) in seen.items():
        print(f"  {k:>12}   {t}   {en[:95]}")
