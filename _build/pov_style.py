# -*- coding: utf-8 -*-
"""POV 无出镜频道的视觉风格圣经 + 长版提示词骨架。

为什么要写得这么长：
    用户原话：「对于内容要有细节描述，整个提示词可以很长，但是要丰富的详细的对内容进行描述，
    画面要求高清……文字生成出来的画面输入生图或者生视频工具，最后呈现的图片或者视频人物保持一致。」

    短提示词（≤30 词）出图随机的概率很大——风格、镜头、人物都不固定。
    长提示词（≥250 词）能锁定镜头、色温、渲染管线和「人物一致性」。

四条铁律（每个镜头都必须遵守）：

1. **人物必须在画面里**。
   注意：这条在 2026-08-30 被推翻重写过。原来的写法是「不出脸，只拍手 / 背影 / 纯物件」，
   结果 102 个镜头生出来全是静物，一个人物都没有 —— 因为角色卡只说「如果出现人就长这样」，
   而镜头主体写的是「一张黑桌子」，模型不会凭空加人进去。
   **角色卡 ≠ 让角色出现。每一个镜头都必须显式写出「她在哪里、在做什么、脸朝哪边」。**
   两个频道的差别只在「露不露脸」，不在「有没有人」：
   - AI 频道：约四成镜头是能看清脸的肖像（脸占画面上三分之一），其余是过肩 / 侧脸 / 低头 / 手部特写
   - 金融频道：继续保持 POV 惯例不露脸，但**手必须是她的手**，镜头里必须有她的身体姿态
2. **不烧字**。图里不出现任何文字、数字、logo、界面。
   所有文字都在 Remotion 里用真字体叠加 —— 又快又准，还能随时改。
3. **同一个人看镜头**。SHARED_FACE 在**每一条**提示词里都嵌入——
   同一张脸、同一种发色、同一种肤色、同一双手。
4. **一条光**。每场戏只有一个可见光源，色温固定。
   这是让一组 AI 图看起来像「同一部片」成本最低的方法。

prompt 组成：
    img_en = SHARED_FACE + CHARACTER + ON_CAMERA + <镜头专属: 她在哪 she> + <镜头专属: 场景 core> + IMG_TAIL
    vid_en = SHARED_FACE + CHARACTER + ON_CAMERA + <镜头专属: 她在哪 she> + <镜头专属: 运镜 motion> + VID_TAIL
每条图片提示词约 850–1000 词，可直接整段复制喂给生图工具。
"""

# ============================================================ 通用尾巴
# ---------------------------------------------------------------------------
# 单帧铁律：Midjourney 等工具默认一次吐 2x2 四宫格，必须在正负两侧同时压掉。
# 正面说「只出一张」，负面把各种网格/分镜说法全列一遍，双保险。
# ---------------------------------------------------------------------------
_SINGLE_FRAME_POS = (
    "IMPORTANT FRAMING RULE: this is ONE single frame — a single still from a film, "
    "photographed from ONE camera angle at ONE moment in time. "
    "Output exactly one image. "
)
_SINGLE_FRAME_NEG = (
    "split screen, split-screen panels, panel grid, storyboard layout, contact sheet, "
    "film strip, multiple panels, four-image grid, 2x2 grid, quad grid, diptych, triptych, "
    "collage, image borders, panel dividers, thumbnails, duplicate variations of the same scene, "
    "before-and-after comparison layout, multiple views of the same subject."
)

_NEG_BASE = (
    "Do NOT include: any text, letters, numbers, words, signage with readable type, "
    "logos, brand names, watermarks, UI screenshots, charts, graphs, "
    "readable fine print, distorted hands, extra fingers, melted objects, "
    "warped perspective, oversaturated colors, lens flare abuse, plastic-looking skin, "
    "bad anatomy, low resolution, painterly stylization, anime stylization, "
    "cartoon outline edges, watercolor bleed, moiré patterns."
)

