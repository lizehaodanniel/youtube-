# -*- coding: utf-8 -*-
"""金融频道 · 火柴人故事版成片包（@TheMoneyMoo / finance-stick）

按 STICK FIGURE ANIMATION PIPELINE V2 BY PROVENTUBE.docx 的六个状态产出：
    STATE 1 剧本分析 → STATE 2 画风（STYLE 1）→ STATE 3 节奏（4–5 秒 / 10–13 词）
    → STATE 4 beat 拆分 → STATE 5 图片提示词 → STATE 6 动画提示词

和旧版 pov_fin.py 的区别（不是同一个东西，不要互相套用）：
    pov_fin.py    真人 POV 写实风 · 有固定女性 host · 60 镜
    fin_stick.py  火柴人 3D 卡通风 · 四个固定角色（你 / Maya / Devon / Priya）· 88 镜

运行：python3 generate_stick.py
数字口径见 _build/stick_numbers.py，改输入重跑，不手改。
"""
import datetime

from stick_world import (STYLE_LOCK, ENV, CHAR, ENV_CN, CHAR_CN, IMG_TAIL, VID_TAIL,
                         NEGATIVE, img_prompt, vid_prompt, word_count)
import stick_act1
import stick_act2
import stick_act3
import stick_act4

CHANNEL_KEY = "finance-stick"
CHANNEL_LABEL = "金融 · 火柴人故事版（美国观众）(@TheMoneyMoo)"

TOPIC_EN = "POV: It's 1:47 AM And You're Doing The Math Again"
TOPIC_CN = "POV：凌晨 1:47，你又在算那笔账"

BEATS = stick_act1.BEATS + stick_act2.BEATS + stick_act3.BEATS + stick_act4.BEATS

WPS = 2.5          # 每秒词数，文档 STATE 4 的换算基准
CLIP_SEC = 6       # 文档 STATE 6：每条动画片段固定 6 秒

# ============================================================ ① 选题
PICK = {
    "one_liner": "把「先还债还是先投资」这道被讲烂的辩题，改成一个有具体时刻、具体数字、"
                 "三个具体人的故事：同样是 8000 美元，利率一变，正确答案就翻面。",
    "why": [
        {"h": "参考频道已经验证了这个格式",
         "b": "@LucasGrant-usa（14.6K 订阅）近 30 条视频几乎全是 POV 第二人称理财叙事，"
              "「POV: 你用收入的一半生活，悄悄变富，没人发现」5 天 1.5 万播放；"
              "@Inkexplainer96（58.1K 订阅，14 条视频 644 万播放，2026 年 4 月开号）"
              "用的是 2D 动画沉浸式故事，把观众塞进「你一觉醒来变成…」的具体处境。"
              "两者叠加 = 第二人称 POV 选题 + 2D 动画叙事表达。"},
        {"h": "搜索需求常青，不是追热点",
         "b": "「should I pay off debt or invest」每年都在新人身上重演一次。做常青题，"
              "一条视频能吃三年。"},
        {"h": "绝大多数同题视频给的是立场，不是分界线",
         "b": "一半说永远先还债，一半说永远先投资。两边都对，因为两边站在不同的利率区间里说话。"
              "给分界线 = 天然差异化。"},
        {"h": "三个算例天然就是三个角色",
         "b": "Maya 22.15% / Devon 7.14% / Priya 3.5%，本金和月供完全相同，唯一变量是利率。"
              "这组对比不需要任何铺垫就能画出来。"},
        {"h": "结论可复算，禁得起评论区挑刺",
         "b": "所有数字来自 _build/stick_numbers.py，连「7% 这条线」都是二分法解出来的"
              "（打平点 6.77%），不是拍脑袋。"},
    ],
    "demand": "「pay off debt vs invest」是常青搜索意图，长期有量。",
    "gap": "市面内容缺的不是答案，是分界线。给「看你的利率」这种正确但无用的话，"
           "不如给一个具体的数字和一条今晚就能执行的动作。",
    "risk": "风险是把话说死。所以全片明确讲：7% 是长期、税前、平均值，不是保证；"
            "22% 是合同利率，是确定的。把不确定和确定摆在一起，结论才站得住。",
    "verdict": "做。这是本频道最该有的一条「基石视频」——未来所有还债 / 投资内容都可以指向它。",
}

