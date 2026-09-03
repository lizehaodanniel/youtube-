# -*- coding: utf-8 -*-
"""金融频道 · 火柴人故事版「世界锁」

这一层只定义**不会变**的东西：画风锁定描述、环境清单、角色形象锁、以及提示词拼装函数。
具体每一镜的动作 / 机位 / 动画写在 stick_act1~stick_act4.py。

为什么要把「世界」和「镜头」分开：
    火柴人动画最大的坑是跨镜头串型——同一个人在第 3 镜是方脑袋，第 40 镜变成圆脑袋。
    修法就是把画风 / 环境 / 形象全部抽成**常量**，每一条提示词都逐字引用同一段文字，
    一条镜头提示词里只写「这一镜发生了什么」。改形象只改这里，88 条提示词同步生效。

数字全部来自 _build/stick_numbers.py 的实算结果，不手写。核对口径：
    MAYA  22.15% → 20 个月 / $1,569 利息 / 对照投资 20 个月收益 $574  → 还债赢 $995
    DEVON  7.14% → 17 个月 / $  432 利息 / 对照投资 17 个月收益 $408  → 基本打平 $24
    PRIYA   3.5% → 17 个月 / $  205 利息 / 对照投资 17 个月收益 $408  → 投资赢 $204
    打平点（二分求解）≈ 6.77%
    最低还款 2% → 1,344 个月 ≈ 112 年 / $83,071 利息 / 首月 $160
    首月利息 8,000 × 22.15% / 12 = $147.67
    401(k) 年薪 $70,000 → 自缴 6% = $350/月 → 公司配 $175/月 = $2,100/年
    IRS 2026：个人递延上限 $24,500
"""

# ============================================================ 画风锁（STYLE 1 · 逐字引用）
# 来自 STICK FIGURE ANIMATION PIPELINE V2 BY PROVENTUBE.docx 的 STYLE 1 LOCKED DESCRIPTION。
# 文档要求：每一条图片提示词都要原样包含这一段。一个字都不要改。
STYLE_LOCK = (
    "Hyper realistic 3D cartoon illustration style. The stick figure character has a large "
    "perfectly round pure white head with a thick bold black circular outline, large expressive "
    "cartoon eyes with colored pupils and white sclera, thick bold emotive black eyebrows, and a "
    "wide open mouth showing teeth when expressing strong emotions. Hair is volumetric detailed "
    "and scene appropriate. The stick figure body has thin uniform black line arms and legs. "
    "Clothing is fully rendered in 3D cartoon style with visible fabric texture, stitching "
    "details, fold shading, and proper depth. The background environment is a fully rendered 3D "
    "cinematic cartoon scene with rich saturated colors, volumetric atmospheric lighting, "
    "dramatic depth of field blur on background elements, and realistic light behavior from all "
    "practical light sources in the scene. The overall quality feels like a high budget animated "
    "series or premium cartoon short film. Bold confident character outline contrasting against "
    "the richly rendered environment. 16:9, ultra detailed."
)

