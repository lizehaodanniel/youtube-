# -*- coding: utf-8 -*-
"""
build.py — 把句子级素材合成为 packages.json

职责：
1. 读取每个包的句子素材（*_ch*.py 的 LINES）与实操卡（*_demos.py 的 DEMOS）。
2. 按「章节时长 + 句内词数」自动分配每句的起止时间，保证时间轴连续且总时长精确。
3. 为每条图片提示词统一拼接 host 角色卡前缀与画质/画幅后缀，保证跨图一致。
4. 保留 packages.json 原有元信息（标题、Hook、缩略图、标签等），只替换 script，
   并新增 demo_cards、sentence_count、word_count、duration 等字段。
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import ai_ch1_4, ai_ch5_6, ai_ch7_8, ai_demos          # noqa: E402
import fin_ch1_4, fin_ch5_6, fin_ch7_8, fin_demos      # noqa: E402
import fin_videos                                      # noqa: E402
import ai_videos                                       # noqa: E402

# ---------------------------------------------------------------- 角色卡前缀
HOST_PREFIX = {
    "ai": (
        # 3D 卡通女性创作者形象（@AIcheatcodeplaybook 的 "CHEAT CODE" 频道风格）。
        # 风格与金融包卡通牛保持一致：Pixar-inspired semi-realistic 3D render。
        # 注意：host 描述里不带任何具体品牌文字（避免 Midjourney 文字糊），也不复刻 t-shirt 印字。
        "host: a consistent 3D animated young female creator, Pixar-inspired semi-realistic 3D render, "
        "large expressive eyes, long straight light-blonde hair, wearing a black baseball cap and large black "
        "over-ear headphones, a fitted pink t-shirt, a small cross necklace, black arm sleeves with buckle "
        "straps, black lace-up pants, sitting in a modern high-rise apartment studio with a microphone on a "
        "boom arm, a coffee mug and a dark sofa, large floor-to-ceiling windows showing a city skyline at "
        "dusk, purple and magenta neon ambient light, soft three-point studio lighting, shallow depth of "
        "field, clean render",
        "host：风格一致的 3D 卡通年轻女性创作者，皮克斯风格半写实 3D 渲染，大而富有表现力的眼睛，浅金色长直发，"
        "黑色棒球帽与大黑色 over-ear 耳机，粉色贴身 T 恤，小十字架项链，黑色带搭扣臂套，黑色系带裤，"
        "坐在现代高层公寓工作室，桌前有支臂麦克风、咖啡杯与深色沙发，落地窗外是黄昏城市天际线，"
        "紫色与品红色霓虹环境光，柔和三点布光，浅景深，干净渲染",
    ),
    "finance": (
        # 卡通牛 host（非真人）。频道 @TheMoneyMoo + 参考 v12 同为卡通牛，视觉语言一致。
        "host: a consistent 3D animated cartoon cow mascot, Pixar-inspired semi-realistic 3D render, "
        "standing upright anthropomorphically with hooves-as-hands, soft fluffy white fur with warm caramel-brown "
        "patches around the eyes and ears, two small curved ivory horns, a small tuft of cream hair on the forehead, "
        "large expressive round brown eyes with bright highlights, a big soft pink nose, gentle calm friendly smile, "
        "short stout friendly proportions, wearing a neat navy-blue vest over a light shirt, "
        "in a tidy minimal study with a wooden desk, a calculator and a notebook",
        "host：风格一致的 3D 卡通奶牛吉祥物，皮克斯风格半写实 3D 渲染，拟人直立、以蹄为手，柔软蓬松白毛、眼周与耳部有焦糖棕斑块，"
        "两只小巧弯曲的象牙色牛角，额前一撮奶油色毛发，大而富有表现力的圆棕色眼睛带高光，柔软粉色大鼻子，温和沉稳的友善微笑，"
        "矮胖友好体型，浅色衬衫外搭整洁深蓝小马甲，位于简洁书房，木质书桌上放着计算器与笔记本",
    ),
}
SUFFIX_EN = ", ultra-detailed, 8k resolution, cinematic composition, --ar 16:9 --v 6.0"
SUFFIX_ZH = "，超高细节，8k 分辨率，电影级构图，--ar 16:9 --v 6.0"


def words(text):
    return len(re.findall(r"[A-Za-z0-9$%'-]+", text))


def fmt(sec):
    return f"{sec // 60}:{sec % 60:02d}"


def build_script(sources, chapters, host_prefix_en, host_prefix_zh):
    """sources: [(LINES 列表, [(start_sec, end_sec, count), ...]), ...]"""
    flat = []
    for lines, ch_specs in sources:
        cursor = 0
        for start, end, count in ch_specs:
            chunk = lines[cursor:cursor + count]
            cursor += count
            if len(chunk) != count:
                raise ValueError(f"章节句数不符：期望 {count}，实际 {len(chunk)}")
            wsum = sum(words(l[0]) for l in chunk) or 1
            acc = start
            for i, (en, zh, viz, demo_id, scene_en, scene_zh) in enumerate(chunk):
                share = (end - start) * words(en) / wsum
                if i == len(chunk) - 1:
                    nxt = end          # 最后一句补齐到章节末尾，避免累积误差
                else:
                    nxt = int(round(acc + share))
                    nxt = max(nxt, acc + 1)
                flat.append({
                    "t": f"{fmt(acc)}-{fmt(nxt)}",
                    "sec": [acc, nxt],
                    "wc": words(en),
                    "en": en,
                    "zh": zh,
                    "viz": viz,
                    "demo": {"need": bool(demo_id), "card": demo_id},
                    "img_en": f"{host_prefix_en}, {scene_en}{SUFFIX_EN}",
                    "img_zh": f"{host_prefix_zh}，{scene_zh}{SUFFIX_ZH}",
                })
                acc = nxt
    # 校验时间轴连续
    for a, b in zip(flat, flat[1:]):
        if a["sec"][1] != b["sec"][0]:
            raise ValueError(f"时间轴不连续：{a['t']} → {b['t']}")
    for r in flat:
        r.pop("sec")
    return flat


# ---------------------------------------------------------------- 章节时间轴
AI_SOURCES = [
    (ai_ch1_4.LINES, [(0, 15, 4), (15, 30, 4), (30, 75, 11), (75, 150, 18)]),
    (ai_ch5_6.LINES, [(150, 225, 18), (225, 300, 18)]),
    (ai_ch7_8.LINES, [(300, 375, 18), (375, 420, 11)]),
]
FIN_SOURCES = [
    (fin_ch1_4.LINES, [(0, 15, 4), (15, 30, 4), (30, 85, 13), (85, 150, 15)]),
    (fin_ch5_6.LINES, [(150, 225, 21), (225, 300, 18)]),
    (fin_ch7_8.LINES, [(300, 375, 18), (375, 420, 12)]),
]

AI_STARTS = [0, 15, 30, 75, 150, 225, 300, 375]
FIN_STARTS = [0, 15, 30, 85, 150, 225, 300, 375]


def attach_videos(cards, video_map):
    """给实操卡挂上镜头级视频提示词；缺镜头的卡给一条兜底提示。"""
    for c in cards:
        v = video_map.get(c["id"])
        if not v:
            continue
        c["video_prompts"] = v["shots"]
        c["video_neg"] = {
            "ai-video": v["neg_host"],
            "screen": v["neg_screen"],
        }
    missing = [c["id"] for c in cards if c["id"] not in video_map]
    if missing:
        print(f"  ⚠️ 缺视频提示词的实操卡：{missing}")
    return cards


def refresh_chapters(chapters, starts):
    out = []
    for c, s in zip(chapters, starts):
        name = re.sub(r"^\d+:\d+\s*", "", c)
        out.append(f"{fmt(s)} {name}")
    return out


def main():
    pkg_path = os.path.join(ROOT, "packages.json")
    with open(pkg_path, encoding="utf-8") as f:
        data = json.load(f)

    hp_ai, hp_fin = HOST_PREFIX["ai"], HOST_PREFIX["finance"]

    ai_script = build_script(AI_SOURCES, AI_STARTS, hp_ai[0], hp_ai[1])
    fin_script = build_script(FIN_SOURCES, FIN_STARTS, hp_fin[0], hp_fin[1])

    by_key = {p["channel_key"]: p for p in data["packages"]}

    ai = by_key["ai"]
    ai["script"] = ai_script
    ai["demo_cards"] = attach_videos(ai_demos.DEMOS, ai_videos.VIDEOS)
    ai["chapters"] = refresh_chapters(ai["chapters"], AI_STARTS)
    ai["sentence_count"] = len(ai_script)
    ai["word_count"] = sum(r["wc"] for r in ai_script)
    ai["duration"] = "7:00"
    ai["operator_breakdown"]["retention_curve"] = (
        "0:00–0:15 先亮成品文件夹与报价；0:15–0:30 承诺交付物；0:30–1:15 代入「工具很多却没有产品」并立三条规则；"
        "1:15–2:30 ChatGPT 需求→文案，展示一次 AI 编造并人工删除；2:30–3:45 Canva 一模板复制七图 + 五项验收单；"
        "3:45–5:00 CapCut 素材到可发布短视频，含字幕纠错与静音检查；5:00–6:15 计时表与报价边界，展示修改一次后时薪下降；"
        "6:15–7:00 金句「别卖 AI，卖文件」+ 模板与 CTA。句子级配图约每 4 秒一换，避免长时间对着同一画面。"
    )
    # AI 包 host 同步：3D 卡通女性创作者（@AIcheatcodeplaybook 频道风格）
    ai["character_card"] = (
        "虚拟主人公：3D 卡通年轻女性创作者（皮克斯风格半写实 3D 渲染），大而富有表现力的眼睛，浅金色长直发，"
        "黑色棒球帽配大黑色 over-ear 耳机，粉色贴身 T 恤，小十字架项链，黑色带搭扣臂套，黑色系带裤；"
        "场景为现代高层公寓工作室，桌前有支臂麦克风、咖啡杯与深色沙发，落地窗外是黄昏城市天际线，紫色与品红霓虹环境光。"
        "镜头以中近景 + 屏幕录制为主，语气亲切有活力，不使用「保证月入」。全部画面为非真人卡通形象，不出现真实人物。"
    )
    ai["host"] = (
        "AI 创作者（卡通形象）：3D 卡通女性，戴黑帽与大耳机，背景高层公寓紫色霓虹；"
        "不是喊口号，而是打开文件当场演示三件工具怎么串成可交付的一套。"
    )
    ai["host_note"] = (
        "AI 包为 3D 卡通女性 host，与金融包卡通牛一样不使用真人形象，也不参考过去版本的真人男创作者人设；"
        "先用成品反向证明交付物是文件不是工具，再用 ChatGPT / Canva / CapCut 三件工具的屏幕实操拆流程、立规则、给报价边界。"
        "全部收入数字均为示例计算，发布前需用真实账户或服务条款核对。"
    )
    # 缩略图用频道新视觉语言重写：紫色霓虹公寓 + 卡通女创作者 + 工具徽标
    ai["thumbs"] = [
        {
            "ver": "A",
            "desc": "卡通女创作者在紫色霓虹公寓里举起成品文件夹，前景是 100 美元报价单",
            "img_en": "YouTube thumbnail, a consistent 3D animated young female creator, Pixar-inspired semi-realistic "
                      "3D render, large expressive eyes, long light-blonde hair, black baseball cap and large black "
                      "over-ear headphones, fitted pink t-shirt, black arm sleeves, sitting in a modern high-rise "
                      "apartment studio with purple and magenta neon light, large windows showing a city skyline at "
                      "dusk, holding up a printed deliverable folder with one hand while a one-hundred-dollar quote "
                      "sheet sits on the desk in front, three small tool icons floating nearby, bold white and pink "
                      "typography, ultra-detailed, 8k --ar 16:9 --v 6.0",
            "img_zh": "YouTube 缩略图，风格一致的 3D 卡通年轻女性创作者，皮克斯风格半写实 3D 渲染，大而富有表现力的眼睛，"
                      "浅金色长发，黑色棒球帽与大黑色 over-ear 耳机，粉色贴身 T 恤，黑色臂套，坐在紫色与品红霓虹光的高层公寓工作室，"
                      "落地窗外是黄昏城市天际线，一只手举起打印好的交付物文件夹，桌前摆着一张一百美元报价单，"
                      "三个小工具图标浮在附近，粉白色粗体字，超高细节，8k --ar 16:9 --v 6.0",
        },
        {
            "ver": "B",
            "desc": "三栏对照：100 美元交付 vs 工具堆，霓虹公寓中的 3D 女创作者指着对比箭头",
            "img_en": "YouTube thumbnail, split-screen with three columns comparing one hundred dollars on the left, "
                      "a stack of unrelated AI tool icons in the middle, and a single clean deliverable file on the "
                      "right, a consistent 3D animated young female creator, Pixar-inspired semi-realistic 3D render, "
                      "black baseball cap, large over-ear headphones, pink t-shirt, pointing one hand at the gap "
                      "between the columns, purple and magenta neon background, bold yellow and white text, "
                      "ultra-detailed, 8k --ar 16:9 --v 6.0",
            "img_zh": "YouTube 缩略图，三栏分屏：左侧是一百美元，中间是杂乱的 AI 工具图标堆，右侧是一个干净的交付物文件，"
                      "风格一致的 3D 卡通年轻女性创作者，皮克斯风格半写实 3D 渲染，黑色棒球帽，大耳机，粉色 T 恤，"
                      "一只手指向栏与栏之间的差距，紫品红霓虹背景，黄色与白色粗体字，超高细节，8k --ar 16:9 --v 6.0",
        },
    ]

    fin = by_key["finance"]
    fin["script"] = fin_script
    fin["demo_cards"] = attach_videos(fin_demos.DEMOS, fin_videos.VIDEOS)
    # 金融包 host 改为卡通牛，全局元信息同步（character_card / host / 缩略图 / host_note）
    fin["character_card"] = (
        "虚拟主人公：3D 卡通奶牛吉祥物（皮克斯风格半写实 3D 渲染），拟人直立、以蹄为手，白毛配焦糖棕斑块，"
        "两只小象牙色牛角，圆眼睛、粉色大鼻子，浅色衬衫外搭深蓝小马甲；场景为简洁书房，木质书桌上有计算器、笔记本与白板。"
        "镜头以中近景 + 屏幕录制为主，语气克制，不使用「稳赚」「保证跑赢」。全部画面为非真人卡通形象，不出现真实人物。"
    )
    fin["host"] = (
        "金融教育者（卡通形象）：3D 卡通奶牛吉祥物，深蓝小马甲，语速稳，背景简洁书房；"
        "不是喊口号，而是打开官方数据页和计算器当场演示。"
    )
    fin["host_note"] = (
        "金融包为 3D 卡通牛 host，不使用真人形象的 host，也不参考 AI 包的真人创作者人设；"
        "先设局，再用真实数字和屏幕实操完成数学揭穿，给出决策框架、陷阱和唯一例外。"
        "所有收益数字均为示例计算，发布前回 Federal Reserve / NY Fed / Investor.gov / 401(k) 计划文件核对。"
    )
    fin["thumbs"] = [
        {
            "ver": "A",
            "desc": "卡通牛举账单，粗体 '22% FIRST?'，右侧红色 APR 圈选",
            "img_en": "YouTube thumbnail, a consistent 3D animated cartoon cow mascot, Pixar-inspired semi-realistic "
                      "3D render, standing upright with hooves-as-hands, fluffy white fur with caramel-brown patches, "
                      "two small curved ivory horns, large round brown eyes, soft pink nose, wearing a navy-blue vest, "
                      "holding up a credit-card statement with one hoof, huge red circled '22% APR' beside it, "
                      "bold yellow text 'PAY THIS FIRST?', high contrast yellow and red background, "
                      "ultra-detailed, 8k --ar 16:9 --v 6.0",
            "img_zh": "YouTube 缩略图，风格一致的 3D 卡通奶牛吉祥物，皮克斯风格半写实 3D 渲染，拟人直立、以蹄为手，"
                      "蓬松白毛配焦糖棕斑块，两只小巧象牙色牛角，圆棕色大眼睛，柔软粉鼻子，穿深蓝小马甲，"
                      "一只蹄举起信用卡账单，旁边是巨大红色圈选「22% APR」，黄色粗体字「PAY THIS FIRST?」，"
                      "高对比黄红背景，超高细节，8k --ar 16:9 --v 6.0",
        },
        {
            "ver": "B",
            "desc": "决策树对比：MATCH → DEBT → INVEST，数字 22% vs 7%，卡通牛指向转折点",
            "img_en": "YouTube thumbnail, clean split-screen decision tree reading MATCH then DEBT then INVEST, "
                      "giant numbers 22% versus 7%, a consistent 3D animated cartoon cow mascot, Pixar-inspired "
                      "semi-realistic 3D render, fluffy white fur with caramel-brown patches, small ivory horns, "
                      "wearing a navy-blue vest, pointing one hoof at the turning point of the tree, "
                      "bold white and green text, ultra-detailed, 8k --ar 16:9 --v 6.0",
            "img_zh": "YouTube 缩略图，干净的分屏决策树，顺序为 MATCH → DEBT → INVEST，巨大数字 22% 对比 7%，"
                      "风格一致的 3D 卡通奶牛吉祥物，皮克斯风格半写实 3D 渲染，蓬松白毛配焦糖棕斑块，小巧象牙色牛角，"
                      "穿深蓝小马甲，一只蹄指向决策树的转折点，白色与绿色粗体字，超高细节，8k --ar 16:9 --v 6.0",
        },
    ]
    fin["chapters"] = refresh_chapters(fin["chapters"], FIN_STARTS)
    fin["sentence_count"] = len(fin_script)
    fin["word_count"] = sum(r["wc"] for r in fin_script)
    fin["duration"] = "7:00"
    fin["operator_breakdown"]["retention_curve"] = (
        "0:00–0:15 先圈出账单 APR 与 22% 的确定成本；0:15–0:30 给出三问测试；0:30–1:25 代入「投资在涨但利息更快」并区分确定与预期；"
        "1:25–2:30 打开 G.19 与复利计算器，建立可复核性；2:30–3:45 三案例只改利率，看边界在哪；"
        "3:45–5:00 三个陷阱并指到文件上的具体字段；5:00–6:15 401(k) match 例外与五步顺序；"
        "6:15–7:00 可复算金句 + 三问表与 CTA。句子级配图约每 4 秒一换，避免长时间对着同一画面。"
    )

    with open(pkg_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    for key, script in (("ai", ai_script), ("finance", fin_script)):
        total = sum(r["wc"] for r in script)
        print(f"{key}: {len(script)} 句, {total} 词, 首句 {script[0]['t']}, 末句 {script[-1]['t']}")
        # 词数密度校验：每句词数应大致匹配其时长（约 2.4 词/秒）
        bad = []
        for r in script:
            a, b = r["t"].split("-")
            dur = (int(b.split(":")[0]) * 60 + int(b.split(":")[1])) - (int(a.split(":")[0]) * 60 + int(a.split(":")[1]))
            if dur and r["wc"] < dur * 1.4:
                bad.append((r["t"], r["wc"], dur))
        print(f"  词数偏少的句子：{len(bad)}")
        for t, w, d in bad[:6]:
            print(f"    {t} ({d}s) 仅 {w} 词")


if __name__ == "__main__":
    main()
