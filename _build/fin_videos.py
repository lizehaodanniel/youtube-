# -*- coding: utf-8 -*-
# 金融包 · 实操卡镜头级视频提示词（卡通牛 host）
#
# 每张实操卡一组镜头。mode 决定怎么用：
#   "ai-video" → 可直接喂给 Runway Gen-3 / Kling 1.6 / Veo 3 生成（纯画面，不含文字）
#   "screen"   → 这是你自己录屏 + After Effects 做的，AI 提示词只作氛围 B-roll 参考
#                （视频模型生成带文字的 UI 会糊，不要指望它出可读的 APR 数字）

VHOST = (
    "a consistent 3D animated cartoon cow mascot, Pixar-inspired semi-realistic 3D render, "
    "standing upright with hooves-as-hands, fluffy white fur with caramel-brown patches around the eyes and ears, "
    "two small curved ivory horns, a cream tuft of hair on the forehead, large expressive round brown eyes, "
    "soft pink nose, gentle calm smile, wearing a neat navy-blue vest over a light shirt"
)

STAGE = (
    "in a tidy minimal home study with a wooden desk, a calculator, a notebook and a warm desk lamp, "
    "soft three-point studio lighting, shallow depth of field, Pixar-style 3D animation, "
    "smooth 24fps motion, clean render"
)

NEG_HOST = (
    "no text, no subtitles, no watermark, no extra limbs, no deformed hooves, no flickering, "
    "no morphing face, no camera shake, no realistic human skin, no live-action footage"
)

NEG_SCREEN = (
    "no readable garbled text, no watermarks, no lens flare, no motion sickness camera swing, "
    "no blurry UI, no frozen frame, no strobing"
)


def _host(action, camera, seconds):
    return f"{VHOST}, {action}, {STAGE}, {camera}, {seconds} seconds"


def _screen(action, camera, seconds):
    return (
        f"cinematic animated screen-capture style shot, {action}, clean flat UI design, "
        f"dark navy interface with amber and red highlight accents, {camera}, "
        f"soft glow on the highlighted element, subtle motion blur on transitions, {seconds} seconds"
    )


