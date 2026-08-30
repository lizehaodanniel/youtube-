#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描成片包口播里出现的具体数字，用于人工核实用例真实性。

两条正则：
  1. NUMERIC —— 阿拉伯数字形式（$8,000 / 22% / 20 months）
  2. WORDED  —— 英文数词形式（twenty months / fifteen hundred）

⚠️ 第二条是必须的。英文财经口播习惯把数字拼写成单词（"twenty months and
just over fifteen hundred in interest"），只跑第一条会误报「口播中未出现
数字」，然后整批数字就没人核了。
"""
import json
import re
import os

NUMERIC = re.compile(
    r"\$\s?\d[\d,\.]*|\b\d+(?:\.\d+)?\s?%|\b\d+\s(?:years?|months?|weeks?|days?)\b"
)

WORD = (
    r"\b(?:twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|"
    r"ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|"
    r"one|two|three|four|five|six|seven|eight|nine|"
    r"hundred|thousand|million|percent|months?|years?)\b"
)
WORDED = re.compile(
    r"(?:\b[a-z]+-\b)*" + WORD + r"(?:\s(?:and\s)?" + WORD + r")*",
    re.I,
)

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pkgs = json.load(open(os.path.join(root, "packages.json"), encoding="utf-8"))

for p in pkgs["packages"]:
    print("=" * 78)
    print(p["channel_key"], "|", p["topic"])

    seen = {}
    for b in p["script"]:
        for m in NUMERIC.findall(b["en"]):
            seen.setdefault(m.strip(), (b["t"], b["en"]))
    if seen:
        print("  --- 阿拉伯数字形式 ---")
        for k, (t, en) in seen.items():
            print(f"  {k:>14}   {t}   {en[:88]}")
    else:
        print("  --- 阿拉伯数字形式：（无） ---")

    seen2 = {}
    for b in p["script"]:
        for m in WORDED.findall(b["en"]):
            key = m.strip()
            if len(key) < 4:
                continue
            seen2.setdefault(key, (b["t"], b["en"]))
    if seen2:
        print("  --- 英文数词形式（人工核对用）---")
        for k, (t, en) in seen2.items():
            print(f"  {k:>26}   {t}   {en[:76]}")
    else:
        print("  --- 英文数词形式：（无） ---")

    if not seen and not seen2:
        print("  （口播中未出现数字）")
    print()
    print("  提示：以上每一条都要能回答「这个数从哪来、能不能复算」。")
    print("        答不上来的，要么补出处，要么标成假设值。")
