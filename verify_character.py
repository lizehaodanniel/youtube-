# -*- coding: utf-8 -*-
"""人物出镜校验 —— 每次改完提示词必跑。

背景（2026-08-30）：角色卡写得很详细，但只说「如果出现人，就长这样」。
而镜头主体描述写的是「一张黑桌子」，模型不会凭空加人 → 102/102 全静物。
这个脚本就是防止那类 bug 再发生：不靠肉眼，用断言卡死。
"""
import json
import re
import sys

SHOTS = "remotion/src/shots.json"


def wc(s):
    return len(re.findall(r"[A-Za-z0-9'’\-]+", s))


def check():
    pkgs = json.load(open(SHOTS, encoding="utf-8"))
    fail = 0

    for p in pkgs:
        ss = p["shots"]
        n = len(ss)
        key = p["channel_key"]
        print(f"\n=== {key}  {n} 镜 ===")

        def hit(pred):
            return sum(1 for s in ss if pred(s))

        # 1. 强制出镜指令块必须在
        c = hit(lambda s: "ON-CAMERA RULE" in s["img_en"])
        print(f"  出镜指令块      {c}/{n}" + ("" if c == n else "   ✗"))
        fail += 0 if c == n else 1

        # 2. 每个镜头都要有 ON CAMERA: 段（她在这一镜的位置）
        c = hit(lambda s: "ON CAMERA:" in s["img_en"])
        print(f"  ON CAMERA 段    {c}/{n}" + ("" if c == n else "   ✗"))
        fail += 0 if c == n else 1

        # 3. 画面主体里必须真的提到 she / her（不是只在角色卡里）
        def scene_has_she(s):
            b = s["img_en"]
            i = b.find("ON CAMERA:")
            j = b.find("Visual reference")
            if i < 0 or j < 0:
                return False
            seg = b[i:j]                      # 就是「她在哪」那一段
            return bool(re.search(r"\b(she|her)\b", seg, re.I))

        c = hit(scene_has_she)
        print(f"  主体提到 she/her {c}/{n}" + ("" if c == n else "   ✗"))
        fail += 0 if c == n else 1

        # 4. 视频提示词同样要带
        c = hit(lambda s: "ON CAMERA:" in s["vid_en"])
        print(f"  vid 带 ON CAMERA {c}/{n}" + ("" if c == n else "   ✗"))
        fail += 0 if c == n else 1

        # 5. 五个一致性标记
        marks = {
            "共用面孔": "The SAME woman appears in every shot of both channels",
            "发色":     "platinum ash-blonde",
            "禁男人":   "never a man",
            "单帧":     "Output exactly one image",
            "禁四宫格": "2x2 grid",
        }
        for k in ("img_en", "vid_en"):
            line = " · ".join(
                f"{m} {sum(1 for s in ss if m in s[k])}/{n}" for m in marks.values())
            print(f"  {k:7s} {line}")
            for m in marks.values():
                cnt = sum(1 for s in ss if m in s[k])
                if cnt != n:
                    fail += 1

        # 6. 镜头类型分布
        kinds = {}
        for s in ss:
            kinds[s.get("cam", "?")] = kinds.get(s.get("cam", "?"), 0) + 1
        print("  镜头类型 " + "  ".join(f"{k} {v}" for k, v in sorted(kinds.items())))

        # 7. 词数
        for k in ("img_en", "vid_en"):
            w = [wc(s[k]) for s in ss]
            print(f"  {k:7s} 词数 平均 {sum(w)//n} | 最短 {min(w)} | 最长 {max(w)}")

        # 8. 负面词分流 & 残留
        v0 = ss[0]["img_en"]
        has_fin = "human faces" in v0
        has_ai = "another woman" in v0
        print(f"  负面词  FIN_NEG(human faces)={has_fin}  AI_NEG(another woman)={has_ai}")
        if key == "finance" and not has_fin:
            print("   ✗ 金融频道丢了禁脸规则"); fail += 1
        if key == "ai" and not has_ai:
            print("   ✗ AI 频道丢了禁第二人规则"); fail += 1

        allp = [s[k] for s in ss for k in ("img_en", "vid_en")]
        for w in ("headphone", "beanie", "black cap", "hoodie"):
            c = sum(1 for v in allp if w in v.lower())
            if c:
                print(f"   ✗ 残留旧 host 特征 '{w}' x{c}"); fail += 1
        print("  残留旧 host 特征 0 ✓")

    print("\n" + ("✓ 全部通过" if fail == 0 else f"✗ {fail} 项未通过"))
    return fail


if __name__ == "__main__":
    sys.exit(1 if check() else 0)