# ============================================================ ② 标题（5 选 1）
TITLES = [
    {
        "title": "POV: It's 1:47 AM And You're Doing The Math Again",
        "cn": "POV：凌晨 1:47，你又在算那笔账",
        "formula": "POV + 具体时刻 + 具体动作",
        "why": "Lucas Grant 频道近 30 条里绝大多数就是这个公式。具体时刻比具体金额更容易对号入座，"
               "因为它卖的不是数字，是「你也这样过」的那一秒。",
        "pick": True,
    },
    {
        "title": "I Ran The Same $8,000 Debt At 3 Rates. The Answer Flipped.",
        "cn": "同一笔 8000 的债，我按三种利率各跑了一遍。答案翻面了。",
        "formula": "穷举动作 + 反转点",
        "why": "「答案会翻面」是最强好奇心钩子之一，而且它在本片里是真的——"
               "Maya 那边还债赢 995，Priya 那边投资赢 204。",
        "pick": False,
    },
    {
        "title": "The 7% Line: Pay Off Debt Or Invest First?",
        "cn": "7% 这条线：先还债还是先投资？",
        "formula": "命名法则 + 原题",
        "why": "给这个辩题起一个名字，让它变成可传播的概念。缺点是情绪偏弱，"
               "适合作为 A/B 测试里的理性版本。",
        "pick": False,
    },
    {
        "title": "Your Minimum Payment Is Not A Payment Plan",
        "cn": "你的最低还款额，不是一个还款计划",
        "formula": "否定常识 + 直接断言",
        "why": "反常识钩子。全片最硬的一个数字就在这一句后面：112 年、83,071 美元利息。"
               "风险是标题里没有「钱」之外的信息量，点击后需要前面几秒立刻兑现。",
        "pick": False,
    },
    {
        "title": "Two People Owe $8,000. One Should Invest. One Shouldn't.",
        "cn": "两个人都欠 8000。一个该去投资，一个不该。",
        "formula": "并列反差 + 悬置判断",
        "why": "并列结构天然逼人看完。缺点是没有点出「为什么」，好奇心全靠画面和前三秒。",
        "pick": False,
    },
]

# ============================================================ ③ 缩略图（3 选 1）
THUMBS = [
    {
        "id": 1,
        "name": "凌晨的厨房 · 手机光打脸",
        "concept": "深夜厨房，主角低头坐在桌前，手机从下方把脸照亮，桌上摊着一张纸。"
                   "画面右侧留白放标题字。",
        "overlay": ["1:47 AM", "$8,000", "$412"],
        "why": "冷色调 + 单一光源是这套画风里最强的构图。三个数字互相打脸，"
               "观众在缩略图阶段就已经开始算账了。",
        "prompt_en": " ".join([
            STYLE_LOCK,
            ENV["kitchen_night"],
            CHAR["you"],
            "He sits hunched at the oak table with both forearms flat on the wood and his head "
            "bowed forward, holding a phone in both hands down at chest height so the screen "
            "throws cold pale light straight up onto his face from below, his eyes wide and his "
            "mouth slightly open. A single sheet of paper lies flat on the table beside his hands. "
            "Camera is a medium close shot from the front at eye level with the warm pendant bulb "
            "burning out of focus directly above his head and the dark kitchen falling away "
            "behind him.",
            IMG_TAIL,
        ]),
    },
    {
        "id": 2,
        "name": "三个人 · 三条光",
        "concept": "Maya / Devon / Priya 并排站在长桌后，每人手按一叠钱，"
                   "三束窗光把三个人各照成一团。",
        "overlay": ["22.15%", "7.14%", "3.5%"],
        "why": "三个角色同时出场，一眼就告诉观众「这是对比型内容」。三个百分数是这条视频的骨架。",
        "prompt_en": " ".join([
            STYLE_LOCK,
            ENV["counting_table"],
            CHAR["maya"], CHAR["devon"], CHAR["priya"],
            "All three stand in a row along the far side of the long oak table, each one resting "
            "both hands flat on top of their own stack of green banknotes, all three looking "
            "straight toward the camera with three different expressions. Maya stands at the left "
            "with her jaw set, Devon in the middle with his shoulders lifted in a shrug, Priya at "
            "the right with her head level and her mouth in a flat unimpressed line. Camera is a "
            "level medium wide shot from the near end of the table looking down its full length, "
            "the brass desk lamp throwing one warm rake of light that touches all three of them "
            "equally while the far end of the hall sinks into deep warm shadow.",
            IMG_TAIL,
        ]),
    },
    {
        "id": 3,
        "name": "黄铜天平 · 一条线",
        "concept": "巨大的黄铜天平立在大厅中央，主角蹲在地上，手指按在粉笔数字线的某一点上。",
        "overlay": ["7%", "WHERE THE ANSWER FLIPS"],
        "why": "全片唯一的「概念画面」。天平 = 二选一，数字线上的一个点 = 分界线，"
               "两者同框就是这条视频的论点。",
        "prompt_en": " ".join([
            STYLE_LOCK,
            ENV["ledger_room"],
            CHAR["you"],
            "He crouches low on the oak floor beside the long chalk number line, pressing the "
            "flat of one hand down onto a single marked point while the other hand braces against "
            "the boards, his head turned to look up at the towering giant brass balance scale "
            "behind him. Camera is a medium wide shot from floor level at the far end of the hall, "
            "the chalk line running from the bottom of frame straight toward the base of the "
            "scale, with warm shafts of window light falling across the floor in broad bands and "
            "dust drifting slowly through every beam.",
            IMG_TAIL,
        ]),
    },
]

