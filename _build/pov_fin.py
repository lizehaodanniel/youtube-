# -*- coding: utf-8 -*-
"""金融频道 POV 成片源（@TheMoneyMoo）

格式：无出镜、无录屏、无真实证件。全部画面由 AI 生图/生视频，旁白叙事，
Remotion 叠加字幕与数字。

数字全部来自 _build/fin_numbers.py 的实算结果，不手写。核对口径：
  Maya  22.15% → 20 个月 / $1,569 利息 / 对照投资 20 个月收益 $574  → 还债赢 $995
  Devon  7.14% → 17 个月 / $  432 利息 / 对照投资 17 个月收益 $408  → 基本打平 $24
  Priya   3.5% → 17 个月 / $  205 利息 / 对照投资 17 个月收益 $408  → 投资赢 $203
  首月利息 8,000 × 22.15% / 12 = $147.67
  最低还款 2% → 约 100 年 / $75,989 利息
  IRS 2026： elective deferral $24,500
"""

from pov_style import (FIN_IMG_HEAD, FIN_IMG_TAIL, FIN_VID_HEAD, FIN_VID_TAIL,
                       FIN_CHARACTER, FIN_ONCAMERA, FIN_BIBLE,
                       THUMB_HEAD, THUMB_TAIL, build_prompts)

CHANNEL_KEY = "finance"
CHANNEL_LABEL = "金融 · 财经商业（美国观众）(@TheMoneyMoo)"

# ============================================================ ① 选题
TOPIC_EN = "POV: You Make $70,000 And Still Have $412 Saved"
TOPIC_CN = "POV：你年薪 7 万，存款却只有 412 美元"

PICK = {
    "one_liner": "把「先还债还是先投资」这个被讲烂的辩题，改造成一道有明确分界线的数学题："
                 "你的利率是在 7% 上面，还是下面。上面就还债，下面就先拿配比再投资。",
    "why": [
        {"h": "搜索需求是常青的，不是追热点",
         "b": "「should I pay off debt or invest」这类词在美国区 YouTube 和 Google 上常年有量，"
              "因为它每年都在新人身上重演一次。做常青题，一条视频能吃三年。"},
        {"h": "绝大多数同题视频给的是立场，不是分界线",
         "b": "搜一圈你会发现，一半的视频说「永远先还债」，另一半说「永远先投资」。"
              "两边都对，因为两边都在自己的利率区间里说话。给分界线 = 天然差异化。"},
        {"h": "POV 格式把「说教」变成「照镜子」",
         "b": "参考频道 POV Finance 的 21:50 长片，8 天 11.4 万播放——"
              "它全程没有教你做任何事，只是把观众放进一个具体的处境里。第二人称是这个格式的引擎。"},
        {"h": "全部画面可 AI 生成，不依赖任何外部素材",
         "b": "不出现真实账单、银行 App、401(k) 后台。既解决了找不到素材的问题，"
              "也避开了隐私和合规风险。"},
        {"h": "结论可复算，禁得起评论区挑刺",
         "b": "三个案例的数字全部来自 fin_numbers.py 的月度复利实算，"
              "任何人在评论区拿计算器对，结论都不会变。"},
    ],
    "demand": "「pay off debt vs invest」是常青搜索意图；本频道选题盘里它同时出现在下拉词、"
              "评论区与 Reddit 三个来源，属于交叉验证过的需求。",
    "gap": "市面内容缺的不是答案，是**分界线**。给「看你的利率」这种正确但无用的话，"
           "不如给一个具体的数字（7%）和一条可以今晚执行的动作。",
    "risk": "风险是把话说死。所以全片两次强调：7% 是长期、税后前、且是平均值不是保证；"
            "22% 是合同利率，确定的。把不确定性和确定性摆在同一屏上，结论才站得住。",
    "verdict": "做。这是本频道最该有的一条「基石视频」——"
               "未来所有还债/投资相关的内容都可以指向它。",
}

# ============================================================ ② 标题（5 选 1）
TITLES = [
    {
        "title": "POV: You Make $70,000 And Still Have $412 Saved",
        "cn": "POV：你年薪 7 万，存款却只有 412 美元",
        "formula": "POV + 具体收入 + 具体余额",
        "why": "两个具体数字互相打脸，制造「说的就是我」的代入感。"
               "POV 前缀本身在首页信息流里就是一个高识别度标签。",
        "pick": True,
    },
    {
        "title": "The 7% Rule: Pay Off Debt or Invest First?",
        "cn": "7% 法则：先还债还是先投资？",
        "formula": "命名法则 + 原题",
        "why": "给这个辩题起一个名字，让它变成可传播的概念。"
               "缺点是不带情绪，适合作为 A/B 测试里的理性版本。",
        "pick": False,
    },
    {
        "title": "I Compared Every Interest Rate. The Answer Flips At 7%.",
        "cn": "我把每种利率都算了一遍，答案在 7% 处反转",
        "formula": "穷举动作 + 反转点",
        "why": "「答案会反转」是最强的好奇心钩子之一，且它是真的——"
               "Maya 那边还债赢 $995，Priya 那边投资赢 $203。",
        "pick": False,
    },
    {
        "title": "Your Credit Card Is Charging You $147 A Month (Here's The Math)",
        "cn": "你的信用卡每月收你 147 美元（这是算法）",
        "formula": "具体金额 + 承诺给算法",
        "why": "$147 是 8,000 余额 × 22.15% ÷ 12 的真实结果。"
               "具体金额比「高利率」有力十倍。风险是容易被误读成恐吓，"
               "所以全片第 2 段先用一整段拆掉羞耻感。",
        "pick": False,
    },
    {
        "title": "POV: You Finally Looked At Your APR",
        "cn": "POV：你终于看了一眼自己的 APR",
        "formula": "POV + 一个微小动作",
        "why": "最短、最有余味的一个。缺点是信息量低，点击率依赖缩略图配合。"
               "留给 A/B 测试。",
        "pick": False,
    },
]

# ============================================================ ③ 缩略图（3 张）
THUMBS = [
    {
        "id": 1,
        "name": "A 版 · 数字对撞（首选）",
        "concept": "一只手举着一张信用卡，卡片上方悬浮两个巨大数字：左边 22%（琥珀色，"
                   "像在燃烧），右边 7%（冷青色）。中间一道竖向裂缝把画面劈成两半。",
        "overlay": ["22%", "7%", "（底部一行小字）ONE OF THESE IS A CONTRACT"],
        "why": "两个数字对撞是这类内容点击率最高的结构。加「其中一个是合同」这一行字，"
               "把纯信息图变成一个问题。",
        "core": ("A single hand, seen from the wrist down, holding one plain matte-black credit card "
                 "vertically between thumb and forefinger, the card filling the right third of the frame. "
                 "The card is blank with no text and no numbers. The background is split vertically down "
                 "the middle: the left half is warm amber and orange, the right half is cold teal and "
                 "slate blue, the two halves separated by a thin glowing seam. "
                 "The amber side is lit from below like heat, the teal side is lit flat and cold. "
                 "Extreme contrast, deep shadows, the hand is rim-lit by both colors at once. ")
                 + THUMB_TAIL,
    },
    {
        "id": 2,
        "name": "B 版 · 空钱包与满罐（故事版）",
        "concept": "桌面上一只翻开的空钱包，旁边一只玻璃罐里堆满折起来的钞票。"
                   "钱包在暗处，玻璃罐被一束暖光照亮。",
        "overlay": ["$412", "（箭头）", "（底部）THE SAME PERSON"],
        "why": "讲「同一个人，两种结局」的故事感，情绪拉得更满。"
               "$412 这个数字足够小、足够具体，会让人停下来。",
        "core": ("A dark wooden tabletop seen from a low three-quarter angle. "
                 "On the left, an open empty brown leather wallet lying flat, its compartments visibly empty, "
                 "sitting in deep shadow. On the right, a large clear glass jar packed tightly with folded "
                 "banknotes, catching a single warm shaft of light from the upper right, the bills glowing amber. "
                 "A strong diagonal shaft of daylight cuts across the whole scene from the top right corner. "
                 "The left half of the frame is almost black, the right half is warm and bright. "
                 "The wallet and jar are roughly equal in size, creating a clear visual comparison. ")
                 + THUMB_TAIL,
    },
    {
        "id": 3,
        "name": "C 版 · 分界线（概念版）",
        "concept": "一条横贯画面的发光水平线，线上方是密集的红色数字雨向下坠，"
                   "线下方是稀疏的绿色向上箭头。线本身标着 7%。",
        "overlay": ["7%", "（线上）PAY IT OFF", "（线下）INVEST IT"],
        "why": "最高级也最抽象的一版。适合频道已经有一定认知度后使用——"
               "它卖的是「我有一条法则」，不是「我有一个故事」。",
        "core": ("A dark, almost black abstract space with a single horizontal glowing line running "
                 "straight across the middle of the frame, the line emitting a warm amber light. "
                 "Above the line, dozens of small glowing red-orange particles and thin vertical streaks "
                 "are falling downward, dense and chaotic. "
                 "Below the line, a few clean green upward-pointing arrows are rising in an orderly rhythm. "
                 "Sharp separation between the two halves, dramatic contrast, volumetric light, "
                 "dark cinematic background with no clutter, no readable type anywhere. ")
                 + THUMB_TAIL,
    },
]
for _t in THUMBS:
    _t["prompt_en"] = THUMB_HEAD + _t["core"]
    _t["prompt_cn"] = "（中文说明见「概念」与「叠加文字」两栏；生图时直接复制英文提示词即可，中文仅用于你理解画面。）"

