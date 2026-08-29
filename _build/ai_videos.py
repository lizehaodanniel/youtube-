# -*- coding: utf-8 -*-
# AI 包 · 实操卡镜头级视频提示词（3D 卡通女创作者 host）
#
# mode 含义：
#   "ai-video" → 可直接喂 Runway Gen-3 / Kling 1.6 / Veo 3 生成（纯画面，不含文字）
#   "screen"   → 这是你自己录屏 + After Effects 做的，AI 提示词只作氛围 B-roll 参考
#                （视频模型生成带文字的 UI 会糊，不要指望它出可读的真实输出）

AHOST_VIDEO = (
    "a consistent 3D animated young female creator, Pixar-inspired semi-realistic 3D render, "
    "large expressive eyes, long straight light-blonde hair, black baseball cap and large black "
    "over-ear headphones, fitted pink t-shirt, small cross necklace, black arm sleeves with buckle "
    "straps, black lace-up pants"
)

ASTAGE = (
    "in a modern high-rise apartment studio with a microphone on a boom arm, a coffee mug and "
    "a dark sofa, large floor-to-ceiling windows showing a city skyline at dusk, purple and "
    "magenta neon ambient light, soft three-point studio lighting, shallow depth of field, "
    "Pixar-style 3D animation, smooth 24fps motion, clean render"
)

NEG_HOST = (
    "no text, no subtitles, no watermark, no extra limbs, no deformed hands, no flickering, "
    "no morphing face, no camera shake, no realistic human skin, no live-action footage"
)

NEG_SCREEN = (
    "no readable garbled text, no watermarks, no lens flare, no motion sickness camera swing, "
    "no blurry UI, no frozen frame, no strobing"
)


def _host(action, camera, seconds):
    return f"{AHOST_VIDEO}, {action}, {ASTAGE}, {camera}, {seconds} seconds"


def _screen(action, camera, seconds):
    return (
        f"cinematic animated screen-capture style shot, {action}, clean flat UI design, "
        f"dark interface with purple and pink accent highlights, {camera}, "
        f"soft glow on the highlighted element, subtle motion blur on transitions, {seconds} seconds"
    )


