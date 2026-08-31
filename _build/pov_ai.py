# -*- coding: utf-8 -*-
"""AI 频道 POV 成片源（@AIcheatcodeplaybook）

格式：无出镜、无录屏、无「我让 ChatGPT 生成了 X」这类不可复现的承诺。
全部画面由 AI 生图/生视频，旁白叙事，Remotion 叠加字幕与界面。

诚实性红线：全片不声称任何工具会返回某个确定结果。所有演示都表述为
「流程 + 判断标准」，观众照做得到的是同一套流程，不保证同一份输出。
"""

from pov_style import (AI_IMG_HEAD, AI_IMG_TAIL, AI_VID_HEAD, AI_VID_TAIL,
                       AI_CHARACTER, AI_BIBLE, THUMB_HEAD, THUMB_TAIL)

CHANNEL_KEY = "ai"
CHANNEL_LABEL = "AI · 科技数码 (@AIcheatcodeplaybook)"

# ============================================================ ① 选题
TOPIC_EN = "POV: You Have 47 AI Tools And Use 2 Of Them"
TOPIC_CN = "POV：你收藏了 47 个 AI 工具，真正在用的只有 2 个"

PICK = {
    "one_liner": "把「AI 工具推荐」这个内卷到死的内容类型，翻转成「你为什么收集而不落地」——"
                 "并给一条三问测试 + 一条能今晚跑通的流程。",
    "why": [
        {"h": "受众规模最大，且痛点最具体",
         "b": "几乎每个用 AI 的人都有那个收藏夹。说中它 = 一秒代入，"
              "这是 AI 区少数不需要解释背景就能懂的开场。"},
        {"h": "市面上 99% 的同类内容在加剧这个问题",
         "b": "「十大 AI 工具」越多，观众的工具就越多、落地就越少。"
              "做一条反着说的视频，在同质化信息流里天然突出。"},
        {"h": "POV 格式把「教程」变成「照镜子」",
         "b": "参考 POV Finance 的 21:50 长片，8 天 11.4 万播放。"
              "第二人称叙事让观众先认领处境，再接受方法。"},
        {"h": "全部画面可 AI 生成，零外部素材",
         "b": "不需要任何软件录屏、不需要展示真实账号、不需要第三方界面截图。"
              "暗调屏幕光的风格本身就是 AI 生图最稳的题材之一。"},
        {"h": "不依赖任何工具的确定性输出",
         "b": "全片只讲流程和判断标准，不讲「我输入 X 得到 Y」。"
              "观众照做得到同一套方法，不承诺同一份结果——这样才禁得起挑刺。"},
    ],
    "demand": "本频道选题盘里 ai tools for business / ai automation for beginners / "
              "prompt engineering is dead 三条下拉词同时升温，"
              "指向同一个情绪：工具太多，落地太少。",
    "gap": "所有人都在回答「用哪个工具」，没人回答「怎么判断该留哪个」。"
           "给工具的是流量，给判断标准的是频道。",
    "risk": "最大的风险是变成空谈。所以第 5 段必须给一条具体到分钟数的完整流程，"
            "第 6 段必须自己说出三个会失败的地方。",
    "verdict": "做。这条是 AI 频道的定位宣言——"
               "「cheatcode」不是更多工具，是把一个流程跑通。",
}

# ============================================================ ② 标题（5 选 1）
TITLES = [
    {
        "title": "POV: You Have 47 AI Tools And Use 2 Of Them",
        "cn": "POV：你收藏了 47 个 AI 工具，真正在用的只有 2 个",
        "formula": "POV + 具体数量对比",
        "why": "47 和 2 的落差本身就是钩子，且每个人心里都有自己的两个数字。"
               "「POV」前缀在信息流里是高识别度标签。",
        "pick": True,
    },
    {
        "title": "I Deleted 45 AI Tools. Here's What Actually Worked.",
        "cn": "我删掉了 45 个 AI 工具。真正有用的只有这些。",
        "formula": "极端动作 + 结果承诺",
        "why": "「删掉」比「推荐」更有反差，且自带故事感。"
               "缺点是略带点击诱饵味，需要缩略图和开头一起兜住。",
        "pick": False,
    },
    {
        "title": "Stop Collecting AI Tools. Start Building One Workflow.",
        "cn": "别再收集 AI 工具了。去搭一条流程。",
        "formula": "停止 A + 开始 B",
        "why": "最清晰的主张型标题，适合频道形象。缺点是情绪弱，"
               "适合作为 A/B 里的理性版本。",
        "pick": False,
    },
    {
        "title": "The 3-Question Test That Kills Bad AI Tools",
        "cn": "三个问题，淘汰掉没用的 AI 工具",
        "formula": "命名方法 + 数量",
        "why": "给方法起名字 = 可传播。「kills」比「筛选」有力十倍。"
               "适合有搜索意图的观众。",
        "pick": False,
    },
    {
        "title": "What If You Only Used 2 AI Tools For 30 Days",
        "cn": "如果 30 天里你只用 2 个 AI 工具",
        "formula": "What If + 约束条件",
        "why": "参考频道 John's Money Adventures 的标准句式，在美国区验证过。"
               "约束条件天然制造好奇。",
        "pick": False,
    },
]