# ============================================================ ④ 框架（8 段）
FRAMEWORK = [
    {"id": 1, "name": "设局 The Setup", "window": "0:00–1:12",
     "job": "把观众放进一个具体到不能再具体的人生切片，全程不说教。",
     "line": "You're thirty. You make seventy thousand. You have four hundred and twelve dollars.",
     "points": ["用三个具体数字开场，不用形容词",
                "先说「你不是不努力」，把观众的防御卸掉",
                "结尾给承诺：一个数字，一条规则，11 分钟"],
     "risk": "最容易被跳过的一段。所以前三句必须每一句都带一个新数字。"},
    {"id": 2, "name": "否认 It Wasn't Laziness", "window": "1:12–2:34",
     "job": "拆掉羞耻感，并指出钱消失的三个真实位置。",
     "line": "Money doesn't leave your life in drips. It leaves in three large, automatic transactions.",
     "points": ["先承认「拿铁理论」的失败，观众才听得进去",
                "三个漏点：利息 / 升级过的生活方式 / 从未到手的钱",
                "只承诺解决第一个——收窄范围，提高可信度"],
     "risk": "这一段容易显得说教。口语用「你被告诉过」而不是「你应该」。"},
    {"id": 3, "name": "第一个数字 The 22%", "window": "2:34–4:02",
     "job": "把利息从抽象百分比变成每月可以感知的金额。",
     "line": "Twenty-two percent of every unpaid dollar, every year, compounding monthly.",
     "points": ["给官方出处：Fed G.19 的当期发布页",
                "关键提醒：索引页只是日历，表格在带日期的页面里",
                "落地成 $147/月——这一步是全片最重要的翻译"],
     "risk": "数字来源必须说清是「当期数据」，并提醒观众自己核对数据月份。"},
    {"id": 4, "name": "第二个数字 The 7%", "window": "4:02–5:30",
     "job": "把对比项讲完整，尤其是它的三个限定条件。",
     "line": "You're not comparing seven to twenty-two. You're comparing a maybe to a certain.",
     "points": ["7% = 长期、扣通胀后、税前，三个限定词一个都不能省",
                "强调它是平均值不是保证，而信用卡利率是合同",
                "结尾抛出反转预告，防止中段掉线"],
     "risk": "不能把 7% 说成保守估计就算完，必须说它为什么不保证。"},
    {"id": 5, "name": "三个人的故事 Three Lives", "window": "5:30–7:24",
     "job": "只改利率一个变量，让结论自己浮出来。",
     "line": "Three people. Same debt. Same cash. One thing is different.",
     "points": ["Maya 22.15% → 还债赢 $995",
                "Devon 7.14% → 打平，只差 $24",
                "Priya 3.5% → 投资赢 $203",
                "三个数字共同指向同一条分界线"],
     "risk": "三个人必须真的只有一个变量不同，否则观众会觉得你在操纵。"},
    {"id": 6, "name": "加速器 The Free 100%", "window": "7:24–8:56",
     "job": "给出比两边都强的第三选项，并说清它的代价。",
     "line": "A one hundred percent return, on day one, in writing. And it expires every paycheck.",
     "points": ["401(k) 配比是写在计划文件里的 100% 回报",
                "看两行：配比公式 与 归属时间表（vesting）",
                "$60k 年薪下的实算：$3,600 自己出，雇主补 $1,800",
                "IRS 2026 上限 $24,500，但配比只看你的缴费，不看上限"],
     "risk": "配比条款每家不同，必须反复强调「看你自己那份计划文件」。"},
    {"id": 7, "name": "时间线 Twenty Years", "window": "8:56–10:12",
     "job": "把规则翻译成今晚 / 本月 / 之后 三个动作。",
     "line": "Above seven, kill the debt. Below seven, take the match first, then invest the rest.",
     "points": ["先给一句话规则，让人能记住",
                "再拆成三个时间点的具体动作",
                "「今晚」这个动作必须小到 10 分钟能做完"],
     "risk": "规则讲完观众就想走了。用「rules don't survive a bad week」把人拉回来。"},
    {"id": 8, "name": "收口 Tonight", "window": "10:12–11:30",
     "job": "用一个极端对比收尾，把行动压缩到今晚十分钟。",
     "line": "The minimum payment is not a payment plan. It's a subscription to the debt.",
     "points": ["最低还款 2% → 约 100 年 / $75,989 利息",
                "对照 $500/月 → 20 个月还清，同一笔债同一个人",
                "CTA 只做一件事：今晚查 APR，和 7 比"],
     "risk": "不要在这段加第二个 CTA。一个 CTA 的转化率远高于三个。"},
]