# 金融频道：继续「不出脸」，负面词里保留禁人脸。
FIN_NEG = _NEG_BASE[:-1] + ", " + (
    "human faces, visible faces, recognizable facial features, "
    "a clearly identifiable person, frontal portraits."
) + " " + _SINGLE_FRAME_NEG + "."

# AI 频道：允许女主角本人出脸，但除了她之外不能出现任何第二个人。
AI_NEG = _NEG_BASE[:-1] + ", " + (
    "any face other than the character's, a second person, another woman, another man, "
    "a crowd, bystanders, extra people in the background, "
    "a changed or inconsistent face, a different woman than the character reference card."
) + " " + _SINGLE_FRAME_NEG + "."

# ---------------------------------------------------------------------------
# 共用面孔：两个频道是同一个人。脸 / 发色 / 肤色 / 五官写死，
# 只有「服装」和「出镜方式」按频道分开，这样跨频道也是同一张脸。
# ---------------------------------------------------------------------------
SHARED_FACE = (
    "Character reference card — this woman is the subject of this shot, she is in the frame. "
    "The SAME woman appears in every shot of both channels — identical face, identical hair, "
    "identical skin tone, never a different person, never a man. "
    "Photorealistic East-Asian woman, age 24 to 28, the quiet-muse / clean-girl look. "
    "Face: oval with a softly rounded jaw, fair warm-toned skin with a natural dewy finish, "
    "no heavy makeup, no contour, no dramatic highlights — just healthy skin with one soft highlight "
    "on the cheekbone. "
    "Eyes: almond-shaped, double-lid, dark brown iris, calmly half-lidded, looking just past the camera, "
    "no mascara, no eyeliner, no eyeshadow. "
    "Eyebrows: naturally thick but groomed straight, soft dark brown, no arch, no filler. "
    "Nose: small with a straight bridge and a softly rounded tip, never sharp or sculptural. "
    "Lips: full and softly defined with a clear cupid's bow, natural pink-nude, one layer of clear gloss, "
    "no overline, no lipstick color. "
    "Hair: platinum ash-blonde with slightly darker natural roots for depth, no bangs, smooth and silky "
    "with a single soft highlight where the key light hits, never oily, never frizzy. "
    "Two interchangeable lengths — pick one per shot and do not mix within the same shot: "
    "(A) chin-length soft blunt bob with a gentle outward flick at the ends, or "
    "(B) long straight hair falling to mid-chest. "
    "Hands: slim fingers, short unpolished nails, a thin matte-silver band on the right fourth finger. "
    "Body language: unhurried, grounded, the posture of someone who has spent the afternoon reading; "
    "shoulders relaxed, slight inward curl, never posed, never smiling broadly, "
    "expression neutral or one faint closed-mouth smile. "
    "Camera relationship: a soft 45-degree key light from camera-left, gentle window fill from above, "
    "never from below, never a hard shadow under the chin, never a beauty-ring reflection in the iris. "
    "Cohesion rule: even if every other detail changes, her face, hair color, skin tone and hands "
    "must read as the same woman across all shots and both channels. "
)

# ============================================================ 金融频道
FIN_BIBLE = {
    "name": "安静的现实主义 · Quiet Realism",
    "signature": "青蓝阴影 + 琥珀高光；每场只有一个可见光源；不出脸；画面下三分之一留白给字幕。",
    "palette": [
        ("阴影 Shadow", "#16232B", "冷青蓝，压住画面四角"),
        ("中间调 Midtone", "#4A5C63", "灰蓝墙面 / 木质家具"),
        ("高光 Highlight", "#E8A54B", "琥珀色，只出现在光源附近"),
        ("点缀 Accent", "#7FD1C1", "极少量，只用在「希望感」镜头"),
    ],
    "lens": "虚拟 35mm 变形镜头，f/1.8 浅景深，轻微胶片颗粒，体积雾。",
    "motif": "一只巴掌大的黄铜奶牛小摆件，随意出现在约 40% 的镜头里（书架、窗台、桌面角落）。"
             "这是频道的品牌签名，不占主体、不抢戏。",
    "arc": "全片色温跟随情绪：S1–S2 冷灰蓝 → S3–S4 冷到发青 → S5 回暖 → S6–S8 琥珀主导。",
}

