#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_report.py — 每日/每月「选题推荐报告 + 置顶成片包」渲染器
用法:
    python3 generate_report.py <input_json> <output_html>

每份 panel 含 5 个板块（选题推荐）：
  1 · YouTube 搜索建议信号  2 · 题材热度走向  3 · 评论区痛点→原创角度
  4 · 选题筛选表（做/不做）  5 · 起步内容比例 + 合规红线

若输入 JSON 无 "packages" 键，则自动加载同目录 packages.json，
把两个完整成片包渲染在报告置顶上方。

纯标准库实现，无第三方依赖。
"""
import json
import sys
import os
import html
import datetime

PANEL_ACCENT = {
    "ai": ("#7c5cff", "#22d3ee"),
    "finance": ("#f5b301", "#34d399"),
}


def esc(s):
    return html.escape(str(s if s is not None else ""))


def tag(s):
    t = esc(s)
    cls = "ever" if "常青" in t or "Ever" in t else ("hot" if ("升温" in t or "Rising" in t or "Hot" in t) else "")
    return f'<span class="tag {cls}">{t}</span>'


def signal_card(s):
    topic = esc(s.get("topic", ""))
    tags = "".join(tag(x) for x in (s.get("tags") or []))
    items = s.get("items") or []
    lis = "".join(f"<li>{esc(i)}</li>" for i in items)
    insight = esc(s.get("insight", ""))
    return f"""
      <div class="card">
        <h3>{topic}</h3>
        <div class="tags">{tags}</div>
        <ul>{lis}</ul>
        <div class="src">洞察：{insight}</div>
      </div>"""


def trend_table(rows):
    body = ""
    for r in rows:
        ttype = esc(r.get("type", ""))
        tcls = "hot" if ("Rising" in ttype or "升温" in ttype or "Breakout" in ttype) else ("ever" if "常青" in ttype else "")
        body += f"""<tr>
          <td><b>{esc(r.get('topic',''))}</b></td>
          <td>{esc(r.get('signal',''))}</td>
          <td><span class="tag {tcls}">{ttype}</span></td>
          <td>{esc(r.get('note',''))}</td>
        </tr>"""
    return f"""
      <table>
        <tr><th>题材</th><th>信号（真实数据 / 下拉词）</th><th>类型</th><th>是否饱和 / 注意</th></tr>
        {body}
      </table>"""


def painpoints_block(p):
    headline = esc(p.get("headline", ""))
    points = "".join(f"<li>{esc(x)}</li>" for x in (p.get("points") or []))
    angles = ""
    for a in (p.get("angles") or []):
        problem = esc(a.get("problem", ""))
        idea = esc(a.get("idea", ""))
        title = esc(a.get("title", ""))
        angles += f"""<li>
          <b>原问题：</b>{problem}<br>
          <b>原创角度：</b>{idea}<br>
          <b>建议标题：</b><span class="pill">{title}</span>
        </li>"""
    return f"""
      <div class="panel">
        <p class="big">最突出的跨主题痛点：<b>{headline}</b></p>
        <ul>{points}</ul>
        <p><b>原创角度转化：</b></p>
        <ul class="angles">{angles}</ul>
      </div>"""


def screening_table(rows):
    body = ""
    for r in rows:
        hot = esc(r.get("hot", ""))
        pain = esc(r.get("pain", ""))
        orig = esc(r.get("original", ""))
        verdict = esc(r.get("verdict", ""))
        vcls = "do" if verdict.startswith("做") and "不" not in verdict else ("dont" if "不" in verdict else "warn")
        def cell(v):
            c = "yes" if v == "是" else ("no" if v == "否" else "")
            return f'<td class="ctr {c}">{v}</td>'
        body += f"""<tr>
          <td>{esc(r.get('topic',''))}</td>
          <td class="src">{esc(r.get('source',''))}</td>
          {cell(hot)}{cell(pain)}{cell(orig)}
          <td class="ctr {vcls}">{verdict}</td>
        </tr>"""
    return f"""
      <table>
        <tr>
          <th style="width:24%">选题</th><th style="width:14%">来源</th>
          <th class="ctr" style="width:8%">近30天<br>有热度</th>
          <th class="ctr" style="width:8%">有具体<br>痛点</th>
          <th class="ctr" style="width:9%">能提供<br>原创解释/数据</th>
          <th class="ctr" style="width:10%">做不做</th>
        </tr>
        {body}
      </table>
      <div class="src" style="margin-top:8px">评分维度：① 近 30 天有热度 ② 有具体痛点 ③ 能提供原创解释/数据。满足 ≥3 项才做。</div>"""


def ratio_block(r):
    ratios = "".join(
        f"<li><b>{esc(x.get('pct',''))} {esc(x.get('name',''))}</b>：{esc(x.get('items',''))}</li>"
        for x in (r.get("ratios") or [])
    )
    comp = "".join(f"<li>{esc(x)}</li>" for x in (r.get("compliance") or []))
    return f"""
      <div class="panel">
        <p class="big">建议起步比例：</p>
        <ul>{ratios}</ul>
      </div>
      <div class="note"><b>发布前合规红线（必须执行）：</b>
        <ol style="margin:6px 0 0;padding-left:20px">{comp}</ol>
      </div>"""


def section(num, title):
    return f'<h2><span class="num">{num}</span> · {esc(title)}</h2>'


def panel_block(panel):
    key = panel.get("key", "ai")
    c1, c2 = PANEL_ACCENT.get(key, ("#7c5cff", "#22d3ee"))
    label = esc(panel.get("label", ""))
    handle = esc(panel.get("handle", ""))
    audience = esc(panel.get("audience", ""))

    signals = panel.get("signals") or []
    trends = panel.get("trends") or []
    pain = panel.get("painpoints") or {}
    screen = panel.get("screening") or []
    ratio = panel.get("ratio") or {}

    signals_html = "".join(signal_card(s) for s in signals) if signals else '<div class="empty">暂无信号</div>'
    trends_html = trend_table(trends) if trends else ""
    pain_html = painpoints_block(pain) if pain else ""
    screen_html = screening_table(screen) if screen else ""
    ratio_html = ratio_block(ratio) if ratio else ""

    return f"""
    <section class="panel-sec" style="--c1:{c1};--c2:{c2}">
      <div class="sec-head">
        <div class="sec-label">{label}</div>
        <div class="sec-handle">{handle} · 受众：{audience}</div>
      </div>

      {section(1, 'YouTube 搜索建议信号（真实下拉词）')}
      <div class="grid">{signals_html}</div>

      {section(2, '题材热度走向判断')}
      {trends_html}

      {section(3, '评论区痛点 → 原创角度')}
      {pain_html}

      {section(4, '选题筛选表（做 / 不做）')}
      {screen_html}

      {section(5, '起步内容比例 + 合规红线')}
      {ratio_html}
    </section>"""


def script_table(beats, ns="pkg"):
    rows = ""
    for b in beats:
        en = b.get("en", "")
        wc = b.get("wc")
        if wc is None:
            wc = len(en.split())
        rows += f"""<tr>
          <td class="tm">{esc(b.get('t',''))}</td>
          <td class="ctr wc">{esc(str(wc))}</td>
          <td class="en">{esc(en)}</td>
          <td class="zh">{esc(b.get('zh',''))}</td>
          <td class="viz">{esc(b.get('viz',''))}</td>
          <td class="ctr demo-cell">{demo_summary(b.get('demo'), ns)}</td>
          <td class="img-en">{esc(b.get('img_en',''))}</td>
          <td class="img-zh">{esc(b.get('img_zh',''))}</td>
        </tr>"""
    return f"""<div class="script-wrap"><table class="script">
      <colgroup>
        <col style="width:86px"><col style="width:46px"><col style="width:300px">
        <col style="width:284px"><col style="width:132px"><col style="width:74px"><col style="width:300px"><col style="width:268px">
      </colgroup>
      <tr><th>时间段</th><th class="ctr">词数</th><th>英文口播(左)</th><th>中文翻译(右)</th><th>分镜/情绪</th><th class="ctr">实操卡</th><th>图片提示词·英</th><th>图片提示词·中</th></tr>
      {rows}
    </table></div>"""


def demo_summary(demo, ns="pkg"):
    """句子级表格里只放一个「实操卡 N」编号徽标，完整内容在下方实操执行卡区块。"""
    if not demo or not demo.get("need"):
        return '<span class="demo-no">—</span>'
    card = demo.get("card")
    if card is None:
        return '<span class="demo-badge">实操</span>'
    return f'<a class="demo-badge" href="#{esc(ns)}-demo-card-{esc(card)}" title="跳到实操卡 {esc(card)}">实操卡 {esc(card)}</a>'


def operator_block(op):
    if not op:
        return ""
    curve = esc(op.get("retention_curve", ""))
    emotions = "".join(f"<li>{esc(x)}</li>" for x in (op.get("emotion_triggers") or []))
    anchor = esc(op.get("demand_anchor", ""))
    checklist = "".join(f"<li>{esc(x)}</li>" for x in (op.get("operator_checklist") or []))
    return f'''<div class="operator-grid">
      <div class="operator-card"><h4>Retention 曲线</h4><p>{curve}</p></div>
      <div class="operator-card"><h4>情绪触发点</h4><ul>{emotions}</ul></div>
      <div class="operator-card"><h4>需求锚定</h4><p>{anchor}</p></div>
      <div class="operator-card"><h4>编导执行清单</h4><ul>{checklist}</ul></div>
    </div>'''


def legacy_demo_cards(beats):
    """兼容旧格式：若 script 里仍是 label/screen/steps/proof 结构，就地转成实操卡。"""
    cards = []
    idx = 0
    for b in beats:
        d = b.get("demo") or {}
        if not d.get("need"):
            continue
        idx += 1
        cards.append({
            "id": idx,
            "title": d.get("label", "必须实操"),
            "window": b.get("t", ""),
            "software": d.get("screen", ""),
            "shots": "（旧格式）全屏屏幕录制，鼠标动作放慢。",
            "steps": [{"do": s, "see": ""} for s in (d.get("steps") or [])],
            "verify": d.get("proof", ""),
            "pitfalls": [],
            "audio": "",
        })
    return cards


def demo_plan_block(cards, ns="pkg"):
    """渲染完整实操执行卡：镜头语言 + 逐步操作（动作→看到什么）+ 验收 + 常见坑 + 配音对齐。"""
    if not cards:
        return '<div class="empty">本期无强制实操段落。</div>'
    rows = ""
    for c in cards:
        cid = esc(c.get("id", ""))
        title = esc(c.get("title", ""))
        window = esc(c.get("window", ""))
        software = esc(c.get("software", ""))
        shots = esc(c.get("shots", ""))
        verify = esc(c.get("verify", ""))
        audio = esc(c.get("audio", ""))

        steps_html = ""
        for i, s in enumerate(c.get("steps") or [], start=1):
            do_txt = esc(s.get("do", ""))
            see_txt = esc(s.get("see", ""))
            steps_html += f'''<tr>
              <td class="ctr step-n">{i}</td>
              <td class="step-do"><b>动作：</b>{do_txt}</td>
              <td class="step-see"><b>屏幕上会看到：</b>{see_txt}</td>
            </tr>'''

        pitfalls = "".join(f"<li>{esc(x)}</li>" for x in (c.get("pitfalls") or []))

        rows += f'''<div class="demo-card" id="{esc(ns)}-demo-card-{cid}">
          <div class="demo-card-head">
            <span class="demo-card-no">实操卡 {cid}</span>
            <span class="demo-card-title">{title}</span>
            <span class="demo-card-window">⏱ {window}</span>
          </div>
          <div class="demo-card-meta"><b>用到：</b>{software}</div>
          <div class="demo-card-shots"><b>镜头怎么拍：</b>{shots}</div>
          <table class="demo-steps">
            <tr><th class="ctr" style="width:34px">#</th><th style="width:44%">操作动作（你做什么）</th><th>画面里会出现什么（用来验收）</th></tr>
            {steps_html}
          </table>
          <div class="demo-verify"><b>✅ 验收标准：</b>{verify}</div>
          {f'<div class="demo-pitfalls"><b>⚠️ 常见坑：</b><ul>{pitfalls}</ul></div>' if pitfalls else ''}
          {f'<div class="demo-audio"><b>🎙 配音对齐：</b>{audio}</div>' if audio else ''}
          {video_prompts_block(c.get("video_prompts"), c.get("video_neg"))}
        </div>'''
    return f'<div class="demo-card-list">{rows}</div>'


def video_prompts_block(shots, neg_map):
    """镜头级视频提示词。mode=ai-video 可直接喂视频模型；mode=screen 建议实拍录屏 + AE。"""
    if not shots:
        return ""
    neg_map = neg_map or {}
    rows = ""
    for s in shots:
        mode = s.get("mode", "ai-video")
        if mode == "ai-video":
            badge = '<span class="vp-mode vp-ai">AI 视频生成</span>'
            tip = "可直接喂 Runway Gen-3 / Kling 1.6 / Veo 3"
        else:
            badge = '<span class="vp-mode vp-screen">录屏 + AE</span>'
            tip = "建议自己录屏做，AI 提示词仅作氛围 B-roll 参考（模型生成可读 UI 文字会糊）"
        rows += f'''<div class="vp">
          <div class="vp-head">
            <b>{esc(s.get("shot", ""))}</b>
            <span class="vp-dur">{esc(s.get("dur", ""))}</span>
            {badge}
          </div>
          <div class="vp-tip">{tip}</div>
          <div class="vp-en">{esc(s.get("en", ""))}</div>
          <div class="vp-zh">{esc(s.get("zh", ""))}</div>
          <div class="vp-neg"><b>负面提示词：</b>{esc(neg_map.get(mode, ""))}</div>
        </div>'''
    return f'''<div class="vp-block">
      <div class="vp-block-head">镜头级视频提示词（{len(shots)} 个镜头）</div>
      {rows}
    </div>'''


def reference_block(refs):
    if not refs:
        return ""
    rows = ""
    for r in refs:
        rows += f'''<li><a href="{esc(r.get("url", ""))}" target="_blank" rel="noopener">{esc(r.get("title", r.get("label", "参考链接")))}</a>
          <span class="ref-use">借鉴：{esc(r.get("use_for", ""))}</span>
          <span class="ref-no-copy">边界：{esc(r.get("do_not_copy", "只借鉴结构，不复制内容"))}</span>
        </li>'''
    return f'''<div class="reference-block"><h3>可借鉴的实操视频 / 工具链接（只借鉴镜头结构，不抄台词）</h3><ul>{rows}</ul></div>'''


def package_block(pkg):
    key = pkg.get("channel_key", "ai")
    c1, c2 = PANEL_ACCENT.get(key, ("#7c5cff", "#22d3ee"))
    label = esc(pkg.get("channel_label", ""))
    topic = esc(pkg.get("topic", ""))
    topic_cn = esc(pkg.get("topic_cn", ""))
    host = esc(pkg.get("host", ""))
    host_note = esc(pkg.get("host_note", ""))
    decision = esc(pkg.get("decision", ""))
    character = esc(pkg.get("character_card", ""))
    hook = esc(pkg.get("hook", ""))
    hook_zh = esc(pkg.get("hook_zh", ""))
    titles = "".join(f"<li>{esc(t)}</li>" for t in (pkg.get("titles") or []))
    # 三个 Hook 备选（按类型）
    hook_options_html = ""
    for h in (pkg.get("hook_options") or []):
        htype = esc(h.get("type", ""))
        hlabel = esc(h.get("label", ""))
        hen = esc(h.get("en", ""))
        hzh = esc(h.get("zh", ""))
        hook_options_html += f"""<div class="hook-opt">
          <div class="hook-type">{htype}</div>
          <div class="hook-label">{hlabel}</div>
          <div class="hook-en">{hen}</div>
          <div class="hook-zh">{hzh}</div>
        </div>"""
    script_html = script_table(pkg.get("script") or [], ns=key)
    arc = esc(pkg.get("emotion_arc", ""))
    thumbs = ""
    for th in (pkg.get("thumbs") or []):
        thumbs += f"""<div class="thumb">
          <div class="ver">{esc(th.get('ver',''))} 版</div>
          <div>{esc(th.get('desc',''))}</div>
          <div class="img-en" style="margin-top:6px">{esc(th.get('img_en',''))}</div>
          <div class="img-zh">{esc(th.get('img_zh',''))}</div>
        </div>"""
    desc = esc(pkg.get("description", ""))
    tags = "  ".join(f"<code>{esc(t)}</code>" for t in (pkg.get("tags") or []))
    chapters = "".join(f"<li>{esc(c)}</li>" for c in (pkg.get("chapters") or []))
    source_links = "  ".join(f'<a href="{esc(x.get("url", ""))}" target="_blank" rel="noopener">{esc(x.get("label", "来源"))}</a>' for x in (pkg.get("source_links") or []))
    op_html = operator_block(pkg.get("operator_breakdown") or {})
    demo_plan_html = demo_plan_block(pkg.get("demo_cards") or legacy_demo_cards(pkg.get("script") or []), ns=key)
    refs_html = reference_block(pkg.get("reference_videos") or [])
    word_count = pkg.get("word_count")
    sentence_count = pkg.get("sentence_count") or len(pkg.get("script") or [])
    if word_count is None:
        word_count = sum(len((b.get("en") or "").split()) for b in (pkg.get("script") or []))
    dur = esc(pkg.get("duration", ""))
    stats_html = (f'<div class="pkg-stats">'
                  f'<span class="stat"><b>{esc(sentence_count)}</b> 句</span>'
                  f'<span class="stat"><b>{esc(word_count)}</b> 词</span>'
                  f'<span class="stat">时长 <b>{dur}</b></span>'
                  f'<span class="stat">图片提示词 <b>{esc(sentence_count)}</b> 条（每句一图）</span>'
                  f'</div>')
    return f"""
    <section class="pkg" id="pkg-{key}" style="--c1:{c1};--c2:{c2}">
      <div class="pkg-head">
        <div>
          <div class="pkg-label">🎬 完整成片包 · {label}</div>
          <div class="pkg-topic"><span class="en">{topic}</span> ／ {topic_cn}</div>
        </div>
        <button type="button" class="pkg-copy-btn" data-pkg-id="pkg-data-{key}" onclick="copyPkg(this)">
          <span class="pkg-copy-icon">📋</span><span class="pkg-copy-label">复制整包 JSON</span>
        </button>
      </div>
      <div class="pkg-sub">Host：{host}</div>
      {f'<div class="host-note">⚠️ {host_note}</div>' if host_note else ''}
      {f'<div class="pkg-sec"><h3>虚拟主人公 / 画面统一规范</h3><div>{character}</div></div>' if character else ''}
      <div class="pkg-sec"><h3>选题决策</h3><div>{decision}</div></div>
      {f'<div class="pkg-sec"><h3>运营拆解：为什么观众会继续看</h3>{op_html}</div>' if op_html else ''}
      <div class="pkg-sec"><h3>黄金前 15 秒 Hook（推荐 / 主用）</h3>
        <div class="hook-en">{hook}</div>
        {f'<div class="hook-zh" style="margin-top:6px;color:var(--mut)">{hook_zh}</div>' if hook_zh else ''}
        {f'<h4 style="margin:14px 0 8px;color:var(--mut);font-size:13px;font-weight:600">三个 Hook 备选（按类型，可任选其一替换主用）</h4><div class="hook-options">{hook_options_html}</div>' if hook_options_html else ''}
      </div>
      <div class="pkg-sec"><h3>两个炸裂标题</h3><ul class="titles">{titles}</ul></div>
      <div class="pkg-sec"><h3>分镜脚本表（句子级 · 一句一图 · 英中分栏）</h3>{stats_html}{script_html}</div>
      <div class="pkg-sec"><h3>实操执行卡（镜头语言 + 逐步动作 + 验收 + 常见坑）</h3>{demo_plan_html}</div>
      <div class="pkg-sec"><h3>情绪弧（Hook→Aha→Payoff）</h3><div>{arc}</div></div>
      {refs_html}
      <div class="pkg-sec"><h3>YouTube 封面缩略图（A/B 两版·英中双语）</h3><div class="thumbs">{thumbs}</div></div>
      <div class="pkg-sec"><h3>自动三件套</h3>
        <ul class="triple">
          <li><b>视频简介：</b>{desc}</li>
          <li><b>标签：</b>{tags}</li>
          <li><b>章节：</b><ul>{chapters}</ul></li>
          {f'<li><b>一手来源：</b><span class="source-links">{source_links}</span></li>' if source_links else ''}
        </ul>
      </div>
    </section>"""


def render(spec, base_dir=None):
    title = esc(spec.get("title", "热点看台"))
    date = esc(spec.get("date", datetime.date.today().isoformat()))
    rtype = spec.get("type", "daily")
    rtype_label = "每日选题推荐" if rtype == "daily" else "月度爆款选题盘点"
    subtitle = esc(spec.get("subtitle", ""))
    panels = spec.get("panels", [])
    panels_html = "\n".join(panel_block(p) for p in panels)

    # 置顶成片包：优先取 spec.packages，否则自动加载同目录 packages.json
    packages = spec.get("packages") or []
    if not packages and base_dir:
        ppath = os.path.join(base_dir, "packages.json")
        if os.path.exists(ppath):
            try:
                with open(ppath, encoding="utf-8") as f:
                    packages = json.load(f).get("packages", [])
            except Exception:
                packages = []
    packages_html = "\n".join(package_block(p) for p in packages) if packages else ""

    # 整包 JSON 注入：每个包一份 <script type="application/json">，复制按钮读它的 textContent
    pkg_data_blocks = ""
    for p in packages:
        k = p.get("channel_key", "")
        if not k:
            continue
        json_str = json.dumps(p, ensure_ascii=False, indent=2)
        # 防 </script> 提前结束标签
        json_str = json_str.replace("</", "<\\/")
        pkg_data_blocks += f'<script type="application/json" id="pkg-data-{k}">\n{json_str}\n</script>\n'

    generated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · {date}</title>
<style>
  :root {{
    --bg:#0f1419; --panel:#1a2230; --panel2:#141c28; --line:#2a3548;
    --txt:#e6edf3; --mut:#9aa7b8; --acc:#4da3ff; --green:#3fb950; --red:#f85149;
    --amber:#d29922; --chip:#22304a;
  }}
  * {{ box-sizing:border-box; }}
  body {{
    margin:0; background:var(--bg); color:var(--txt);
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;
    line-height:1.6; padding:32px 20px 64px;
  }}
  .wrap {{ max-width:1040px; margin:0 auto; }}
  header.hero {{
    background:linear-gradient(135deg,#7c5cff 0%,#22d3ee 100%);
    border-radius:16px; padding:24px 26px; color:#0b0d12; margin-bottom:8px;
  }}
  .hero h1 {{ margin:0 0 6px; font-size:25px; letter-spacing:.5px; }}
  .hero .meta {{ font-size:13px; opacity:.82; }}
  .hero .sub {{ margin-top:8px; font-size:13.5px; font-weight:600; }}
  h2 {{ font-size:18px; margin:30px 0 12px; padding-left:11px; border-left:4px solid var(--c1, var(--acc)); }}
  h2 .num {{
    display:inline-block; min-width:22px; height:22px; line-height:22px; text-align:center;
    background:var(--c1,var(--acc)); color:#0b0d12; border-radius:6px; font-size:13px; font-weight:800; margin-right:8px;
  }}
  .sub {{ color:var(--mut); font-size:13px; margin-bottom:6px; }}
  .panel-sec {{
    background:var(--panel); border:1px solid var(--line); border-radius:14px;
    padding:8px 20px 22px; margin:18px 0; border-top:4px solid var(--c1, var(--acc));
  }}
  .sec-head {{ display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; margin:14px 0 4px; }}
  .sec-label {{ font-size:20px; font-weight:800; background:linear-gradient(90deg,var(--c1),var(--c2)); -webkit-background-clip:text; background-clip:text; color:transparent; }}
  .sec-handle {{ font-size:12.5px; color:var(--mut); margin-top:4px; }}
  .grid {{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; }}
  @media(max-width:820px){{ .grid {{ grid-template-columns:1fr; }} }}
  .card {{ background:var(--panel2); border:1px solid var(--line); border-radius:10px; padding:13px 15px; }}
  .card h3 {{ margin:0 0 8px; font-size:15px; color:var(--acc); }}
  .panel-sec .card h3 {{ color:var(--c1); }}
  .tags {{ margin:2px 0 6px; }}
  .tag {{ display:inline-block; font-size:11px; padding:2px 8px; border-radius:20px; background:var(--chip); color:var(--mut); margin:2px 4px 2px 0; }}
  .tag.hot {{ background:#3a2230; color:#ff9aa2; }}
  .tag.ever {{ background:#1f3326; color:#7ee0a0; }}
  ul {{ margin:8px 0 0; padding-left:18px; }}
  li {{ margin:4px 0; font-size:13.5px; }}
  .src {{ color:var(--mut); font-size:12px; margin-top:8px; }}
  table {{ border-collapse:collapse; width:100%; font-size:13px; margin-top:6px; }}
  th,td {{ border:1px solid var(--line); padding:9px 10px; text-align:left; vertical-align:top; }}
  th {{ background:var(--panel2); color:var(--mut); font-weight:600; }}
  td.ctr {{ text-align:center; }}
  .yes {{ color:var(--green); font-weight:700; }}
  .no {{ color:var(--red); font-weight:700; }}
  .do {{ color:var(--green); font-weight:700; }}
  .dont {{ color:var(--red); font-weight:700; }}
  .warn {{ color:var(--amber); font-weight:700; }}
  .panel {{ background:var(--panel2); border:1px solid var(--line); border-radius:10px; padding:13px 16px; margin:12px 0; }}
  .big {{ font-size:14.5px; }}
  .pill {{ font-weight:700; color:var(--acc); }}
  .panel-sec .pill {{ color:var(--c1); }}
  .angles li {{ margin:8px 0; }}
  .note {{ background:#1f1a10; border:1px solid #4a3c12; border-radius:10px; padding:13px 16px; color:#e6cf9a; font-size:13px; margin:14px 0; }}
  .note ol {{ margin:6px 0 0; }}
  .disc {{ background:var(--panel2); border:1px dashed var(--line); border-radius:10px; padding:14px 16px; font-size:12px; color:var(--mut); margin-top:22px; }}
  .empty {{ color:var(--mut); font-size:14px; padding:18px; text-align:center; }}
  .pkg {{ background:var(--panel); border:1px solid var(--line); border-radius:14px; padding:8px 20px 22px; margin:18px 0; border-top:4px solid var(--c1, var(--acc)); }}
  .pkg-head {{ display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:12px; margin:14px 0 4px; }}
  .pkg-label {{ font-size:19px; font-weight:800; background:linear-gradient(90deg,var(--c1),var(--c2)); -webkit-background-clip:text; background-clip:text; color:transparent; }}
  .pkg-copy-btn {{
    display:inline-flex; align-items:center; gap:6px; padding:7px 13px; border-radius:8px;
    background:var(--panel2); border:1px solid var(--line); color:var(--txt);
    font-size:12.5px; font-weight:600; cursor:pointer; transition:all .15s ease;
    flex-shrink:0;
  }}
  .pkg-copy-btn:hover {{ background:#1c2434; border-color:var(--c1,var(--acc)); color:var(--c1,var(--acc)); }}
  .pkg-copy-btn:active {{ transform:scale(0.97); }}
  .pkg-copy-btn.is-ok {{ background:#152b25; border-color:#28614d; color:#8ee9bd; }}
  .pkg-copy-btn.is-err {{ background:#2a1212; border-color:#7a2222; color:#ff9aa2; }}
  .pkg-topic {{ font-size:14px; color:var(--mut); margin-top:4px; }}
  .pkg-topic .en {{ color:var(--txt); font-weight:700; }}
  .pkg-sub {{ font-size:12.5px; color:var(--mut); }}
  .pkg-sec {{ margin:14px 0 6px; }}
  .pkg-sec h3 {{ font-size:15px; margin:0 0 6px; padding-left:9px; border-left:4px solid var(--c1,var(--acc)); color:var(--txt); }}
  .host-note {{ font-size:12px; color:var(--amber); margin-top:4px; }}
  .hook-options {{ display:grid; grid-template-columns:repeat(3,1fr); gap:10px; margin-top:8px; }}
  @media(max-width:820px){{ .hook-options {{ grid-template-columns:1fr; }} }}
  .hook-opt {{ background:var(--panel2); border:1px solid var(--line); border-radius:10px; padding:10px 12px; }}
  .hook-opt .hook-type {{ font-size:11px; font-weight:800; letter-spacing:.5px; color:var(--c1); text-transform:uppercase; }}
  .hook-opt .hook-label {{ font-size:11.5px; color:var(--mut); margin:3px 0 7px; }}
  .hook-opt .hook-en {{ font-size:13px; font-weight:600; line-height:1.5; color:var(--txt); }}
  .hook-opt .hook-zh {{ font-size:12px; color:var(--mut); margin-top:5px; line-height:1.55; }}
  .titles li {{ font-weight:600; }}
  .script-wrap {{ overflow-x:auto; margin-top:6px; }}
  table.script {{ table-layout:fixed; min-width:1500px; border-collapse:collapse; width:100%; font-size:12.5px; }}
  table.script th, table.script td {{ border:1px solid var(--line); padding:8px 9px; text-align:left; vertical-align:top; }}
  .script-wrap {{ max-height:78vh; overflow-y:auto; }}
  table.script th {{
    background:var(--panel2); color:var(--mut); font-weight:600;
    position:sticky; top:0; z-index:2; box-shadow:inset 0 -1px 0 var(--line);
  }}
  table.script td.en, table.script td.zh {{ line-height:1.5; }}
  table.script td.img-en, table.script td.img-zh {{ color:#9fd0ff; font-size:11.5px; line-height:1.45; }}
  table.script tbody tr:nth-child(even) {{ background:rgba(255,255,255,.022); }}
  table.script tbody tr:hover {{ background:rgba(125,180,255,.07); }}
  table.script tbody tr:target {{ background:rgba(63,185,80,.10); }}
  .thumbs {{ display:grid; grid-template-columns:1fr 1fr; gap:12px; }}
  @media(max-width:820px){{ .thumbs {{ grid-template-columns:1fr; }} }}
  .thumb {{ background:var(--panel2); border:1px solid var(--line); border-radius:10px; padding:12px 14px; }}
  .thumb .ver {{ font-weight:800; color:var(--c1); }}
  .triple li {{ margin:5px 0; }}
  .operator-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:10px; }}
  @media(max-width:820px){{ .operator-grid {{ grid-template-columns:1fr; }} }}
  .operator-card {{ background:var(--panel2); border:1px solid var(--line); border-radius:10px; padding:11px 13px; }}
  .operator-card h4 {{ margin:0 0 5px; color:var(--c1); font-size:13px; }}
  .operator-card p, .operator-card li {{ font-size:12.5px; }}
  .operator-card ul {{ margin-top:4px; }}
  .demo-cell {{ min-width:70px; }}
  table.script td.tm {{ font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:11.5px; color:#9fd0ff; white-space:nowrap; }}
  table.script td.wc {{ font-family:ui-monospace,SFMono-Regular,Menlo,monospace; color:var(--mut); }}
  table.script td.viz {{ font-size:12px; color:#e0c07a; }}
  .demo-badge {{
    display:inline-block; padding:2px 7px; border-radius:6px; font-size:11px; font-weight:700;
    background:#152b25; border:1px solid #28614d; color:#8ee9bd; text-decoration:none; white-space:nowrap;
  }}
  .demo-badge:hover {{ background:#1c3a31; color:#b6f5d6; }}
  .demo-no {{ color:#4b5a6e; font-size:12px; }}
  .pkg-stats {{ display:flex; flex-wrap:wrap; gap:8px; margin:2px 0 8px; }}
  .pkg-stats .stat {{
    background:var(--panel2); border:1px solid var(--line); border-radius:20px;
    padding:3px 12px; font-size:12px; color:var(--mut);
  }}
  .pkg-stats .stat b {{ color:var(--txt); font-size:13px; }}
  .demo-card-list {{ display:grid; gap:12px; }}
  .demo-card {{
    background:var(--panel2); border:1px solid var(--line); border-left:4px solid #3fb950;
    border-radius:10px; padding:12px 14px; font-size:12.5px; scroll-margin-top:12px;
  }}
  .demo-card:target {{ border-color:#3fb950; box-shadow:0 0 0 2px rgba(63,185,80,.25); }}
  .demo-card-head {{ display:flex; align-items:baseline; flex-wrap:wrap; gap:8px; margin-bottom:7px; }}
  .demo-card-no {{
    background:#152b25; border:1px solid #28614d; color:#8ee9bd;
    font-size:11px; font-weight:800; padding:2px 8px; border-radius:6px;
  }}
  .demo-card-title {{ font-size:14px; font-weight:700; color:var(--txt); }}
  .demo-card-window {{
    margin-left:auto; font-size:11.5px; color:var(--mut);
    font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  }}
  .demo-card-meta {{ color:#9fd0ff; font-size:12px; margin-bottom:5px; }}
  .demo-card-shots {{
    background:#1b2432; border:1px solid #2f3d54; border-radius:7px;
    padding:7px 10px; color:#d7e3f2; font-size:12px; margin-bottom:8px; line-height:1.6;
  }}
  table.demo-steps {{ margin-top:2px; font-size:12px; }}
  table.demo-steps th, table.demo-steps td {{ padding:6px 8px; }}
  table.demo-steps td.step-n {{ color:var(--mut); font-weight:800; }}
  table.demo-steps td.step-do {{ color:#e6edf3; }}
  table.demo-steps td.step-see {{ color:#9aa7b8; }}
  .demo-verify {{
    background:#12291f; border:1px solid #2b5c45; border-radius:7px;
    padding:7px 10px; color:#a8e6c4; font-size:12px; margin-top:8px; line-height:1.6;
  }}
  .demo-pitfalls {{
    background:#2a1e12; border:1px solid #5a4322; border-radius:7px;
    padding:7px 10px; color:#e8c894; font-size:12px; margin-top:7px;
  }}
  .demo-pitfalls ul {{ margin:4px 0 0; padding-left:18px; }}
  .demo-pitfalls li {{ font-size:12px; margin:2px 0; }}
  .demo-audio {{
    background:#16202e; border:1px solid #2f4a63; border-radius:7px;
    padding:7px 10px; color:#b8d4ee; font-size:12px; margin-top:7px; line-height:1.6;
  }}
  .vp-block {{ margin-top:9px; border-top:1px dashed var(--line); padding-top:9px; }}
  .vp-block-head {{ font-size:12.5px; font-weight:700; color:#8ee9bd; margin-bottom:7px; }}
  .vp {{ background:#101a24; border:1px solid #2b3d50; border-radius:8px; padding:8px 10px; margin-bottom:7px; }}
  .vp-head {{ display:flex; align-items:center; flex-wrap:wrap; gap:7px; margin-bottom:4px; }}
  .vp-head b {{ font-size:12.5px; color:#e6edf3; }}
  .vp-dur {{
    font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:11px;
    color:var(--mut); background:var(--panel2); border:1px solid var(--line);
    border-radius:5px; padding:1px 6px;
  }}
  .vp-mode {{ font-size:10.5px; font-weight:700; padding:1px 7px; border-radius:5px; }}
  .vp-ai {{ background:#152b25; border:1px solid #28614d; color:#8ee9bd; }}
  .vp-screen {{ background:#2a2013; border:1px solid #6b4f22; color:#e0b46a; }}
  .vp-tip {{ font-size:11px; color:var(--mut); margin-bottom:5px; }}
  .vp-en {{
    font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:11.5px;
    line-height:1.55; color:#9fd0ff; background:#0c1118;
    border:1px solid #1e2a38; border-radius:6px; padding:6px 8px; word-break:break-word;
  }}
  .vp-zh {{ font-size:12px; color:var(--txt); margin-top:5px; line-height:1.6; }}
  .vp-neg {{
    font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:11px;
    color:#dba0a0; margin-top:5px; line-height:1.5; word-break:break-word;
  }}
  .reference-block {{ background:#111d2c; border:1px solid #2f5c7a; border-radius:10px; padding:12px 15px; margin:14px 0; }}
  .reference-block h3 {{ color:#9fd0ff; font-size:14px; margin:0 0 5px; }}
  .reference-block li {{ margin:8px 0; }}
  .reference-block a, .source-links a {{ color:#9fd0ff; }}
  .ref-use, .ref-no-copy {{ display:block; color:var(--mut); font-size:11.5px; margin-top:2px; }}
  .ref-no-copy {{ color:#d9b98e; }}
  .source-links a {{ margin-right:8px; }}
  code {{ background:#0c1118; padding:1px 6px; border-radius:5px; color:#9fd0ff; font-size:12px; }}
  footer {{ text-align:center; color:var(--mut); font-size:12px; margin-top:10px; line-height:1.8; }}
</style>
</head>
<body>
  <div class="wrap">
    <header class="hero">
      <h1>{title}</h1>
      <div class="meta">📅 {date} · {rtype_label} · 生成于 {generated}</div>
      {f'<div class="sub">{subtitle}</div>' if subtitle else ''}
    </header>

    {packages_html}

    {panels_html}

    <div class="disc">
      搜索下拉词为实时抓取的真实数据（YouTube Autocomplete API，美国区）；趋势与痛点判断基于公开报道与社区讨论的近似分析，未经 Google Trends 交互曲线与逐视频播放量复核。选题最终决策请以发布前的一手数据核实为准。本报告为研究方法演示，非投资建议。成片包文案请以发布前一手来源复核，标注教育/演示内容。
    </div>
    <footer>由 WorkBuddy AI「每日热点看台」自动生成 · 灵感选题用途</footer>
  </div>

  {pkg_data_blocks}

  <script>
  function copyPkg(btn) {{
      const id = btn.getAttribute('data-pkg-id');
      const data = document.getElementById(id);
      if (!data) {{ btn.classList.add('is-err'); setTimeout(()=>btn.classList.remove('is-err'),1500); return; }}
      const text = data.textContent;
      const fallback = () => {{
          const ta = document.createElement('textarea');
          ta.value = text; ta.style.position='fixed'; ta.style.left='-9999px';
          document.body.appendChild(ta); ta.select();
          try {{ document.execCommand('copy'); success(); }} catch(e) {{ fail(); }}
          document.body.removeChild(ta);
      }};
      const success = () => {{
          btn.classList.add('is-ok');
          const lbl = btn.querySelector('.pkg-copy-label');
          const old = lbl.textContent; lbl.textContent = '已复制 ✓'; btn.disabled = true;
          setTimeout(()=>{{ btn.classList.remove('is-ok'); lbl.textContent = old; btn.disabled = false; }}, 1500);
      }};
      const fail = () => {{
          btn.classList.add('is-err');
          const lbl = btn.querySelector('.pkg-copy-label');
          const old = lbl.textContent; lbl.textContent = '复制失败';
          setTimeout(()=>{{ btn.classList.remove('is-err'); lbl.textContent = old; }}, 1500);
      }};
      if (navigator.clipboard && navigator.clipboard.writeText) {{
          navigator.clipboard.writeText(text).then(success).catch(fallback);
      }} else {{ fallback(); }}
  }}
  </script>
</body>
</html>"""


def main():
    if len(sys.argv) < 3:
        print("用法: python3 generate_report.py <input_json> <output_html>", file=sys.stderr)
        sys.exit(1)
    in_path, out_path = sys.argv[1], sys.argv[2]
    with open(in_path, "r", encoding="utf-8") as f:
        spec = json.load(f)
    html_out = render(spec, base_dir=os.path.dirname(os.path.abspath(in_path)))
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"OK: 已生成 {out_path} ({len(html_out)} bytes)")


if __name__ == "__main__":
    main()