VIDEOS = {
    1: {
        "neg_host": NEG_HOST,
        "neg_screen": NEG_SCREEN,
        "shots": [
            {
                "shot": "S1 · 走入画面捧起成品",
                "mode": "ai-video",
                "dur": "4s",
                "en": _host(
                    "stepping into frame from the left, leaning forward and lifting a labeled deliverable folder "
                    "from the desk with both hands, holding it at chest height and looking into the camera",
                    "camera pushes in from a medium shot to a medium close-up",
                    "4",
                ),
                "zh": "卡通女创作者从画面左侧走入，弯下腰用双手捧起桌面上贴好标签的成品文件夹，举到胸前看向镜头。镜头从中景推到中近景。4 秒。",
            },
            {
                "shot": "S2 · Finder 文件列表",
                "mode": "screen",
                "dur": "5s",
                "en": _screen(
                    "a Finder window opens, ten files listed in order with clean numbered names, the mouse "
                    "cursor glides slowly down the list and hovers on three representative files one at a time",
                    "static locked-off shot",
                    "5",
                ),
                "zh": "Finder 窗口打开，10 个文件按顺序排列、命名规范；鼠标缓慢滑下文件列表，依次停在 3 个代表性文件上各 1 秒。机位固定。5 秒。",
            },
            {
                "shot": "S3 · 圈出报价单",
                "mode": "ai-video",
                "dur": "3s",
                "en": _host(
                    "sliding a quote sheet out of the folder, holding it up to the camera and using a pen to "
                    "circle the included-versus-excluded line, then nodding once",
                    "camera holds a medium close-up",
                    "3",
                ),
                "zh": "卡通女创作者从文件夹里抽出一张报价单，举到镜头前用笔圈住「包含/不包含」那一行，然后点一下头。中近景固定。3 秒。",
            },
        ],
    },
    2: {
        "neg_host": NEG_HOST,
        "neg_screen": NEG_SCREEN,
        "shots": [
            {
                "shot": "S1 · 需求单标题自动写入",
                "mode": "screen",
                "dur": "4s",
                "en": _screen(
                    "a blank document types its own title 'Coffee Shop Content Sprint', then a small red "
                    "tag in parentheses reading FICTIONAL fades in next to the title",
                    "static locked-off shot",
                    "4",
                ),
                "zh": "空白文档自动打出标题「Coffee Shop Content Sprint」，标题旁淡入一个红色小标签「FICTIONAL」。机位固定。4 秒。",
            },
            {
                "shot": "S2 · 三栏逐个填入",
                "mode": "screen",
                "dur": "4s",
                "en": _screen(
                    "three column headers appear, Audience, Business problem, Deliverables, then each "
                    "column fills line by line, the last line about content for seven days glowing softly",
                    "static locked-off shot with a very slow push in",
                    "4",
                ),
                "zh": "三个列标题依次出现：Audience / Business problem / Deliverables；每列逐行填入文字，最后一行「7 天内容」柔光高亮。机位固定并极慢推近。4 秒。",
            },
            {
                "shot": "S3 · 对镜头比三",
                "mode": "ai-video",
                "dur": "3s",
                "en": _host(
                    "sitting back from the screen and facing the camera, holding up three fingers in a calm "
                    "counting gesture, slight serious expression",
                    "camera holds a medium close-up",
                    "3",
                ),
                "zh": "卡通女创作者从屏幕前回过身面对镜头，平静地竖起三根手指比划 3，表情认真。中近景固定。3 秒。",
            },
        ],
    },
    3: {
        "neg_host": NEG_HOST,
        "neg_screen": NEG_SCREEN,
        "shots": [
            {
                "shot": "S1 · ChatGPT 输入并发送",
                "mode": "screen",
                "dur": "4s",
                "en": _screen(
                    "a chat input box pastes a four-line brief automatically, then a structured instruction "
                    "appends below it, finally the send button pulses and the cursor clicks it",
                    "static locked-off shot",
                    "4",
                ),
                "zh": "聊天输入框自动粘贴一段 4 行的 brief，结构化要求追加在下方，发送按钮被光标点击。机位固定。4 秒。",
            },
            {
                "shot": "S2 · 表格输出 + 标红编造",
                "mode": "screen",
                "dur": "4s",
                "en": _screen(
                    "a seven-row table streams out line by line, three rows are then highlighted in red with a "
                    "small floating tag reading INVENTED beside each",
                    "static locked-off shot",
                    "4",
                ),
                "zh": "7 行表格逐行流出，其中 3 行被红色高亮，每行旁边浮出一个小标签「INVENTED」。机位固定。4 秒。",
            },
            {
                "shot": "S3 · 摇头 + 删",
                "mode": "ai-video",
                "dur": "3s",
                "en": _host(
                    "shaking her head with a small frown, then making a single short swipe gesture in the air "
                    "as if crossing something out, and looking back at the camera",
                    "camera holds a close-up on the face",
                    "3",
                ),
                "zh": "卡通女创作者轻轻摇头皱眉，抬手在空气中划一个简短的手势表示「划掉」，然后回看镜头。面部近景。3 秒。",
            },
        ],
    },
    4: {
        "neg_host": NEG_HOST,
        "neg_screen": NEG_SCREEN,
        "shots": [
            {
                "shot": "S1 · Canva 画布 + 品牌面板",
                "mode": "screen",
                "dur": "4s",
                "en": _screen(
                    "a square blank canvas appears, a left-side panel slides open showing two brand colors "
                    "and one brand font locked in",
                    "static locked-off shot",
                    "4",
                ),
                "zh": "正方形空白画布出现，右侧品牌面板滑出，已固定 2 个品牌色与 1 个字体。机位固定。4 秒。",
            },
            {
                "shot": "S2 · Logo 吸附对齐",
                "mode": "screen",
                "dur": "4s",
                "en": _screen(
                    "a logo is dragged from the sidebar and snaps to the top-left corner, alignment guides "
                    "flash briefly when the position is correct",
                    "static locked-off shot",
                    "4",
                ),
                "zh": "Logo 从素材栏被拖到左上角，位置对齐的瞬间辅助线闪一下。机位固定。4 秒。",
            },
            {
                "shot": "S3 · 7 页缩略图依次出现",
                "mode": "screen",
                "dur": "3s",
                "en": _screen(
                    "left-side thumbnails count up from one to seven, each new page sliding in with a soft pop",
                    "static locked-off shot",
                    "3",
                ),
                "zh": "左侧缩略图从 1 张增加到 7 张，每新一页用柔和小弹出动画滑入。机位固定。3 秒。",
            },
            {
                "shot": "S4 · 在笔记上画 7 个圈",
                "mode": "ai-video",
                "dur": "3s",
                "en": _host(
                    "drawing seven small circles in a row on a notebook on the desk with a pen, then tapping "
                    "the last circle once and looking up at the camera",
                    "camera holds a medium close-up on the desk",
                    "3",
                ),
                "zh": "卡通女创作者在桌上笔记本里用笔画一排 7 个小圈，点最后一下后抬头看向镜头。桌面中近景。3 秒。",
            },
        ],
    },
    5: {
        "neg_host": NEG_HOST,
        "neg_screen": NEG_SCREEN,
        "shots": [
            {
                "shot": "S1 · 五项清单逐项打勾",
                "mode": "screen",
                "dur": "4s",
                "en": _screen(
                    "a small checklist card appears bottom-right, five empty boxes, one by one a check mark "
                    "draws itself in each box with a small pop",
                    "static locked-off shot",
                    "4",
                ),
                "zh": "右下角出现五项清单卡，5 个空框，每框依次出现打勾动画并轻微弹出。机位固定。4 秒。",
            },
            {
                "shot": "S2 · 指向清单 + 举 5 根指头",
                "mode": "ai-video",
                "dur": "3s",
                "en": _host(
                    "pointing one hand toward the checklist card, then raising the same hand and holding up "
                    "all five fingers with a confident expression",
                    "camera holds a medium close-up",
                    "3",
                ),
                "zh": "卡通女创作者用一只手指向清单卡，随后抬起同一只手竖起 5 根手指，表情自信。中近景固定。3 秒。",
            },
        ],
    },
    6: {
        "neg_host": NEG_HOST,
        "neg_screen": NEG_SCREEN,
        "shots": [
            {
                "shot": "S1 · 3 段素材入时间线",
                "mode": "screen",
                "dur": "4s",
                "en": _screen(
                    "a vertical video project opens, three clips are dragged into the timeline and snap into "
                    "place in order, total length about thirty seconds",
                    "static locked-off shot",
                    "4",
                ),
                "zh": "竖屏项目打开，3 段素材依次拖入时间线并吸附到位，总长约 30 秒。机位固定。4 秒。",
            },
            {
                "shot": "S2 · 字幕轨道逐行出现",
                "mode": "screen",
                "dur": "3s",
                "en": _screen(
                    "an auto-caption track appears below the video, caption lines stream in one after the "
                    "other matching the speech",
                    "static locked-off shot",
                    "3",
                ),
                "zh": "视频下方出现自动字幕轨道，字幕行逐行出现并对口播。机位固定。3 秒。",
            },
            {
                "shot": "S3 · 改写 cold blue → cold brew",
                "mode": "screen",
                "dur": "3s",
                "en": _screen(
                    "a mis-typed caption reading COLD BLUE is selected and rewritten to COLD BREW, the line "
                    "briefly highlights in green when the edit lands",
                    "static locked-off shot",
                    "3",
                ),
                "zh": "被误打成 COLD BLUE 的字幕行被选中并改写为 COLD BREW，落字瞬间整行短暂高亮绿色。机位固定。3 秒。",
            },
            {
                "shot": "S4 · 嘘手势",
                "mode": "ai-video",
                "dur": "3s",
                "en": _host(
                    "raising one index finger to her lips in a quiet gesture, serious expression, eyes locked "
                    "on the camera to signal sound-off review",
                    "camera holds a close-up on the face",
                    "3",
                ),
                "zh": "卡通女创作者竖起一根食指贴在唇前做「嘘」手势，表情严肃，盯镜头示意静音审片。面部近景。3 秒。",
            },
        ],
    },
    7: {
        "neg_host": NEG_HOST,
        "neg_screen": NEG_SCREEN,
        "shots": [
            {
                "shot": "S1 · 计时表逐行填入",
                "mode": "screen",
                "dur": "4s",
                "en": _screen(
                    "a two-column spreadsheet fills itself row by row, Task then Minutes, brief fifteen, "
                    "captions thirty-five, Canva fifty-five, video forty-five, QC twenty",
                    "static locked-off shot with a very slow push in",
                    "4",
                ),
                "zh": "两列表格逐行自动填入：Task / Minutes，brief 15 / captions 35 / Canva 55 / video 45 / QC 20。机位固定并极慢推近。4 秒。",
            },
            {
                "shot": "S2 · 合计 + 除法 + 时薪",
                "mode": "screen",
                "dur": "4s",
                "en": _screen(
                    "the total cell reads 170 minutes, then converts to 2.83 hours, then the calculator result "
                    "100 divided by 2.83 approximately 35 appears in a separate pop-up",
                    "static locked-off shot",
                    "4",
                ),
                "zh": "合计格显示 170 分钟，换算为 2.83 小时，弹出小计算器显示 100 ÷ 2.83 ≈ 35。机位固定。4 秒。",
            },
            {
                "shot": "S3 · 惊讶到认真",
                "mode": "ai-video",
                "dur": "3s",
                "en": _host(
                    "pointing one finger at the on-screen number, eyebrows rising slightly in a brief surprise, "
                    "then the expression settles into a calm serious look back at the camera",
                    "camera holds a medium close-up",
                    "3",
                ),
                "zh": "卡通女创作者用一根手指指着屏幕上的数字，眉毛短暂上抬带出惊讶，然后表情恢复平静认真地回看镜头。中近景固定。3 秒。",
            },
        ],
    },
    8: {
        "neg_host": NEG_HOST,
        "neg_screen": NEG_SCREEN,
        "shots": [
            {
                "shot": "S1 · 4 个模板高亮",
                "mode": "screen",
                "dur": "4s",
                "en": _screen(
                    "a folder opens, four template files are highlighted in turn with a soft glow while the "
                    "other deliverable files stay dimmed",
                    "static locked-off shot",
                    "4",
                ),
                "zh": "文件夹打开，4 个模板文件依次被柔光高亮，其余本次成品保持低亮。机位固定。4 秒。",
            },
            {
                "shot": "S2 · 邮件草稿首句",
                "mode": "screen",
                "dur": "4s",
                "en": _screen(
                    "an email draft opens with exactly one recipient, the first sentence is a specific observation "
                    "highlighted in soft green to stand out from the rest of the message",
                    "static locked-off shot",
                    "4",
                ),
                "zh": "邮件草稿打开，收件人仅 1 个，首句是一项具体观察并被柔绿高亮以区别于其他文字。机位固定。4 秒。",
            },
            {
                "shot": "S3 · 平视的告别手势",
                "mode": "ai-video",
                "dur": "4s",
                "en": _host(
                    "facing the camera in a calm medium close-up, raising one open hand in a small no-pressure "
                    "wave, expression warm and composed",
                    "camera holds still, very slow push in",
                    "4",
                ),
                "zh": "卡通女创作者正面对镜头中近景，平静地抬起一只张开的手做小幅「不施压的招呼」，表情温和从容。机位固定并极慢推近。4 秒。",
            },
        ],
    },
}