# ============================================================ ③ 缩略图（3 张）
THUMBS = [
    {
        "id": 1,
        "name": "A 版 · 47 对 2（首选）",
        "concept": "一面暗墙上有几十个发光的小方图标，密密麻麻；"
                   "其中只有两个是亮青色的，其余全部是熄灭的深灰。",
        "overlay": ["47", "2", "（底部一行小字）ONE OF THESE IS YOU"],
        "why": "数量对撞 + 「其中一个是你」的身份指认，是这类内容点击率最高的结构。"
               "放大到手机尺寸时，两个亮块依然一眼可辨。",
        "core": ("A dark charcoal wall filling the frame, covered edge to edge with a dense grid of "
                 "identical small rounded-square icons, about fifty of them, each icon recessed and unlit, "
                 "rendered in flat dark grey. Exactly two icons, positioned in the lower third and slightly "
                 "off-centre, glow with intense cyan light, spilling soft bloom onto the wall around them. "
                 "Everything else is dim and uniform. Clean product-render aesthetic, sharp edges, "
                 "dramatic contrast between the two lit icons and the dead grid. ")
                 + THUMB_TAIL,
    },
    {
        "id": 2,
        "name": "B 版 · 被图表淹没（情绪版）",
        "concept": "一个人的背影坐在桌前，被前方半空中悬浮的一大团发光图标包围，"
                   "人很小、图标很多，压迫感直接。",
        "overlay": ["（大字）TOO MANY", "（小字）ONE WORKFLOW"],
        "why": "用构图本身讲「被淹没」，不需要任何解释文字。"
               "背影不出脸，符合频道视觉规范。",
        "core": ("A dark room seen from behind a seated figure, the person a small dark silhouette in the "
                 "lower centre of the frame facing a desk. Floating in the air between the figure and the "
                 "camera is a dense swirling cloud of dozens of small glowing cyan and violet square icons, "
                 "crowding the entire upper two thirds of the frame and pressing in toward the figure. "
                 "The only light comes from the glowing cloud. The figure is small, still, and slightly "
                 "overwhelmed. Deep black background, strong vignette. ")
                 + THUMB_TAIL,
    },
    {
        "id": 3,
        "name": "C 版 · 乱堆 vs 流水线（对比版）",
        "concept": "画面竖着劈成两半：左半是一团纠缠的发光线缆和杂乱图标，"
                   "右半是一条干净的、笔直的、亮着的流水线。",
        "overlay": ["（左）BEFORE", "（右）AFTER"],
        "why": "BEFORE / AFTER 是最稳的点击结构，且它直接承诺「这条视频会给你一个转变」。"
               "适合频道已经有一定认知度后使用。",
        "core": ("A frame split cleanly down the middle into two halves. "
                 "The left half is filled with a tangled chaotic mass of glowing cables, loose wires and "
                 "scattered small icons, all knotted together in a visual mess, lit in uneasy violet. "
                 "The right half is completely clean: a single straight horizontal glowing cyan line "
                 "running across a smooth dark surface like a conveyor, with three evenly spaced bright "
                 "nodes along it. Sharp vertical seam between the two halves, no objects crossing it. ")
                 + THUMB_TAIL,
    },
]
for _t in THUMBS:
    _t["prompt_en"] = THUMB_HEAD + _t["core"]
    _t["prompt_cn"] = "（中文说明见「概念」与「叠加文字」两栏；生图时直接复制英文提示词，中文仅用于你理解画面。）"

# ============================================================ ④ 框架（8 段）
FRAMEWORK = [
    {"id": 1, "name": "设局 The Bookmark Graveyard", "window": "0:00–1:05",
     "job": "用一个具体到可笑的数字把观众钉在座位上，并保证不给工具清单。",
     "line": "Forty-seven tools saved. Two you actually opened this month.",
     "points": ["第一个数字必须具体到个位，不能说「几十个」",
                "立刻承诺：这条视频一个工具都不推荐",
                "反向承诺 = 在信息流里唯一的差异化"],
     "risk": "反向承诺有风险，观众会怀疑是标题党。所以第 2 段立刻兑现。"},
    {"id": 2, "name": "否认 Why It's Not Lazy", "window": "1:05–2:20",
     "job": "把责任从观众身上拿走，指向推荐机制本身。",
     "line": "You're not undisciplined. You're being fed a business model.",
     "points": ["「十大工具」类内容的商业模式决定了它必须不断给新东西",
                "收藏的那一刻多巴胺已经给完了，落地是另一回事",
                "这一段的任务是把观众的羞耻换成清醒"],
     "risk": "不能变成控诉同行。语气是「我懂这套机制」，不是「他们骗你」。"},
    {"id": 3, "name": "第一个真相 Tools Aren't Assets", "window": "2:20–3:30",
     "job": "给出核心观点：工具会过期，流程不会。",
     "line": "A tool is a rental. A workflow is equity.",
     "points": ["工具会涨价、改版、关停；流程是你自己的",
                "判断标准：这个工具消失后，我的流程还剩多少",
                "把「会用工具」和「有流程」彻底分开"],
     "risk": "这句是全片的观点支点，必须配一个具体到能想象的画面（租房 vs 房子）。"},
    {"id": 4, "name": "三问测试 The 3-Question Test", "window": "3:30–4:40",
     "job": "给一条可立即执行的判断规则，这是全片最可分享的部分。",
     "line": "Which step does it replace? What goes in? Who catches it when it's wrong?",
     "points": ["问一：它替换我流程里的哪一步（答不上 = 删）",
                "问二：它的输入是什么（需要我先整理 = 慢）",
                "问三：它错了谁发现（没人发现 = 不能用）",
                "三问里任何一问答不上，这个工具就进回收站"],
     "risk": "三个问题必须一个比一个狠，否则观众只会记住第一个。"},
    {"id": 5, "name": "一条流程 One Workflow", "window": "4:40–6:00",
     "job": "把三问测试用在一条真实流程上，给到分钟级的具体度。",
     "line": "Three hours on Monday. Twenty minutes every Monday after that.",
     "points": ["选一件每周都要做的事，不是一次性的",
                "先手写一遍完整流程，再决定哪一步交给 AI",
                "关键动作：把「判断标准」写下来，这是唯一不能外包的",
                "不承诺任何工具的确定输出，只承诺流程可复用"],
     "risk": "这一段最容易被观众跳过。所以开头先给「3 小时 → 20 分钟」这个结果。"},
    {"id": 6, "name": "三个坑 The Three Failures", "window": "6:00–7:10",
     "job": "自己说出会失败的地方，这是信任的来源。",
     "line": "Every AI workflow breaks in one of three places. I'll tell you all three.",
     "points": ["坑一：权限 —— 它拿不到你要它处理的东西",
                "坑二：幻觉 —— 它会非常自信地编造一个不存在的东西",
                "坑三：没有兜底 —— 没人复核，错误会一路走到客户那里"],
     "risk": "主动暴露缺点会掉一部分好感，但留下的观众信任度翻倍。值得。"},
    {"id": 7, "name": "反转 Why Less Is Faster", "window": "7:10–8:20",
     "job": "给一个反直觉的机制解释，制造「啊哈」时刻。",
     "line": "Every tool you add costs you a decision. Decisions are the expensive part.",
     "points": ["每个工具都带来一次选择成本：用哪个、怎么传、结果放哪",
                "工具越多，决策成本吃掉的效率越多",
                "少而深的流程，比多而浅的收藏快得多"],
     "risk": "这一段讲机制，容易抽象。必须回到「你每周一早上那 10 分钟」。"},
    {"id": 8, "name": "收口 Tonight + 互动钩子", "window": "8:20–9:30",
     "job": "给一个今晚能做完的极简动作，并设计一个必须评论的问题。",
     "line": "Tonight: delete everything that fails question one. Then tell me what's left.",
     "points": ["动作小到 10 分钟：只做第一问，删掉答不上的",
                "互动钩子：让观众在评论区报「最后剩几个」",
                "这是全片唯一的 CTA，不要再加第二个"],
     "risk": "CTA 一定要具体到能被评论。「留下什么」比「你怎么看」好 10 倍。"},
]