# ============================================================ 环境锁（14 个，全片只用这些）
# 文档 STATE 1 要求「Environment Decisions」一旦锁定，所有提示词都只能从这张表里取。
ENV = {
    "kitchen_night": (
        "The environment is a small American rental kitchen at 1:47 a.m.: a warm oak dining table "
        "with faded water rings, one warm pendant bulb hanging low on a black cord directly above "
        "the table, a closed laptop pushed against the wall, a cold half-full mug, a humming "
        "refrigerator visible in the background, laminate counters, and a window over the sink "
        "showing deep blue night with a single distant streetlight."
    ),
    "kitchen_dawn": (
        "The environment is the same small American rental kitchen at early dawn: cool pale blue "
        "light coming through the window over the sink, the warm pendant bulb now switched off, "
        "the same warm oak table with faded water rings, a cold mug, a closed laptop, and long "
        "soft shadows stretching across the laminate floor."
    ),
    "bathroom": (
        "The environment is a narrow apartment bathroom in the morning: a fogged rectangular "
        "mirror with a chrome frame above a white pedestal sink, a toothbrush in a ceramic cup, a "
        "small window with frosted glass letting in flat cold daylight, pale green tiled walls, "
        "and a folded towel on a rail."
    ),
    "cubicle": (
        "The environment is an open-plan American office cubicle in the late afternoon: beige "
        "fabric partitions, a grey laminate desk with a dual-monitor arm, an office chair, a "
        "sticky note stuck to the monitor bezel, a lukewarm paper coffee cup, and rows of "
        "identical empty desks fading into blurred background depth."
    ),
    "sidewalk": (
        "The environment is a grey American city sidewalk at 8 a.m.: cracked concrete paving, a "
        "bus stop shelter with a scratched plastic bench, a red fire hydrant, a row of brick "
        "storefronts with rolled-down grates, thin morning mist, and commuters blurred into soft "
        "background shapes."
    ),
    "grocery": (
        "The environment is a fluorescent-lit supermarket aisle: tall shelves stacked with "
        "colorful cereal boxes and canned goods, a red shopping cart, glossy white linoleum "
        "floor reflecting the ceiling lights, a green price tag strip along the shelf edge, and "
        "the aisle receding into blurred depth."
    ),
    "ledger_room": (
        "The environment is a vast warm hall made of aged oak and brass: a giant brass balance "
        "scale standing in the center on a stone pedestal, a long chalk number line painted "
        "across the floor boards, tall arched windows throwing warm shafts of light through "
        "floating dust, and rows of empty wooden chairs fading into shadow."
    ),
    "maya_apt": (
        "The environment is a cluttered studio apartment mid-move: stacked cardboard boxes with "
        "handwritten labels, a mattress leaning against the wall, a small round table buried "
        "under unopened envelopes and a single credit card statement, a bare bulb on a wire, and "
        "a window showing a brick wall across the alley."
    ),
    "devon_driveway": (
        "The environment is a suburban driveway at golden hour: a ten-year-old silver sedan with "
        "a chipped front bumper, an open garage door revealing a pegboard of hand tools and a "
        "folded tarp, oil stains on the concrete, a garden hose coiled on a hook, and low warm "
        "sunlight raking across the asphalt."
    ),
    "priya_studio": (
        "The environment is a tidy plant-filled home studio: a pale birch desk with a closed "
        "laptop and a ceramic pen cup, a corkboard pinned with a credit-union calendar and "
        "postcards, six potted plants on a floating shelf, a woven rug, and soft even daylight "
        "from a wide window with sheer curtains."
    ),
    "counting_table": (
        "The environment is a long oak counting table inside the warm brass hall: three neat "
        "stacks of green banknotes spaced evenly along the table, three small folded name cards "
        "in front of each stack, a brass desk lamp at one end, and deep warm shadow swallowing "
        "the far end of the table."
    ),
    "trap_room": (
        "The environment is a dark circular chamber dominated by a giant wooden hamster wheel "
        "built from oversized credit-card rectangles, a dented metal bucket with a steady leak "
        "dripping onto the stone floor, a single cold overhead work lamp, and wet reflective "
        "stone walls closing in from both sides."
    ),
    "home_office": (
        "The environment is a small home office desk at night: an open laptop glowing on a "
        "walnut surface, a ring of sticky notes along the monitor edge, a desk lamp with a warm "
        "shade, a closed spiral notebook, a phone lying face up, and a dark bookshelf blurred "
        "behind the chair."
    ),
    "porch": (
        "The environment is a wooden front porch at golden hour: a low railing with chipped "
        "white paint, a mailbox on a post at the bottom of the steps, a potted fern, a doormat, "
        "and long warm amber light stretching across the boards with the front door blurred open "
        "behind."
    ),
}