# ============================================================ ⑤ 分镜（60 镜）
# (段, 窗口, 英文口播, 中文口播, 画面, 情绪/节奏, 动效, img_core, vid_core)
_SHOTS = [

# ---------- S1 设局 ----------
(1, "0:00–0:10",
 "You're thirty years old. You make seventy thousand dollars a year. And right now, you have four hundred and twelve dollars in your bank account.",
 "你三十岁。年薪七万美元。而现在，你的银行账户里，有四百一十二美元。",
 "凌晨五点四十的厨房，一杯没喝完的凉咖啡，手机反扣在台面上，屏幕边缘漏出一线蓝光。",
 "开场三句，每句一个新数字。语速压到最慢，句子之间留足一秒空白。",
 "push-in",
 "A dim kitchen at five-forty in the morning, a half-full ceramic mug of coffee gone cold, a faint skin formed on the surface, a condensation ring dried into the oak countertop. A smartphone lies face-down beside it, a thin edge of blue light bleeding onto the wood. Venetian blinds cast hard horizontal stripes of pre-dawn grey-blue light across the wall. Dust motes drift in a single shaft.",
 "slowly push the camera straight in toward the mug and the phone, closing about twelve percent over the shot, no lateral movement"),

(1, "0:10–0:21",
 "You're not reckless. You're not lazy. You pay every bill on time. You have never once missed a payment.",
 "你不鲁莽，也不懒。你每一笔账单都按时付。你一次都没有逾期过。",
 "一双手在整理一叠信封，动作很稳，把它们按到期日排成一列。",
 "语气从陈述转成辩护——像是在替观众对别人说这句话。",
 "drift-right",
 "A pair of hands, forearms visible, sleeves of a soft grey worn cotton sweater, neatly arranging a row of cream-white envelopes on a pale wooden table. The hands move with calm precision, aligning each envelope edge to edge. Late afternoon light from a window on the left rakes across the table, picking up the paper fibre and the weave of the sweater. Shallow focus, the far end of the row falls out of focus.",
 "pan the camera slowly to the right along the row of envelopes, following the direction the hands are working, smooth and unhurried"),

(1, "0:21–0:33",
 "You've done everything you were told to do. And somehow, at the end of every single month, there is nothing left.",
 "让你做的每一件事，你都做了。可不知道为什么，每个月月底，什么都不剩。",
 "日历翻到最后一天，桌面上一只空的玻璃杯，旁边是一张对折的工资单。",
 "「and somehow」要说得轻，像困惑而不是控诉。",
 "push-in",
 "A clean minimal desk seen from a high three-quarter angle, a wall calendar flipped to the final day of the month, one corner curling. Beside it an empty drinking glass with a dried watermark ring at the bottom, and a single folded payslip, the fold creased but the paper blank. Cool flat window light from the right, long soft shadow cast to the left. Everything is tidy, nothing is chaotic.",
 "push the camera slowly and straight into the calendar page, letting the glass and payslip drift toward the edge of frame"),

(1, "0:33–0:46",
 "Here's what nobody says out loud: this isn't a discipline problem. It's a math problem. And the math has a number in it you've probably never looked at.",
 "有一句话没人说出口：这不是自制力的问题，这是一道数学题。而这道数学题里有一个数，你可能从来没看过。",
 "一扇门缝里透出光，光落在地板上形成一条细长的亮带。",
 "全片第一次转向。「a number you've never looked at」是第一个钩子收口。",
 "push-in",
 "A dark hallway at night, a single interior door standing ajar by about ten centimetres, a blade of warm amber light spilling from the gap onto a dark hardwood floor and cutting a long thin trapezoid across it. The rest of the hallway is in deep teal shadow. Fine dust is visible suspended in the light blade. Nothing else in frame, no furniture, complete stillness.",
 "push the camera slowly straight toward the gap in the door, the light blade widening very slightly as we approach"),

(1, "0:46–0:58",
 "In the next eleven minutes I'm going to show you that number, and then I'm going to show you exactly what to do with it.",
 "接下来的十一分钟，我会把这个数字指给你看，然后告诉你拿它怎么办。",
 "一双手摊开一张空白的纸，纸上是空的，等待被写。",
 "给出承诺。语速稍微加快，进入「我要开始了」的节奏。",
 "hold",
 "A pair of hands holding a single sheet of blank heavyweight cream paper, open and flat, presented toward the camera at a slight angle. The paper is completely blank. Behind it, a dark blurred room with one warm table lamp out of focus creating a soft amber bokeh circle in the upper right. The hands are lit from the front by cool window light and rimmed warm from behind.",
 "hold the camera almost perfectly still with only a very slight two percent creep forward, the paper trembling almost imperceptibly"),

(1, "0:58–1:06",
 "No budgeting apps. No spreadsheets to download. No course.",
 "不用记账 App。不用下载表格。没有课程。",
 "三样东西被依次推到画面外：手机、笔记本电脑、一个信封。",
 "节奏变短促，三连否定。每一句一个切点，语气略带好笑。",
 "drift-right",
 "A clean empty desk surface, cool grey light. Three objects sit in a row waiting: a smartphone face-down, a closed laptop, and a sealed envelope. The surface is pale birch with visible grain. A single overhead pendant lamp casts a soft pool of light from above, leaving the edges of the desk in shadow. No clutter, no cables, nothing else on the desk.",
 "pan slowly right across the three objects in sequence, pausing imperceptibly on each one"),

(1, "1:06–1:12",
 "Just one number, and one rule.",
 "只有一个数字，和一条规则。",
 "画面收束到一只手，食指在一张纸上点了一下。",
 "全片最短的一句，说完留两秒静默再进下一段。",
 "hold",
 "Extreme close-up of a single index finger tapping once on the surface of blank cream paper, the fingertip catching a warm highlight. The paper fills the frame, its fibre texture sharply visible. Behind the finger, everything falls into a soft dark blur. Very shallow depth of field, one warm light source from the upper left, the rest of the frame in cool shadow.",
 "hold completely still, only the faintest ambient grain movement, the finger does not move again"),

# ---------- S2 否认 ----------
(2, "1:12–1:25",
 "First, let's kill the shame, because shame is what keeps people from looking.",
 "先说一件事：把羞耻感拿掉。因为正是羞耻感，让人不肯去看那张账单。",
 "一只手把一张纸翻过去盖住，动作很轻，像是不忍心看。",
 "语气放软。这一段是在替观众说话，不是在教观众。",
 "push-in",
 "A hand turning a single sheet of paper face-down on a wooden table, the motion caught mid-turn. The paper is blank on both sides. Warm late-afternoon light enters from a window behind, backlighting the paper so its edge glows. The table surface is worn oak with old scratches. A ceramic mug sits out of focus in the background. The mood is gentle, not dramatic.",
 "push the camera slowly in as the hand releases the paper and withdraws out of frame"),

(2, "1:25–1:38",
 "You have been told your whole life that being broke is a character flaw. That it's lattes. That it's avocado toast.",
 "你这辈子一直被告诉：没钱是性格问题。是拿铁的问题。是牛油果吐司的问题。",
 "桌上摆着三样小东西：一杯外带咖啡、一片吐司、一张收据——都很干净、很普通。",
 "这里允许一丝讽刺，但不要刻薄。讽刺的对象是那套说法，不是观众。",
 "drift-right",
 "A small wooden café table seen from above at a slight angle. Three ordinary objects arranged in a loose triangle: a plain white takeaway coffee cup with a brown cardboard sleeve, a single slice of toast on a small ceramic plate, and a folded paper receipt. Soft natural light from the upper left, gentle shadows, warm neutral tones. Everything is clean, modest, and completely unremarkable.",
 "pan slowly right across the three objects, letting them pass out of frame one at a time"),

(2, "1:38–1:52",
 "So you cut the small things. You bring lunch. You cancel one streaming service. And your bank account does not move.",
 "于是你砍掉了那些小东西。自己带饭。退订一个流媒体。然后你的银行账户纹丝不动。",
 "一只手在冰箱里拿出一只饭盒，放到台面上；旁边一台电视是暗的。",
 "「does not move」四字要说得极慢，重音落在 move。",
 "push-in",
 "An open refrigerator door seen from the side, cool white interior light spilling out into a dim kitchen. A hand reaches in and lifts out a simple rectangular food container with a clear lid. On the counter beside the fridge, a dark television screen sits black and reflective, catching a faint blue-grey sheen. The kitchen is tidy and ordinary, late evening, no other light on.",
 "push the camera slowly toward the container as the hand sets it down on the counter"),

(2, "1:52–2:05",
 "Because the small things were never the leak. Money doesn't leave your life in drips. It leaves in three large, automatic, invisible transactions.",
 "因为那些小东西从来就不是漏点。钱不是一滴一滴漏掉的。它是通过三笔巨大的、自动的、你看不见的交易离开的。",
 "一根水管接在一个几乎看不见的接口上，水从接缝处稳定地渗出，在地面形成一小片水光。",
 "这是第二段的核心句。说到「three large」时画面要给一个停顿。",
 "push-in",
 "Close-up of a copper pipe joint in a dim basement, a thin but steady thread of water seeping from the seam and running down the pipe, pooling into a small dark reflective puddle on a concrete floor below. A single bare bulb hangs out of focus in the background casting a hard warm pool of light. The concrete is rough and stained. Deep teal shadows fill the surrounding space.",
 "push the camera slowly in toward the seam, the water thread catching the light as it moves"),

(2, "2:05–2:18",
 "One is interest. One is the version of your lifestyle you upgraded and never went back on. And one is the money you never see, because it never reaches your paycheck.",
 "一个是利息。一个是你升级之后再也没降回去的生活方式。还有一个是，你从来没见过的钱——因为它根本没到过你的工资条上。",
 "三个并排的空玻璃罐，第一个在滴水，第二个里放着一把车钥匙，第三个是空的、落了灰。",
 "三个漏点各停半秒。说到「never reaches your paycheck」时语气最轻。",
 "drift-right",
 "Three identical clear glass jars standing in a row on a plain wooden shelf against a dark wall. The first jar has a few drops of water sliding down its inner wall. The second contains a single set of car keys resting at the bottom. The third is completely empty with a fine layer of dust on its glass. A single warm light from the left rakes across the jars, each casting a long shadow to the right.",
 "pan slowly to the right across all three jars, holding briefly on each one"),

(2, "2:18–2:28",
 "Only the first one is a math problem you can solve this evening.",
 "这三笔里，只有第一笔，是一道你今晚就能解开的数学题。",
 "三只罐子里只有最左那只被一盏小灯照亮，另外两只退回暗处。",
 "收窄范围。这一句是全片可信度的支点——只承诺能做到的事。",
 "push-in",
 "The same three glass jars on the shelf, but now only the leftmost jar is lit by a small warm lamp just outside the frame, its glass glowing amber and the water drops inside catching the light. The other two jars have fallen into deep shadow and are barely visible. The dark wall behind is almost black. Strong contrast between the lit jar and the darkness.",
 "push the camera slowly in toward the lit jar until it fills most of the frame"),

(2, "2:28–2:34",
 "So let's start there.",
 "那就从它开始。",
 "手指落在罐子的玻璃上，画面在接触的瞬间定住。",
 "六个字，说完立刻切。这是段落之间的呼吸口。",
 "hold",
 "Extreme close-up of a fingertip touching the cool glass surface of the lit jar, a small circle of warmth spreading where the skin meets the glass, faint condensation around the contact point. The jar's curved glass fills the frame, catching a warm highlight along its rim. Everything behind is a soft dark amber blur.",
 "hold perfectly still, only the faintest drift of ambient dust in the light"),

# ---------- S3 第一个数字 ----------
(3, "2:34–2:47",
 "Open the Federal Reserve's consumer credit release. It's called the G.19, and it comes out once a month.",
 "打开美联储的消费者信贷报告。它叫 G.19，每个月发布一次。",
 "一双手翻开一份厚重的官方文件，纸边整齐，页眉处是空白的（真实文字由 Remotion 叠）。",
 "进入数据段。语气变成「我带你走一遍」的向导感，不要念稿腔。",
 "push-in",
 "A pair of hands opening a thick bound government report on a wide desk, the paper heavy and cream-coloured with a clean printed header block that is completely blank. A desk lamp with a brass arm casts a warm pool of light from the upper left. The desk is dark walnut. Behind, a blurred bookshelf. The scene feels institutional but warm, like a library at night.",
 "push the camera slowly in toward the open page as the hands smooth it flat"),

(3, "2:47–3:00",
 "Go to the dated release page, not the index — the index is just a calendar of dates with no tables on it.",
 "要进带日期的当期发布页，不是那个索引页——索引页只是一列日期，上面一张表都没有。",
 "两页并排：左边是一列密密麻麻的日期链接，右边是带表格的页面。左边的日期是空白的。",
 "这一句是给真去查的人的。说得具体、说得像提醒朋友。",
 "drift-right",
 "Two documents side by side on a desk seen from above. On the left, a page that is entirely a long vertical list of blank date lines with no other content, printed on plain white paper. On the right, a page filled with the blank grid structure of a data table, ruled rows and columns with no text. A single warm desk lamp lights both from above. The contrast between the empty list and the structured grid is obvious.",
 "pan slowly from the left page across to the right page, settling on the table grid"),

(3, "3:00–3:12",
 "Find the table called Terms of Credit, then Commercial bank interest rates, then Credit card plans.",
 "找到叫 Terms of Credit 的表，然后是 Commercial bank interest rates，然后是 Credit card plans。",
 "手指沿着表格左侧往下移动，停在其中一行；那一行是空白的。",
 "三个层级说清楚，别跳。观众是照着做的。",
 "push-in",
 "Close-up of a finger tracing slowly down the left margin of a wide printed data table, moving past several ruled rows before stopping at one specific row. The row is blank. The paper is aged white with a faint ruling grid. Warm directional light from the left creates a soft shadow under the finger. The surrounding rows are slightly out of focus.",
 "push the camera slowly in as the finger comes to rest on the row"),

(3, "3:12–3:26",
 "As of the most recent quarter, accounts that were actually charged interest sat at twenty-two point one five percent.",
 "截至最近一个季度，真正被计息的账户，利率是百分之二十二点一五。",
 "那只手停住的那一行，被一束侧光打亮。（数字 22.15% 由 Remotion 叠加，图里不烧字）",
 "第一次报出这个数字。说完停一拍，让观众反应。",
 "hold",
 "Close-up of a single ruled row in a printed data table, the paper filling the frame. A narrow blade of warm side-light rakes across that one row, leaving the rows above and below it in soft shadow. The paper fibre and the ink-free ruled lines are visible in sharp detail. Nothing on the page is readable. The rest of the scene is a dark warm blur.",
 "hold perfectly still, the light blade does not move, only film grain breathes"),

(3, "3:26–3:40",
 "Twenty-two. Not twenty-two dollars. Twenty-two percent of every unpaid dollar, every single year, compounding monthly.",
 "二十二。不是二十二美元。是你每一块没还的钱，每一年要交百分之二十二，而且是按月复利。",
 "一枚硬币立在桌面上，背后是 12 个等距的小刻度在缓慢延伸。",
 "「Not twenty-two dollars」是防误解的补丁，一定要说。",
 "push-in",
 "A single coin standing upright on its edge on a dark wooden tabletop, caught in a shaft of warm light. Behind it, twelve small evenly spaced marks are pressed into the wood in a receding line, each one slightly smaller as it moves away into the shadow. The background is deep teal darkness. The coin is rim-lit, its edge catching a bright amber highlight against the dark.",
 "push the camera slowly in toward the upright coin, the row of marks sliding past on either side"),

(3, "3:40–3:52",
 "Now translate that into something you can feel. On a balance of eight thousand dollars, twenty-two percent is about one hundred and forty-eight dollars in the first month alone.",
 "现在把它翻译成你能感觉到的东西。八千美元的余额，百分之二十二的利率，光第一个月，就是大约一百四十八美元。",
 "一叠钞票里，最上面那几张被一只手抽走，剩下的那叠没有变厚。",
 "这是全片最重要的一次翻译。说到 $148 时停顿最长。",
 "push-in",
 "A stack of banknotes lying on a dark tabletop seen from a low angle. A hand enters from the right and lifts away the top few notes. The remaining stack is visibly no thicker than before. Warm light from a single lamp on the left catches the edges of the paper. The background is a soft dark blur with one out-of-focus warm highlight. The mood is matter-of-fact, not sad.",
 "push the camera slowly in toward the remaining stack as the hand withdraws out of frame"),

(3, "3:52–4:02",
 "That is the leak. Not the latte.",
 "这才是漏点。不是那杯拿铁。",
 "那只外带咖啡杯被轻轻推到画面边缘，虚焦。",
 "八个英文词，全片第一处真正的「重击」。说完立刻切。",
 "hold",
 "The white takeaway coffee cup standing alone on the wooden table, now pushed toward the edge of the frame and thrown completely out of focus, its white shape a soft blurred blob against a dark warm background. The background holds a single out-of-focus amber highlight. Everything is still. The cup is clearly no longer the subject.",
 "hold completely still, no camera movement at all"),

# ---------- S4 第二个数字 ----------
(4, "4:02–4:14",
 "Now the number on the other side. The number you've been told to chase: seven percent.",
 "现在说另一边的数字。那个你一直被告知要去追的数字：百分之七。",
 "画面从暖色切到冷色。一扇窗，外面是灰蓝的天。",
 "色彩第一次明显转冷。观众会感到「换了一边」。",
 "pull-out",
 "A window seen from inside a dim room, tall and narrow, looking out onto a flat pale grey-blue sky with no detail. A thin curtain hangs motionless at the left edge. The window frame is painted off-white and slightly worn. The interior of the room is much darker than the window, creating a clean silhouette. Cool flat light fills the frame with almost no warmth.",
 "pull the camera slowly straight back from the window, revealing more of the dark room around it"),

(4, "4:14–4:26",
 "Seven percent is the long-run average return of the US stock market, after inflation, before tax. Say it out loud with all three qualifiers.",
 "百分之七是美国股市的长期平均回报，扣掉通胀之后、扣掉税之前。说这句话的时候，三个限定词一个都不能省。",
 "三块透明玻璃板叠在一起，每块上都有一层薄雾，叠得越多越看不清。",
 "「all three qualifiers」要一字一顿。这是在教观众怎么识破别人的数字。",
 "push-in",
 "Three sheets of frosted glass stacked with a small gap between each, standing upright on a dark surface and lit from behind by a cool cyan light. Each sheet adds a layer of diffusion, so the light behind becomes progressively softer and less distinct through the stack. The edges of each sheet catch a thin bright rim. The background is near-black. Clean, precise, almost laboratory-like.",
 "push the camera slowly in toward the stack of glass sheets, the diffusion deepening as we approach"),

(4, "4:26–4:38",
 "Long-run: it means twenty years, not twenty months. After inflation: the real number on your statement is higher and buys less. Before tax: you don't keep all of it.",
 "长期：是二十年，不是二十个月。扣掉通胀：你账单上的数字更大，但买到的更少。税前：你拿不到全部。",
 "三个画面元素依次被照亮：一条很长的刻度尺 / 一只缩水的购物袋 / 一把剪刀把一张纸剪掉一角。",
 "三个短句，节奏一样，形成排比。每句配一个视觉。",
 "drift-right",
 "Three small objects arranged in a row on a dark stone surface, each with its own small pool of cool light: a long wooden ruler receding into darkness, a deflated paper shopping bag collapsed in on itself, and a pair of steel scissors with a corner of blank paper resting between the blades. The background is black. Each object is sharply lit and separated from the next by darkness.",
 "pan slowly to the right across the three objects, holding briefly on each pool of light"),

(4, "4:38–4:50",
 "And the one that matters most: it's an average, not a guarantee. Some years it's up thirty. Some years it's down twenty.",
 "而最关键的一点：它是平均值，不是保证。有些年份涨三十，有些年份跌二十。",
 "一条起伏的曲线被投影在墙上——但曲线是空白的轮廓，没有数字。",
 "「average, not a guarantee」是这一段的核心，重音放在 guarantee。",
 "drift-right",
 "A plain white wall in a dark room, with a smooth undulating band of soft cyan light projected across it, rising and falling in several gentle peaks and troughs. The band has no numbers, no grid, no labels. The wall texture is visible in the lit areas. The room around is black. The light band looks organic and unstable, faintly wavering at the edges.",
 "pan slowly to the right following the undulating band of light along the wall"),

(4, "4:50–5:02",
 "Your credit card rate is not an average. It's a contract. It does not have a bad year.",
 "而你的信用卡利率不是平均值。它是一份合同。它不会有坏年份。",
 "同一面墙上，那道起伏的光带被一道笔直的、锐利的、不动的琥珀色光线取代。",
 "全片最强的一句对比。画面从「波动的青」直接切到「平直的琥珀」。",
 "hard",
 "The same dark room and white wall, but now a single perfectly straight horizontal line of hard amber light cuts across it, sharp-edged, unwavering, and absolutely level. The line is thin and intense, casting a clean falloff above and below. The wall texture is crisp in its glow. The surrounding room remains black. The light does not move or flicker in any way.",
 "hold the camera completely still, the amber line is perfectly static and unchanging"),

(4, "5:02–5:14",
 "So you're not comparing seven to twenty-two. You're comparing a maybe to a certain.",
 "所以你不是在拿七和二十二比。你是在拿「也许」和「一定」比。",
 "天平的两端：一端是一团会飘散的雾，另一端是一块实心铁块。",
 "这一句是这一段的收口金句。说完留一秒。",
 "push-in",
 "A simple balance scale standing on a dark stone table, seen slightly from the side. On the left pan rests a loose mass of pale drifting vapour that is slowly dissipating. On the right pan sits a single solid block of dark iron, heavy and unmoving. The left pan is tilted high, the right pan is weighted down. A single cool light from above, deep shadows below. The contrast between vapour and iron is the whole point.",
 "push the camera slowly in toward the centre column of the scale, both pans staying in frame"),

(4, "5:14–5:30",
 "But here's the part almost every video skips: the moment your debt is cheaper than seven percent, the answer flips completely. I'll show you exactly where.",
 "但有一件事几乎所有视频都跳过了：当你的债务利率低于百分之七的那一刻，答案会彻底反过来。我等下会指给你看，反在哪里。",
 "那道琥珀色的直线，从中间开始，向下弯折成一个明显的折角。",
 "中段的保命钩子。没有它，一半观众会在第 5 分钟走掉。",
 "push-in",
 "The same straight amber line of light on the dark wall, but now it has a sharp kink in the middle where it angles downward in a clean decisive bend, the two halves meeting at a single bright vertex. The line is otherwise sharp and unwavering. The vertex glows slightly brighter than the rest of the line. The room is black around it.",
 "push the camera slowly in toward the bright vertex where the line bends"),

# ---------- S5 三个人的故事 ----------
(5, "5:30–5:42",
 "Three people. Same eight thousand dollars of debt. Same five hundred dollars a month of extra cash. One thing is different.",
 "三个人。同样是八千美元的债务。同样是每月五百美元的余钱。只有一件事不一样。",
 "三张并排的卡片，前两张完全相同，第三张上有一个不同的标记。",
 "进入全片核心。语速提起来，变成「我给你讲个东西」的节奏。",
 "drift-right",
 "Three identical blank index cards lying in a neat row on a dark tabletop, seen from above at a slight angle. The first two cards are exactly the same. On the third card sits a single small brass object, the only difference between them. Warm directional light from the upper left casts three parallel shadows to the right. The table is dark wood with visible grain. Nothing else is in frame.",
 "pan slowly to the right across the three cards, settling on the third one with the object on it"),

(5, "5:42–5:54",
 "Maya's rate is twenty-two point one five percent. Devon's is seven point one four — a new car loan. Priya's is three point five — a student loan.",
 "Maya 的利率是百分之二十二点一五。Devon 是百分之七点一四，一笔新车贷。Priya 是百分之三点五，一笔学生贷。",
 "三件物品依次落位：一张信用卡、一把车钥匙、一顶学士帽的流苏。",
 "三个人名要说得像真人，不要念成 ABC。每个名字后停半拍。",
 "drift-right",
 "Three objects arranged in a row on a dark surface, each in its own pool of light: a plain matte-black credit card, a single car key fob, and a graduation tassel with a small cap charm. The lighting moves from warm amber on the left through neutral to cool on the right. Deep shadow separates each object from the next. Seen from a low three-quarter angle, sharp focus throughout.",
 "pan slowly to the right across the three objects, the light shifting from warm to cool as we move"),

(5, "5:54–6:06",
 "Maya pays hers off in twenty months and hands over one thousand five hundred and sixty-nine dollars in interest.",
 "Maya 用二十个月还清，前后交了一千五百六十九美元的利息。",
 "二十枚硬币排成一列，其中约七枚被单独推到一边，颜色变暗。",
 "第一个结论。数字说得慢，让观众跟上。",
 "drift-right",
 "A long single row of identical coins laid out on dark wood, seen from above at an angle, twenty coins in a line receding slightly into shadow. At one end of the row, a group of about seven coins has been pushed slightly out of the line and has fallen into shadow, duller and darker than the rest. Warm raking light from the left catches the edges of the coins still in the light.",
 "pan slowly along the row of coins from the lit end toward the shadowed group"),

(5, "6:06–6:18",
 "Devon takes seventeen months and pays four hundred and thirty-two. Priya takes seventeen months and pays two hundred and five.",
 "Devon 用十七个月，付了四百三十二。Priya 也用十七个月，付了两百零五。",
 "两小堆硬币并排，一堆明显比另一堆小，但都远小于 Maya 那堆。",
 "「也用十七个月」——点出时间一样、金额不同，这是后面的伏笔。",
 "drift-right",
 "Two small piles of coins side by side on the dark wooden surface, one pile slightly larger than the other, both of them noticeably smaller than a pile would be in the previous shot. Warm light from the left, both piles casting short shadows to the right. The wood grain is visible between them. A third empty spot on the surface shows where a much larger pile once sat.",
 "pan slowly from the first small pile across to the second, then onto the empty spot"),

(5, "6:18–6:30",
 "Now run the other path. Same five hundred a month, but they invest it instead, at seven percent, for the same number of months.",
 "现在换另一条路。同样是每月五百，但他们不去还债，而是拿去投资，按百分之七算，时间一样长。",
 "同一条路径分成两条岔路：一条通向一扇关着的门，一条通向一扇开着的门。",
 "明确说明这是对照组，且只有一个变量在变。",
 "push-in",
 "A narrow dark corridor opening into a clean Y-shaped fork, two diverging passageways leading away from the viewer. The left passage ends at a closed door in warm amber light. The right passage ends at an open doorway spilling cool cyan light. The floor is polished dark stone reflecting both colours. No figures, no signage, no text. The fork point is sharply lit where the two colours meet.",
 "push the camera slowly straight forward into the fork, the two passages opening wider on either side"),

(5, "6:30–6:42",
 "Maya's twenty months of investing turns five hundred a month into about ten thousand five hundred and seventy-four dollars. That's a gain of five hundred and seventy-four.",
 "Maya 那二十个月的投资，把每月五百变成大约一万零五百七十四美元。收益是五百七十四。",
 "二十枚硬币全部留在盘里，旁边多出一枚很小的硬币。",
 "先说总额再说收益，避免观众混淆本金和收益。",
 "push-in",
 "A shallow wooden tray seen from above holding twenty identical coins arranged in a neat grid, all of them present. Beside the grid, right at the edge of the tray, sits one single smaller coin, isolated and catching the warm light. The tray is dark walnut with visible grain. Warm light from the upper left, a soft shadow falls to the lower right. The single small coin is the clear focal point.",
 "push the camera slowly in toward the single small coin at the edge of the tray"),

(5, "6:42–6:54",
 "So Maya is choosing between saving one thousand five hundred and sixty-nine in interest, or earning five hundred and seventy-four in the market.",
 "所以 Maya 面对的选择是：省下一千五百六十九的利息，还是在市场里赚五百七十四。",
 "天平再次出现：一端是很高的硬币塔，另一端是矮很多的一堆。",
 "把两个数字摆在同一个画面上，让结论自己出现，不要替观众下结论。",
 "hold",
 "A simple balance scale on a dark stone table seen from the side. The left pan holds a tall column of stacked coins, high and heavy. The right pan holds a much lower, smaller stack. The scale is clearly tipped toward the left. Cool overhead light with warm amber accents on the coins. Deep shadow around the base. The difference in height between the two stacks is unmistakable.",
 "hold the camera completely still, the scale does not move"),

(5, "6:54–7:06",
 "Paying the card wins by nine hundred and ninety-five dollars. Not close.",
 "还信用卡赢，赢九百九十五美元。根本不接近。",
 "天平重重地压向一侧，底座在桌面上压出一道影子。",
 "「Not close.」两个词，全片最干脆的一句。",
 "hard",
 "The same balance scale, now seen from a lower angle and tipped hard to the left, the left pan resting almost against the stone table while the right pan is raised high. The base of the scale presses into the surface, throwing a hard shadow. Warm amber light dominates now, cool light recedes. The frame is tight and the imbalance is total and unambiguous.",
 "hold the camera still, then a very slow three percent creep in on the resting pan"),

(5, "7:06–7:16",
 "Devon: saving four hundred and thirty-two versus earning four hundred and eight. A tie. Twenty-four dollars.",
 "Devon：省下四百三十二，对上赚四百零八。打平。差二十四美元。",
 "天平这一次几乎水平，只有极轻微的倾斜。",
 "语速放慢，「A tie.」单独成句。这是全片最反直觉的一刻。",
 "hold",
 "The same balance scale on the stone table, now almost perfectly level, the two pans separated by only a couple of centimetres of height difference. Both pans hold nearly equal small stacks of coins. Cool neutral light from above, no warm accent. The stillness and the near-balance of the scale is the entire point of the image. Deep shadow at the base.",
 "hold the camera completely still, the scale breathes almost imperceptibly"),

(5, "7:16–7:24",
 "Priya: saving two hundred and five versus earning four hundred and eight. Now investing wins, by about two hundred.",
 "Priya：省下两百零五，对上赚四百零八。这一次投资赢了，赢大约两百。",
 "天平向另一侧倾斜，幅度不大但方向明确。",
 "「Now investing wins」——重心放在 wins，这就是反转。",
 "push-in",
 "The same balance scale, now tipped clearly to the right, the right pan lowered and the left pan raised, with the right stack visibly larger. Cool cyan light now dominates with a faint warm rim on the coins. The stone table is dark and reflective beneath. The tilt is decisive but not extreme, maybe fifteen degrees. Deep shadow fills the background.",
 "push the camera slowly in toward the lowered right pan"),

# ---------- S6 加速器 ----------
(6, "7:24–7:35",
 "And for Devon and Priya there's a third option that beats both, and almost nobody uses it.",
 "而对 Devon 和 Priya 来说，还有第三个选项，比两边都强，而且几乎没人用。",
 "在那两条岔路之外，地面上出现第三道以前没被注意到的光。",
 "「almost nobody uses it」是最强的稀缺性钩子。语气要带一点不可思议。",
 "push-in",
 "The same dark corridor fork, but now a third narrow passage has become visible between the other two, previously hidden in shadow, its floor catching a thin warm amber line of light that was not there before. The polished stone floor reflects all three paths. The two original doorways are still visible at the edges of frame. No figures, no text, no signage.",
 "push the camera slowly forward into the newly revealed central passage"),

(6, "7:35–7:47",
 "If your employer matches your 401(k), that match is a one hundred percent return, on day one, in writing, in your plan document.",
 "如果你的雇主给你的 401(k) 做配比，那份配比就是百分之一百的回报，第一天就生效，白纸黑字写在你的计划文件里。",
 "一份文件被翻开，两行文字的位置被手指点出（真实文字由 Remotion 叠）。",
 "说到「in writing」时敲一下桌面感的重音。这是可验证的承诺。",
 "push-in",
 "An open bound benefits document lying flat on a dark walnut desk, seen from above at a slight angle. A finger rests on one specific blank line partway down the left page. A brass desk lamp lights the spread from the upper left, the paper casting a soft shadow onto the desk. A pair of reading glasses lies closed beside the document. Everything is still and precise.",
 "push the camera slowly in toward the finger resting on the line"),

(6, "7:47–7:59",
 "Not seven percent. Not an average. One hundred. There is no investment on earth that competes with it, and it expires every single paycheck.",
 "不是百分之七。不是平均值。是一百。地球上没有任何投资能跟它比，而且它每个发薪日都会过期一次。",
 "一枚硬币落下，落进一只正在合上的盒子里。",
 "「it expires every paycheck」——这是全片最紧迫的一句。语速要快。",
 "hard",
 "A single coin caught in mid-air just above an open dark metal cash box whose lid is swinging closed, the coin illuminated by a hard warm light from above while the box below is in shadow. Dust motes hang in the beam. The background is near-black. The moment is suspended, the gap between coin and box still open but clearly closing.",
 "hold the camera still, the coin continues falling and the lid continues closing, nothing else moves"),

(6, "7:59–8:12",
 "Look at your plan for two lines: the match formula, and the vesting schedule. The formula might read fifty percent of your contribution, up to six percent of your pay.",
 "你的计划文件里只看两行：配比公式，和归属时间表。公式可能写着「你缴多少，公司配一半，上限是你工资的百分之六」。",
 "镜头推近到那两行；两行都是空白的，旁边各有一个小图标占位。",
 "把「看两行」这个动作具体化到不能再具体。",
 "push-in",
 "Extreme close-up of two adjacent blank ruled lines in an open document, the paper filling the frame, both lines slightly warmer lit than the rest of the page. To the left of each line sits a small blank circular indent, like a bullet marker. The paper fibre is visible in sharp detail. A soft shadow falls across the lower part of the frame. Nothing on the page is readable.",
 "push the camera slowly in until the two lines fill most of the frame"),

(6, "8:12–8:24",
 "On a sixty thousand dollar salary, six percent is three thousand six hundred a year from you, and the match puts in eighteen hundred. That's free money with a deadline.",
 "六十万美元……抱歉，六万美元的年薪，百分之六就是你自己一年缴三千六，公司那笔配比再补一千八。这是一笔有截止日期的免费钱。",
 "两只手各放一叠钞票进同一个盒子：一叠厚，一叠是它的一半。",
 "口播里故意留一个自我纠正（这是 POV 频道的真实感技巧，不要剪掉）。",
 "push-in",
 "Two hands entering frame from opposite sides, each placing a stack of banknotes into the same open dark metal box. The stack from the left is twice as tall as the stack from the right. Warm light from above catches the edges of the notes. The box sits on a dark table. Both hands withdraw, leaving both stacks side by side and clearly visible inside the box.",
 "push the camera slowly in toward the open box as both hands withdraw from frame"),

(6, "8:24–8:36",
 "Vesting is the catch. A four-year schedule means the match is yours gradually. Leave in month eleven and you may keep none of it.",
 "归属期就是那个陷阱。四年归属的意思是，那笔钱是慢慢变成你的。第十一个月离职，你可能一分都拿不走。",
 "一个透明罐子里的硬币，被一道隔板分成四格，只有第一格是亮的。",
 "「you may keep none of it」是全片最冷的一句。不带感情地说。",
 "drift-right",
 "A clear glass jar divided internally into four equal vertical compartments by thin transparent partitions. Coins fill only the first compartment, which is lit warmly from the left, while the other three compartments are empty and fall into cool shadow. The jar sits on a dark surface. Each partition edge catches a thin highlight. The emptiness of the three sections is deliberate and obvious.",
 "pan slowly to the right across the four compartments, from the lit full one into the empty shadowed ones"),

(6, "8:36–8:48",
 "In twenty twenty-six you can defer up to twenty-four thousand five hundred of your own salary. But the match only applies to your contribution, so the match is the priority, not the ceiling.",
 "二零二六年，你自己最多可以延递两万四千五百美元的工资。但配比只跟你的缴费挂钩，所以优先要拿的是配比，不是去顶那个上限。",
 "一条刻度尺，刻度一直延伸到远端；但一只手只指着靠近自己的那一小段。",
 "纠正一个常见误解。这是让懂行观众也愿意看完的地方。",
 "drift-right",
 "A long wooden measuring scale lying on a dark table, its markings receding far into the shadow at the right end of the frame. A single finger rests on a point very close to the near end of the scale, only a short distance along its length. Warm light from the left illuminates the near portion brightly, the far end disappearing into darkness. The wood grain is crisp in the lit area.",
 "pan slowly to the right along the scale from the finger toward the dark far end, then stop"),

(6, "8:48–8:56",
 "Read your own plan document. Mine is an example. Yours will say something different.",
 "去看你自己那份计划文件。我这个是例子。你那份写的会不一样。",
 "一只手合上文件，把它推向画面外。",
 "合规免责句，但要用口语说，不要念法务腔。",
 "pull-out",
 "A hand closing the bound benefits document on the dark walnut desk and pushing it gently away toward the upper edge of the frame. The brass desk lamp still lights the desk from the upper left, the closed document casting a long soft shadow. The reading glasses remain beside it. The desk surface is now mostly empty and dark.",
 "pull the camera slowly straight back, revealing more of the empty desk around the document"),

# ---------- S7 时间线 ----------
(7, "8:56–9:08",
 "So here's the whole thing, in one sentence you can remember without a screenshot.",
 "所以整个事情，压缩成一句话，一句话你不用截图也能记住。",
 "画面清空。只剩一束光照在桌面中央。",
 "进入收束段。语速慢下来，进入「我要给你结论了」的节奏。",
 "push-in",
 "A completely empty dark walnut tabletop with a single warm pool of light falling onto its centre from directly above, the light forming a clean circle. Everything outside the circle falls into deep shadow. The wood grain is visible only inside the pool of light. No objects, no clutter, nothing else. The frame is almost entirely dark with one bright island in the middle.",
 "push the camera slowly straight down toward the pool of light on the table"),

(7, "9:08–9:20",
 "Compare your interest rate to seven. Above seven, kill the debt first. Below seven, take the match first, then invest the rest.",
 "把你的利率和七比。在七以上，先干掉债务。在七以下，先拿配比，剩下的再投资。",
 "那束光里浮现一条水平线，把光池分成上下两层。（数字由 Remotion 叠）",
 "全片的金句。一句一停，让观众在心里复述一遍。",
 "hold",
 "The same dark tabletop with the pool of warm light, but now a single straight horizontal line of brighter light has appeared across the middle of the pool, dividing it cleanly into an upper half and a lower half. The upper half is warmer and more intense, the lower half slightly cooler. Everything outside the pool remains in deep shadow. The line is perfectly level and steady.",
 "hold the camera completely still, the line of light does not move or flicker"),

(7, "9:20–9:32",
 "That's it. That's the rule. Everything else is detail.",
 "就这样。这就是那条规则。其他的都是细节。",
 "光池边缘的东西全部退进黑暗，只剩中间那一条线。",
 "「Everything else is detail.」说得随意一点，反而更有力。",
 "pull-out",
 "The same table and pool of light, but now the surrounding area has fallen into total darkness and only the horizontal line of light remains visible, floating in blackness with the faintest edge of the table still catching a glow. The line is isolated and unmistakable. No other detail survives in the frame.",
 "pull the camera slowly straight back, the line of light shrinking toward the centre of frame"),

(7, "9:32–9:45",
 "Now let's make it a timeline instead of a rule, because rules don't survive a bad week.",
 "现在把规则换成一条时间线，因为规则熬不过一个糟糕的星期。",
 "那条线开始向右延伸，上面出现三个间隔均匀的刻度点。",
 "「rules don't survive a bad week」是全片最有共鸣的一句之一。",
 "drift-right",
 "The same horizontal line of light, now extending further to the right across a dark space, with three evenly spaced small bright nodes glowing along its length, each node a point of slightly more intense light. The line continues past the last node into shadow. The background is pure black. The nodes are evenly spaced like stations on a route.",
 "pan slowly to the right along the line, passing each of the three glowing nodes in sequence"),

(7, "9:45–9:56",
 "Tonight: you look up one number. Your APR. Ten minutes, one number, that's the whole assignment.",
 "今晚：查一个数。你的 APR。十分钟，一个数，这就是全部的作业。",
 "第一个刻度点被放大，旁边是一只手机，屏幕是暗的。",
 "把「今晚」这个动作压缩到最小，降低行动门槛。",
 "push-in",
 "Close-up of the first glowing node on the line of light, now enlarged and filling more of the frame, with a smartphone lying face-down on the dark surface just beside it, the phone's screen dark. The node's warm light catches the edge of the phone. Everything else is black. The composition is simple: one bright node, one dark phone, nothing else.",
 "push the camera slowly in toward the node and the phone beside it"),

(7, "9:56–10:02",
 "This month: if it's above seven, every extra dollar goes at the balance, and you stop contributing above the match.",
 "这个月：如果在七以上，每一块多余的钱都砸向余额，并且在配比之上停止追加缴费。",
 "第二个刻度点亮起，旁边是一叠朝着同一个方向移动的钞票。",
 "「stop contributing above the match」是有争议的一句话，语气要稳、要确定。",
 "push-in",
 "The second glowing node on the line, now lit, with a small neat stack of banknotes beside it on the dark surface, the notes all oriented in the same direction as if being sent somewhere. Warm light from the node catches their edges. The background is black. The sense of a single directed movement is clear and uncluttered.",
 "push the camera slowly in toward the second node and the stack of notes"),

(7, "10:02–10:12",
 "After that: the money you were sending to interest becomes the money you send to yourself. Same amount. Different destination.",
 "再往后：你原本送去还利息的那笔钱，变成你送给自己的钱。金额一样，目的地不同。",
 "第三个刻度点亮起，那条路径从它出发，拐向一个更开阔的方向。",
 "全片的情感高点。语气要轻，不要煽情。",
 "pull-out",
 "The third glowing node on the line, now the brightest of the three, with the line of light continuing past it and curving away toward a wider, more open area of soft warm light in the distance. The immediate foreground around the node is dark. The distant glow suggests space and openness without showing any specific place.",
 "pull the camera slowly straight back, revealing the line curving away into the open warm distance"),

# ---------- S8 收口 ----------
(8, "10:12–10:26",
 "One more number, because it explains why this feels impossible and why it isn't.",
 "还有一个数字，因为它能解释：为什么这件事感觉不可能，以及为什么它其实可能。",
 "画面回到那张空桌子，光池重新出现。",
 "最后一段的开场。留一秒静默再说。",
 "push-in",
 "Return to the empty dark walnut tabletop with the single round pool of warm light from above, exactly as before, the wood grain visible inside the circle and deep shadow everywhere else. A few fine dust motes drift through the beam. The scene is completely still and completely empty, waiting.",
 "push the camera slowly down toward the pool of light on the empty table"),

(8, "10:26–10:40",
 "If you pay only the minimum — usually two percent of the balance — that eight thousand dollars takes about a hundred years, and costs about seventy-six thousand dollars in interest.",
 "如果你只还最低还款——通常是余额的百分之二——那八千美元要还大约一百年，利息总共大约七万六千美元。",
 "一条极其漫长的、延伸出画面之外的刻度带，远处几乎看不见尽头。",
 "「a hundred years」说完停一拍。这个数字自己会说话。",
 "push-in",
 "A long strip of small evenly spaced marks running across a dark surface from the near foreground all the way to the far edge of the frame, where they become so small and dense that they disappear into shadow long before reaching any end. Warm light rakes across the near marks, fading completely toward the far end. The sense of endless distance is immediate.",
 "push the camera slowly forward along the strip of marks, which continues endlessly"),

(8, "10:40–10:52",
 "The minimum payment is not a payment plan. It's a subscription to the debt.",
 "最低还款不是还款计划。它是给这笔债务办的一张订阅。",
 "一枚硬币落进一个开着口的小盒，盒子下方连着一根不断延伸的管子。",
 "全片最好的一句比喻。说完留两秒，不要马上接下一句。",
 "hold",
 "A single coin dropping into a small open dark container, below which a thin pipe leads away and continues out of frame, suggesting an endless recurring drain. Hard warm light from above on the coin and the rim of the container, the pipe disappearing into deep shadow. The background is black. The image reads instantly as a recurring charge.",
 "hold the camera completely still, the coin has already landed, nothing moves"),

(8, "10:52–11:04",
 "But at five hundred a month, the same debt is gone in twenty months. Same debt. Same person. One number changed.",
 "但如果每月还五百，同一笔债务，二十个月就消失了。同一笔债。同一个人。只有一个数字变了。",
 "一条短得多的刻度带，只有二十格，尽头就在画面内。",
 "「Same debt. Same person. One number changed.」三连短句，节奏一致。",
 "pull-out",
 "A short strip of exactly twenty evenly spaced marks running across the dark surface, both the beginning and the clearly visible end contained within the frame, brightly lit by warm light from the left. The shortness of the strip is the point. Beyond its end the dark surface is clean and empty. No shadow, no clutter.",
 "pull the camera slowly straight back until the entire twenty-mark strip is visible end to end"),

(8, "11:04–11:16",
 "You don't need more discipline. You need to know which number you're actually fighting.",
 "你不需要更多自制力。你需要知道，你真正在跟哪个数字打仗。",
 "一束光照在一枚硬币上，硬币周围一片漆黑。",
 "这一句是全片的主题句。说得慢、说得平。",
 "push-in",
 "A single coin lying flat in the centre of a dark surface, illuminated by one hard shaft of warm light from directly above that isolates it completely, the surrounding surface falling to pure black a short distance away. The coin's surface detail is crisp in the light. Dust drifts faintly in the beam. Nothing else exists in the frame.",
 "push the camera slowly straight down toward the single lit coin"),

(8, "11:16–11:24",
 "So tonight, ten minutes. Find the APR. Compare it to seven. You'll know what to do before you go to sleep.",
 "所以今晚，十分钟。找到你的 APR。和七比一下。睡觉之前，你就知道该怎么做了。",
 "窗外天已经黑了，室内一盏台灯还亮着。",
 "CTA 只给一个动作。不要加「点赞订阅」。",
 "pull-out",
 "A dim interior seen through a window from outside at night, a single warm desk lamp glowing in an otherwise dark room, its light pooling on an empty desk. The window frame is dark, the glass faintly reflective. Outside is blue-black night. The scene is quiet and resolved, the lamp the only warm thing in frame.",
 "pull the camera slowly straight back from the window, the lamp shrinking to a single warm point"),

(8, "11:24–11:30",
 "I'll see you in the next one.",
 "下期见。",
 "台灯熄灭，画面沉入黑暗，只剩一点余温。",
 "说完立刻收。不要加片尾卡。",
 "hold",
 "The same dark room seen through the window, but the desk lamp has just gone out, leaving only a faint residual warm glow on the desk surface that is already fading. The room is now almost entirely blue-black. The window frame is barely visible. Nothing moves. The image is on the edge of total darkness.",
  "hold the camera completely still as the last of the warm glow fades to black"),
]

