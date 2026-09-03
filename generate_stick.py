# -*- coding: utf-8 -*-
"""金融频道 · 火柴人故事版渲染器

    python3 generate_stick.py [输出路径]

复用 generate_pov.py 的 CSS 与「带底色富文本复制」JS，不重写一份。
与 generate_pov.py 输出的是两套完全不同的成片包，不要互相套用。

先跑：python3 verify_stick.py   （改完任何一镜都必须跑）
再跑：python3 generate_stick.py
"""
import datetime
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "_build"))

import fin_stick                    # noqa: E402
from generate_pov import CSS, JS, esc, pbox, workflow_block  # noqa: E402

EXTRA_CSS = """
.lockgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:12px}
.lock{border:1px solid var(--line);border-radius:12px;padding:14px;background:var(--card)}
.lock h4{margin:0 0 4px;font-size:14px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.lock .cn{color:var(--dim);font-size:12px;margin-bottom:8px}
.tag{font-size:11px;padding:1px 7px;border-radius:5px;background:#1e2534;
border:1px solid var(--line);color:var(--mut);font-weight:600}
.tag.you{color:var(--ok);border-color:rgba(94,230,168,.3)}
.tag.maya{color:#f0a94b;border-color:rgba(240,169,75,.3)}
.tag.devon{color:#5ab8e8;border-color:rgba(90,184,232,.3)}
.tag.priya{color:#c9a0ff;border-color:rgba(201,160,255,.3)}
.an{display:grid;grid-template-columns:150px 1fr;gap:6px 14px;font-size:13px}
.an dt{color:var(--dim);font-weight:600}
.an dd{margin:0;color:var(--mut);line-height:1.65}
.sh .pr{max-width:400px}
.sh .pr div{max-height:150px}
.script{background:#0e1119;border:1px solid var(--line);border-radius:9px;padding:14px 16px;
font:13.5px/1.85 ui-monospace,Menlo,monospace;color:#cdd6e6;white-space:pre-wrap}
.script b{color:var(--ok);font-weight:600}
.neg{font:12px/1.7 ui-monospace,Menlo,monospace;color:#b9c4d8}
"""


def analysis_block(rows):
    return '<dl class="an">' + "".join(
        f"<dt>{esc(k)}</dt><dd>{esc(v)}</dd>" for k, v in rows) + "</dl>"


def locks_block(p):
    """世界锁：画风 + 14 个环境 + 4 个角色 + 负面词。改这里 = 全片 88 镜同步改。"""
    out = ['<div class="hint">下面这些是「锁」。每一条图片提示词都逐字引用了它们，'
           '所以你在生图工具里看到的画面才会跨镜头保持一致。'
           '改形象 / 改配色只改这里，88 条提示词同步生效。</div>']
    out.append(pbox("画风锁 · STYLE 1（每一条图片提示词的第 1 句，逐字引用）",
                    p["style_lock"], "lk-style"))

    out.append('<div class="sec" style="font-size:15px">角色形象锁（4 个）</div>')
    out.append('<div class="lockgrid">')
    for key in ("you", "maya", "devon", "priya"):
        out.append(f'''<div class="lock">
          <h4>{esc(p["char_cn"][key])}<span class="tag {key}">{key}</span></h4>
          <div class="cn">出场 {sum(1 for s in p["shots"] if key in s["who"])} 镜</div>
          {pbox("形象锁 · 复制后垫图用", p["char_lock"][key], f"lk-{key}")}
        </div>''')
    out.append("</div>")

    out.append('<div class="sec" style="font-size:15px">环境锁（14 个）</div>')
    out.append('<div class="lockgrid">')
    for key, txt in p["env_lock"].items():
        n = sum(1 for s in p["shots"] if s["env"] == key)
        out.append(f'''<div class="lock">
          <h4>{esc(p["env_cn"][key])}<span class="tag">{key}</span></h4>
          <div class="cn">用到 {n} 镜</div>
          {pbox("环境锁", txt, f"lk-{key}")}
        </div>''')
    out.append("</div>")

    out.append(pbox("通用负面词 · 所有生图工具共用（Midjourney 用 --no，即梦 / SD 贴进负面框）",
                    p["negative"], "lk-neg"))
    return "\n".join(out)