# ============================================================ 角色形象锁（4 个，逐字引用）
# 文档 STATE 1 要求「Character Appearance Lock」逐字出现在每个角色出场的每一条提示词里。
CHAR = {
    "you": (
        "The protagonist is a stick figure with a large perfectly round pure white head and a "
        "thick bold black circular outline. He has large expressive cartoon eyes with hazel "
        "pupils and white sclera, thick bold emotive black eyebrows, and a wide open mouth "
        "showing teeth when he reacts strongly. His hair is short, volumetric, dark brown and "
        "slightly messy at the back. His body is thin uniform black line arms and legs. He wears "
        "a heather-grey cotton crewneck sweatshirt rendered in 3D with visible knit fabric "
        "texture, ribbed cuffs and hem, a stitched shoulder seam and soft fold shading, plus "
        "dark navy cotton joggers with a white drawstring, simple grey sneakers, and a thin "
        "silver watch on his left wrist."
    ),
    "maya": (
        "Maya is a stick figure with a large perfectly round pure white head and a thick bold "
        "black circular outline. She has large expressive cartoon eyes with emerald-green pupils "
        "and white sclera, thick bold emotive black eyebrows, and a wide open mouth showing "
        "teeth when she reacts strongly. Her hair is a shoulder-length volumetric auburn bob "
        "with a side part. Her body is thin uniform black line arms and legs. She wears a "
        "mustard-yellow cable-knit sweater rendered in 3D with visible yarn texture, braided "
        "cable stitching, ribbed cuffs and soft fold shading, plus charcoal-grey trousers and "
        "small gold hoop earrings."
    ),
    "devon": (
        "Devon is a stick figure with a large perfectly round pure white head and a thick bold "
        "black circular outline. He has large expressive cartoon eyes with warm brown pupils and "
        "white sclera, thick bold emotive black eyebrows, and a wide open mouth showing teeth "
        "when he reacts strongly. His hair is a short volumetric black afro with a defined "
        "rounded silhouette. His body is thin uniform black line arms and legs. He wears a teal "
        "hooded sweatshirt rendered in 3D with visible fleece texture, a stitched kangaroo "
        "pocket, ribbed cuffs, drawstrings and soft fold shading, plus tan chino trousers and "
        "white low-top sneakers."
    ),
    "priya": (
        "Priya is a stick figure with a large perfectly round pure white head and a thick bold "
        "black circular outline. She has large expressive cartoon eyes with dark brown pupils and "
        "white sclera, thick bold emotive black eyebrows, and a wide open mouth showing teeth "
        "when she reacts strongly. Her hair is long, straight, volumetric jet-black hair tied in "
        "a low ponytail. Her body is thin uniform black line arms and legs. She wears a cream "
        "cotton blouse under an open rust-brown knit cardigan rendered in 3D with visible wool "
        "texture, a stitched button placket, ribbed cuffs and soft fold shading, plus olive-green "
        "trousers and a thin silver bangle on her right wrist."
    ),
}

CHAR_CN = {
    "you": "主角（观众的替身 · 灰毛衣 + 深蓝运动裤）",
    "maya": "Maya（22.15% 信用卡 · 芥黄麻花毛衣）",
    "devon": "Devon（7.14% 车贷 · 青绿连帽衫）",
    "priya": "Priya（3.5% 信用社贷款 · 奶油衬衫 + 锈棕开衫）",
}

ENV_CN = {
    "kitchen_night": "厨房 · 凌晨 1:47",
    "kitchen_dawn": "厨房 · 清晨",
    "bathroom": "卫生间 · 早晨",
    "cubicle": "开放式工位 · 傍晚",
    "sidewalk": "城市人行道 · 早 8 点",
    "grocery": "超市货架过道",
    "ledger_room": "黄铜大厅 · 巨型天平与数字线",
    "maya_apt": "Maya 的公寓 · 搬家纸箱",
    "devon_driveway": "Devon 的车道 · 旧银色轿车",
    "priya_studio": "Priya 的工作室 · 植物与软木board",
    "counting_table": "长橡木清点桌 · 三叠钞票",
    "trap_room": "陷阱房 · 信用卡做的巨型跑轮",
    "home_office": "家庭办公桌 · 夜间",
    "porch": "门廊 · 黄金时刻",
}