# 跨镜头人物一致性卡——每个有人的镜头里都嵌入这段
# 这是「最后呈现的图片或者视频人物保持一致」的核心
FIN_CHARACTER = (
    SHARED_FACE
    + "Finance-channel framing: she is seen only as hands from the wrist down, or as a figure from behind, "
    "or as a soft silhouette with the face in deep shadow and never readable — this channel keeps the "
    "POV convention, so show her body language and her hands, not a clean portrait. "
    "Finance-channel wardrobe, the only outfit she wears in this channel: a soft cotton crewneck sweater "
    "in warm heather grey with a visible fine weave, no logos, no prints, no graphics. "
    "Minimal jewelry only: one thin matte-silver chain with a tiny round pendant at the collarbone, "
    "small thin silver hoops in both ears, plus the thin matte-silver band on her right fourth finger. "
    "Signature object appearing in roughly 40 percent of shots: a five-centimeter polished brass cow "
    "figurine with a soft amber sheen, placed unobtrusively on a shelf, a tabletop corner, "
    "or a windowsill, never the focal point, sometimes only an out-of-focus bokeh blob in the foreground. "
)

# 金融频道同样需要「人在场」的保险，但不出脸。
# 没有这一段，模型会把镜头画成纯静物（2026-08-30 实测 60/60 全静物）。
# 同样只保留一句话，不喧宾夺主。
FIN_PRESENCE = (
    "The same woman described above is present in every shot of this film, "
    "though her face is never shown — only her body, her hands, and her shadow."
)

FIN_IMG_HEAD = (
    "Cinematic photorealistic 3D render, virtual 35mm anamorphic lens, f/1.8 shallow depth of field, "
    "subtle 35mm film grain, gentle volumetric haze, physically based rendering with ray-traced "
    "global illumination, soft contact shadows, accurate subsurface scattering on skin, "
    "true 8K material micro-detail on wood grain, fabric weave, condensation droplets, "
    "fingerprint smudges on glass, dust on surfaces. "
    "Exactly one visible practical light source inside the frame; mood comes from that one source alone. "
    "Color grade: desaturated teal-blue shadows, warm amber highlights, muted midtones, "
    "slightly crushed blacks, clean highlight roll-off, a faint Kodak Vision3 5219  film stock feel. "
    "Composition rule: the lower third of the frame is kept visually quiet and uncluttered for caption overlay. "
    "Visual reference: the still life cinematography of Roger Deakins meets the color restraint of "
    "Autumn Durald Arkapaw. "
)

FIN_IMG_TAIL = (
    "Mood: quiet, unhurried, observational, faintly melancholic but never grim, never poverty porn. "
    "Atmosphere: a barely-there breath of dust drifting in the light, the faintest possible haze, "
    "the suggestion of time passing but no visible clocks or calendars. "
    "Technical: ultra-sharp where the eye lands, soft and creamy where it does not, "
    "no halation, no bloom abuse, no vignette so heavy it crushes the corners. "
    "Horizontal 16:9 composition, native 1920x1080, "
    "high dynamic range with detail preserved in both shadows and highlights. "
    + _SINGLE_FRAME_POS
    + FIN_NEG
)

FIN_VID_HEAD = (
    "Live-action cinematic camera move on the still scene above, single unbroken take, "
    "5 seconds at 24 fps, motion blur enabled, no cuts, no camera shake, no handheld wobble. "
    "Camera motion is locked to exactly one axis and one direction for the entire clip. "
)