FRAMEWORK_ONE_LINER = (
    "第二人称 POV 故事（不教、不劝，只把观众放进一个具体的凌晨）→ 抛出「答案不是立场，是一个数字」"
    " → 同一笔 8000 美元跑三个利率，让三个人的答案自己打起来 → 收在「最低还款才是真正吃掉你的东西」。"
)

ANALYSIS = [
    ("Topic", "同样的 8,000 美元债务、同样的月供 500 美元，利率一变，「先还债还是先投资」"
              "的正确答案就翻面。"),
    ("Niche", "个人理财 / 债务管理。常青搜索意图，每年在新一批背着卡债的观众身上重演一次。"),
    ("Target Audience", "25–40 岁美国上班族，有稳定收入但存款见底，手上有一张 20% 上下的信用卡。"
                        "他们要的不是励志，是一个可以今晚就照做的判断标准。"),
    ("Tone and Mood", "前 5 镜低压、私密、几乎无声；中段转成冷静的实验感（三个人、三组数字）；"
                      "「最低还款」一段转冷、转硬；结尾回到温暖、克制、不煽情。"),
    ("Theme and World", "当代美国。四个被反复使用的真实空间：凌晨的出租屋厨房、黄铜大厅"
                        "（唯一的概念空间，天平 + 粉笔数字线）、三个角色各自的生活场景、"
                        "以及最低还款的「陷阱房」。"),
    ("Recommended Beat Timing", "4–5 秒 / 10–13 词。这是一条 6–7 分钟的中长片，"
                                "论点密度高但情绪需要停留，2–3 秒会切碎，6–7 秒会拖。"),
]


# ============================================================ 组装
def fmt_tc(sec):
    return f"{sec:.1f}s"


def build():
    shots = []
    cursor = 0.0
    for i, b in enumerate(BEATS, 1):
        wc = word_count(b["narr"])
        dur = wc / WPS
        start = cursor
        end = cursor + dur
        cursor = end
        img = img_prompt(b["env"], b["who"], b["act"], b["cam"], b["light"])
        vid = vid_prompt(*b["a"])
        shots.append({
            "id": f"F{i:02d}",
            "sec": 1 if i <= 5 else 2,
            "n": i,
            "window": f"{fmt_tc(start)} – {fmt_tc(end)}",
            "dur": round(dur, 1),
            "wc": wc,
            "en": b["narr"],
            "zh": b["zh"],
            "env": b["env"],
            "env_cn": ENV_CN[b["env"]],
            "who": b["who"],
            "who_cn": "、".join(CHAR_CN[w] for w in b["who"]),
            "img_en": img,
            "vid_en": vid,
        })

    total_words = sum(s["wc"] for s in shots)
    duration = cursor
    mm, ss = divmod(int(round(duration)), 60)

    return {
        "channel_key": CHANNEL_KEY,
        "channel_label": CHANNEL_LABEL,
        "topic": TOPIC_EN,
        "topic_cn": TOPIC_CN,
        "framework_one_liner": FRAMEWORK_ONE_LINER,
        "pick": PICK,
        "style": "STYLE 1 · HYPER REALISTIC 3D CARTOON",
        "beat_timing": "4–5 秒 / 10–13 词（2.5 词每秒）",
        "titles": TITLES,
        "thumbs": THUMBS,
        "analysis": ANALYSIS,
        "char_lock": CHAR,
        "char_cn": CHAR_CN,
        "env_lock": ENV,
        "env_cn": ENV_CN,
        "negative": NEGATIVE,
        "shots": shots,
        "shot_count": len(shots),
        "word_count": total_words,
        "duration": f"{mm}:{ss:02d}",
        "built_at": datetime.date.today().isoformat(),
    }


if __name__ == "__main__":
    p = build()
    print(f'{p["shot_count"]} 镜 / {p["word_count"]} 词 / {p["duration"]}')
    for s in p["shots"][:3]:
        print(f'  {s["id"]} {s["window"]:>16}  {s["wc"]:2d}w  {s["en"]}')
    print("  ...")
    print(f'  图片提示词均长 {sum(word_count(s["img_en"]) for s in p["shots"]) // len(p["shots"])} 词')
    print(f'  视频提示词均长 {sum(word_count(s["vid_en"]) for s in p["shots"]) // len(p["shots"])} 词')
