# -*- coding: utf-8 -*-
"""AI 频道（aicheatcode / AI Cheatcode Playbook）实操素材清单。

背景：8 张实操卡里引用了一堆文件（7 张 PNG、文案文档、MP4、报价单…），
但只写了文件名，没写「里面该是什么」。本模块把每个素材的具体内容全部写死：

  - 图片素材  → 图片提示词（英 + 中），可直接喂 Midjourney
  - 视频素材  → 视频提示词（英 + 中），可直接喂 Runway / Kling / Veo
  - 文档/文案 → 完整可复制的全文（不是描述，是成品本身）

虚构客户固定为 **TWO MILE COFFEE**（街角咖啡店，客群是两英里内的上班族与学生），
全片所有素材都围绕这一家店，保证 7 张图看起来像同一个 campaign。
"""

# ---------------------------------------------------------------- 素材后缀
IMG_SUFFIX_EN = ", commercial photography, ultra-detailed, 8k resolution, square crop, --ar 1:1 --v 6.0"
IMG_SUFFIX_ZH = "，商业摄影，超高细节，8k 分辨率，方形裁切，--ar 1:1 --v 6.0"

VID_SUFFIX_EN = ", smooth handheld camera, natural motion, no text overlay, cinematic, 4k"
VID_SUFFIX_ZH = "，平稳手持镜头，自然运动，无文字叠加，电影感，4k"