# ============================================================ 她在哪（每个镜头必填）
#
# 和 AI 频道同一天补的，原因一样：只有角色卡、没有「她在这一镜里在哪」，
# 模型就会把镜头画成静物或一只飘在黑暗里的手。
#
# 金融频道的分寸和 AI 频道不同，这里是 POV 惯例：**人在场，脸不出**。
# 每一条都要做到两件事：
#   1. 让观众感觉到一个身体在画面后面（袖口、肩线、背影、膝盖、重心）
#   2. 脸始终不可读（深阴影、转开、出画、或从背后拍）
# 如果一条描述同时满足不了这两点，重写，不要将就。
#
# 服装只有一件：暖灰色棉质圆领毛衣（heather-grey cotton crewneck sweater）。
SHE = [
    # ---- S1 设局 ----
    ("hands", "She sits at the kitchen table in the heather-grey crewneck sweater, both hands wrapped "
              "around the cold ceramic mug. Her forearms rest on the table edge, cuffs pushed to the "
              "wrist. Her head is bowed and cropped out at the top of the frame; the back of her "
              "platinum hair is just visible as a soft shape in the dim light."),
    ("hands", "Her hands and forearms from the wrist down, the cuffs of the heather-grey sweater "
              "visible, arranging the row of cream envelopes. Her shoulders are a soft dark mass at "
              "the top of the frame. Her face is not in the composition."),
    ("back", "She stands at the minimal desk, seen from behind and slightly above, one hand resting "
             "flat beside the curling calendar corner. Her back and the crown of her platinum head "
             "fill the lower third of the frame. No face."),
    ("silhouette", "She stands in the dark hallway beside the ajar door, a silhouette facing away from "
                   "camera toward the blade of amber light. Her shoulder and the edge of her sweater "
                   "sleeve catch a thin amber rim. Her face is turned into the doorway and unreadable."),
    ("hands", "Her hands from the wrist down hold the blank sheet of cream paper up toward the camera. "
              "The heather-grey cuffs are visible at both wrists, the thin matte-silver band on her "
              "right fourth finger. Her torso is a soft dark shape behind the paper; her face is "
              "hidden by the sheet."),
    ("hands", "She sits at the empty desk, both hands resting flat on its surface at the near edge, "
              "fingers spread slightly. The heather-grey cuffs sit at her wrists. Her shoulders and the "
              "base of her throat are a dark mass at the top of frame; her face is cropped out."),
    ("hands", "Extreme close on her right index finger tapping the paper. Only the fingertip and the "
              "first knuckle are in frame, the heather-grey cuff a soft blur far behind. Her face is "
              "not in the composition."),
    ("hands", "Her right hand turns the sheet face-down, caught mid-motion. Forearm enters from the "
              "right, heather-grey cuff pushed back, silver band visible. Her torso is an out-of-focus "
              "dark shape above; no face."),
    ("back", "Seen from above and behind, she sits at the small café table, her shoulders and the back "
             "of her platinum head in the upper frame, hands resting on the table around the three "
             "objects. Her face is turned down and away."),
    ("silhouette", "She stands at the open refrigerator in side silhouette, the cool white interior "
                   "light rimming the front of her body — her shoulder, her forearm reaching in, the "
                   "edge of her platinum hair. Her face is turned into the fridge and unreadable."),
    ("hands", "She crouches beside the copper pipe joint, her right hand reaching in from the lower "
              "right to touch the seeping thread of water. The heather-grey cuff is pushed back, the "
              "silver band catching a glint. Her shoulder and the side of her torso fill the right "
              "third of frame; her head is cropped out above."),
    ("back", "She stands at the shelf, seen from behind, her back and shoulders filling the lower "
             "third of the frame as she looks at the three glass jars. The crown of her platinum head "
             "is level with the middle shelf. No face."),

    # ---- S2 诊断 ----
    ("back", "She stands at the shelf in the same position, now leaning slightly toward the single lit "
             "jar. Her back, shoulder line and the back of her head are readable; her face stays "
             "turned away into shadow."),
    ("hands", "Extreme close on her fingertip touching the glass of the lit jar. Her other fingers "
              "curl softly behind it, heather-grey cuff a blur at the edge of frame. Her face is not "
              "in the composition."),
    ("hands", "Her hands from the wrist down open the heavy bound report on the wide desk, both palms "
              "flat on the cream paper. Heather-grey cuffs at both wrists, silver band on the right "
              "fourth finger. Her shoulders are a dark mass at the top of frame; her face is cropped "
              "out."),
    ("back", "Seen from above and behind, she sits at the desk with the two documents in front of her, "
             "head bowed, one forearm resting on the table's near edge. Her back and the crown of her "
             "head fill the upper frame. No face."),
    ("hands", "Her right index finger traces down the left margin of the printed table. Forearm enters "
              "from the lower right, heather-grey cuff pushed to the elbow, the page's shadow falling "
              "across her knuckles. Her face is not in the composition."),
    ("hands", "Extreme close on her fingertip resting at the end of the ruled row. The heather-grey "
              "cuff is a soft blur at the bottom of frame. Her face is not in the composition."),
    ("hands", "Her right hand has just released the upright coin, fingers still curved from the motion, "
              "the heather-grey cuff at the wrist. Her torso is a dark shape behind and above, out of "
              "focus; her face is not readable."),
    ("hands", "Her hand enters from the right and rests on the stack of banknotes, fingers splayed "
              "slightly. The heather-grey cuff is pushed back, the silver band catching the warm light. "
              "Her shoulder is a dark curve at the top of the frame; no face."),
    ("hands", "Her right hand pushes the white takeaway cup toward the frame edge, the heather-grey "
              "cuff visible, the silver band on her fourth finger. Her forearm and shoulder fill the "
              "right third of the composition; her head is cropped out."),

    # ---- S3 三条路 ----
    ("back", "She stands at the window with her back to camera, one hand resting on the sill. Her "
             "silhouette and the crown of her platinum head are readable against the pale grey-blue "
             "sky. Her face is turned to the glass and unreadable."),
    ("hands", "Her two hands hold the three sheets of frosted glass upright from below, fingers "
              "visible through the frosted surface as soft shapes. Heather-grey cuffs at both wrists. "
              "Her shoulders are a dark mass above; her face is cropped out."),
    ("back", "Seen from above and behind, she leans over the dark stone surface, both palms flat on "
             "it, looking down at the three objects. Her back and the back of her platinum head fill "
             "the upper frame. No face."),
    ("silhouette", "She stands in the dark room facing the white wall, a full-body silhouette against "
                   "the projected band of cyan light. Her shape is clear — shoulders, the fall of her "
                   "hair, her posture — but her face is in shadow and unreadable."),
    ("silhouette", "She stands in the same spot facing the wall, now with the straight amber line "
                   "crossing at her shoulder height. Her silhouette is sharper, the amber line cutting "
                   "across her sweater. Her face stays in shadow."),
    ("hands", "Her two hands steady the balance scale on the stone table, one on each side of its "
              "base. Heather-grey cuffs at both wrists, silver band visible on the right. Her "
              "shoulders are a dark mass at the top of frame; her face is cropped out."),
    ("silhouette", "She stands back from the wall, arms crossed loosely, looking at the kinked amber "
                   "line. Her silhouette is readable from behind — the set of her shoulders is doing "
                   "the acting. Her face is turned away."),
    ("hands", "Her hands from the wrist down rest flat on the dark tabletop on either side of the "
              "three blank index cards. Heather-grey cuffs, silver band on the right fourth finger. "
              "Her torso is a soft dark shape above; no face."),
    ("back", "Seen from above and behind, she leans over the three objects on the dark surface, "
             "weight on her forearms. Her back and the crown of her head fill the upper frame. No "
             "face."),
    ("hands", "Her right hand lays the row of twenty coins out along the dark wood, fingers guiding "
              "each one into place. The heather-grey cuff is pushed back. Her forearm and shoulder "
              "occupy the right third; her head is cropped out."),
    ("hands", "Her two hands hover above the two piles of coins, comparing them, palms down and "
              "fingers spread. Heather-grey cuffs at both wrists. Her shoulders are a dark mass at "
              "the top of frame; her face is not in the composition."),

    # ---- S4 选择 ----
    ("silhouette", "She stands at the mouth of the corridor where it forks, seen from behind, her "
                   "silhouette small against the two diverging passages. Her posture is still, "
                   "weighing. Her face is turned away down the corridor."),
    ("hands", "Her two hands hold the shallow wooden tray of twenty coins, one at each end, thumbs "
              "visible on the rim. Heather-grey cuffs at both wrists. Her torso is a dark shape "
              "behind; her face is cropped out."),
    ("hands", "Her right hand stacks coins into the tall column on the left pan of the scale, "
              "movements small and careful. The heather-grey cuff is pushed to the wrist, the silver "
              "band catching the light. Her shoulder fills the right third; no face."),
    ("silhouette", "She stands beside the tipped balance scale, seen from behind and slightly to the "
                   "side, head tilted toward the lower pan. Her silhouette reads clearly, her face "
                   "does not."),
    ("silhouette", "She stands beside the now-level scale in the same position, her shoulders dropping "
                   "a little. Seen from behind; her face stays unreadable."),
    ("silhouette", "She stands beside the scale tipped the other way, seen from behind, one hand "
                   "resting on the stone table's edge. Her silhouette carries the reaction. No face."),
    ("silhouette", "She stands at the fork where the third passage has appeared, seen from behind, "
                   "turned slightly toward it. Her silhouette and the fall of her platinum hair are "
                   "readable; her face is in shadow."),
    ("back", "Seen from above and behind, she sits at the walnut desk with the open benefits document "
             "in front of her, one forearm on the desk's near edge. Her back and the crown of her head "
             "fill the upper frame. No face."),

    # ---- S5 落地 ----
    ("hands", "Her right hand has just released the coin above the open cash box, fingers still open. "
              "The heather-grey cuff is visible, the silver band catching the hard light. Her forearm "
              "and shoulder fill the upper right; her head is cropped out."),
    ("hands", "Extreme close on her finger resting between the two blank ruled lines. The heather-grey "
              "cuff is a soft blur at the bottom of frame. Her face is not in the composition."),
    ("hands", "Her two hands enter from opposite sides of the frame, each placing a stack of "
              "banknotes into the same open container. Heather-grey cuffs at both wrists, the silver "
              "band on her right fourth finger. Her torso is a dark mass above; no face."),
    ("hands", "Her two hands hold the four-compartment glass jar steady on the dark surface, one on "
              "each side. Heather-grey cuffs pushed to the wrists. Her shoulders are a soft dark shape "
              "at the top of frame; her face is cropped out."),
    ("hands", "Her right index finger rests on the long wooden measuring scale, tracing its length "
              "into the shadow. The heather-grey cuff is pushed back, the silver band visible. Her "
              "forearm occupies the lower right; her face is not in the composition."),
    ("hands", "Her right hand closes the bound benefits document and pushes it away across the walnut "
              "desk, the motion final. The heather-grey cuff is visible at the wrist. Her shoulder and "
              "the side of her torso fill the right third; her head is cropped out."),

    # ---- S6 结果 ----
    ("hands", "She sits at the empty walnut table, both hands resting palms-down on its surface just "
              "outside the warm pool of light. The heather-grey cuffs sit at her wrists, the silver "
              "band catching one warm glint. Her shoulders are a dark mass at the top of frame; her "
              "face is cropped out."),
    ("hands", "She sits at the same table, hands resting on its surface, her right index finger "
              "extended along the line of bright light. Heather-grey cuff pushed back. Her shoulders "
              "are a soft dark shape above; no face."),
    ("hands", "She sits at the table in near-total darkness, only her two hands and the heather-grey "
              "cuffs visible in the line of light. The silver band on her right fourth finger catches "
              "the only highlight. Her face is entirely lost in the dark."),
    ("hands", "She sits at the table, both hands resting flat on the dark surface, her right index "
              "finger pointing along the line toward the three glowing nodes. Heather-grey cuffs "
              "visible. Her shoulders are a dark mass at the top of frame; her face is cropped out."),
    ("hands", "Her right hand rests open beside the first glowing node, palm up, the heather-grey cuff "
              "catching the node's light. Her forearm enters from the lower right. Her face is not in "
              "the composition."),
    ("hands", "Her right hand rests beside the second glowing node with its small stack of banknotes, "
              "fingers relaxed. The heather-grey cuff is pushed back, the silver band visible. Her "
              "shoulder fills the right third; no face."),
    ("hands", "Her right hand rests beside the third and brightest node, the light climbing her "
              "knuckles. Heather-grey cuff at the wrist. Her forearm and shoulder occupy the lower "
              "right of frame; her head is cropped out."),
    ("hands", "She sits at the table exactly as before, both hands palms-down on the dark wood outside "
              "the round pool of warm light. The heather-grey cuffs and the silver band are the only "
              "warm highlights on her. Her face is cropped out."),
    ("hands", "Her right index finger rests at the start of the long strip of small marks, ready to "
              "trace along it. The heather-grey cuff is pushed back. Her forearm enters from the "
              "lower right; her face is not in the composition."),
    ("hands", "Her right hand has just released the coin above the small open container, fingers still "
              "curved. The heather-grey cuff is visible at the wrist. Her forearm and shoulder fill "
              "the upper right; her head is cropped out."),
    ("hands", "Her right index finger rests at the last of the twenty marks, having traced the whole "
              "strip. The heather-grey cuff is pushed to the wrist. Her forearm occupies the lower "
              "right; her face is not in the composition."),
    ("hands", "Her right hand rests flat on the dark surface beside the single coin, fingers relaxed "
              "and still. The heather-grey cuff catches the hard shaft of warm light, the silver band "
              "glinting. Her shoulder is a dark curve at the top of frame; no face."),

    # ---- S7 收尾 ----
    ("silhouette", "Seen through the window from outside, she sits at the desk inside, a warm silhouette "
                   "against the dim room — the shape of her shoulders, the fall of her platinum hair, "
                   "the curve of her back as she leans toward the lamp. Her face is turned away and "
                   "unreadable."),
    ("silhouette", "Seen through the same window, she is still in the chair but the lamp has gone out. "
                   "She is now only a darker shape within the dark — the outline of her head and "
                   "shoulders against the last residual glow. Her face is not readable; the image is "
                   "on the edge of total darkness."),
]
assert len(SHE) == len(_SHOTS), f"SHE {len(SHE)} 条 / _SHOTS {len(_SHOTS)} 条 —— 必须一一对应"