# ============================================================ ⑤ 分镜（48 镜）
_SHOTS = [

# ---------- S1 设局 ----------
(1, "0:00–0:11",
 "Forty-seven tools saved. Two you actually opened this month. And a folder you're slightly embarrassed about.",
 "收藏了四十七个工具。这个月真正打开的，两个。还有一个你自己都不好意思点开的文件夹。",
 "深夜的桌面，一台笔记本屏幕是暗的，旁边一只手悬在触控板上方，犹豫着。",
 "三个短句，第一句就给具体数字。语速慢，「two」说完停半拍。",
 "push-in",
 "A dark desk at one in the morning, a closed laptop with a black screen reflecting nothing, a mug with a dried coffee ring beside it. A hand hovers a few centimetres above the trackpad, caught in hesitation. The only light is a thin cyan edge glow leaking from the laptop's closed seam and a dim violet desk lamp far out of focus in the background. Near-black room, heavy vignette.",
 "push the camera slowly straight in toward the hovering hand and the dark laptop"),

(1, "0:11–0:24",
 "You're not going to get another list from me today. No top ten. No tools you've never heard of.",
 "今天我不会再给你一份清单。没有十大，没有你没听过的工具。",
 "一只手把一叠厚厚的卡片推到画面外，动作干脆。",
 "反向承诺。语气要笃定，这是全片立信的第一步。",
 "drift-right",
 "A hand pushing a thick stack of blank index cards off the near edge of a dark desk, the cards sliding away and out of frame. The desk surface is matte black with a faint cyan reflection. A single cool light source from the upper left leaves the rest of the desk in shadow. The motion is decisive and slightly impatient.",
 "pan the camera slowly to the right following the stack of cards as it leaves the frame"),

(1, "0:24–0:38",
 "Because the problem was never that you're missing a tool. The problem is that you're collecting instead of building.",
 "因为问题从来不是你缺一个工具。问题是你在收集，而不是在搭建。",
 "桌面上摊着一堆散落的零件，没有一件是装好的。",
 "「collecting instead of building」是全片的主张句。重音落在 building。",
 "push-in",
 "A dark desk surface scattered with dozens of small loose electronic components, connectors, cable ends and unassembled parts, spread out in disorder with nothing connected to anything. Cool cyan rim light from the left edge, violet fill from behind. Every part is sharply rendered and obviously unused. The scene reads as potential that has never been assembled.",
 "push the camera slowly down toward the scattered components on the dark desk"),

(1, "0:38–0:52",
 "And there's a reason for it, and it isn't that you're undisciplined. I'll show you the mechanism in a second.",
 "而这件事是有原因的，原因不是你没有自制力。我马上把那套机制讲给你听。",
 "镜头从零件堆抬起，画面尽头出现一扇亮着光的窗。",
 "抛出「mechanism」这个词，制造第一个知识缺口。",
 "pull-out",
 "The same dark desk with scattered components, but the camera has lifted to reveal a window at the far end of the room, a soft cyan glow spilling in through blinds and cutting horizontal bands across the dark space. The components are now smaller in frame. The room is otherwise black. The light suggests something is happening outside.",
 "pull the camera slowly back and slightly up, revealing the glowing window at the far end"),

(1, "0:52–1:05",
 "First, the number that made me make this video: I counted mine. Sixty-three saved. Four used.",
 "先说一个让我决定拍这条视频的数字：我数了我自己的。收藏六十三个，用了四个。",
 "一只手在纸上写下一个数字，然后停住，看着它。",
 "自曝数字 = 让自己和观众站在一边。这是 POV 频道的信任开关。",
 "push-in",
 "A hand holding a pen, having just written a single number on a blank dark notebook page, the pen now lifted and still. The page is blank apart from the fresh mark. A warm-yellow desk lamp lights the page from the upper right while the rest of the desk falls into cool cyan shadow. The hand is tense and unmoving, caught in the moment after the realisation.",
 "push the camera slowly in toward the fresh number on the page"),

# ---------- S2 否认 ----------
(2, "1:05–1:20",
 "You're not undisciplined. You're being fed a business model, and you don't need to feel bad about it.",
 "你没有自制力问题。你是被一套商业模式在喂养，这件事你不用觉得愧疚。",
 "一条传送带上不断送来新的小盒子，一只手来不及拆。",
 "语气放软。「you don't need to feel bad」要说得真诚。",
 "drift-right",
 "A dark industrial conveyor belt running from the left edge into deep shadow, carrying a continuous line of small sealed matte boxes moving steadily toward the viewer. A single hand at the near end is still unwrapping the previous box and has clearly fallen behind. Cool cyan strip lighting above, violet shadow below. The pace of the belt is relentless and slightly faster than the hand.",
 "pan the camera slowly to the right along the moving conveyor of boxes"),

(2, "1:20–1:36",
 "Every list video has to give you something new, because a list of tools you already have is a video nobody clicks.",
 "每一条清单类视频都必须给你新东西，因为一份你本来就有的工具清单，是没人会点开的一条视频。",
 "屏幕上一个播放按钮和一条曲线，曲线只在有新东西时才上升（界面元素为空白占位）。",
 "讲机制，不讲道德。语气是分析，不是控诉。",
 "push-in",
 "A dark room with a single large wall-mounted display showing a clean blank interface panel with one prominent circular play control and an empty chart area beside it, the panel glowing cyan. The display is the only light source, casting a cool pool on the dark floor. No readable content anywhere. The room is otherwise black and still.",
 "push the camera slowly in toward the glowing blank panel on the wall"),

(2, "1:36–1:52",
 "So the supply never stops. And every time you save one, you get the feeling of having made progress without doing any of the work.",
 "所以供给永远不会停。而你每收藏一个，就获得了一种「我有进展」的感觉——却一点活都没干。",
 "一只手把一张卡片放进文件夹，文件夹合上，画面立刻变暗一点。",
 "「feeling of progress」是这一段的关键洞察。说到这里语速放慢。",
 "hold",
 "A hand placing a single blank card into an accordion folder, then closing the folder's flap over it. As the flap closes the scene dims very slightly, as if a small amount of light has been consumed. The folder sits on a matte black desk lit by a thin cyan edge from the left. Everything else is in shadow. The action feels complete and slightly hollow.",
 "hold the camera completely still as the folder closes and the light dims a fraction"),

(2, "1:52–2:06",
 "Saving is the cheapest possible version of starting. That's why it feels so good and accomplishes so little.",
 "收藏，是「开始」最廉价的一种形式。所以它感觉那么好，却几乎什么都没完成。",
 "一枚硬币投进一个玻璃罐，罐子里已经堆了很多硬币，但没有一枚被动过。",
 "这一句是这一段最好的一句。可以稍微停顿一下再说完。",
 "push-in",
 "A clear glass jar on a dark desk, already half full of identical coins that have clearly never been touched or spent, a fine layer of dust on the jar's shoulder. A hand drops one more coin in through the slot at the top. Cool cyan light rakes across the glass from the left, warm yellow from a distant lamp behind. The coins inside are still and inert.",
 "push the camera slowly in toward the coin dropping into the slot"),

(2, "2:06–2:20",
 "None of that is a character flaw. It's just how the feed works. Now let's talk about what's actually worth keeping.",
 "这些都不是性格缺陷。这只是信息流的运作方式。现在来说什么才真的值得留下来。",
 "传送带在画面边缘停住，一只手把它关掉。",
 "收尾句要轻，像是在说「好了，翻篇」。",
 "hard",
 "The same dark conveyor belt, now stopped, the boxes motionless in a row receding into shadow. A hand reaches in from the right side of frame and rests on a control lever at the belt's edge, having just switched it off. The cyan strip light above flickers once and goes dark, leaving only a dim violet ambient glow. Stillness settles over the scene.",
 "hold the camera completely still, the belt does not move again"),

# ---------- S3 第一个真相 ----------
(3, "2:20–2:34",
 "Here's the distinction that fixed this for me. A tool is a rental. A workflow is equity.",
 "帮我修好这件事的，是这样一个区分：工具是租的，流程是你的资产。",
 "左边是一把挂在墙上的钥匙，右边是一张地契模样的文件（均为空白占位）。",
 "全片的观点支点。两句对称，一句一个画面。",
 "drift-right",
 "Two objects side by side on a dark wall, each in its own light. On the left, a single key hanging from a small hook, lit cold cyan, obviously temporary. On the right, a folded heavy document with an embossed seal, lit warm yellow, obviously permanent. The wall between them is textured near-black. The contrast in lighting and material carries the whole meaning.",
 "pan the camera slowly from the hanging key across to the sealed document"),

(3, "2:34–2:48",
 "Tools get repriced, redesigned, shut down, or quietly get worse after an update. Your workflow is the one part that stays with you.",
 "工具会改价、改版、关停，或者某次更新之后悄悄变差。而流程，是唯一会一直留在你手里的那部分。",
 "一排应用在手机屏幕上，其中一个正在变灰（界面为空白占位）。",
 "说到「quietly get worse」时语气带一点无奈的好笑。",
 "push-in",
 "Close-up of a smartphone lying on a dark desk, screen showing a grid of blank rounded-square application tiles. One tile near the centre is visibly desaturated and dimmer than the others, clearly on its way out. Cool cyan screen glow is the only light, spilling onto the desk surface. Everything else in the room is black. No readable text anywhere on the screen.",
 "push the camera slowly in toward the one dimming tile on the screen"),

(3, "2:48–3:02",
 "So here's the test I use, and it's brutal: if this tool vanished tomorrow, how much of my process survives?",
 "所以我现在用这样一个测试，它很残酷：如果这个工具明天消失，我的流程还能剩下多少？",
 "一只手从一个结构里抽走一块积木，整个结构晃了一下但没塌。",
 "「brutal」这个自评很重要，它证明你不是在推销。",
 "push-in",
 "A small tower of interlocking blocks standing on a dark table, built from about a dozen pieces. A hand has just removed one block from the lower middle of the structure. The tower is visibly wobbling, caught at the very start of its lean, but has not yet collapsed. Cool cyan light from the left, warm rim from behind. The tension is in the moment before the fall.",
 "push the camera slowly in toward the removed gap in the wobbling tower"),

(3, "3:02–3:16",
 "If the answer is most of it, the tool was a nice-to-have. If the answer is none of it, you didn't have a process, you had a subscription.",
 "如果答案是「大部分还在」，那这个工具只是锦上添花。如果答案是「一点都不剩」——那你有的不是流程，是一张订阅。",
 "另一只结构：抽走一块，整个塌成一堆。",
 "「you had a subscription」是这一段最狠的一句。不带情绪地说。",
 "hard",
 "A different small tower of blocks on the same dark table, but this one has completely collapsed into a loose scattered pile, one block still rocking slightly on top of the heap. The hand that removed the block has already withdrawn from frame. Cool cyan light from the left falls flat across the debris. There is no structure left, only parts.",
 "hold the camera completely still on the collapsed pile, the last block settling"),

(3, "3:16–3:30",
 "That's the whole reason two tools beat forty-seven. Two are load-bearing. Forty-seven are decoration.",
 "这就是「两个」能打赢「四十七个」的全部原因。两个是承重的，四十七个是装饰。",
 "两根结实的柱子撑着一个结构，旁边散落着一堆没人用的装饰件。",
 "这一段收口。两句话讲完，不要展开。",
 "pull-out",
 "A clean architectural structure on a dark surface: two thick solid vertical columns supporting a simple heavy horizontal beam, the whole thing clearly load-bearing and stable, lit warm yellow from above. Scattered on the dark floor around the base are dozens of small unused decorative pieces, dim and ignored. Everything else is black. The structural contrast is unmistakable.",
 "pull the camera slowly back, revealing the two columns and the scattered decoration around them"),

# ---------- S4 三问测试 ----------
(4, "3:30–3:44",
 "So how do you decide what stays? Three questions. And they get progressively harder to answer.",
 "那怎么决定留什么？三个问题。而且它们一个比一个难答。",
 "三张空白卡片依次排在暗桌上，第三张明显更远、更暗。",
 "进入全片最可分享的部分。语气变成「我给你个东西」。",
 "drift-right",
 "Three blank cards laid out in a receding diagonal line on a matte black desk, the first card close and brightly lit, the second further and dimmer, the third furthest and barely visible in the far shadow. Cool cyan light from the upper left falls off quickly with distance. Nothing on any of the cards. The increasing difficulty is built into the composition.",
 "pan the camera slowly along the diagonal from the near bright card toward the far dark one"),

(4, "3:44–3:58",
 "Question one: which step does it replace? Not which task, which step. If you can't name the exact step, it goes.",
 "问题一：它替换的是哪一步？不是哪件事，是哪一步。如果你说不出具体那一步，它就该走。",
 "一条流程线上有五个节点，一只手只能指在其中两个上。",
 "「Not which task, which step」是精准度的关键，重音要重。",
 "push-in",
 "A clean horizontal process line rendered on a dark surface, marked with five evenly spaced circular nodes connected by thin glowing segments. A single hand is pointing at one specific node in the middle, while the other four nodes sit unaddressed. Cyan light traces the line, violet fills the shadow behind. Everything is precise, geometric, and deliberately empty of text.",
 "push the camera slowly in toward the one node the hand is pointing at"),

(4, "3:58–4:12",
 "Question two: what does it need from me first? If the answer is a clean file I have to prepare by hand every time, it's not saving you time, it's moving it.",
 "问题二：它首先需要我给它什么？如果答案是「一份我每次都要手工整理的干净文件」，那它没有省你的时间，它只是把时间挪了个位置。",
 "一只手在整理一叠散乱的纸，整理的时间明显比后面那步长。",
 "「moving it」是全句的转折，说完停半拍。",
 "drift-right",
 "A dark desk with a messy scatter of loose papers on the left that a hand is laboriously straightening into a neat pile, and a small clean glowing device on the right waiting idle. The pile of papers is visibly much larger than the device. Cool light from above, the right side of the desk in shadow. The imbalance between the long preparation and the small tool is obvious.",
 "pan the camera slowly from the messy papers across to the small idle device"),

(4, "4:12–4:26",
 "Question three, and this is the one that kills most of them: when it's wrong, who catches it?",
 "问题三，也是淘汰掉大多数工具的那个：当它错了的时候，谁会发现？",
 "一份输出文件上有一处明显的错误，旁边没有人在看（文件为空白占位）。",
 "「kills most of them」——语气要带一点警告。",
 "push-in",
 "A single sheet of output paper lying alone on a dark desk under a hard cyan light, one corner of the sheet visibly wrong: a smudge, a misalignment, a clear defect near the bottom edge. There is no one at the desk. A second empty chair sits pushed back in the blurred background. The error is sitting there completely unobserved. Deep shadows everywhere else.",
 "push the camera slowly in toward the visible defect on the unattended page"),

(4, "4:26–4:40",
 "If the answer is nobody, or the answer is hopefully someone downstream, you don't have automation. You have a liability with a nice interface.",
 "如果答案是「没人」，或者「希望下游有人会发现」——那你拥有的不是自动化，你拥有的是一份界面漂亮的负债。",
 "一个漂亮的盒子被打开，里面是纠缠成一团的线。",
 "全片最好的一句比喻。说完留一秒。",
 "push-in",
 "A beautifully designed matte-black box with a precision-milled lid, the lid lifted open at an angle to reveal the inside, which is a densely tangled knot of cables and wires crammed in with no order at all. Warm yellow rim light catches the pristine outer edge of the box, while the inside is lit cold violet. The contrast between the flawless exterior and the chaos within is total.",
 "push the camera slowly in toward the open box and the tangle of cables inside"),

# ---------- S5 一条流程 ----------
(5, "4:40–4:54",
 "Let me show you what this looks like on something real. One task I do every single Monday. It used to take three hours.",
 "让我拿一件真事讲给你听。有一件事我每个周一都要做，以前要花三个小时。",
 "一只手在日历上圈出每周一，日历是空白的。",
 "进入演示段。语速提起来，变成「我给你看点东西」。",
 "push-in",
 "A blank wall calendar seen at a slight angle, a hand drawing a circle around one recurring day of the week in each of several consecutive rows, marking the same weekday over and over down the page. Cool cyan desk lamp light from the upper right, deep shadow falling to the left. The repetition of the marked day is immediately readable as a weekly ritual.",
 "push the camera slowly in toward the column of circled days on the calendar"),

(5, "4:54–5:08",
 "I wrote the whole thing out by hand first. Every step, including the boring ones, before I gave any of it to a tool.",
 "我先把整件事手写了一遍。每一步都写，包括那些无聊的步骤——在我把任何一步交给工具之前。",
 "一叠手写流程的纸，从第一张一直排到最后一张，铺满桌面。",
 "强调「手写」。这是反直觉的，但它是真的。",
 "drift-right",
 "A dark desk covered with a long sequence of handwritten process pages laid out in order, stretching from the near foreground all the way into shadow at the back, about a dozen sheets. The handwriting is dense and real-looking. A pen lies across the nearest page. Warm yellow lamp light from the left, the far pages disappearing into cool shadow.",
 "pan the camera slowly along the row of handwritten pages from the near end toward the far end"),

(5, "5:08–5:22",
 "And here's the part people skip: I wrote down what good looks like. The standard I'd judge the output against.",
 "而这一步是大多数人跳过的：我把「什么叫做得好」写了下来。就是那个我用来判断产出的标准。",
 "一张纸上单独列着几行标准，被一盏小灯照亮（内容为空白占位）。",
 "「what good looks like」是全片的隐藏主角。说到这里语气加重。",
 "push-in",
 "A single sheet of paper alone on a dark desk, ruled with a handful of short blank lines spaced apart, each line headed by a small empty checkbox. A small warm yellow lamp beside the page lights it from the right, leaving the rest of the desk in cool darkness. The page is clearly a checklist of standards rather than a task list.",
 "push the camera slowly in toward the short checklist under the warm lamp"),

(5, "5:22–5:34",
 "That standard is the one thing I never hand over. Everything else is negotiable. That one page is the whole asset.",
 "这份标准，是唯一一样我从不交出去的东西。其他都可以谈。那一页纸，就是全部资产。",
 "一只手把那一页单独抽出来，放进一个文件夹，其余的纸被推到一边。",
 "「the whole asset」——呼应第 3 段的 equity。",
 "push-in",
 "A hand lifting one single sheet of paper away from a larger stack and placing it carefully into a slim dark folder, while the rest of the stack is pushed casually aside into shadow. The folder is warm-lit and clearly important, the discarded stack cool and dim. The desk is otherwise empty. The act of separation is deliberate and careful.",
 "push the camera slowly in toward the folder as the single page is placed inside"),

(5, "5:34–5:48",
 "Then, and only then, I asked question one for each step: which step does a tool actually replace here?",
 "在那之后，也只有在那之后，我针对每一步去问第一个问题：这一步，真的有工具能替换吗？",
 "那只手沿着流程线移动，在三个节点上停下，其余节点跳过。",
 "「and only then」要说得慢，这是顺序的价值。",
 "drift-right",
 "A hand tracing slowly along a glowing process line on a dark surface, stopping and resting briefly at three of the nodes while passing straight over the others without pausing. Cyan light travels with the hand. The skipped nodes stay dim, the three selected nodes brighten as the hand rests on each. The background is black and empty.",
 "pan the camera slowly along the line following the hand as it stops at each selected node"),

(5, "5:48–6:00",
 "Three hours on the first Monday. Twenty minutes every Monday after that. And I'm not going to tell you which tools I used, because that's the part that changes.",
 "第一个周一，三个小时。之后的每个周一，二十分钟。至于我用了哪些工具，我不打算告诉你——因为那正是会变的那部分。",
 "两个时间块并排：一个很长，一个很短。",
 "兑现第 1 段的反向承诺。这是全片最涨信任的一句。",
 "hold",
 "Two horizontal bars side by side on a dark surface, glowing cyan. The upper bar is long, stretching across most of the frame. The lower bar is short, about a ninth of that length, sitting directly beneath it and aligned at the left edge. Both bars are clean and unlabelled. Warm violet fill light from behind separates them from the black background. The size difference tells the whole story.",
 "hold the camera completely still, the two bars do not change"),

# ---------- S6 三个坑 ----------
(6, "6:00–6:12",
 "Now the part nobody puts in their video: where this breaks. Every AI workflow I've built has failed in one of three places.",
 "现在说没人会放进视频里的部分：它会在哪里崩。我搭过的每一条 AI 流程，都在这三个地方之一失败过。",
 "一条完好的流程线，其中三处被标为暗红色（界面为空白占位）。",
 "主动暴露缺点。语气要平，像在报天气预报。",
 "push-in",
 "A long clean glowing process line running across a dark surface, but with three specific segments along it dimmed to a dark uneasy red while the rest stays cyan. The three weak points are evenly spaced and clearly marked by their colour alone. Violet ambient fill from behind. No text, no labels. The viewer can see exactly where the structure is fragile.",
 "push the camera slowly along the line toward the first of the dark red weak segments"),

(6, "6:12–6:26",
 "Failure one: permissions. It can't reach the thing you want it to work on, and it will fail in a way that looks like success.",
 "失败一：权限。它拿不到你希望它处理的那个东西，而且它会用一种「看起来像成功」的方式失败。",
 "一扇锁着的门，门缝里透出光，一只手推不动。",
 "「looks like success」是最危险的一种失败。重音放在 success。",
 "push-in",
 "A solid dark door in a near-black corridor, a thin line of cyan light visible along the bottom edge, a hand pressed flat against the door pushing with real effort. The door does not move. A small glowing green indicator panel beside the handle suggests everything is fine. The contradiction between the reassuring light and the immovable door is the point.",
 "push the camera slowly in toward the hand and the glowing green indicator on the locked door"),

(6, "6:26–6:40",
 "Failure two: it invents things. Confidently, fluently, with perfect formatting, and a source that does not exist.",
 "失败二：它会编东西。自信地、流畅地、格式完美地——而那个出处，根本不存在。",
 "一份整洁漂亮的文档，其中一行的引注指向一个空白。",
 "「Confidently, fluently, with perfect formatting」三连，节奏要快。",
 "push-in",
 "A beautifully formatted document lying flat under a hard white light, every line perfectly aligned and professional. At the bottom of the page one line ends with a citation marker pointing to a footnote area that is completely blank. The page is otherwise immaculate. Cool cyan fill, deep shadow around the paper's edge. The emptiness where the source should be is unmistakable.",
 "push the camera slowly in toward the citation marker and the blank footnote beneath it"),

(6, "6:40–6:52",
 "Failure three: nobody reviews it. And an unreviewed error doesn't stay in your draft folder. It walks out the door with your name on it.",
 "失败三：没人复核。而一个没有被复核的错误，不会老老实实待在你的草稿箱里。它会带着你的名字走出门。",
 "一份文件滑过桌面，穿过门缝，消失在外面的光里。",
 "「walks out the door with your name on it」是全片最有画面感的一句。",
 "drift-right",
 "A single sheet of paper sliding rapidly across a dark desk surface toward a doorway at the far side of the room, passing under the partly open door and disappearing into the bright light beyond. The paper catches a cool cyan sheen as it moves. The room is dark, the gap under the door is bright. The paper is clearly leaving and cannot be recalled.",
 "pan the camera quickly to the right following the paper as it slides under the door and out of sight"),

(6, "6:52–7:10",
 "So build the review step before you build the automation step. Not after. That single ordering decision is the difference between a workflow and a liability.",
 "所以：先搭复核那一步，再搭自动化那一步。不是反过来。就这一个顺序上的决定，决定了你拿到的是一条流程，还是一份负债。",
 "两个盒子，标着顺序：复核盒在前，自动化盒在后（标记为空白占位）。",
 "给出可执行结论。说完停一拍，进入第 7 段。",
 "hold",
 "Two clean matte-black boxes sitting in a clear left-to-right sequence on a dark surface, connected by a short glowing arrow pointing rightward. The left box has a small circular inspection lens motif on its lid, the right box has a small gear motif. Cyan light rims both boxes, warm yellow fills the arrow between them. The order is the entire meaning of the image.",
 "hold the camera completely still, only the arrow between the boxes glows steadily"),

# ---------- S7 反转 ----------
(7, "7:10–7:24",
 "Now the counterintuitive part, and it's the reason less is actually faster.",
 "现在说反直觉的那部分，也是为什么「更少」反而真的更快。",
 "两条路：一条分叉很多，一条笔直；分叉那条明显更长。",
 "「counterintuitive」是好奇心钩子，给观众一个留下的理由。",
 "drift-right",
 "A dark schematic space seen from above, showing two routes from a common starting point to the same destination. The upper route branches repeatedly into many small forks and detours, its path visibly long and tangled. The lower route is a single straight clean line. Cyan light marks the straight route, dim violet marks the branching one.",
 "pan the camera slowly to the right from the starting point along both routes toward the shared destination"),

(7, "7:24–7:38",
 "Every tool you add costs you a decision. Which one for this, how do I get the file in, where does the output go.",
 "你每加一个工具，都要付出一次决策。这一步用哪个、文件怎么给它、结果放哪儿。",
 "三个问号状的空白标记，依次悬在一条流程线上。",
 "「a decision」是这一段的关键词，重音要给足。",
 "push-in",
 "A single glowing process line on a dark surface with three small blank diamond-shaped markers hovering above it at intervals, each marker a point where the line pauses and must choose. Cyan light from the line, violet fill behind. The markers are empty and unresolved. The sense of repeated small hesitations builds along the line.",
 "push the camera slowly along the line from one hovering decision marker to the next"),

(7, "7:38–7:52",
 "Those decisions are the expensive part. Not the tool, not the subscription price. The ten seconds of hesitation every single morning.",
 "这些决策才是贵的那部分。不是工具，不是订阅费。是每天早上那十秒钟的犹豫。",
 "一只手悬在几个几乎一样的东西上方，停住不动。",
 "把抽象成本落到「十秒钟」。这是让观众点头的一句。",
 "hold",
 "A hand hovering indecisively a few centimetres above a row of nearly identical small dark objects on a matte black desk, unable to choose between them. Cool cyan edge light from the left leaves the hand half in shadow. Nothing moves. The hesitation is captured perfectly, the moment stretched out and slightly uncomfortable.",
 "hold the camera completely still, the hand does not move"),

(7, "7:52–8:06",
 "Two tools you know cold will beat forty-seven you're still evaluating. Not because two is virtuous, but because it's faster.",
 "两个你熟到不用想的工具，会打赢四十七个你还在评估的。不是因为「两个」更道德，而是因为它更快。",
 "两只手熟练地操作两件工具；旁边那堆四十七件落满灰。",
 "「Not because two is virtuous」——主动拆掉道德叙事，这段才站得住。",
 "push-in",
 "Two hands working fluidly and without hesitation across two familiar tools on a dark desk, the motion practised and fast. Off to one side, a large pile of dozens of identical small devices sits untouched under a visible layer of dust. Warm yellow light on the working hands, cold violet on the abandoned pile. The contrast between fluency and stagnation is immediate.",
 "push the camera slowly in toward the two hands working without pausing"),

(7, "8:06–8:20",
 "Think about your Monday morning. The ten minutes you spend deciding is the ten minutes you were trying to save.",
 "想想你的周一早上。你花在「决定」上的那十分钟，正是你一开始想省下来的那十分钟。",
 "一只手看着时钟，另一只手还没开始动。",
 "这一段收口，把机制拉回具体场景。",
 "push-in",
 "Close-up on a dark desk at dawn, a small analogue clock face in the left of frame showing early morning, and a hand resting motionless on the desk beside it, having not yet started anything. Pale cool daylight beginning to enter from a window off-frame. The scene is still and slightly rueful. Nothing has been done yet and time is already passing.",
 "push the camera slowly in toward the clock face and the idle hand beside it"),

# ---------- S8 收口 + 互动钩子 ----------
(8, "8:20–8:34",
 "So tonight, ten minutes, one question. Not three. One.",
 "所以今晚，十分钟，一个问题。不是三个。就一个。",
 "三张卡片里，只有第一张被留下，另外两张被拿走。",
 "把动作压缩到最小。语速放慢，进入收尾节奏。",
 "push-in",
 "A hand lifting away two of the three blank cards from the dark desk, leaving the first card alone and brightly lit in the centre of frame. The other two are already out of the composition. Cool cyan light from above pools on the single remaining card. The reduction is clean and final.",
 "push the camera slowly in toward the single remaining card"),

(8, "8:34–8:48",
 "Go through your saved list and for each one ask: which step does this replace? If you can't answer in five seconds, delete it.",
 "把你收藏的清单过一遍，对每一个问一句：它替换的是哪一步？如果你五秒钟内答不上来，删掉。",
 "一只手把卡片一张一张划走，速度越来越快。",
 "给出明确的删除标准（5 秒）。具体标准 = 可执行。",
 "drift-right",
 "A hand sweeping blank cards rapidly off the near edge of a dark desk one after another, a few cards already caught mid-fall below the frame edge, the motion accelerating and slightly ruthless. Cool cyan edge light catches each card as it goes. The remaining pile on the desk is visibly shrinking. The action feels liberating rather than sad.",
 "pan the camera quickly to the right following the accelerating sweep of cards leaving the desk"),

(8, "8:48–9:02",
 "Don't research it. Don't give it a second chance. You've already given it forty-six.",
 "别去查它。别再给它一次机会。你已经给过它四十六次了。",
 "最后一张卡片被划走，桌面空了。",
 "「You've already given it forty-six」是这一段的笑点，也是真话。",
 "hold",
 "A completely empty matte black desk surface, the very last card having just been swept away, one card still tumbling through the air at the edge of frame. A single cool cyan light from above pools on the clean centre of the desk. Nothing remains. The emptiness is the point and it feels clean rather than lost.",
 "hold the camera completely still, the last card tumbles out of frame"),

(8, "9:02–9:16",
 "What's left is your real stack. It's smaller than you think, and it's enough. It was always enough.",
 "剩下的，才是你真正的工具箱。它比你以为的小，但它够了。它一直都够。",
 "空桌面上只剩两件工具，被暖黄光照亮。",
 "情感落点。语气要轻，不要煽情。",
 "push-in",
 "The same empty dark desk, but now just two small familiar tools rest on its surface side by side, lit warmly from above by a soft yellow lamp while the rest of the desk falls into cool shadow. They are modest, well-used, and sufficient. Dust motes drift in the warm beam. The scene is resolved and quiet.",
 "push the camera slowly down toward the two tools in the warm pool of light"),

(8, "9:16–9:24",
 "Now tell me in the comments: how many did you start with, and what's left?",
 "现在在评论区告诉我：你一开始有多少个，最后剩了几个？",
 "画面留白，只有那两件工具和一盏灯。",
 "CTA 只给一个，且必须能被具体回答。这是互动率的关键。",
 "pull-out",
 "The same quiet desk with the two tools under the warm lamp, the camera now wider, showing more of the dark empty room around the desk and a single window with pale pre-dawn light at the far edge of frame. The scene is calm, finished, and waiting. No other elements.",
 "pull the camera slowly straight back, revealing the quiet room around the desk"),

(8, "9:24–9:30",
 "I read every one of them. See you in the next one.",
 "每一条我都会看。下期见。",
 "灯灭，画面沉入黑暗，只剩一点余温。",
 "说完立刻收，不加片尾卡。",
 "hold",
 "The same dark room, but the warm desk lamp has just switched off, leaving only a faint residual glow on the desk surface that is already fading toward black. The two tools are barely visible silhouettes. The window's pale light remains at the edge of frame. Nothing moves. The image sits on the edge of total darkness.",
 "hold the camera completely still as the last warmth fades away"),
]

