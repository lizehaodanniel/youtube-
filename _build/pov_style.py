# -*- coding: utf-8 -*-
"""POV 无出镜频道的视觉风格圣经 + 长版提示词骨架。

为什么要写得这么长：
    用户原话：「对于内容要有细节描述，整个提示词可以很长，但是要丰富的详细的对内容进行描述，
    画面要求高清……文字生成出来的画面输入生图或者生视频工具，最后呈现的图片或者视频人物保持一致。」

    短提示词（≤30 词）出图随机的概率很大——风格、镜头、人物都不固定。
    长提示词（≥250 词）能锁定镜头、色温、渲染管线和「人物一致性」。

四条铁律（每个镜头都必须遵守）：

1. **她必须在画面里，而且脸要能拍**。
   注意这条被推翻过两次，别再走回头路：
   - 第一次（2026-08-30 早）：写「不出脸，只拍手 / 背影 / 纯物件」→ 102 镜全静物。
     因为角色卡只是条件句「如果出现人就长这样」，镜头主体写「一张黑桌子」模型不会凭空加人。
   - 第二次（2026-08-30 晚）：改成「人在场，但金融频道脸永不露出」→ 人物被写死成
     「只有手腕以下的手 / 裁掉脸的后脑勺 / 深阴影剪影」，姿态压抑、画面阴郁，
     用户直接反馈「不仅把人脸写没了，还把人物写得极其压抑」「观众看了不舒服」。
   - 现在（2026-08-31）：**用户有参考图，跨镜头人脸一致性由「垫图 + 后期统一」保证，
     不需要靠「不露脸」来规避串脸风险。** 两个频道都正常拍她，脸可以正对镜头，
     表情跟着剧情走。唯一禁止的是「把她拍成无脸的躯干」。
   **角色卡 ≠ 让角色出现。每一个镜头都必须显式写出「她在哪里、在做什么、什么表情」。**
2. **不烧字**。图里不出现任何文字、数字、logo、界面。
   所有文字都在 Remotion 里用真字体叠加 —— 又快又准，还能随时改。
3. **同一个人看镜头**。SHARED_FACE 在**每一条**提示词里都嵌入——
   同一张脸、同一种发色、同一种肤色、同一双手。
4. **一条光，但别把画面压死**。
   每场戏只有一个**可见**光源，色温固定，这是让一组 AI 图看起来像「同一部片」成本最低的方法。
   但「暗调」不等于「压黑」：阴影必须有细节、皮肤必须是暖的、背景必须有质感。
   曾经的调色（青蓝阴影 + 压黑 + 琥珀高光）被用户判为「观众看了不舒服」，已全换。

prompt 组成：
    img_en = SHARED_FACE + CHARACTER + PRESENCE + <镜头专属: 她在哪 she> + <风格段> + <场景 core> + IMG_TAIL
    vid_en = SHARED_FACE + CHARACTER + PRESENCE + <镜头专属: 她在哪 she> + <运镜> + <场景 motion> + VID_TAIL
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
    "cartoon outline edges, watercolor bleed, moiré patterns, "
    "crushed blacks, pure-void black backgrounds, cold-only teal lighting."
)

# 两个频道都是同一位女主，跨镜头人脸一致性由参考图垫图 + 后期统一保证，
# 不靠「不露脸」来规避。两个频道的负面词统一为「禁第二个人，禁换脸」。
FIN_NEG = _NEG_BASE[:-1] + ", " + (
    "any face other than the character's, a second person, another woman, another man, "
    "a crowd, bystanders, extra people in the background, "
    "a changed or inconsistent face, a different woman than the character reference card."
) + " " + _SINGLE_FRAME_NEG + "."

AI_NEG = FIN_NEG

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
    "healthy skin with one soft highlight on the cheekbone — no heavy makeup, no contour, no "
    "dramatic highlights. "
    "Eyes: almond-shaped, double-lid, warm dark brown iris, naturally expressive — her gaze "
    "follows the scene (sometimes to camera, sometimes down at her hands, sometimes off-frame), "
    "no mascara, no eyeliner, no eyeshadow. "
    "Eyebrows: naturally thick but groomed straight, soft dark brown, no arch, no filler. "
    "Nose: small with a straight bridge and a softly rounded tip, never sharp or sculptural. "
    "Lips: full and softly defined with a clear cupid's bow, natural pink-nude, one layer of "
    "clear gloss, no overline, no lipstick color — a small genuine smile, a soft exhale, "
    "or a quietly thoughtful look are all welcome; never a frozen model blank. "
    "Hair: platinum ash-blonde with slightly darker natural roots for depth, no bangs, smooth "
    "and silky with a single soft highlight where the key light hits, never oily, never frizzy. "
    "Two interchangeable lengths — pick one per shot and do not mix within the same shot: "
    "(A) chin-length soft blunt bob with a gentle outward flick at the ends, or "
    "(B) long straight hair falling to mid-chest, as in the reference photos. "
    "Hands: slim fingers, short unpolished nails, a thin matte-silver band on the right fourth finger. "

    "Body language: natural and grounded, but not frozen — she can be curious, tired, amused, "
    "relieved, focused, gently skeptical. A real expression that matches the scene is always "
    "better than a posed model blank stare. Shoulders relaxed, never rigid, never posing for "
    "the camera. "

    "Wardrobe — her personal style is minimalist, soft, and naturally feminine; no logos, "
    "no prints, no graphics, no loud colors. Pick from this drawer, do not invent anything else, "
    "do not lock her into one outfit per channel: "
    "1. a soft cotton or cashmere crewneck sweater in warm heather grey, oatmeal, or cream; "
    "2. a loose white or oatmeal linen button-up shirt, sometimes half-tucked; "
    "3. a matte-white wide-strap cotton camisole with thin spaghetti straps; "
    "4. an oversized oatmeal-cream knit cardigan, usually worn open over the camisole; "
    "5. high-waisted cream, beige, or oat trousers — soft wool or cotton, slightly tapered; "
    "6. a simple slip dress in white or oat silk-satin with thin spaghetti straps (her "
    "\"dressed up\" option for evening or formal scenes). "
    "Minimal jewelry only: a thin matte-silver chain with a tiny round pendant at the collarbone, "
    "small thin silver hoops in both ears, plus the thin matte-silver band on her right fourth finger. "
    "Pick the outfit to match the scene's mood — kitchen and cafe scenes lean warm and soft; "
    "desk scenes can use the camisole with sleeves pushed up; evening scenes get the slip dress. "
    "Never put her in black, neon, athletic wear, prints, branded items, or anything graphic. "

    "Camera relationship: a soft 45-degree key light from camera-left, gentle window fill from above, "
    "never from below, never a hard shadow under the chin, never a beauty-ring reflection in the iris. "
    "Cohesion rule: even if every other detail changes, her face, hair color, skin tone and hands "
    "must read as the same woman across all shots and both channels. "
)

# ============================================================ 金融频道
FIN_BIBLE = {
    "name": "暖日常现实主义 · Warm Everyday Realism",
    "signature": "暖燕麦 / 米色中间调 + 蜜光高光；阴影保留细节不压黑；"
                 "她就是这部片的主角，脸该看就看（手部和物件特写时镜头可以自然地不拍脸，"
                 "但不是规则、不是 POV 铁律）。所有界面元素由 Remotion 后叠，图里一律不画。",
    "palette": [
        ("阴影 Shadow", "#2E3A42", "柔和深灰蓝，保留细节，不压黑"),
        ("中间调 Midtone", "#C9BCA8", "温暖燕麦/米色，画面主体色"),
        ("高光 Highlight", "#F2D9A8", "柔和蜜光，光源附近、皮肤上"),
        ("点缀 Accent", "#8FC7B5", "极少量，只用在「希望感」镜头"),
    ],
    "lens": "虚拟 35mm 变形镜头，f/1.8 浅景深，轻微胶片颗粒，少量体积雾。",
    "motif": "一只巴掌大的黄铜奶牛小摆件，随意出现在约 30% 的镜头里（书架、窗台、桌面角落）。"
             "这是频道的品牌签名，不占主体、不抢戏。",
    "arc": "全片色温跟随情绪：S1–S2 暖燕麦 → S3–S4 略加深但仍暖 → S5–S8 蜜光主导（'家里亮起来了'）。",
}

# 跨镜头人物一致性卡——不再锁死「不露脸 / 只拍手」。
# 用户有参考图（jimeng-2026-08-30-2282.png / 4463.png），跨镜头人脸一致性由垫图 + 后期统一保证。
# 服装也从 SHARED_FACE 的共用衣柜里挑，不再写死一件暖灰毛衣。
FIN_CHARACTER = (
    SHARED_FACE
    + "Finance-channel framing: she is filmed naturally — a clean portrait is welcome when "
    "the shot calls for it, her face can meet the camera or look off-frame as the scene demands. "
    "When the moment is about her hands, the camera may close on her hands from the wrist down "
    "with the rest of her body in soft focus; when the moment is about her back, the camera may "
    "frame her from behind. There is NO rule against showing her face — the only rule is that "
    "the framing must serve the scene. "
    "Signature object appearing in roughly 30 percent of shots: a five-centimeter polished brass "
    "cow figurine with a soft amber sheen, placed unobtrusively on a shelf, a tabletop corner, "
    "or a windowsill, never the focal point, sometimes only an out-of-focus bokeh blob in the foreground. "
    "Reference vibe: the warm domestic cinematography of Wong Kar-wai's \"In the Mood for Love\" "
    "meets the quiet restraint of Autumn Durald Arkapaw. "
)

# 金融频道的 PRESENCE：她就是这部片的主角。不再写「脸永不展示」。
FIN_PRESENCE = (
    "The same woman described above is the subject of every shot in this film."
)

FIN_IMG_HEAD = (
    "Cinematic photorealistic 3D render, virtual 35mm anamorphic lens, f/1.8 shallow depth of field, "
    "subtle 35mm film grain, gentle volumetric haze, physically based rendering with ray-traced "
    "global illumination, soft contact shadows, accurate subsurface scattering on skin, "
    "true 8K material micro-detail on wood grain, fabric weave, condensation droplets, "
    "fingerprint smudges on glass, dust on surfaces. "
    "Exactly one visible practical light source inside the frame; mood comes from that one source alone. "
    "Color grade: warm, breathable, easy on the eyes — soft window daylight or warm practical lamp "
    "as the key, creamy oatmeal and honey midtones, gentle amber highlights, shadows lifted and open "
    "with visible detail rather than crushed, low-to-medium contrast, skin rendered warm and healthy, "
    "a whisper of Kodak Portra 400 grain. "
    "Explicitly avoid: teal-and-orange grading, crushed blacks, cold blue casts, heavy desaturation, "
    "muddy grey skin. "
    "Composition rule: the lower third of the frame is kept visually quiet and uncluttered for caption overlay. "
    "Visual reference: the warm domestic cinematography of Wong Kar-wai's \"In the Mood for Love\" "
    "meets the quiet restraint of Autumn Durald Arkapaw. "
)

FIN_IMG_TAIL = (
    "Mood: warm, observational, quietly hopeful — the feeling of a Sunday morning kitchen, "
    "or a late afternoon when the light comes in golden. Never grim, never poverty porn, never bleak. "
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
    "Ambient life only: a curl of steam rising from a mug, dust motes drifting, a curtain "
    "breathing in a draft, the brass cow figurine catching a single glint as the light moves. "
    + _SINGLE_FRAME_POS
    + FIN_NEG
)

# ============================================================ AI 频道
AI_BIBLE = {
    "name": "深夜屏幕光 · Late-Night Screen Glow",
    "signature": "深炭蓝背景（不是纯黑）+ 青/暖双色光；她就是这部片的主角，"
                 "脸该看就看，特写手部时可以自然不拍脸（不是规则，是叙事需要）；"
                 "所有界面元素由 Remotion 后叠，图里一律不画。",
    "palette": [
        ("底色 Base", "#141A24", "深炭蓝，占画面 50–60%，保留纹理"),
        ("主光 Key", "#38D9F0", "青色，屏幕边缘光"),
        ("暖光 Warm", "#FFB86B", "暖橙，台灯补光，救阴影、暖皮肤"),
        ("点缀 Accent", "#A78BFA", "紫色，轮廓补光"),
    ],
    "lens": "虚拟 40mm，f/2.0，中等暗角（不重压），屏幕 + 台灯组合光源，浅胶片颗粒。",
    "motif": "她本人的三件套固定摆在桌面上，是频道的签名物：一只白色陶瓷马克杯（杯壁常留一圈干掉的咖啡渍）、"
             "一叠空白的厚索引卡、一支细哑光银戒（不戴时搁在杯托旁）。"
             "注意：旧的「黑色棒球帽 + 大耳罩耳机」签名物已随旧 host 一起废弃，任何地方都不要再说。",
    "arc": "S1–S2 冷青（信息过载）→ S3–S5 青暖交替（拆解中渐渐回暖）→ S6 暖橙（跑通）→ S7 冷青（警示）→ S8 暖橙收尾。",
}

AI_CHARACTER = (
    SHARED_FACE
    + "AI-channel framing: she is filmed naturally — a clean portrait is welcome when the shot calls "
    "for it, her face may meet the camera, look down at the screen, or look off-frame as the scene "
    "demands. Her face may turn, look down, look away — but she is the subject, not a prop; when "
    "the framing cuts the face out, the rest of her body still carries the scene. There is no rule "
    "forcing her face into every shot — only that the framing serves the story. "
    "AI-channel screen-light rule: when a screen is the dominant light source, it lights her face "
    "from the front — cool cyan climbing one cheek, a warm practical lamp or amber rim tracing the "
    "opposite jawline. The face is never lost in total darkness. "
    "AI-channel wardrobe — picked from the shared wardrobe drawer (linen shirt / oatmeal cardigan / "
    "matte-white camisole / slip dress), rotate naturally, never invent new silhouettes, never put "
    "her in black, neon, athletic wear, prints, or branded items. "
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
    "moderate vignette (not crushing, just framing), subtle chromatic aberration on bright edges, "
    "physically based rendering with ray-traced global illumination, "
    "screen-glow as the key light plus a warm practical lamp filling the shadows, "
    "soft bloom on emissive surfaces, subtle film grain, true 8K material micro-detail on "
    "keycap texture, cable braiding, fingerprint smudges on glass, dust in the light beam. "
    "The environment is a late-night room that still breathes — a deep charcoal-blue background "
    "rather than a black void, the background always retains some visible texture (book spines, "
    "a window outline, the faint pattern of a wall). Brightness comes from a screen as the key, "
    "indicator LEDs, and one warm practical lamp that lifts the shadows. "
    "Color grade: cool cyan screen glow as the key, paired with a warm amber practical lamp so "
    "the shadows keep detail, a soft violet rim separating the subject from the background, "
    "skin tones stay warm and healthy against the cool light. "
    "Explicitly avoid: pure black backgrounds, crushed blacks, cold-only teal lighting, "
    "heavy desaturation, muddy grey skin. "
    "Composition: keep the lower third visually quiet for caption overlay, "
    "keep the center-left area clear so a floating UI panel can be composited later. "
    "Visual reference: the product cinematography of Apple keynote mixed with the warm late-night "
    "working aesthetic of Wong Kar-wai's \"In the Mood for Love\". "
)

AI_IMG_TAIL = (
    "Mood: focused, late-night, precise, but warm and human — the feeling of building something "
    "at one in the morning with a desk lamp on, premium tech-product aesthetic, clean and uncluttered, "
    "no cyberpunk cliches, no neon signs, no rain, no graffiti, no skyline in the background. "
    "Atmosphere: a fan spinning almost imperceptibly, a cursor blinking, dust drifting through "
    "the light beam, the faintest reflection of the screen on the matte desk surface, the silver "
    "pendant at her collarbone catching a single glint as she breathes. "
    "Technical: ultra-sharp where the eye lands, no halation on the cyan, no bloom that washes out "
    "text edges, no vignette so heavy it crushes the subject. "
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
   人脸是 YouTube 缩略图最强的点击变量，没有之一。
   缩略图让她的脸占画面 40%–60%，配一个大表情（皱眉 / 愣住 / 无奈地笑），
   再用高对比色块和指向性构图兜底。
   串脸的顾虑由「参考图垫图 + 后期统一」解决，不靠「不露脸」。
   （这条 2026-08-30 改过一次「必须露脸」，2026-08-31 又改了一次：不是规则层强制，
   而是 AI 频道的缩略图因为点击率需要把脸当作主视觉；正片镜头里是「该看就看」。）
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
# 金融频道缩略图也允许她出脸（用户有参考图，脸不是问题），但更克制，多用场景元素而不是脸。
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