# ================================================================ 7 张 PNG
# 卡 1（成品展示）和卡 4（Canva 制作）共用同一份定义，保证两处永远一致。
SEVEN_PNGS = [
    {
        "file": "01-monday-cold-brew.png",
        "topic": "周一 · 冷萃上新",
        "headline": "COLD BREW IS HERE",
        "sub": "18-hour steep. Monday only: $3.",
        "cta": "GET ONE MONDAY",
        "brief": "开场第一张，必须是整组里最「贵气」的一张：玻璃杯 + 大冰块 + 水珠，冷萃的琥珀色要压得住深棕背景。",
        "img_en": (
            "Product photo of a tall clear glass filled with cold brew coffee, large hand-cut ice cubes, "
            "condensation beads running down the glass, deep amber-brown liquid, three coffee beans scattered "
            "on a warm cream surface, soft natural window light from the left, a soft shadow falling to the right, "
            "shallow depth of field, clean minimal studio composition, no text, no people"
        ) + IMG_SUFFIX_EN,
        "img_zh": (
            "产品摄影：一只高玻璃杯装满冷萃咖啡，大块手切冰块，杯壁挂满往下流的凝结水珠，深琥珀棕色液体，"
            "暖奶油色台面上散落三颗咖啡豆，左侧柔和自然窗光，右侧落下柔和阴影，浅景深，极简干净的棚拍构图，"
            "无文字，无人物"
        ) + IMG_SUFFIX_ZH,
    },
    {
        "file": "02-tuesday-student-20.png",
        "topic": "周二 · 学生折扣 20%",
        "headline": "TUESDAY, STUDENTS DRINK CHEAPER",
        "sub": "20% off with a student ID. All day.",
        "cta": "SHOW YOUR ID",
        "brief": "要一眼看懂「学生」：证件、帆布包带、笔记本三件套。咖啡用外带纸杯（学生是带走喝的），不要用堂食杯。",
        "img_en": (
            "Product photo of a kraft paper takeaway coffee cup with a white lid on a light oak desk, "
            "a student ID card lying face down beside it, a canvas backpack strap and a small spiral notebook, "
            "morning light from a window, warm neutral tones, soft shadow, shallow depth of field, "
            "clean lifestyle composition, no readable text, no people"
        ) + IMG_SUFFIX_EN,
        "img_zh": (
            "产品摄影：一只牛皮纸外带咖啡杯配白色杯盖，放在浅橡木桌面上，旁边反扣着一张学生证，"
            "一根帆布书包带和一个小螺旋笔记本，窗外晨光，暖中性色调，柔和阴影，浅景深，"
            "干净的生活方式构图，无可读文字，无人物"
        ) + IMG_SUFFIX_ZH,
    },
    {
        "file": "03-wednesday-7am.png",
        "topic": "周三 · 早鸟 7 点开门",
        "headline": "WE OPEN AT 7. YOU KNOW WHY.",
        "sub": "First hour, drip is $2.",
        "cta": "SEE YOU AT SEVEN",
        "brief": "全组唯一一张空景。清晨斜射的金色光线是重点，蒸汽要淡，不能糊住镜头。店里必须没人。",
        "img_en": (
            "Interior of a small cozy coffee shop at sunrise, completely empty, warm golden light streaming "
            "through the front window in long beams, an espresso machine on the wooden counter with a thin "
            "steam haze, a chalkboard on the brick wall, hanging pendant lamps, calm quiet morning mood, "
            "shallow depth of field, no people, no text"
        ) + IMG_SUFFIX_EN,
        "img_zh": (
            "小店咖啡馆室内，日出时分，完全无人的空景，温暖的金色光线从前窗斜射进来形成长光束，"
            "木质吧台上一台意式咖啡机冒着淡淡蒸汽，砖墙上一块小黑板，几盏吊灯，安静的清晨氛围，"
            "浅景深，无人物，无文字"
        ) + IMG_SUFFIX_ZH,
    },
    {
        "file": "04-thursday-pairing.png",
        "topic": "周四 · 咖啡配甜点",
        "headline": "COFFEE NEEDS A PARTNER",
        "sub": "Any drip + almond croissant, $6.",
        "cta": "ADD THE CROISSANT",
        "brief": "俯拍（overhead）构图，和前 3 张的平视形成节奏变化。亚麻餐布的褶皱要保留，别拍得像 plastic。",
        "img_en": (
            "Overhead flat-lay product photo of a ceramic coffee cup filled with black coffee and an almond "
            "croissant on a crumpled linen napkin, a few coffee beans scattered nearby, warm natural light "
            "from the upper left, soft shadows, earthy neutral palette, shallow depth of field, "
            "editorial food photography, no text, no people"
        ) + IMG_SUFFIX_EN,
        "img_zh": (
            "俯拍平铺产品摄影：一只陶瓷咖啡杯装着黑咖啡，旁边一块杏仁可颂，放在有褶皱的亚麻餐布上，"
            "附近散落几颗咖啡豆，左上方暖自然光，柔和阴影，大地色中性色调，浅景深，"
            "杂志级美食摄影，无文字，无人物"
        ) + IMG_SUFFIX_ZH,
    },
    {
        "file": "05-friday-weekend.png",
        "topic": "周五 · 周末预告（三杯 flight）",
        "headline": "THE WEEKEND STARTS FRIDAY 4PM",
        "sub": "Cold brew flights, three for $9.",
        "cta": "TASTE ALL THREE",
        "brief": "三只小杯一字排开，颜色从浅烘到深烘有明显递进 —— 这是全组唯一靠「排列」取胜的一张。逆光打透液体。",
        "img_en": (
            "Product photo of three small glasses of cold brew coffee in a row on a dark wooden board, "
            "the liquid shade graduating from light amber to deep espresso brown left to right, "
            "backlit so the liquid glows, a few ice cubes and one small mint sprig, warm rim light, "
            "shallow depth of field, no text, no people"
        ) + IMG_SUFFIX_EN,
        "img_zh": (
            "产品摄影：三只小玻璃杯装冷萃咖啡，一字排开放在深色木板上，液体颜色从左到右由浅琥珀渐变到深浓缩棕，"
            "逆光让液体透亮发光，几块冰块和一小枝薄荷，暖色轮廓光，浅景深，无文字，无人物"
        ) + IMG_SUFFIX_ZH,
    },
    {
        "file": "06-saturday-two-miles.png",
        "topic": "周六 · 邻里 / 两英里",
        "headline": "TWO MILES. THAT'S THE WHOLE PLAN.",
        "sub": "We only serve the neighbourhood.",
        "cta": "COME SAY HI",
        "brief": "傍晚外景，室内灯光透出窗户是暖黄的关键。自行车和行道树是「邻里感」的两个道具，缺一就变成地产广告。",
        "img_en": (
            "Exterior of a small corner coffee shop storefront at early dusk, warm amber interior light "
            "glowing through large windows, a simple hanging sign, a bicycle leaning against the brick wall, "
            "a street tree with autumn leaves, wet pavement reflecting the light, cozy neighbourhood mood, "
            "no people, no readable text"
        ) + IMG_SUFFIX_EN,
        "img_zh": (
            "街角小咖啡店店面外景，黄昏初临，温暖的琥珀色室内灯光透过大窗户亮起来，一块简洁的挂牌，"
            "一辆自行车斜靠在砖墙上，一棵秋天的行道树，湿漉漉的路面反射灯光，温馨的邻里氛围，"
            "无人物，无可读文字"
        ) + IMG_SUFFIX_ZH,
    },
    {
        "file": "07-sunday-reminder.png",
        "topic": "周日 · 最后提醒",
        "headline": "LAST CALL ON THE COLD BREW",
        "sub": "Sunday 5pm, we dump the batch.",
        "cta": "ONE MORE CUP",
        "brief": "收尾图，情绪要「快没了」：半空杯、化掉的冰、杯口的咖啡渍。光比要暗一档，跟 01 形成首尾呼应。",
        "img_en": (
            "Product photo of a half-empty glass of cold brew coffee, melted ice cubes, dried coffee stains "
            "on the rim, on a dark wooden table next to a glass coffee pot with only a small amount left, "
            "late afternoon moody light, darker exposure, warm brown tones, shallow depth of field, "
            "editorial food photography, no text, no people"
        ) + IMG_SUFFIX_EN,
        "img_zh": (
            "产品摄影：一只喝剩一半的冷萃咖啡杯，冰块已经融化，杯口留着干掉的咖啡渍，"
            "深色木桌上旁边是一只只剩一点咖啡的玻璃咖啡壶，傍晚偏暗的氛围光，曝光压暗一档，暖棕色调，"
            "浅景深，杂志级美食摄影，无文字，无人物"
        ) + IMG_SUFFIX_ZH,
    },
]