# ============================================================ 组装
def shots():
    out = []
    for i, (sec, win, en, zh, vis, emo, mot, img_core, vid_core) in enumerate(_SHOTS, 1):
        kind, she = SHE[i - 1]
        p = build_prompts(FIN_IMG_HEAD, FIN_IMG_TAIL, FIN_VID_HEAD, FIN_VID_TAIL,
                          FIN_CHARACTER, FIN_ONCAMERA, she, img_core, vid_core)
        out.append({
            "id": f"F{i:02d}",
            "sec": sec,
            "window": win,
            "en": en,
            "zh": zh,
            "visual": vis,
            "emotion": emo,
            "motion": mot,
            "cam": kind,          # hands / back / silhouette
            "she": she,           # 她在画面里的确切位置，报告里单列一栏给用户看
            "img_en": p["img_en"],
            "vid_en": p["vid_en"],
        })
    return out


def build():
    s = shots()
    words = sum(len(x["en"].split()) for x in s)
    return {
        "channel_key": CHANNEL_KEY,
        "channel_label": CHANNEL_LABEL,
        "topic": TOPIC_EN,
        "topic_cn": TOPIC_CN,
        "style_bible": FIN_BIBLE,
        "pick": PICK,
        "titles": TITLES,
        "thumbs": THUMBS,
        "framework": FRAMEWORK,
        "shots": s,
        "shot_count": len(s),
        "word_count": words,
        "duration": "11:30",
        "framework_one_liner": "三个人的对比故事（Maya 22.15% / Devon 7.14% / Priya 3.5%），"
                              "只改利率一个变量，结论在 7% 处反转。",
        "numbers_source": "_build/fin_numbers.py（月度复利实算，可复现）",
    }


if __name__ == "__main__":
    d = build()
    print(d["topic"], "|", d["shot_count"], "shots |", d["word_count"], "words |", d["duration"])
    print("avg img prompt words:",
          sum(len(x["img_en"].split()) for x in d["shots"]) // len(d["shots"]))
