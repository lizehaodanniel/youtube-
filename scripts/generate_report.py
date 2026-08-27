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


def script_table(beats):
    rows = ""
    for b in beats:
        en = b.get("en", "")
        rows += f"""<tr>
          <td>{esc(b.get('t',''))}</td>
          <td class="ctr">{esc(str(len(en.split())))}</td>
          <td class="en">{esc(en)}</td>
          <td class="zh">{esc(b.get('zh',''))}</td>
          <td>{esc(b.get('viz',''))}</td>
          <td class="demo-cell">{demo_summary(b.get('demo'))}</td>
          <td class="img-en">{esc(b.get('img_en',''))}</td>
          <td class="img-zh">{esc(b.get('img_zh',''))}</td>
        </tr>"""
    return f"""<div class="script-wrap"><table class="script">
      <colgroup>
        <col style="width:90px"><col style="width:56px"><col style="width:330px">
        <col style="width:330px"><col style="width:170px"><col style="width:360px"><col style="width:230px"><col style="width:230px">
      </colgroup>
      <tr><th>时间段</th><th class="ctr">词数</th><th>英文口播(左)</th><th>中文翻译(右)</th><th>分镜/情绪</th><th>实操展示（必须拍）</th><th>图片提示词·英</th><th>图片提示词·中</th></tr>
      {rows}
    </table></div>"""


def demo_summary(demo):
    if not demo or not demo.get("need"):
        return '<span class="demo-no">口播 / 普通画面</span>'
    label = esc(demo.get("label", "必须实操"))
    screen = esc(demo.get("screen", ""))
    steps = "".join(f"<li>{esc(x)}</li>" for x in (demo.get("steps") or []))
    proof = esc(demo.get("proof", ""))
    return f'''<div class="demo-yes"><b>{label}</b>
      <div class="demo-screen">录屏：{screen}</div>
      <ol>{steps}</ol>
      <div class="demo-proof">验收：{proof}</div>
    </div>'''


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


def demo_plan_block(beats):
    rows = ""
    for b in beats:
        d = b.get("demo") or {}
        need = d.get("need", False)
        label = esc(d.get("label", "普通口播/画面"))
        screen = esc(d.get("screen", ""))
        steps = "".join(f"<li>{esc(x)}</li>" for x in (d.get("steps") or []))
        proof = esc(d.get("proof", ""))
        cls = "demo-plan-yes" if need else "demo-plan-no"
        rows += f'''<div class="demo-plan {cls}">
          <div class="demo-plan-head"><b>{esc(b.get("t", ""))}</b> · {label}</div>
          <div><b>录屏对象：</b>{screen or "无"}</div>
          {f'<ol>{steps}</ol>' if steps else '<div class="src">这一段不需要软件实操，可用口播+图示。</div>'}
          {f'<div class="demo-proof">验收：{proof}</div>' if proof else ''}
        </div>'''
    return f'<div class="demo-plan-list">{rows}</div>'


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
    script_html = script_table(pkg.get("script") or [])
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
    demo_plan_html = demo_plan_block(pkg.get("script") or [])
    refs_html = reference_block(pkg.get("reference_videos") or [])
    return f"""
    <section class="pkg" style="--c1:{c1};--c2:{c2}">
      <div class="pkg-head">
        <div>
          <div class="pkg-label">🎬 完整成片包 · {label}</div>
          <div class="pkg-topic"><span class="en">{topic}</span> ／ {topic_cn}</div>
        </div>
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
      <div class="pkg-sec"><h3>分镜脚本表（句子级·英中分栏 + 图片提示词 + 实操标注）</h3>{script_html}</div>
      <div class="pkg-sec"><h3>实操执行清单（哪一段必须录屏、怎么录、验收什么）</h3>{demo_plan_html}</div>
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
  .pkg-head {{ display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; margin:14px 0 4px; }}
  .pkg-label {{ font-size:19px; font-weight:800; background:linear-gradient(90deg,var(--c1),var(--c2)); -webkit-background-clip:text; background-clip:text; color:transparent; }}
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
  table.script {{ table-layout:fixed; min-width:1440px; border-collapse:collapse; width:100%; font-size:12.5px; }}
  table.script th, table.script td {{ border:1px solid var(--line); padding:8px 9px; text-align:left; vertical-align:top; }}
  table.script th {{ background:var(--panel2); color:var(--mut); font-weight:600; }}
  table.script td.en, table.script td.zh {{ line-height:1.5; }}
  table.script td.img-en, table.script td.img-zh {{ color:#9fd0ff; font-size:11.5px; }}
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
  .demo-cell {{ min-width:320px; }}
  .demo-yes {{ background:#152b25; border:1px solid #28614d; border-radius:8px; padding:8px 9px; color:#d4f6e7; }}
  .demo-no {{ color:var(--mut); font-size:12px; }}
  .demo-screen {{ color:#9fe4c5; font-size:11.5px; margin-top:3px; }}
  .demo-yes ol {{ margin:5px 0 0; padding-left:18px; }}
  .demo-yes li {{ font-size:11.5px; margin:2px 0; }}
  .demo-proof {{ color:#b8d9cd; font-size:11px; margin-top:5px; }}
  .demo-plan-list {{ display:grid; grid-template-columns:1fr 1fr; gap:10px; }}
  @media(max-width:820px){{ .demo-plan-list {{ grid-template-columns:1fr; }} }}
  .demo-plan {{ background:var(--panel2); border:1px solid var(--line); border-left:4px solid var(--mut); border-radius:9px; padding:10px 12px; font-size:12px; }}
  .demo-plan-yes {{ border-left-color:#3fb950; }}
  .demo-plan-no {{ border-left-color:#64748b; }}
  .demo-plan-head {{ color:var(--txt); margin-bottom:4px; }}
  .demo-plan ol {{ margin:5px 0 0; padding-left:18px; }}
  .demo-plan li {{ font-size:12px; margin:3px 0; }}
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