# ================================================================ 文案文档
COPY_DECK = """TWO MILE COFFEE — COPY DECK
7 captions · plainspoken · short sentences · no exclamation marks
----------------------------------------------------------------

01 · MONDAY — cold brew launch
Cold brew, eighteen hours in the making, ready at seven tomorrow morning.
We made one small batch. When it's gone, it's gone.
Three dollars for the first fifty cups.
#coldbrew #twomilecoffee

02 · TUESDAY — student 20%
Bring a student ID on Tuesday and take twenty percent off anything in a cup.
No minimum. No app. No sign-up.
Just the card.
#studentdiscount #twomilecoffee

03 · WEDNESDAY — 7am opening
We open at seven. That is earlier than you want, and exactly when you need it.
Drip coffee is two dollars for the first hour.
Then it goes back to normal.
#earlybird #twomilecoffee

04 · THURSDAY — pairing
Coffee is better with something to dip.
Any drip and an almond croissant, six dollars together.
We bake them in the back, twelve at a time.
#coffeeandpastry #twomilecoffee

05 · FRIDAY — weekend preview
The weekend starts at four on Friday. We know, because that is when the line starts.
Three cold brews, three roasts, nine dollars.
Taste them in order, light to dark.
#coldbrewflight #twomilecoffee

06 · SATURDAY — two miles
We are not trying to reach the whole city.
Two miles, that is the plan. If you can walk here, you are the customer we built this for.
Come say hi. We remember orders, not names.
#neighbourhood #twomilecoffee

07 · SUNDAY — last call
Last call on the cold brew. Sunday at five we dump whatever is left.
It is not a trick. We brew fresh Monday.
One more cup, then go home.
#lastcall #twomilecoffee

----------------------------------------------------------------
Voice rules used across all seven:
  · Short sentences. One idea per sentence.
  · No exclamation marks.
  · Every number is a number the shop can actually honour.
  · No claim about health, no invented reviews, no invented awards.
"""


# ================================================================ 报价单
QUOTE = """TWO MILE COFFEE — CONTENT SPRINT QUOTE
(FICTIONAL SAMPLE — for demonstration only)

PROJECT      One week of launch content for a cold brew launch
PREPARED BY  [your name]
DATE         [date]
VALID FOR    14 days

----------------------------------------------------------------
DELIVERABLES
----------------------------------------------------------------
  7 × square social graphics      1080 × 1080, PNG
  7 × captions                    edited for voice, plain text
  1 × vertical video              30 seconds, 1080 × 1920, MP4
  1 × copy deck                   all 7 captions in one text file
  +   source files                Canva link + CapCut project file

PRICE                             $100 USD
TURNAROUND                        3 days from brief approval

----------------------------------------------------------------
INCLUDED
----------------------------------------------------------------
  [x] 1 round of revisions (all 10 files, in one batch)
  [x] Source files handed over at the end
  [x] You provide: logo, 2 brand colours, licensed product photos

----------------------------------------------------------------
NOT INCLUDED
----------------------------------------------------------------
  [ ] Posting, scheduling or community management
  [ ] Paid ads, boosting or ad budget
  [ ] Promised reach, follower growth or sales
  [ ] Photo shoots — we use your photos or licensed stock only
  [ ] Copywriting for menus, websites or packaging

----------------------------------------------------------------
REVISION POLICY
----------------------------------------------------------------
  A second round is billed at $35 / hour, 90 minutes minimum.
  That is $52.50 before the second round even starts, which is
  why the brief has to be signed off before we build anything.

----------------------------------------------------------------
SCOPE (4 lines — read this before signing)
----------------------------------------------------------------
  1. One round of revisions.
  2. Client supplies logo and licensed photos.
  3. Three-day delivery from brief approval.
  4. No promise of results. We promise files, not outcomes.

This is a fictional sample created for a tutorial video.
No real client, no real invoice, no real money.
"""


# ================================================================ 卡 2 需求单
BRIEF_DOC = """COFFEE SHOP CONTENT SPRINT — BRIEF (FICTIONAL)

CLIENT'S WORDS
  "We want more people to come in next week."

AUDIENCE
  Office workers and students within two miles.
  They walk past the door twice a day. They are not looking for a
  destination, they are looking for a reason to stop.

BUSINESS PROBLEM
  A cold brew launches next week.
  They need seven days of content and currently have none.
  The window is one week. After launch the content is worthless.

DELIVERABLES
  7 graphics · 7 captions · 1 vertical video

EXPLICITLY NOT INCLUDED
  [ ] No paid ads
  [ ] No posting on their behalf
  [ ] No promise of viral reach

----------------------------------------------------------------
Why this template works:
  One audience. One problem. One deliverable list. One exclusion list.
  If any of those four is missing, the project will grow.
"""


# ================================================================ 卡 3 ChatGPT
PROMPT_V1 = """You are writing social media captions for a small neighbourhood
coffee shop.

Shop: Two Mile Coffee, a corner shop. Most customers live or work
within two miles.

This week: they are launching a cold brew. Doors open at 7am.
On Tuesday, students get 20% off with an ID.

Audience: office workers and students who walk past the door twice
a day.

Task: write a table with 7 rows, one row per day, Monday to Sunday.

Columns:
  Hook | Customer situation | One proof point | CTA | What to verify

Keep the tone friendly and energetic. Make it sound exciting.

Output a markdown table only. No preamble."""