# ============================================================ 提示词尾（一致性 + 单帧 + 无字）
# 文档 STATE 5 的 STRICT RULES 全部落在这里：无字、无分格、不近于中近景、
# 不与上一镜同机位、画面必须是「动作即将开始」的那一帧（方便图生视频）。
IMG_TAIL = (
    "Everything visible in frame belongs to this one single scene. Absolutely no text, no "
    "letters, no numbers, no captions, no logos and no watermarks anywhere in the image. No "
    "split panels, no side-by-side frames, no comic grid, no storyboard layout — this is ONE "
    "single frame. No extra people, no duplicate characters, no stray hands, arms or feet "
    "belonging to nobody. The camera framing must not repeat the previous shot. The figure is "
    "posed at the exact starting point of the action, completely still and ready to move, not "
    "caught mid-motion. No extreme close-up — the closest acceptable framing is a medium close "
    "shot."
)

VID_TAIL = (
    "The clip runs for exactly 6 seconds. No text, no letters, no captions and no logos appear "
    "at any point. No lip sync, no talking mouth movement, no dialogue. The character's "
    "appearance, clothing and proportions never change during the clip. Nothing morphs, warps or "
    "distorts. No smoke, sparks or atmospheric effects appear without a visible physical source "
    "already in the shot. All storytelling is carried by physical movement only."
)

NEGATIVE = (
    "text, letters, words, numbers, captions, subtitles, watermark, logo, signature, split "
    "screen, 2x2 grid, four panels, comic panel grid, storyboard layout, diptych, triptych, "
    "collage, duplicate character, two heads on one body, cloned figure, extra person, crowd, "
    "floating hands, floating feet, detached limbs, extra arms, extra legs, six fingers, deformed "
    "hands, extreme close-up, macro face shot, morphing, warping, blurry smeared face, "
    "photorealistic human, real photograph, live actor, anime style, chibi, low resolution, "
    "jpeg artifacts"
)

# ============================================================ 视频提示词的六段骨架
# 文档 STATE 6 硬性要求按这个顺序写：机位 → 环境先动什么 → 角色第一个动作 →
# 镜头怎么动 + 为什么 → 角色接着做什么 → 最后一帧长什么样。
# 每段之间用固定连接词串起来，保证 120–180 词、结构不会跑偏。
# 注意第三段：a3 自己就带着主语（"he lifts…" / "Maya turns…"），
# 所以模板里不能再写 "The character then {a3}"，否则会拼出 "The character then he lifts…"。
VID_ORDER = (
    "Camera at the start of the clip: {a1}. "
    "The first thing that moves in the environment is {a2}. "
    "{a3}. "
    "As that happens, the camera {a4}. "
    "Next, {a5}. "
    "The final frame holds on {a6}."
)


def B(narr, zh, env, who, act, cam, light, a1, a2, a3, a4, a5, a6):
    """一条 beat 的 13 个字段。

    narr 口播英文（10–13 词）· zh 中文 · env 环境锁 key · who 出场角色 key 元组
    act  这一镜「动作即将开始」的那一帧在发生什么
    cam  机位与景别（不能和上一镜重复，最近只能到中近景）
    light 光线、色调、情绪
    a1–a6 视频提示词六段：起始机位 / 环境先动什么 / 角色第一个动作 / 镜头怎么动 /
           角色接着做什么 / 最后一帧
    """
    return dict(narr=narr, zh=zh, env=env, who=tuple(who), act=act, cam=cam,
                light=light, a=(a1, a2, a3, a4, a5, a6))


def img_prompt(env, who, act, cam, light):
    """拼一条图片提示词：画风锁 + 环境锁 + 角色锁 + 动作 + 机位 + 光与情绪 + 尾。"""
    chars = " ".join(CHAR[w] for w in who)
    return " ".join([STYLE_LOCK, ENV[env], chars, act.strip(), cam.strip(),
                     light.strip(), IMG_TAIL])


def vid_prompt(a1, a2, a3, a4, a5, a6):
    """拼一条视频提示词：六段骨架 + 尾。a3 带主语，首字母要大写。"""
    a3 = a3.strip()
    a3 = a3[0].upper() + a3[1:] if a3 else a3
    body = VID_ORDER.format(a1=a1.strip(), a2=a2.strip(), a3=a3,
                            a4=a4.strip(), a5=a5.strip(), a6=a6.strip())
    return body + " " + VID_TAIL


def word_count(s):
    return len(str(s).split())