def shots_block(shots):
    rows = ""
    for s in shots:
        cls = " hook" if s["sec"] == 1 else ""
        who_tags = "".join(f'<span class="tag {w}">{w}</span>' for w in s["who"])
        rows += f'''<tr class="{cls.strip()}">
          <td class="id">{esc(s["id"])}{'<span class="hooktag">开头</span>' if s["sec"] == 1 else ''}</td>
          <td class="win">{esc(s["window"])}</td>
          <td class="en">{esc(s["en"])}<div class="zh">{esc(s["zh"])}</div></td>
          <td class="vi">{esc(s["env_cn"])}<div style="margin:5px 0">{who_tags}</div>
            <div style="color:#5b6880">{esc(s["dur"])}s · {s["wc"]} 词</div></td>
          <td class="pr"><div>{esc(s["img_en"])}</div>
            <button class="mini" data-text="{esc(s['img_en'])}" data-label="图片提示词 · {esc(s['id'])}">复制图片</button></td>
          <td class="pr"><div>{esc(s["vid_en"])}</div>
            <button class="mini" data-text="{esc(s['vid_en'])}" data-label="动画提示词 · {esc(s['id'])}">复制动画</button></td>
        </tr>'''
    return f'''<table class="sh" id="shots-stick"><thead><tr>
      <th>镜号</th><th>时间</th><th>口播 英文 / 中文</th><th>场景 / 角色</th>
      <th>图片提示词（{sum(1 for _ in shots)} 条，逐条可复制）</th>
      <th>动画提示词（6 秒 / 条）</th></tr></thead><tbody>{rows}</tbody></table>'''


def script_block(shots):
    """纯口播全文，直接丢给 TTS。"""
    return "".join(f"<b>{esc(s['id'])}</b>  {esc(s['en'])}\n" for s in shots)


def titles_block(titles):
    rows = ""
    for i, t in enumerate(titles, 1):
        on = " on" if t.get("pick") else ""
        rows += f'''<div class="t{on}"><div class="badge">{i}</div><div style="flex:1">
          <div class="en">{esc(t["title"])}{'<span class="pill pick">推荐</span>' if t.get('pick') else ''}</div>
          <div class="cn">{esc(t["cn"])}</div>
          <div class="meta"><b>公式：</b>{esc(t["formula"])}<br><b>为什么：</b>{esc(t["why"])}</div>
        </div>
        <button class="mini" data-text="{esc(t['title'])}" data-label="标题">复制</button></div>'''
    return rows


def thumbs_block(thumbs):
    out = '<div class="thumbs">'
    for th in thumbs:
        ov = "".join(f"<span>{esc(x)}</span>" for x in th.get("overlay", []))
        out += f'''<div class="th">
          <h4>{esc(th["name"])}{'<span class="pill pick">首选</span>' if th['id'] == 1 else ''}</h4>
          <div class="concept">{esc(th["concept"])}</div>
          <div class="ov">{ov}</div>
          <div class="why"><b>为什么能点：</b>{esc(th["why"])}</div>
          {pbox("缩略图生图提示词", th["prompt_en"], f"thm-{th['id']}")}
        </div>'''
    return out + "</div>"


def render(p, out_path):
    today = p["built_at"]
    hook_n = sum(1 for s in p["shots"] if s["sec"] == 1)
    html = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>火柴人故事版成片包 · {today}</title><style>{CSS}{EXTRA_CSS}</style></head><body>