OUTPUT_V1 = """| # | Hook | Customer situation | One proof point | CTA | What to verify |
|---|------|--------------------|-----------------|-----|----------------|
| 1 | The cold brew you have been waiting for is finally here | Walking to work, too hot for a latte | Steeped for 18 hours | Get one Monday | 18 hours — confirm with the barista |
| 2 | Students, this one is for you | Between classes, counting coins | Rated 5 stars by 200+ regulars | Show your ID Tuesday | INVENTED — no such review exists |
| 3 | Early birds get the good stuff | Alarm at 6:40, needs coffee by 7 | Doors open at seven | See you at seven | 7am opening — on the door, check |
| 4 | Your coffee called, it wants a croissant | Mid-morning slump at the desk | Voted best pastry in the city | Add the croissant | INVENTED — no such award exists |
| 5 | The weekend starts now | Friday afternoon, done with work | Three roasts on one flight | Taste all three | Flight price $9 — confirm |
| 6 | Good coffee, two miles from your door | Saturday walk, no plan | Hundreds of neighbours already come | Come say hi | INVENTED — no such number exists |
| 7 | Last chance before we dump it | Sunday, one more errand | Cold brew is antioxidant rich | One more cup | INVENTED — health claim, delete |

3 cells to mark red during the video:
  Row 2 · "Rated 5 stars by 200+ regulars"  -> INVENTED REVIEW
  Row 4 · "Voted best pastry in the city"   -> INVENTED AWARD
  Row 7 · "antioxidant rich"                -> HEALTH CLAIM
"""


PROMPT_V2 = """Regenerate rows 2, 4 and 6 only.
Leave rows 1, 3, 5 and 7 exactly as they are.

New rule for the new rows:
  Every number, price, rating, award or health claim must be
  something the shop can verify. If you cannot ground it in a fact
  the shop gave you, write VERIFY in that cell. Do not invent it.

Then, for rows 1, 3 and 5, rewrite the Hook in this voice:
  · Plainspoken
  · Short sentences, one idea each
  · No exclamation marks
  · No marketing adjectives (amazing, incredible, delicious)
  · No invented proof

Show me the corrected table, and below it list what you changed."""


FINAL_CAPTIONS = """FINAL — 3 rewritten captions (plainspoken voice)

01 · MONDAY
Cold brew, eighteen hours in the making, ready at seven tomorrow morning.
We made one small batch. When it's gone, it's gone.
Three dollars for the first fifty cups.

03 · WEDNESDAY
We open at seven. That is earlier than you want, and exactly when you need it.
Drip coffee is two dollars for the first hour.
Then it goes back to normal.

05 · FRIDAY
The weekend starts at four on Friday. We know, because that is when the line starts.
Three cold brews, three roasts, nine dollars.
Taste them in order, light to dark.

----------------------------------------------------------------
What changed from the first draft:
  · Deleted the invented 5-star review
  · Deleted the invented "best pastry" award
  · Deleted the health claim
  · Cut every exclamation mark
  · Every remaining number is one the shop can honour
"""


# ================================================================ 卡 4 品牌规范
BRAND_KIT = """TWO MILE COFFEE — BRAND KIT (fictional, for this demo)

COLOURS
  Espresso    #3B2314   ← background, headlines
  Cream       #F5E9D7   ← background, body text on dark
  Terracotta  #C75B39   ← CTA button only, one per graphic

FONT
  Headline : Inter Bold, all caps, letter-spacing +2%
  Body     : Inter Regular, sentence case
  (Any clean geometric sans works. Do not mix two families.)

LOGO
  Format : PNG, transparent background, min 1000px wide
  Place  : top-left, 48px margin from both edges
  Rule   : never stretch, never recolour, never add a drop shadow

LAYOUT GRID (applies to all 7 pages)
  1080 × 1080
  Product photo : bottom half, bled to the edge
  Headline      : top third, 2 lines maximum
  CTA button    : horizontally centred, 96px above the bottom edge
  Safe margin   : 48px on all four sides

ONE RULE THAT MATTERS
  Set colours and font ONCE in the brand kit, before page 1.
  If you set them page by page, page 5 will be slightly off and
  nobody will be able to tell you why.
"""


NAMING_LIST = """FILE NAMING — 7 exports from Canva

  01-monday-cold-brew.png
  02-tuesday-student-20.png
  03-wednesday-7am.png
  04-thursday-pairing.png
  05-friday-weekend.png
  06-saturday-two-miles.png
  07-sunday-reminder.png

RULES
  · Two-digit prefix keeps them in order in every file browser
  · Lowercase, hyphens only, no spaces, no underscores
  · The name says the day and the offer, not the design
  · Same prefix order is reused for the 7 captions in the copy deck

WHY BOTHER
  When the client opens the folder, the filenames are the first
  thing they read. "Canva design (3).png" says you were improvising.
"""


# ================================================================ 卡 5 验收清单
QC_CHECKLIST = """FIVE-POINT QC — run this on every one of the 7 pages

  [ ] 1. LOGO      Correct file, sharp at 100%, not stretched,
                   in the same corner on all 7 pages
  [ ] 2. COLOURS   Taken from the brand kit, not eyedropped
                   off a photo. Check the hex, not your eyes.
  [ ] 3. OFFER     Price, day and discount match the brief.
                   This is the one that gets people refunds.
  [ ] 4. SPELLING  Read every word out loud. Shop name and
                   product name twice. Autocorrect will not
                   catch a wrong product name.
  [ ] 5. LICENCE   Every photo is either supplied by the client
                   or licensed stock. Screenshot the licence.

ANY ONE BOX UNCHECKED = THE PAGE IS NOT DONE.
Do not fix it later. Fix it now, while the file is open.
"""