# ============================================================ 组装
def shots():
    out = []
    for i, (sec, win, en, zh, vis, emo, mot, img_core, vid_core) in enumerate(_SHOTS, 1):
        out.append({
            "id": f"A{i:02d}",
            "sec": sec,
            "window": win,
            "en": en,
            "zh": zh,
            "visual": vis,
            "emotion": emo,
            "motion": mot,
            "img_en": AI_CHARACTER + " " + AI_IMG_HEAD + img_core + " " + AI_IMG_TAIL,
            "vid_en": AI_CHARACTER + " " + AI_VID_HEAD + vid_core + " " + AI_VID_TAIL,
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
        "style_bible": AI_BIBLE,
        "pick": PICK,
        "titles": TITLES,
        "thumbs": THUMBS,
        "framework": FRAMEWORK,
        "shots": s,
        "shot_count": len(s),
        "word_count": words,
        "duration": "9:30",
        "framework_one_liner": "反常识 + 三问测试 + 一个真实流程（3 小时到 20 分钟）+ 主动暴露三个坑 + 互动钩子。",
        "numbers_source": "本片不含需外部核对的数据；所有流程判断标准均为可自测的真伪标准。",
    }


if __name__ == "__main__":
    d = build()
    print(d["topic"], "|", d["shot_count"], "shots |", d["word_count"], "words |", d["duration"])
