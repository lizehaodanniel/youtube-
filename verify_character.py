# -*- coding: utf-8 -*-
"""人物出镜校验 —— 每次改完提示词必跑。

背景（2026-08-30）：角色卡写得很详细，但只说「如果出现人，就长这样」。
而镜头主体描述写的是「一张黑桌子」，模型不会凭空加人 → 102/102 全静物。
这个脚本就是防止那类 bug 再发生：不靠肉眼，用断言卡死。

2026-08-31 改锚点：提示词里不再有「ON-CAMERA RULE」「ON CAMERA:」这类工程化标签
（用户要的是「根据口播讲故事的图片提示词」）。「她在画面里」现在直接写成场景的第一句，
紧跟在那一句 PRESENCE 后面。所以本脚本改为按 PRESENCE 标记 + 风格段开头来切段。
"""
import json
import re
import sys

SHOTS = "remotion/src/shots.json"

# 一句话的「她在场」保险句，两个频道共用开头
PRESENCE_MARK = "The same woman described above"
# 风格段的开头 —— 故事段一结束就是它
STYLE_MARKS = (
    "Cinematic photorealistic 3D render",   # 图片提示词的风格段
    "Live-action cinematic camera move",    # 视频提示词的运镜段
    "YouTube thumbnail",                    # 缩略图
)

FACE_HINT = re.compile(
    r"\b(her face|Her face|her profile|Her profile|her expression|Her expression"
    r"|eyes meeting|her eyes|Her eyes|three-quarter|looking at the camera"
    r"|looking straight)\b")
# 金融频道是 POV 不出脸的，但「她的脸不在画面里」这句话本身也带 face 这个词
# （"Her face is not in the composition" / "her face is cropped out" / "turned down and away"），
# 所以必须把这些否定写法全列出来，否则会把 60 条安全镜头全误判成露脸。
FACE_BLOCKED = re.compile(
    r"not readable|unreadable|not shown|never shown|in shadow|silhouette"
    r"|is not visible|not visible|cannot be seen|hidden"
    r"|not in the composition|not in frame|out of frame|cropped"
    r"|turned away|turned down|facing away|the back of her"
    r"|in profile away|obscured|unseen"
    r"|lost in|swallowed by|engulfed|only a shape|an outline", re.I)


def wc(s):
    return len(re.findall(r"[A-Za-z0-9'’\-]+", s))


def she_seg(s, k):
    """切出「她在这个镜头里的位置 / 姿态」那一段故事文字。

    PRESENCE 句之后、风格段之前的那一截。切不出来就返回 None（= 这条没写人物）。
    """
    b = s[k]
    i = b.find(PRESENCE_MARK)
    if i < 0:
        return None
    i = b.find(".", i) + 1          # 跳过 PRESENCE 那一句
    if i <= 0:
        return None
    for m in STYLE_MARKS:
        j = b.find(m, i)
        if j >= 0:
            return b[i:j].strip()
    return None


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

        # 1. PRESENCE 一句话必须在（图片 + 视频都要有）
        for k in ("img_en", "vid_en"):
            c = hit(lambda s, k=k: PRESENCE_MARK in s[k])
            print(f"  {k:7s} PRESENCE  {c}/{n}" + ("" if c == n else "   ✗"))
            fail += 0 if c == n else 1

        # 2. 必须有「她在这一镜」的故事段（不再是空头角色卡）
        for k in ("img_en", "vid_en"):
            c = hit(lambda s, k=k: she_seg(s, k) is not None)
            print(f"  {k:7s} 故事段      {c}/{n}" + ("" if c == n else "   ✗"))
            fail += 0 if c == n else 1

        # 3. 故事段里必须真的提到 she / her（不是只在角色卡里出现）
        def seg_has_she(s, k):
            g = she_seg(s, k)
            return bool(g) and bool(re.search(r"\b(she|her)\b", g, re.I))

        for k in ("img_en", "vid_en"):
            c = hit(lambda s, k=k: seg_has_she(s, k))
            print(f"  {k:7s} 段内含她    {c}/{n}" + ("" if c == n else "   ✗"))
            fail += 0 if c == n else 1

        # 4. 故事段不能太短（短过 8 个词 = 没真写，模型还是会画静物）
        def seg_len(s, k):
            g = she_seg(s, k)
            return wc(g) if g else 0

        for k in ("img_en", "vid_en"):
            short = [s["id"] for s in ss if 0 < seg_len(s, k) < 8]
            print(f"  {k:7s} 段过短      {len(short)}/{n}"
                  + ("" if not short else f"   ✗ {short[:6]}"))
            fail += len(short)

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

        # 6. 露脸镜头占比
        #    两个频道都允许她出脸（用户有参考图），该有脸的地方必须有脸。
        #    阈值：约 30%–80% 之间为合理；过高说明写"portrait"写得过头（失去叙事变化），
        #    过低说明把人物锁死了（2026-08-31 用户原话：「不要把人物脸部锁死」）。
        def face_visible(s):
            g = she_seg(s, "img_en") or ""
            return bool(FACE_HINT.search(g)) and not FACE_BLOCKED.search(g)

        c = hit(face_visible)
        pct = round(c * 100 / n)
        if key == "ai":
            ok = 25 <= pct <= 80
            print(f"  露脸镜头      {c}/{n}（{pct}%）"
                  + ("" if ok else f"   ✗ 应在 25%–80% 之间"))
            fail += 0 if ok else 1
        else:
            # 金融频道：「该有脸的地方有脸」—— 数字 / 表格 / 钞票的特写天然不必露脸。
            # 12% 已经是「不锁死」的信号（曾经是 0%）；再低就要查是不是又把「不露脸」写成规则了。
            ok = 12 <= pct <= 60
            print(f"  露脸镜头      {c}/{n}（{pct}%）"
                  + ("" if ok else f"   ✗ 应在 12%–60% 之间"))
            fail += 0 if ok else 1

        # 7. 词数
        for k in ("img_en", "vid_en"):
            w = [wc(s[k]) for s in ss]
            print(f"  {k:7s} 词数 平均 {sum(w)//n} | 最短 {min(w)} | 最长 {max(w)}")

        # 8. 负面词分流 & 残留
        # 两个频道都用同一张参考图（用户有 jimeng-2026-08-30-2282.png / 4463.png），
        # 负面词统一为「允许她出脸，禁第二个人」。
        v0 = ss[0]["img_en"]
        has_human_face_neg = "human faces" in v0   # 应该都没有
        has_another_person_neg = "another woman" in v0  # 两个频道都应该有
        print(f"  负面词  禁human_faces={has_human_face_neg}  禁another_person={has_another_person_neg}")
        if has_human_face_neg:
            print("   ✗ 提示词里还残留 'human faces' —— 把角色锁死了"); fail += 1
        if not has_another_person_neg:
            print("   ✗ 提示词里缺 'another woman' —— 没禁第二个人"); fail += 1

        allp = [s[k] for s in ss for k in ("img_en", "vid_en")]
        for w in ("headphone", "beanie", "black cap", "hoodie"):
            c2 = sum(1 for v in allp if w in v.lower())
            if c2:
                print(f"   ✗ 残留旧 host 特征 '{w}' x{c2}"); fail += 1
        print("  残留旧 host 特征 0 ✓")

    print("\n" + ("✓ 全部通过" if fail == 0 else f"✗ {fail} 项未通过"))
    return fail


if __name__ == "__main__":
    sys.exit(1 if check() else 0)