QC_CARD_IMG_EN = (
    "A clean dark UI card floating in the corner of a screen, listing five checklist rows with empty "
    "square checkboxes, each row labelled LOGO, COLOURS, OFFER, SPELLING, LICENCE, thin white icons "
    "beside each label, terracotta accent on the first checkbox, minimal flat design, dark espresso "
    "background, soft glow, no other text"
)

QC_CARD_IMG_ZH = (
    "一张干净的深色 UI 卡片浮在屏幕角落，列出五行带空白方形复选框的清单，每行分别标注 "
    "LOGO、COLOURS、OFFER、SPELLING、LICENCE，每个标签旁有细线白色图标，第一个复选框用陶土色高亮，"
    "极简扁平设计，深浓缩咖啡色背景，柔和发光，无其他文字"
)


# ================================================================ 卡 6 CapCut
CLIP_POUR = {
    "en": (
        "Close-up shot of hands pouring cold brew coffee from a glass pot into a tall glass with ice, "
        "the dark liquid catching the light as it falls, condensation on the glass, warm cafe background "
        "out of focus, slow smooth motion, vertical 9:16 framing"
    ) + VID_SUFFIX_EN,
    "zh": (
        "特写镜头：一双手把冷萃咖啡从玻璃壶倒进装了冰块的高杯里，深色液体在下落时透光，"
        "杯壁挂满水珠，背景是虚化的温暖咖啡馆，缓慢平稳的运动，9:16 竖屏构图"
    ) + VID_SUFFIX_ZH,
}

CLIP_DOOR = {
    "en": (
        "Shot of a cafe door being pushed open from outside, a hand on the glass, warm light spilling out "
        "onto the pavement, a small hanging sign swinging slightly, early evening, shallow depth of field, "
        "vertical 9:16 framing"
    ) + VID_SUFFIX_EN,
    "zh": (
        "镜头：咖啡店的门被从外面推开，一只手按在玻璃上，温暖的灯光洒到人行道上，"
        "小挂牌轻轻晃动，傍晚时分，浅景深，9:16 竖屏构图"
    ) + VID_SUFFIX_ZH,
}

CLIP_FINISHED = {
    "en": (
        "Beauty shot of a finished cold brew coffee on a wooden counter, slow push-in, ice cubes settling, "
        "steam-free cold condensation, warm rim light from a window, the cup turning slightly, "
        "vertical 9:16 framing"
    ) + VID_SUFFIX_EN,
    "zh": (
        "产品美图镜头：一杯做好的冷萃咖啡放在木质吧台上，缓慢推近，冰块轻轻沉底，"
        "杯壁是冷冷凝结的水珠，窗户透进暖色轮廓光，杯子微微转动，9:16 竖屏构图"
    ) + VID_SUFFIX_ZH,
}

ONSCREEN_TEXT = """ON-SCREEN TEXT (CapCut text layer)

  Line 1 : COLD BREW LAUNCH
  Line 2 : TUE · STUDENT 20% OFF

PLACEMENT
  Bottom third of the frame, above the caption area
  Font: same geometric sans as the graphics, all caps
  Size: must be readable at arm's length on a phone —
        if you have to lean in, it is too small

TIMING
  Appears at 00:03, stays until the end
  Do not animate it in with a spin. Fade only.
"""

SUBTITLE_TEXT = """AUTO-CAPTIONS — proofread pass

RAW (what the auto-captioner heard):
  00:00  so we made a cold blue
  00:04  eighteen hours in the making
  00:09  three dollars for the first fifty cups

CORRECTED:
  00:00  So we made a cold brew.          <- cold blue -> cold brew
  00:04  Eighteen hours in the making.
  00:09  Three dollars for the first fifty cups.

RECORD THIS ON CAMERA
  Pause on the "cold blue" line. Select the word. Retype it.
  That three-second fix is the whole reason people trust the video.
  If you skip it, the caption says "cold blue" in front of the client.
"""

EXPORT_NAMES = """EXPORT CHECKLIST — CapCut

  cold-brew-launch-30s.mp4        1080 × 1920, H.264, 30fps
  cold-brew-launch.project        CapCut project file (keep it)
  caption.txt                     the 7 captions, plain text

ALL THREE GO IN THE SAME FOLDER AS THE 7 PNGs.

Then: play the mp4 on your phone with the sound OFF.
If the story does not make sense without audio, reshoot the text
layer, do not add a voiceover.
"""


# ================================================================ 卡 7 计时表
TIME_SHEET = """TASK                 MINUTES
Brief intake             15
7 captions               35
Canva · 7 graphics       55
CapCut · 30s video       45
QC pass                  20
---------------------------------
TOTAL                   170
HOURS                 2.83
PRICE                  $100
GROSS HOURLY         $35.32

GROSS = before software, before tax, before any revisions.
It is not your wage. It is the number you show the client so they
understand where the $100 went.

----------------------------------------------------------------
NOW ADD ONE REVISION ROUND

  Revision time           +90 min
  New total              260 min  (4.33 h)
  Same price             $100
  New gross hourly    $23.08      <- down from $35.32

Say this out loud in the video. One revision round and you are
working for two-thirds of the rate you quoted. This is why the
brief gets signed off before anything gets built.
"""

SCOPE_CARD = """SCOPE CARD (4 lines — put this on screen, read it out loud)

  1. One round of revisions.
  2. Client supplies logo and licensed photos.
  3. Three-day delivery from brief approval.
  4. No promise of results. We promise files, not outcomes.

Read line 4 slowly. It is the line that saves you later.
"""