FIN_VID_TAIL = (
    "Everything in the frame stays perfectly stable and consistent across all five seconds: "
    "no morphing, no flicker, no object appearing or disappearing, no change in lighting or "
    "color temperature, no new elements entering frame, no subject deformation. "
    "Ambient life only: dust motes drifting, a curtain breathing, steam rising from a mug, "
    "a shadow slowly lengthening, the brass cow figurine catching a single glint as the light moves. "
    + _SINGLE_FRAME_POS
    + FIN_NEG
)

# ============================================================ AI 频道
AI_BIBLE = {
    "name": "暗调屏幕光 · Dark Screen Glow",
    "signature": "近黑背景 + 青紫双色屏幕反光；她本人出现在每一个镜头里（约四成露脸）；"
                 "所有界面元素由 Remotion 后叠，图里一律不画。",
    "palette": [
        ("底色 Base", "#0B0E14", "近黑，占画面 60% 以上"),
        ("主光 Key", "#22D3EE", "青色，屏幕边缘光"),
        ("副光 Rim", "#7C5CFF", "紫色，轮廓补光"),
        ("点缀 Accent", "#F5D67B", "暖黄，只用在「顿悟」镜头"),
    ],
    "lens": "虚拟 40mm，f/2.0，重暗角，屏幕反射作为唯一光源，轻微色散。",
    "motif": "她本人的三件套固定摆在桌面上，是频道的签名物：一只白色陶瓷马克杯（杯壁常留一圈干掉的咖啡渍）、"
             "一叠空白的厚索引卡、一支细哑光银戒（不戴时搁在杯托旁）。"
             "注意：旧的「黑色棒球帽 + 大耳罩耳机」签名物已随旧 host 一起废弃，任何地方都不要再说。",
    "arc": "S1–S2 冷青（信息过载）→ S3–S5 青紫交替（拆解）→ S6 暖黄（跑通）→ S7 青（警示）→ S8 暖黄收尾。",
}

AI_CHARACTER = (
    SHARED_FACE
    + "AI-channel framing: unlike the finance channel, her face IS shown here — a clean portrait is allowed "
    "and encouraged, occupying at most the upper third of the frame; when only body language is needed, "
    "show her from the neck down or from behind. "
    "AI-channel screen-light rule specific to her face: when a screen is the light source, it must light "
    "HER face from the front — cyan climbing one cheek, violet tracing the opposite jawline and the edge "
    "of her hair. Her face is never in silhouette and never turned fully away from camera for more than "
    "one shot in a row. "
    "AI-channel wardrobe — the only outfits she wears in this channel, rotate between them, "
    "never invent new ones: "
    "a matte-white wide-strap cotton camisole with thin spaghetti straps and a softly scooped neckline; "
    "a loose white linen button-up shirt half-tucked into high-waisted cream trousers; "
    "or an oversized oatmeal-cream knit cardigan over the camisole. No logos, no prints, no graphics. "
    "Minimal jewelry only: one thin matte-silver chain with a tiny round pendant at the collarbone, "
    "small thin silver hoops in both ears, plus the thin matte-silver band on her right fourth finger. "
    "Reference vibe: the still photography of Petra Collins meets the muted color palette of Sofia Coppola. "
)

# ---------------------------------------------------------------------------
# 「她在画面里」—— 一句话的 framing 上下文，2026-08-30 补，2026-08-31 改写法。
#
# 背景：角色卡（SHARED_FACE + CHARACTER）只说「如果出现人，就长这样」；
# 镜头主体写的是「一张黑桌子」「一只手」——模型不会凭空加人，会全部画成静物。
#
# 修法是给每条提示词补一段人物描述（写在 pov_ai.py / pov_fin.py 的 SHE 列表里），
# 直接拼到场景描述前面，作为整段故事的第一句。**不再单独成段、不再用
# 「ON CAMERA:」这种工程化标识**——用户要的是「根据口播讲故事的图片提示词」，
# 那些大写英文标签读起来像施工告示，不像剧本。
#
# 这一句 PRESENCE 只剩一句：作为保险提醒模型「她在场」，不喧宾夺主。
# ---------------------------------------------------------------------------
AI_PRESENCE = (
    "The same woman described above is on camera in every shot of this film."
)