VIDEOS = {
    1: {
        "neg_host": NEG_HOST,
        "neg_screen": NEG_SCREEN,
        "shots": [
            {
                "shot": "S1 · 举起手写的数字卡",
                "mode": "ai-video",
                "dur": "3s",
                "en": _host(
                    "sitting at the desk and picking up a hand-lettered card with both hooves, holding it up so it "
                    "faces the camera, then lowering it slightly and looking up with a serious attentive expression",
                    "camera slowly pushes in from a medium shot to a close-up",
                    "3",
                ),
                "zh": "卡通牛坐在书桌前，双手（蹄）举起一张手写的卡片，正面朝向镜头，随后略微放下并抬起头，表情认真专注。镜头从中景缓慢推近到近景。3 秒。",
            },
            {
                "shot": "S2 · 一个数字铺满全屏",
                "mode": "screen",
                "dur": "5s",
                "en": _screen(
                    "a single large interest-rate figure scales up to fill almost the whole frame on an otherwise "
                    "empty cream-coloured layout, a thin underline draws itself beneath it and a short caption line "
                    "fades in below, a faint red annotation badge appears at the corner reading guaranteed not assumed",
                    "static locked-off shot, no camera movement",
                    "5",
                ),
                "zh": "一个巨大的利率数字放大到几乎铺满画面，背景是空白的奶油色版面；下方自动画出一道细下划线，再淡入一行简短说明，角落出现一枚红色批注徽标。机位固定不动。5 秒。",
            },
            {
                "shot": "S3 · 指向三问表",
                "mode": "ai-video",
                "dur": "4s",
                "en": _host(
                    "lowering the statement and turning to the right side of the frame, extending one hoof to point "
                    "at an empty three-row table beside the desk, then nodding once toward the camera",
                    "camera pans slightly right following the hoof, then holds",
                    "4",
                ),
                "zh": "卡通牛放下账单，转向画面右侧，伸出一只蹄指向桌边的空三行表格，然后朝镜头点一下头。镜头轻微右摇跟随，随后固定。4 秒。",
            },
        ],
    },
    2: {
        "neg_host": NEG_HOST,
        "neg_screen": NEG_SCREEN,
        "shots": [
            {
                "shot": "S1 · 三行标签飞入",
                "mode": "screen",
                "dur": "4s",
                "en": _screen(
                    "an empty spreadsheet builds itself, three row labels slide in one after another from the left "
                    "with a soft ease-out, then three column headers fade in on the right",
                    "static locked-off shot",
                    "4",
                ),
                "zh": "空白表格自动建表，三个行标签从左侧依次滑入（缓出），随后右侧三个列标题淡入。机位固定。4 秒。",
            },
            {
                "shot": "S2 · 白板手写三问",
                "mode": "ai-video",
                "dur": "4s",
                "en": _host(
                    "standing beside a whiteboard holding a marker in one hoof, writing three short lines from top to "
                    "bottom, then capping the marker and turning to face the camera",
                    "camera holds a steady medium shot",
                    "4",
                ),
                "zh": "卡通牛站在白板旁，一只蹄夹着马克笔，从上到下写三行字，写完盖上笔帽转身面对镜头。中景固定机位。4 秒。",
            },
            {
                "shot": "S3 · 示例列 vs 观众列",
                "mode": "screen",
                "dur": "4s",
                "en": _screen(
                    "a completed table where the example column holds values and the viewer column stays empty with a "
                    "gentle pulsing outline inviting input, the example column dims slightly to separate the two",
                    "static locked-off shot with a very slow push in",
                    "4",
                ),
                "zh": "完成的表格里，示例列有数值，观众列空着并以柔和脉冲描边提示填写；示例列轻微压暗以区分两列。机位固定并极缓慢推近。4 秒。",
            },
        ],
    },
    3: {
        "neg_host": NEG_HOST,
        "neg_screen": NEG_SCREEN,
        "shots": [
            {
                "shot": "S1 · 打开官方数据页",
                "mode": "ai-video",
                "dur": "5s",
                "en": _host(
                    "sitting at the desk with a floating translucent browser panel in front, scrolling the panel "
                    "downward with one hoof, brow furrowed in concentration",
                    "camera holds a medium shot with a slow dolly in",
                    "5",
                ),
                "zh": "卡通牛坐在书桌前，面前悬浮一块半透明浏览器面板，用一只蹄向下滚动页面，眉头微皱神情专注。中景缓慢推轨。5 秒。",
            },
            {
                "shot": "S2 · 高亮利率口径",
                "mode": "screen",
                "dur": "5s",
                "en": _screen(
                    "a yellow highlight bar sweeps down a data table and lands on one row, pausing there while a "
                    "second dimmer row stays unhighlighted for contrast",
                    "static locked-off shot",
                    "5",
                ),
                "zh": "黄色高亮条沿数据表格向下扫过，落在某一行并停留；另一行保持不高亮形成对比。机位固定。5 秒。",
            },
            {
                "shot": "S3 · 计算器逐格填数",
                "mode": "screen",
                "dur": "5s",
                "en": _screen(
                    "a compound-interest calculator with four input fields, the cursor jumps field by field filling "
                    "each one, then a red annotation badge pops in beside the return-rate field",
                    "static locked-off shot",
                    "5",
                ),
                "zh": "复利计算器四个输入框，光标逐格跳转并填入数值，随后回报率输入框旁弹出一枚红色批注徽标。机位固定。5 秒。",
            },
            {
                "shot": "S4 · 提醒看发布日期",
                "mode": "ai-video",
                "dur": "4s",
                "en": _host(
                    "pointing one hoof at a date printed on the floating panel, then turning to the camera and "
                    "wagging the hoof side to side in a gentle warning gesture",
                    "camera holds a close-up",
                    "4",
                ),
                "zh": "卡通牛用一只蹄指向悬浮面板上的日期，然后转向镜头，轻轻左右摆动蹄子做出提醒手势。近景固定。4 秒。",
            },
        ],
    },
    4: {
        "neg_host": NEG_HOST,
        "neg_screen": NEG_SCREEN,
        "shots": [
            {
                "shot": "S1 · 只改利率那一格",
                "mode": "screen",
                "dur": "5s",
                "en": _screen(
                    "a payoff calculator where only the interest-rate field changes, its digits count down through "
                    "three values while every other field stays frozen and dimmed, the result figures on the right "
                    "recalculate and settle after each change",
                    "static locked-off shot",
                    "5",
                ),
                "zh": "还款计算器里只有利率字段在变，数字依次跳三个值，其余字段全部冻结并压暗；右侧结果数字每次变化后重新计算并稳定下来。机位固定。5 秒。",
            },
            {
                "shot": "S2 · 「只改这一个」手势",
                "mode": "ai-video",
                "dur": "4s",
                "en": _host(
                    "raising one hoof with a single finger extended while the other hoof rests flat on the desk, "
                    "holding an emphatic but calm expression and nodding once",
                    "camera holds a medium close-up",
                    "4",
                ),
                "zh": "卡通牛举起一只蹄伸出单指，另一只蹄平放在桌上，表情强调但克制，点一下头。中近景固定。4 秒。",
            },
            {
                "shot": "S3 · 三案例并排对比",
                "mode": "screen",
                "dur": "5s",
                "en": _screen(
                    "three result bars grow upward side by side from a baseline, each a different height, with the "
                    "tallest bar tinted red and the shortest tinted green, a faint grid behind them",
                    "static locked-off shot with a slow pull back to reveal all three",
                    "5",
                ),
                "zh": "三根结果柱从基线并排向上生长，高度各不相同，最高的染红、最矮的染绿，背后有淡淡网格。机位固定并缓慢拉远露出全部三根。5 秒。",
            },
        ],
    },
    5: {
        "neg_host": NEG_HOST,
        "neg_screen": NEG_SCREEN,
        "shots": [
            {
                "shot": "S1 · 红框圈三个陷阱字段",
                "mode": "screen",
                "dur": "5s",
                "en": _screen(
                    "three documents laid side by side, a red selection box draws around one clause in each document "
                    "in sequence, each box pulses once when it locks on",
                    "camera glides slowly left to right across the three documents",
                    "5",
                ),
                "zh": "三份文件并排摆放，红色选框依次在每份文件的一个条款上画出，每个框锁定后脉冲一次。镜头在三份文件间缓慢左到右滑移。5 秒。",
            },
            {
                "shot": "S2 · 红笔绿笔交替",
                "mode": "ai-video",
                "dur": "4s",
                "en": _host(
                    "holding a red marker in one hoof and a green marker in the other, alternately marking papers on "
                    "the desk, glancing up at the camera with a wary expression",
                    "camera holds a medium shot",
                    "4",
                ),
                "zh": "卡通牛一只蹄拿红笔、一只蹄拿绿笔，交替在桌上的文件上做标记，抬头看向镜头时表情带警惕。中景固定。4 秒。",
            },
            {
                "shot": "S3 · 连线到表格单元格",
                "mode": "screen",
                "dur": "5s",
                "en": _screen(
                    "highlighted fields on the left connect to cells in a table on the right via thin animated "
                    "connector lines that draw themselves one by one",
                    "static locked-off shot",
                    "5",
                ),
                "zh": "左侧高亮字段通过纤细的动态连线逐条连到右侧表格的对应单元格。机位固定。5 秒。",
            },
        ],
    },
    6: {
        "neg_host": NEG_HOST,
        "neg_screen": NEG_SCREEN,
        "shots": [
            {
                "shot": "S1 · 高亮 match 公式",
                "mode": "screen",
                "dur": "5s",
                "en": _screen(
                    "a retirement plan document scrolls to a section heading, then an amber highlighter sweeps across "
                    "a short formula line and holds",
                    "static locked-off shot with a gentle push in",
                    "5",
                ),
                "zh": "退休计划文件滚动到章节标题，随后琥珀色荧光笔扫过一行简短公式并停留。机位固定并轻微推近。5 秒。",
            },
            {
                "shot": "S2 · 白板算式 + 耸肩",
                "mode": "ai-video",
                "dur": "4s",
                "en": _host(
                    "writing a short equation on a whiteboard, then stopping mid-motion, turning to the camera and "
                    "shrugging both shoulders with an honest puzzled expression",
                    "camera holds a medium shot",
                    "4",
                ),
                "zh": "卡通牛在白板上写一个简短算式，写到一半停下，转身面对镜头耸了耸肩，露出坦诚的困惑表情。中景固定。4 秒。",
            },
            {
                "shot": "S3 · 归属期曲线填充",
                "mode": "screen",
                "dur": "5s",
                "en": _screen(
                    "a horizontal vesting bar fills from left to right in stages, small tick marks appear at each "
                    "milestone year and gently pulse",
                    "static locked-off shot",
                    "5",
                ),
                "zh": "水平归属进度条从左到右分阶段填充，每个里程碑年份处出现小刻度并轻微脉冲。机位固定。5 秒。",
            },
            {
                "shot": "S4 · 白板写五步顺序",
                "mode": "ai-video",
                "dur": "4s",
                "en": _host(
                    "writing five numbered lines down a whiteboard in order, tapping the board once after each line "
                    "is finished",
                    "camera slowly tilts down following the writing",
                    "4",
                ),
                "zh": "卡通牛在白板上按顺序写下五行编号文字，每写完一行轻敲一下板面。镜头随书写缓慢下摇。4 秒。",
            },
        ],
    },
    7: {
        "neg_host": NEG_HOST,
        "neg_screen": NEG_SCREEN,
        "shots": [
            {
                "shot": "S1 · 假设区块展开并与结果并排",
                "mode": "screen",
                "dur": "4s",
                "en": _screen(
                    "an assumptions block unfolds on the right side of a table, its four rows appear one by one, then "
                    "the block slides next to the results block and both lock into a frozen split view",
                    "static locked-off shot",
                    "4",
                ),
                "zh": "表格右侧展开假设区块，四行逐条出现，随后该区块滑到结果区块旁边，两者锁定为并排冻结视图。机位固定。4 秒。",
            },
            {
                "shot": "S2 · 两叠纸并排压平",
                "mode": "ai-video",
                "dur": "4s",
                "en": _host(
                    "placing two small stacks of papers side by side on the desk and flattening them with both palms, "
                    "then looking up and giving a single satisfied nod",
                    "camera holds a medium close-up over the desk",
                    "4",
                ),
                "zh": "卡通牛把两小叠纸并排放在桌上，双掌压平，抬头后满意地点一下头。中近景俯拍桌面。4 秒。",
            },
        ],
    },
    8: {
        "neg_host": NEG_HOST,
        "neg_screen": NEG_SCREEN,
        "shots": [
            {
                "shot": "S1 · 主机位指向下方",
                "mode": "ai-video",
                "dur": "4s",
                "en": _host(
                    "seated and facing the camera in a calm medium close-up, raising one hoof and pointing gently "
                    "toward the lower part of the frame, expression warm and composed",
                    "camera holds still, very slow push in",
                    "4",
                ),
                "zh": "卡通牛坐姿正面中近景，神情平静，抬起一只蹄轻轻指向画面下方，表情温和从容。机位固定并极慢推近。4 秒。",
            },
            {
                "shot": "S2 · 评论框出现关键词",
                "mode": "screen",
                "dur": "4s",
                "en": _screen(
                    "a comment input box where a short four-letter word types itself out and the surrounding bubble "
                    "gives one soft bounce",
                    "static locked-off shot",
                    "4",
                ),
                "zh": "评论输入框里一个四字母短词自动打出来，外框气泡轻微弹跳一次。机位固定。4 秒。",
            },
            {
                "shot": "S3 · 三根债务柱与问号",
                "mode": "screen",
                "dur": "5s",
                "en": _screen(
                    "three vertical bars of different heights stand in a row, a floating question mark hovers and "
                    "bobs above the shortest bar",
                    "static locked-off shot",
                    "5",
                ),
                "zh": "三根高度不同的竖柱排成一行，一个悬浮问号在最矮的那根上方上下轻晃。机位固定。5 秒。",
            },
            {
                "shot": "S4 · 指向空白三问表",
                "mode": "ai-video",
                "dur": "3s",
                "en": _host(
                    "turning slightly and pointing at an empty three-row table on the desk, then looking back at the "
                    "camera and nodding once",
                    "camera holds a medium shot",
                    "3",
                ),
                "zh": "卡通牛微微转身，指向桌上空白的三行表格，然后回看镜头点一下头。中景固定。3 秒。",
            },
        ],
    },
}