# ================================================================ 卡 8 模板 + 邮件
TEMPLATE_PROMPT_SKELETON = """PROMPT SKELETON — reuse for any local business

  You are writing social captions for a [TYPE OF BUSINESS].

  Business: [NAME]. Most customers are within [DISTANCE].

  This week they are [WHAT IS HAPPENING].
  Offer: [SPECIFIC OFFER, WITH NUMBERS].
  Audience: [WHO WALKS PAST THE DOOR, AND WHEN].

  Task: write a table with [N] rows, one per [DAY / POST].
  Columns: Hook | Customer situation | One proof point |
           CTA | What to verify

  Voice rules:
    · Plainspoken, short sentences, no exclamation marks
    · No invented reviews, awards, ratings or health claims
    · If you do not have a fact, write VERIFY

  Output a markdown table only.

FILL THE FOUR BRACKETS AND THIS WORKS FOR ANY SHOP, SALON OR GYM.
Changing the business type is a 30-second edit.
"""

QUOTE_EMAIL = """TO:        owner@twomilecoffee.example   (one recipient only)
SUBJECT:   your Tuesday posts

Hi [name],

I noticed you post almost nothing on Tuesdays, and Tuesdays are
when the students come past.

I can put together seven graphics, seven captions and one 30-second
video for your cold brew week — three days from a yes, one hundred
dollars.

What that does not include: I will not run ads, I will not post for
you, and I will not promise you followers. One round of changes is
included; you send the logo and any photos you own.

If it is not for you, reply "no" and I will leave it there.

[your name]

----------------------------------------------------------------
WHY THIS EMAIL
  · Line 1 is one specific observation, not "hope you are well"
  · Line 2 is a deliverable and a price and a date, in that order
  · Line 3 is the boundary — it makes line 2 believable
  · Line 4 gives them an easy no, which is why they say yes
  · One recipient. If it could be sent to fifty shops, delete it
    and start again.
"""


# ================================================================ 组装
def _png_items(prefix, with_headline=True):
    """7 张 PNG 的素材条目。prefix 用于编号（1-x / 4-x）。"""
    items = []
    for i, p in enumerate(SEVEN_PNGS, 1):
        d = {
            "no": f"{prefix}-{i}",
            "kind": "image",
            "name": p["file"],
            "spec": "1080 × 1080 PNG",
            "brief_zh": p["brief"],
        }
        if with_headline:
            d["on_image_zh"] = f"标题：{p['headline']}　／　副标：{p['sub']}　／　CTA 按钮：{p['cta']}"
        d["img_en"] = p["img_en"]
        d["img_zh"] = p["img_zh"]
        items.append(d)
    return items