AI_IMG_HEAD = (
    "Cinematic photorealistic 3D render, virtual 40mm lens, f/2.0 with shallow focus, "
    "heavy vignette, slight chromatic aberration on bright edges, "
    "physically based rendering with ray-traced global illumination, "
    "screen-glow as the only light source in every shot, soft bloom on emissive surfaces, "
    "subtle film grain, true 8K material micro-detail on keycap texture, cable braiding, "
    "fingerprint smudges on glass, dust in the light beam. "
    "The environment is dark and controlled; all brightness comes from screens, indicator LEDs, "
    "and one dim practical lamp. "
    "Color grade: near-black background occupying most of the frame, cool cyan as the key light from a screen, "
    "violet rim light separating the subject from the background, no other hue allowed. "
    "Composition: keep the lower third visually quiet for caption overlay, "
    "keep the center-left area clear so a floating UI panel can be composited later. "
    "Visual reference: the product cinematography of Apple keynote mixed with the dark-room "
    "working aesthetic of Wong Kar-wai. "
)

AI_IMG_TAIL = (
    "Mood: focused, late-night, precise, the feeling of building something at one in the morning, "
    "premium tech-product aesthetic, clean and uncluttered, no cyberpunk cliches, "
    "no neon signs, no rain, no graffiti, no skyline in the background. "
    "Atmosphere: a fan spinning almost imperceptibly, a cursor blinking, dust drifting through "
    "the single light beam, the faintest reflection of the screen on the matte desk surface. "
    "Technical: ultra-sharp where the eye lands, no halation on the cyan, no bloom that washes out text edges, "
    "no vignette so heavy it crushes the subject. "
    "Horizontal 16:9 composition, native 1920x1080, "
    "high dynamic range with detail preserved in both shadows and the cyan highlights. "
    + _SINGLE_FRAME_POS
    + AI_NEG
)

AI_VID_HEAD = (
    "Live-action cinematic camera move on the still scene above, single unbroken take, "
    "5 seconds at 24 fps, motion blur enabled, no cuts, no camera shake, no glitch effects, "
    "no shutter stutter. Camera motion is locked to exactly one axis and one direction for the entire clip. "
)

AI_VID_TAIL = (
    "Everything in the frame stays perfectly stable and consistent across all five seconds: "
    "no morphing, no flicker, no object appearing or disappearing, no change in lighting or "
    "color temperature, no new elements entering frame, no subject deformation. "
    "Ambient life only: a cursor blinking, a fan spinning, a progress bar filling, "
    "the cyan glow pulsing almost imperceptibly, dust drifting through the light, "
    "the silver pendant at her collarbone catching a single glint as she breathes. "
    + _SINGLE_FRAME_POS
    + AI_NEG
)

# ============================================================ Remotion 动效预设
MOTION_PRESETS = {
    "push-in": {"scale": [1.00, 1.12], "anchor": "center", "easing": "easeOutSine",
                "note": "缓慢推近 · 用于「揭示 / 强调 / 段落开场」"},
    "pull-out": {"scale": [1.12, 1.00], "anchor": "center", "easing": "easeInOutSine",
                 "note": "缓慢拉远 · 用于「收束 / 结尾 / 转场前」"},
    "drift-right": {"x": [0, -60], "scale": [1.06, 1.06], "easing": "linear",
                    "note": "横向平移 · 用于「列举 / 时间推进」"},
    "hold": {"scale": [1.02, 1.05], "anchor": "center", "easing": "linear",
             "note": "几乎静止 · 用于「重句 / 停顿 / 需要看清数字」"},
}

