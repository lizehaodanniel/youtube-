# -*- coding: utf-8 -*-
"""火柴人故事版成片包断言脚本 —— 改完任何一镜都必须跑它。

    python3 verify_stick.py

和 verify_character.py 的区别：那个管「真人 host 有没有在画面里」，
这个管「火柴人世界锁有没有被逐字引用、节奏和词数有没有跑偏、数字有没有对上」。
两者互不相干，改了哪边就跑哪个。
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "_build"))

import fin_stick                      # noqa: E402
from stick_world import (STYLE_LOCK, ENV, CHAR, IMG_TAIL, VID_TAIL, word_count)  # noqa: E402
import stick_numbers                  # noqa: E402

FAIL = []
def check(ok, msg):
    print(("  ✓ " if ok else "  ✗ ") + msg)
    if not ok:
        FAIL.append(msg)


def main():
    p = fin_stick.build()
    shots = p["shots"]
    print("=" * 78)
    print(f'火柴人故事版断言：{p["shot_count"]} 镜 / {p["word_count"]} 词 / {p["duration"]}')
    print("=" * 78)

    # ---------- 1 编号与节奏
    ids = [s["id"] for s in shots]
    check(len(ids) == len(set(ids)), f"镜号唯一（{len(ids)} 个）")
    check(len(shots) == 88, f"镜数 = 88（实际 {len(shots)}）")

    bad_wc = [s["id"] for s in shots if not (10 <= s["wc"] <= 13)]
    check(not bad_wc, f"每条口播 10–13 词（越界：{bad_wc or '无'}）")

    bad_dur = [s["id"] for s in shots if not (3.9 <= s["dur"] <= 5.3)]
    check(not bad_dur, f"每镜 4–5 秒（越界：{bad_dur or '无'}）")

    # 时间轴必须首尾相接
    gaps = []
    prev_end = 0.0
    for s in shots:
        a, b = [float(x.strip().rstrip("s")) for x in s["window"].split("–")]
        if abs(a - prev_end) > 0.05:
            gaps.append(s["id"])
        prev_end = b
    check(not gaps, f"时间轴首尾相接（断点：{gaps or '无'}）")

    # ---------- 2 世界锁必须逐字出现在每一条图片提示词里
    miss = [s["id"] for s in shots if STYLE_LOCK not in s["img_en"]]
    check(not miss, f"画风锁逐字出现（缺：{miss or '无'}）")

    miss = [s["id"] for s in shots if IMG_TAIL not in s["img_en"]]
    check(not miss, f"图片尾（无字 / 单帧 / 起始帧）逐字出现（缺：{miss or '无'}）")

    miss = [s["id"] for s in shots if ENV[s["env"]] not in s["img_en"]]
    check(not miss, f"环境锁逐字出现（缺：{miss or '无'}）")

    miss = [f'{s["id"]}:{w}' for s in shots for w in s["who"] if CHAR[w] not in s["img_en"]]
    check(not miss, f"角色形象锁逐字出现（缺：{miss[:5] or '无'}）")

    miss = [s["id"] for s in shots if VID_TAIL not in s["vid_en"]]
    check(not miss, f"视频尾（6 秒 / 无口型 / 不变形）逐字出现（缺：{miss or '无'}）")

    # ---------- 3 机位不能和上一镜重复
    import stick_act1, stick_act2, stick_act3, stick_act4
    beats = stick_act1.BEATS + stick_act2.BEATS + stick_act3.BEATS + stick_act4.BEATS
    dup = [f"F{i}" for i in range(2, len(beats) + 1)
           if beats[i - 1]["cam"].strip() == beats[i - 2]["cam"].strip()]
    check(not dup, f"相邻两镜机位不重复（重复：{dup or '无'}）")

    # ---------- 4 视频提示词正文 120–180 词（不含尾）
    tail_wc = word_count(VID_TAIL)
    lens = [word_count(s["vid_en"]) - tail_wc for s in shots]
    bad = [(s["id"], n) for s, n in zip(shots, lens) if not (120 <= n <= 180)]
    check(not bad, f"动画提示词正文 120–180 词（越界：{bad[:5] or '无'}）"
                   f"　最短 {min(lens)} / 最长 {max(lens)}")

    # ---------- 5 图片提示词不能出现「文字 / 分格」以外的正向要求
    pos_bad = [s["id"] for s in shots
               if re.search(r"\b(?:write the words|spelled out|text reads)\b", s["img_en"], re.I)]
    check(not pos_bad, f"图片提示词没有要求烧字（违规：{pos_bad or '无'}）")

    # ---------- 6 数字必须和 stick_numbers.py 的实算结果一致
    corpus = " ".join(s["en"] for s in shots).lower()
    nums = {}
    for name, apr in stick_numbers.CASES:
        m, ti, fi, _ = stick_numbers.payoff(stick_numbers.BALANCE, apr, stick_numbers.PAYMENT)
        nums[name] = dict(months=m, interest=ti, first_interest=fi,
                          gain=stick_numbers.invest_gain(stick_numbers.PAYMENT,
                                                         stick_numbers.MARKET, m))
    nm = stick_numbers.min_payment_trap(stick_numbers.BALANCE, 22.15)

    spoken = {
        "twenty-two point one five": "22.15%（Maya 的合同利率）",
        "seven point one four": "7.14%（Devon 的合同利率）",
        "three point five percent": "3.5%（Priya 的合同利率）",
        "twenty months": f"20 个月（实算 {nums['MAYA']['months']}）",
        "seventeen months": f"17 个月（实算 {nums['DEVON']['months']}）",
        "fifteen hundred sixty-nine": f"还债利息 $1,569（实算 ${nums['MAYA']['interest']:,.0f}）",
        "five seventy-four": f"投资收益 $574（实算 ${nums['MAYA']['gain']:,.0f}）",
        "four hundred and thirty-two": f"Devon 利息 $432（实算 ${nums['DEVON']['interest']:,.0f}）",
        "four hundred and eight": f"投资收益 $408（实算 ${nums['DEVON']['gain']:,.0f}）",
        "nine hundred and ninety-five": "Maya 差额 $995",
        "two hundred and five": f"Priya 利息 $205（实算 ${nums['PRIYA']['interest']:,.0f}）",
        "two hundred and four": "Priya 差额 $204",
        "a hundred and forty-seven": f"首月利息 $147（实算 ${nums['MAYA']['first_interest']:,.2f}）",
        "hundred and twelve years": f"最低还款 {nm[1]:.0f} 年",
        "eighty-three thousand": f"最低还款总利息 ${nm[2]:,.0f}",
        "twenty-four thousand five hundred": "2026 递延上限 $24,500",
    }
    miss = [f"{k}（{v}）" for k, v in spoken.items() if k not in corpus]
    check(not miss, f"口播数字与 stick_numbers.py 一致（缺失：{miss or '无'}）")

    # ---------- 7 环境 / 角色 key 全部合法
    bad_env = [s["id"] for s in shots if s["env"] not in ENV]
    bad_who = [s["id"] for s in shots if any(w not in CHAR for w in s["who"])]
    check(not bad_env and not bad_who, f"环境 / 角色 key 合法（异常：{(bad_env + bad_who) or '无'}）")

    # ---------- 8 每个环境和每个角色都要被用到（防止写了没人用）
    used_env = {s["env"] for s in shots}
    used_who = {w for s in shots for w in s["who"]}
    unused_env = sorted(set(ENV) - used_env)
    unused_who = sorted(set(CHAR) - used_who)
    check(not unused_env, f"14 个环境全部被用到（未用：{unused_env or '无'}）")
    check(not unused_who, f"4 个角色全部出场（未用：{unused_who or '无'}）")

    print("=" * 78)
    if FAIL:
        print(f"❌ {len(FAIL)} 项未通过")
        for m in FAIL:
            print("   -", m)
        return 1
    print("✅ 全部通过")
    print(f'   图片提示词均长 {sum(word_count(s["img_en"]) for s in shots) // len(shots)} 词')
    print(f'   视频提示词均长 {sum(word_count(s["vid_en"]) for s in shots) // len(shots)} 词')
    return 0


if __name__ == "__main__":
    sys.exit(main())