CARDS = [
    {
        "id": 1,
        "title": "开场成品文件夹（10 个文件）",
        "note": "这 10 个文件是整支视频的「证据」。观众在前 15 秒如果看不到具体文件，后面讲什么都会变成吹牛。7 张 PNG 的图片提示词与实操卡 4 是同一套（那里是制作视角，这里是成品视角）。",
        "items": _png_items("1") + [
            {
                "no": "1-8",
                "kind": "doc",
                "name": "copy-deck.txt",
                "spec": "纯文本 / Markdown · 7 条配图文案",
                "brief_zh": "7 条社媒配文，一条配一张图。风格统一：短句、无感叹号、每个数字都是店家真能兑现的。直接抄进文档即可，不需要改。",
                "content": COPY_DECK,
            },
            {
                "no": "1-9",
                "kind": "video",
                "name": "cold-brew-launch-30s.mp4",
                "spec": "1080 × 1920 竖屏 · 30 秒 · 无配音也能看懂",
                "brief_zh": "一条 30 秒竖屏视频。三段素材拼接（倒咖啡 → 推门 → 成品杯），屏幕上必须常驻一行活动文字。完整的三段镜头提示词见实操卡 6。",
                "vid_en": (
                    "A 30-second vertical social video for a neighbourhood coffee shop cold brew launch. "
                    "Shot 1 (0-10s): close-up of cold brew being poured over ice, dark liquid catching the light. "
                    "Shot 2 (10-20s): the shop door pushed open from the street, warm light spilling onto the pavement. "
                    "Shot 3 (20-30s): beauty shot of the finished cold brew on a wooden counter, slow push-in. "
                    "Warm muted grade, natural handheld movement, no people speaking to camera"
                ) + VID_SUFFIX_EN,
                "vid_zh": (
                    "一条 30 秒竖屏社媒视频，为街角咖啡店的冷萃上新而拍。"
                    "镜头 1（0-10 秒）：特写，冷萃咖啡浇在冰块上，深色液体透光。"
                    "镜头 2（10-20 秒）：店门从街外被推开，暖光洒到人行道。"
                    "镜头 3（20-30 秒）：做好的冷萃放在木吧台上的美图镜头，缓慢推近。"
                    "暖调柔和调色，自然手持运动，无人物对镜头说话"
                ) + VID_SUFFIX_ZH,
            },
            {
                "no": "1-10",
                "kind": "sheet",
                "name": "quote-two-mile-coffee.txt",
                "spec": "纯文本报价单 · 与口播里的 $100 完全对应",
                "brief_zh": "报价单。包含与不包含必须写成两栏对照 —— 这是全片最容易被截图传播的一张。数字必须和实操卡 7 的计时表一致（170 分钟 / $35.32 毛时薪 / 第二轮修改 $35 每小时）。",
                "content": QUOTE,
            },
        ],
    },
    {
        "id": 2,
        "title": "案例需求单（可照抄的模板）",
        "note": "这张卡只有一件素材：那份需求单文档。全文在下面，直接复制粘贴进 Google Docs / Notion 即可，拍的时候照着打字。",
        "items": [
            {
                "no": "2-1",
                "kind": "doc",
                "name": "brief-two-mile-coffee.md",
                "spec": "文档 · 4 个板块",
                "brief_zh": "需求单模板。四个板块缺一不可：客户原话 / 受众 / 商业问题 / 交付物，外加一份「明确不包含」清单。标题里的 (FICTIONAL) 不能删 —— 防止观众以为是真客户。",
                "content": BRIEF_DOC,
            },
        ],
    },
    {
        "id": 3,
        "title": "ChatGPT：提示词 + 输出 + 修改指令（全部可抄）",
        "note": "这支视频最值钱的一段就是「AI 编造 → 人工标红 → 定向重生成」。下面 4 件素材把这个过程彻底写死：首轮提示词、首轮输出（含 3 处编造，专门留给你标红）、修改指令、最终干净版。",
        "items": [
            {
                "no": "3-1",
                "kind": "doc",
                "name": "prompt-v1.txt",
                "spec": "纯文本 · 粘贴进 ChatGPT 输入框",
                "brief_zh": "首轮提示词（故意写得比较松）。注意最后一句是 Make it sound exciting —— 这句话就是 AI 后面开始编造五星评价的根源，视频里要指出来。",
                "content": PROMPT_V1,
            },
            {
                "no": "3-2",
                "kind": "sheet",
                "name": "output-v1-marked.txt",
                "spec": "7 行 × 5 列表格 · 含 3 处已标红的编造内容",
                "brief_zh": "AI 首轮生成的表格。里面有 3 处编造（虚构五星评价 / 虚构奖项 / 健康功效宣称），视频里你要用红色高亮标出来并写 INVENTED。这份就是你要标红的那份，不用自己再编一遍。",
                "content": OUTPUT_V1,
            },
            {
                "no": "3-3",
                "kind": "doc",
                "name": "prompt-v2-revision.txt",
                "spec": "纯文本 · 第二轮修改指令",
                "brief_zh": "修改指令。两条关键约束：①只重新生成第 2/4/6 行，其余不动（这会演示「定向修改」而不是推倒重来）；②所有事实必须可核实，编不出来就写 VERIFY。",
                "content": PROMPT_V2,
            },
            {
                "no": "3-4",
                "kind": "doc",
                "name": "final-3-captions.txt",
                "spec": "纯文本 · 修改后的 3 条成品",
                "brief_zh": "最终 3 条文案，plainspoken 风格。视频里左右分栏对比时用这份做「右栏」。",
                "content": FINAL_CAPTIONS,
            },
        ],
    },
    {
        "id": 4,
        "title": "Canva：品牌规范 + 7 张图的制作素材",
        "note": "7 张 PNG 就是在这张卡里做出来的。品牌规范先定死，再一页页复制 —— 顺序反了就会 7 张图 7 个色。",
        "items": [
            {
                "no": "4-0",
                "kind": "doc",
                "name": "brand-kit.txt",
                "spec": "2 个品牌色 + 1 个字体 + Logo 规格 + 版式网格",
                "brief_zh": "品牌规范。必须在做第 1 页之前就设好，否则第 5 页的颜色一定会有轻微偏差。这套色板是虚构店的，你可以换成任何客户的。",
                "content": BRAND_KIT,
            },
        ] + _png_items("4") + [
            {
                "no": "4-8",
                "kind": "doc",
                "name": "naming-list.txt",
                "spec": "7 个文件名的完整清单",
                "brief_zh": "导出时的命名规则。两位数字前缀保证任何文件管理器里都按顺序排列。",
                "content": NAMING_LIST,
            },
        ],
    },
    {
        "id": 5,
        "title": "五项验收清单（画中画那张卡）",
        "note": "这张卡需要两样东西：清单本身的文字（贴在画面右下角），以及如果你不想实拍、想用 AI 生成这张清单卡，下面的图片提示词。",
        "items": [
            {
                "no": "5-1",
                "kind": "doc",
                "name": "qc-checklist.txt",
                "spec": "5 项 · 贴在画面右下角的清单",
                "brief_zh": "五项验收清单。念一条勾一条，节奏要和口播对齐。任一项没勾 = 这一页不算完成。",
                "content": QC_CHECKLIST,
            },
            {
                "no": "5-2",
                "kind": "image",
                "name": "qc-card-overlay.png",
                "spec": "可选 · 用 AI 生成清单卡，省去实拍",
                "brief_zh": "如果你不想实拍那张小卡，可以用这个提示词生成一张清单卡做画中画。生成的卡上文字可能是乱码，建议只用它做氛围 B-roll，真正的清单还是自己打一张。",
                "img_en": QC_CARD_IMG_EN,
                "img_zh": QC_CARD_IMG_ZH,
            },
        ],
    },
    {
        "id": 6,
        "title": "CapCut：3 段素材 + 屏幕文字 + 字幕校对",
        "note": "三段素材既可以自己拍，也可以用下面的视频提示词让 Runway / Kling / Veo 生成。屏幕文字和字幕校对文本也都在下面。",
        "items": [
            {
                "no": "6-1",
                "kind": "video",
                "name": "clip-01-pour.mp4",
                "spec": "约 10 秒 · 9:16 竖屏",
                "brief_zh": "第一段：倒咖啡。全片最有质感的一镜，慢一点，让液体透光的瞬间占满画面。",
                "vid_en": CLIP_POUR["en"],
                "vid_zh": CLIP_POUR["zh"],
            },
            {
                "no": "6-2",
                "kind": "video",
                "name": "clip-02-door.mp4",
                "spec": "约 10 秒 · 9:16 竖屏",
                "brief_zh": "第二段：推门。这是「进店」的动作暗示，也是唯一一段有环境光的素材。",
                "vid_en": CLIP_DOOR["en"],
                "vid_zh": CLIP_DOOR["zh"],
            },
            {
                "no": "6-3",
                "kind": "video",
                "name": "clip-03-finished-cup.mp4",
                "spec": "约 10 秒 · 9:16 竖屏",
                "brief_zh": "第三段：成品杯。收尾镜头，推近要慢，留 2 秒静止给屏幕文字。",
                "vid_en": CLIP_FINISHED["en"],
                "vid_zh": CLIP_FINISHED["zh"],
            },
            {
                "no": "6-4",
                "kind": "doc",
                "name": "onscreen-text.txt",
                "spec": "CapCut 文字层的两行内容",
                "brief_zh": "屏幕常驻文字。字号是唯一的硬指标：手臂长度距离下能看清就够，看不清就加大。",
                "content": ONSCREEN_TEXT,
            },
            {
                "no": "6-5",
                "kind": "doc",
                "name": "subtitle-proofread.txt",
                "spec": "自动字幕的校对对照表",
                "brief_zh": "自动字幕的原文 vs 校对后。cold blue → cold brew 这一处必须完整录进画面 —— 这是全片最有说服力的一秒。",
                "content": SUBTITLE_TEXT,
            },
            {
                "no": "6-6",
                "kind": "doc",
                "name": "export-checklist.txt",
                "spec": "导出的 3 个文件",
                "brief_zh": "导出清单。工程文件一定要留，客户要改的时候你会感谢自己。",
                "content": EXPORT_NAMES,
            },
        ],
    },
    {
        "id": 7,
        "title": "计时表与报价计算（$100 从哪来）",
        "note": "这张卡要把 $100 拆给观众看。表格内容和 Scope 卡全文都在下面，照着录入即可。",
        "items": [
            {
                "no": "7-1",
                "kind": "sheet",
                "name": "time-sheet.txt",
                "spec": "Google Sheets / Numbers / Excel",
                "brief_zh": "计时表。五行工时 + 合计 + 换算小时 + 毛时薪，最后加一轮修改看时薪掉多少。合计必须是 170 分钟，和口播里的数字一致。",
                "content": TIME_SHEET,
            },
            {
                "no": "7-2",
                "kind": "doc",
                "name": "scope-card.txt",
                "spec": "4 行 · 贴在屏幕上的范围卡",
                "brief_zh": "范围卡。第 4 行「不承诺结果」要慢慢念 —— 这是保护你自己的那一行。",
                "content": SCOPE_CARD,
            },
        ],
    },
    {
        "id": 8,
        "title": "4 个可复用模板 + 报价邮件全文",
        "note": "收尾卡。四个模板是给观众的「带走的东西」，邮件全文是可直接照抄的 CTA 落地文案。",
        "items": [
            {
                "no": "8-1",
                "kind": "doc",
                "name": "template-01-brief.md",
                "spec": "模板 · 可复用于任何本地小店",
                "brief_zh": "需求单模板（与实操卡 2 那份相同，这里作为「可带走文件」再次出现）。",
                "content": BRIEF_DOC,
            },
            {
                "no": "8-2",
                "kind": "doc",
                "name": "template-02-prompt-skeleton.txt",
                "spec": "模板 · 换 4 个括号就能给任何行业用",
                "brief_zh": "提示词骨架。把四个方括号换掉就能源源不断接单 —— 咖啡店、理发店、健身房通用。这是四个模板里最值钱的一个。",
                "content": TEMPLATE_PROMPT_SKELETON,
            },
            {
                "no": "8-3",
                "kind": "doc",
                "name": "template-03-naming-list.txt",
                "spec": "模板 · 文件命名规则",
                "brief_zh": "命名清单模板。",
                "content": NAMING_LIST,
            },
            {
                "no": "8-4",
                "kind": "sheet",
                "name": "template-04-time-sheet.txt",
                "spec": "模板 · 计时与报价表",
                "brief_zh": "计时表模板。每周接单前填一遍，你才知道自己到底在赚多少。",
                "content": TIME_SHEET,
            },
            {
                "no": "8-5",
                "kind": "doc",
                "name": "outreach-email.txt",
                "spec": "邮件全文 · 单收件人",
                "brief_zh": "开发信全文。四段结构：一句具体观察 → 交付物+价格+周期 → 边界 → 给对方一个轻松说不的出口。如果这封信能群发给五十家店，就删掉重写。",
                "content": QUOTE_EMAIL,
            },
        ],
    },
]