TRANSITIONS = {
    "xfade": "交叉溶解 0.6s（默认，90% 的镜头用它）",
    "hard": "硬切（只在「反转 / 惊醒」处用，全片不超过 3 次）",
    "whip": "快速推到位 0.25s（只在段落第一镜用）",
}

# ============================================================ 缩略图通用规则
THUMB_RULES = """缩略图的三条硬规则（这是点击率的主要变量，不是美术问题）：

1. **手机上要先看清，再好看。** YouTube 首页缩略图实际显示宽度约 210px。
   测试方法：把图缩小到 210px 宽，眯眼看 2 秒 —— 如果读不出主信息，就废了。
   所以：主体必须占画面 60% 以上，元素不超过 3 个，文字不超过 4 个单词。

2. **文字是给眼睛的钩子，不是给内容的摘要。** 缩略图文字只负责制造「问题感」，
   答案在视频里。禁止把标题原文搬上去（标题栏就在旁边，重复 = 浪费）。

3. **AI 频道缩略图必须有人脸，而且要有情绪。**
   这一条在 2026-08-30 改过：原来写的是「本频道不出脸」，那是从「跨镜头串脸」这个顾虑推导出来的，
   但它牺牲的是点击率——人脸是 YouTube 缩略图最强的点击变量，没有之一。
   现在频道有人物形象了，缩略图就让她的脸占画面 40%–60%，配一个大表情
   （皱眉 / 愣住 / 无奈地笑），再用高对比色块和指向性构图兜底。
   串脸的顾虑用「参考图垫图 + 后期统一」解决，不用「不出脸」这个自断一臂的办法。
"""

THUMB_HEAD = (
    "YouTube thumbnail, 1280x720, 16:9, designed to stay legible at 210px wide on mobile. "
    "Cinematic photorealistic 3D render, physically based, dramatic single-source lighting. "
    "Extremely high contrast, bold simple shapes, subject fills at least 60 percent of the frame, "
    "maximum three visual elements, no clutter, no background detail. "
)

THUMB_TAIL = (
    "No brand logos. No watermarks. No photorealistic readable paragraphs. "
    "Leave the top-left corner and the bottom-right corner relatively clear, YouTube overlays sit there. "
    "Slightly oversaturated and punchier than the in-video frames — thumbnails must survive being shrunk."
)

# AI 频道缩略图：她要出脸，占画面 40%–60%，配一个大表情。
# （金融频道继续不出脸，用 THUMB_TAIL 的默认版本即可。）
THUMB_TAIL_FACE = (
    "Her face is in frame and clearly readable, filling 40 to 60 percent of the composition, "
    "with one legible emotion on it — frowning, caught off guard, or a resigned half-smile. "
    "Front-lit so both eyes are visible, eyes looking at the camera, no hair across the face. "
    "No brand logos. No watermarks. No photorealistic readable paragraphs. "
    "Leave the top-left corner and the bottom-right corner relatively clear, YouTube overlays sit there. "
    "Slightly oversaturated and punchier than the in-video frames — thumbnails must survive being shrunk."
)


def build_prompts(bible_head, bible_tail, vid_head, vid_tail,
                  character, presence, she, core, motion_core):
    """把「镜头专属描述」拼成完整提示词。

    she 是「她在这个镜头里的位置 / 姿态 / 脸朝哪边」——这一项不能为空。
    没有它，角色卡只是一句「如果出现人就长这样」，模型会把镜头画成纯静物。
    拼装方式：character + presence(一句话) + she(场景第一句) + 风格 + core + tail。
    she 直接融入正文，不再单独成段、不再用 ON CAMERA 标签——读起来像剧本，不像施工告示。
    """
    head = character
    if presence:
        head = head + " " + presence
    if she:
        head = head + " " + she.strip() + " "
    return {
        "img_en": (head + bible_head + core + " " + bible_tail).strip(),
        "vid_en": (head + vid_head + motion_core + " " + vid_tail).strip(),
    }