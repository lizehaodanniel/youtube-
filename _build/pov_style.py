# -*- coding: utf-8 -*-
"""POV 无出镜频道的视觉风格圣经 + 长版提示词骨架。

为什么要写得这么长：
    用户原话：「对于内容要有细节描述，整个提示词可以很长，但是要丰富的详细的对内容进行描述，
    画面要求高清……文字生成出来的画面输入生图或者生视频工具，最后呈现的图片或者视频人物保持一致。」

    短提示词（≤30 词）出图随机的概率很大——风格、镜头、人物都不固定。
    长提示词（≥250 词）能锁定镜头、色温、渲染管线和「人物一致性」。

四条铁律（每个镜头都必须遵守）：

1. **不出脸**。所有画面只出现「手 / 背影 / 后脑勺 / 纯物件」。
   这是 POV 频道能做长片、跨镜头不串脸的唯一工程前提。
2. **不烧字**。图里不出现任何文字、数字、logo、界面。
   所有文字都在 Remotion 里用真字体叠加 —— 又快又准，还能随时改。
3. **同一个人看镜头**。CHARACTER_BLOCK 在每个有人的镜头里都嵌入——
   同一件衣服、同一种肤色、同一对没有装饰的手。
4. **一条光**。每场戏只有一个可见光源，色温固定。
   这是让一组 AI 图看起来像「同一部片」成本最低的方法。

prompt 组成：
    img_en = CHARACTER_BLOCK + IMG_HEAD + <镜头专属描述 img_core> + IMG_TAIL
    vid_en = CHARACTER_BLOCK + VID_HEAD + <镜头专属运动 vid_core> + VID_TAIL
每条图片提示词约 250–350 词，可直接整段复制喂给生图工具。
"""

# ============================================================ 通用尾巴
_COMMON_NEG = (
    "Do NOT include: any text, letters, numbers, words, signage with readable type, "
    "logos, brand names, watermarks, UI screenshots, charts, graphs, human faces, "
    "readable fine print, distorted hands, extra fingers, melted objects, "
    "warped perspective, oversaturated colors, lens flare abuse, plastic-looking skin, "
    "bad anatomy, low resolution, painterly stylization, anime stylization, "
    "cartoon outline edges, watercolor bleed, moiré patterns."
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
    "Character reference card (use this whenever a person appears in frame): "
    "an unspecified adult, late twenties to mid thirties, fair to medium skin with neutral warmth, "
    "seen only as hands from the wrist down, or as a figure from behind, or as a soft silhouette "
    "with the face in deep shadow and never visible; posture unhurried and slightly slumped, "
    "the body language of someone who has been awake too long thinking about money; "
    "clothing: a soft cotton crewneck sweater in warm heather grey with a visible fine weave, no logos, "
    "no prints, no graphics, the same sweater in every shot it appears; "
    "hands are unadorned except for a single thin brushed-steel band on the fourth finger of the left hand; "
    "fingernails short and unpolished; "
    "signature object appearing in roughly 40 percent of shots: a five-centimeter polished brass cow "
    "figurine with a soft amber sheen, placed unobtrusively on a shelf, a tabletop corner, "
    "or a windowsill, never the focal point, sometimes only an out-of-focus bokeh blob in the foreground. "
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
    "Horizontal 16:9 composition, native 1920x1080 (or up to 3840x2160 for 4K export), "
    "high dynamic range with detail preserved in both shadows and highlights. "
    + _COMMON_NEG
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
    + _COMMON_NEG
)

# ============================================================ AI 频道
AI_BIBLE = {
    "name": "暗调屏幕光 · Dark Screen Glow",
    "signature": "近黑背景 + 青紫双色屏幕反光；不出脸；所有界面元素由 Remotion 后叠，图里一律不画。",
    "palette": [
        ("底色 Base", "#0B0E14", "近黑，占画面 60% 以上"),
        ("主光 Key", "#22D3EE", "青色，屏幕边缘光"),
        ("副光 Rim", "#7C5CFF", "紫色，轮廓补光"),
        ("点缀 Accent", "#F5D67B", "暖黄，只用在「顿悟」镜头"),
    ],
    "lens": "虚拟 40mm，f/2.0，重暗角，屏幕反射作为唯一光源，轻微色散。",
    "motif": "桌面永远有一只黑色棒球帽和一副大耳罩耳机（不戴在人头上，只是摆在那），"
             "是频道的固定签名物。",
    "arc": "S1–S2 冷青（信息过载）→ S3–S5 青紫交替（拆解）→ S6 暖黄（跑通）→ S7 青（警示）→ S8 暖黄收尾。",
}

AI_CHARACTER = (
    "Character reference card (use this whenever a person appears in frame): "
    "an unspecified adult, late twenties to mid thirties, fair skin with neutral warmth, "
    "seen only as hands from the wrist down, or as a silhouette from behind, "
    "or as the back of a head; never the face, never a full figure face-on; "
    "posture focused and slightly hunched forward, the body language of someone building something "
    "late at night; clothing: a dark oversized hoodie in near-black cotton with a soft brushed "
    "interior, no logos, no prints, no graphics, the same hoodie in every shot it appears; "
    "hands unadorned except for a thin dark silicone ring on the fourth finger of the right hand; "
    "fingernails short and clean. "
    "Signature objects that appear in roughly half the shots, always placed in the frame but "
    "never on a person: a matte-black baseball cap with a subtle curved brim resting flat on the desk, "
    "and a pair of large matte-black over-ear headphones with a brushed-metal headband resting beside "
    "the cap. Both objects are static and consistent in every shot they appear in. "
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
    "the single light beam, the faintest reflection of the screen on the matte surface of the cap. "
    "Technical: ultra-sharp where the eye lands, no halation on the cyan, no bloom that washes out text edges, "
    "no vignette so heavy it crushes the subject. "
    "Horizontal 16:9 composition, native 1920x1080 (or up to 3840x2160 for 4K export), "
    "high dynamic range with detail preserved in both shadows and the cyan highlights. "
    + _COMMON_NEG
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
    "the cap and headphones remaining perfectly still. "
    + _COMMON_NEG
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

3. **人脸不是必须的，情绪是必须的。** 本频道不出脸，靠三件事替代人脸的吸引力：
   高对比色块、指向性构图（箭头 / 视线 / 手指方向）、以及一个「不该出现的东西」。
"""

THUMB_HEAD = (
    "YouTube thumbnail, 1280x720, 16:9, designed to stay legible at 210px wide on mobile. "
    "Cinematic photorealistic 3D render, physically based, dramatic single-source lighting. "
    "Extremely high contrast, bold simple shapes, subject fills at least 60 percent of the frame, "
    "maximum three visual elements, no clutter, no background detail. "
)

THUMB_TAIL = (
    "No human face. No brand logos. No watermarks. No photorealistic readable paragraphs. "
    "Leave the top-left corner and the bottom-right corner relatively clear, YouTube overlays sit there. "
    "Slightly oversaturated and punchier than the in-video frames — thumbnails must survive being shrunk."
)


def build_prompts(bible_head, bible_tail, vid_head, vid_tail, character, core, motion_core):
    """把「镜头专属描述」拼成完整提示词。"""
    return {
        "img_en": (character + " " + bible_head + core + " " + bible_tail).strip(),
        "vid_en": (character + " " + vid_head + motion_core + " " + vid_tail).strip(),
    }