<div class="wrap">
  <h1>金融频道 · 火柴人故事版成片包 · {today}</h1>
  <div class="lead">{esc(p["channel_label"])}　·　{p["shot_count"]} 镜 / {p["word_count"]} 词 / {p["duration"]}</div>
  <div class="date">画风：{esc(p["style"])}　·　节奏：{esc(p["beat_timing"])}　·　开头 {hook_n} 镜（已高亮）
  　·　按 STICK FIGURE ANIMATION PIPELINE V2 BY PROVENTUBE 的六个状态产出</div>

  <section class="pkg" style="--c1:#f0a94b;--c2:#7fd1c1">
    <div class="pkg-head"><div>
      <div class="pkg-label">🎬 {esc(p["topic"])}</div>
      <div class="pkg-topic" style="font-size:18px">{esc(p["topic_cn"])}</div>
    </div>
    <div style="text-align:right;color:var(--mut);font-size:13px">
      <div>{p["shot_count"]} 镜　·　{p["word_count"]} 词　·　{p["duration"]}</div>
      <div style="color:var(--dim);font-size:12px;margin-top:3px">同一条视频的 5 个标题 / 3 张封面</div>
    </div></div>

    <div class="framework"><b>本片框架：</b>{esc(p["framework_one_liner"])}</div>

    <div class="sec"><span class="n">1</span>剧本分析（STATE 1）</div>
    {analysis_block(p["analysis"])}

    <div class="sec"><span class="n">2</span>标题（5 选 1 · 同一条视频的 5 个封面文案）</div>
    <div class="subhint">5 个标题讲的都是同一条视频。选 1 个发，剩下的进 A/B 测试。</div>
    {titles_block(p["titles"])}

    <div class="sec"><span class="n">3</span>缩略图（3 选 1 · 同一条视频的 3 种封面构图）</div>
    <div class="subhint">3 张都是这条视频的封面，封面上的文字后期加，提示词里一律不烧字。</div>
    {thumbs_block(p["thumbs"])}
  </section>

  <section class="pkg" style="--c1:#22d3ee;--c2:#7c5cff">
    <div class="pkg-head"><div>
      <div class="pkg-label">🔒 世界锁</div>
      <div class="pkg-topic" style="font-size:18px">画风 · 角色 · 环境 · 负面词</div>
    </div></div>
    {locks_block(p)}
  </section>

  <section class="pkg" style="--c1:#5ee6a8;--c2:#f0a94b">
    <div class="pkg-head"><div>
      <div class="pkg-label">🎞️ 分镜脚本</div>
      <div class="pkg-topic" style="font-size:18px">{p["shot_count"]} 镜 · 逐镜口播 + 详细图片提示词 + 6 秒动画提示词</div>
    </div></div>
    <div class="hint">按镜号顺序生图。绿色左边框的前 {hook_n} 镜是开头。
      每条图片提示词都是「画风锁 + 环境锁 + 角色锁 + 这一镜的动作 + 机位 + 光线情绪 + 一致性尾」的完整长版，
      直接整段复制喂给生图工具，不需要再拼接任何东西。</div>
    <button class="mini tblcp" data-target="shots-stick" data-label="分镜表"
      style="margin-bottom:9px">📋 复制整张分镜表（带样式，粘进 WPS / 飞书 / 微信都带暗色底）</button>
    {shots_block(p["shots"])}

    <details><summary>口播全文（{p["word_count"]} 词 · 直接丢给 TTS）</summary>
      <button class="mini" data-text="{esc(' '.join(s['en'] for s in p['shots']))}"
        data-label="口播全文" style="margin:8px 0">复制口播全文</button>
      <div class="script">{script_block(p["shots"])}</div>
    </details>

    <details><summary>为什么选这个选题（5 条理由 + 一句话结论）</summary>
      <div class="card" style="margin-top:9px">
        <div style="color:var(--tx);font-weight:600;margin-bottom:8px">{esc(p["pick"]["one_liner"])}</div>
        {"".join(f'<div style="margin-bottom:9px"><b style="color:var(--c1)">{esc(w["h"])}</b><div style="color:var(--mut);font-size:13px">{esc(w["b"])}</div></div>' for w in p["pick"]["why"])}
        <div style="margin-top:11px;color:var(--mut);font-size:13px">
          <div><b>需求：</b>{esc(p["pick"]["demand"])}</div>
          <div style="margin-top:5px"><b>市场空白：</b>{esc(p["pick"]["gap"])}</div>
          <div style="margin-top:5px"><b>风险：</b>{esc(p["pick"]["risk"])}</div>
          <div style="margin-top:7px;color:var(--ok)"><b>结论：</b>{esc(p["pick"]["verdict"])}</div>
        </div>
      </div>
    </details>
  </section>

  {workflow_block([p])}
</div>
<div class="toast" id="toast"></div>
<script>{JS}</script>
</body></html>'''
    with io.open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    return out_path


def main():
    p = fin_stick.build()
    # 渲染需要单独拿出画风锁（它不随镜头走，是世界层）
    sys.path.insert(0, os.path.join(HERE, "_build"))
    from stick_world import STYLE_LOCK
    p["style_lock"] = STYLE_LOCK
    p["duration"] = p["duration"]
    p["shot_count"] = p["shot_count"]
    p["word_count"] = p["word_count"]

    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        HERE, "output", f"stick-fin-{datetime.date.today().isoformat()}.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    render(p, out)

    jp = os.path.join(HERE, "remotion", "src", "stick-shots.json")
    with io.open(jp, "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=1)

    print(f'  {p["channel_key"]:14s} {p["shot_count"]:3d} 镜 / {p["word_count"]:4d} 词 / {p["duration"]}')
    print("HTML :", out)
    print("JSON :", jp)
    print("bytes:", os.path.getsize(out))


if __name__ == "__main__":
    main()
