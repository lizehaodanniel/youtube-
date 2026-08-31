# -*- coding: utf-8 -*-
"""POV 成片包渲染器（按用户「第一性原理」精简后的最终版）。

只渲染用户真正会用的东西：
    ① 选题框架（一句话，让你在做之前知道「这条视频用什么讲法」）
    ② 标题 5 选 1（同一内容，5 个不同封面文案）
    ③ 缩略图 3 选 1（同一内容，3 种封面构图）
    ④ 全部分镜（开头就是前几行，不需要单独列出）
    ⑤ 出片三步 + Remotion 是什么

砍掉：单独的「开头」重复段、单独的「框架」表（隐藏在内容里就行）、
单段操作步骤展开说明（太复杂）。

用法：
    python3 generate_pov.py output/pov-YYYY-MM-DD.html
"""
import io
import json
import os
import sys
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "_build"))

import pov_ai  # noqa: E402
import pov_fin  # noqa: E402
from pov_style import THUMB_RULES  # noqa: E402


def esc(s):
    return (str(s or "").replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


ACCENT = {"ai": ("#22d3ee", "#7c5cff"), "finance": ("#f0a94b", "#7fd1c1")}

# ============================================================ CSS
CSS = """
:root{--bg:#0b0d12;--bg2:#12151d;--card:#161a24;--line:#242a38;--tx:#e8ecf4;
--mut:#93a0b8;--dim:#6b7891;--ok:#5ee6a8;--warn:#f0a94b;--bad:#ff6b81;
--ai:#22d3ee;--fin:#f0a94b;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--tx);
font:15px/1.7 -apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;}
.wrap{max-width:1260px;margin:0 auto;padding:28px 20px 90px}
h1{font-size:26px;margin:0 0 6px}
.lead{color:var(--mut);margin:0 0 4px}
.date{color:var(--dim);font-size:13px;margin-bottom:22px}
.sec{margin:34px 0 14px;font-size:19px;font-weight:700;display:flex;align-items:center;gap:9px}
.sec .n{display:inline-flex;width:24px;height:24px;border-radius:7px;background:#242b3a;
color:var(--mut);font-size:13px;align-items:center;justify-content:center;font-weight:700}
.hint{color:var(--dim);font-size:13px;margin:-6px 0 12px}
.subhint{color:var(--ok);font-size:12.5px;margin:-3px 0 12px;letter-spacing:.3px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin-bottom:12px}
.pkg{border:1px solid var(--line);border-radius:16px;padding:20px;margin-bottom:34px;background:var(--bg2)}
.pkg-head{display:flex;justify-content:space-between;align-items:flex-start;gap:14px;flex-wrap:wrap;
padding-bottom:14px;border-bottom:1px solid var(--line)}
.pkg-label{font-size:13px;color:var(--mut);margin-bottom:5px}
.pkg-topic{font-size:21px;font-weight:800;line-height:1.35}
.pkg-topic .cn{display:block;font-size:15px;font-weight:500;color:var(--mut);margin-top:5px}
.pill{display:inline-block;padding:3px 10px;border-radius:999px;font-size:12px;
background:#1e2534;color:var(--mut);border:1px solid var(--line);margin-left:8px}
.pick{background:rgba(94,230,168,.13);color:var(--ok);border-color:rgba(94,230,168,.32);font-weight:700}
/* 框架一句话 */
.framework{background:rgba(240,169,75,.07);border:1px solid rgba(240,169,75,.28);
border-radius:10px;padding:11px 14px;color:#e6c793;font-size:13.5px;margin-bottom:14px}
.framework b{color:var(--warn);font-weight:700}
/* 标题 */
.t{display:flex;gap:12px;align-items:flex-start;padding:13px 15px;border:1px solid var(--line);
border-radius:11px;background:var(--card);margin-bottom:9px}
.t.on{border-color:rgba(94,230,168,.45);background:rgba(94,230,168,.06)}
.t .en{font-size:17px;font-weight:700;line-height:1.4}
.t .cn{color:var(--mut);font-size:13.5px;margin-top:3px}
.t .meta{color:var(--dim);font-size:12.5px;margin-top:7px;line-height:1.6}
.badge{flex:none;width:26px;height:26px;border-radius:8px;background:#242b3a;color:var(--mut);
font-size:12px;font-weight:700;display:flex;align-items:center;justify-content:center;margin-top:2px}
.t.on .badge{background:rgba(94,230,168,.18);color:var(--ok)}
/* 缩略图 */
.thumbs{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:12px}
.th{border:1px solid var(--line);border-radius:12px;padding:14px;background:var(--card)}
.th h4{margin:0 0 8px;font-size:14px}
.th .concept{color:var(--mut);font-size:13px;margin-bottom:8px}
.ov{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px}
.ov span{background:#1e2534;border:1px solid var(--line);border-radius:6px;padding:2px 9px;font-size:12.5px;color:var(--tx)}
.th .why{color:var(--dim);font-size:12.5px;margin:8px 0}
/* 提示词框 */
.pbox{position:relative;background:#0e1119;border:1px solid var(--line);border-radius:9px;
padding:10px 11px;margin-top:8px}
.pbox .lb{font-size:11px;color:var(--dim);letter-spacing:.5px;margin-bottom:5px}
.pbox .txt{font:12.5px/1.65 ui-monospace,SFMono-Regular,Menlo,monospace;color:#cdd6e6;
max-height:240px;overflow:auto;white-space:pre-wrap;word-break:break-word}
.cp{position:absolute;top:7px;right:7px;background:#232b3c;border:1px solid var(--line);
color:var(--mut);border-radius:6px;padding:2px 9px;font-size:11.5px;cursor:pointer}
.cp:hover{color:var(--tx);border-color:#3a465e}
.cp.ok{color:var(--ok);border-color:rgba(94,230,168,.45)}
/* 分镜表 */
.sh{width:100%;border-collapse:collapse;font-size:13px}
.sh th{position:sticky;top:0;z-index:5;background:#10141d;text-align:left;color:var(--dim);
font-weight:600;font-size:11.5px;padding:8px 8px;border-bottom:1px solid var(--line);white-space:nowrap}
.sh td{padding:9px 8px;border-bottom:1px solid #1a2030;vertical-align:top}
.sh tr:hover td{background:rgba(255,255,255,.022)}
/* 开头段（前 N 行）高亮 */
.sh tr.hook td{background:rgba(94,230,168,.04);border-left:2px solid var(--ok);border-right:2px solid var(--ok)}
.sh tr.hook:hover td{background:rgba(94,230,168,.08)}
.hooktag{display:inline-block;font-size:10.5px;color:var(--ok);font-weight:700;
padding:1px 6px;border-radius:4px;background:rgba(94,230,168,.13);margin-left:5px;vertical-align:middle}
.sh .id{font-family:ui-monospace,monospace;color:var(--dim);font-size:11.5px;white-space:nowrap}
.sh .win{font-family:ui-monospace,monospace;color:var(--mut);font-size:11.5px;white-space:nowrap}
.sh .en{line-height:1.55}
.sh .zh{color:var(--mut);font-size:12.5px;line-height:1.55}
.sh .vi{color:var(--dim);font-size:12px}
.sh .mo{font-size:11.5px;color:var(--mut);white-space:nowrap}
.sh .pr{font:11.5px/1.55 ui-monospace,Menlo,monospace;color:#b9c4d8;max-width:330px}
.sh .pr div{max-height:112px;overflow:auto;white-space:pre-wrap;word-break:break-word}
.sh .cam{max-width:250px}
.campill{display:inline-block;font-size:10.5px;font-weight:700;letter-spacing:.3px;
  border:1px solid;border-radius:20px;padding:1px 8px;margin-bottom:5px}
.she{font-size:11.5px;line-height:1.5;color:#8fa0bb;white-space:normal}
.mini{background:#1e2534;border:1px solid var(--line);color:var(--mut);border-radius:5px;
padding:1px 7px;font-size:11px;cursor:pointer;margin-top:5px;display:inline-block}
.mini:hover{color:var(--tx)}
.mini.ok{color:var(--ok)}
/* 操作 */
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px}
.step{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:15px}
.step .k{font-size:12px;color:var(--c1);font-weight:700;letter-spacing:1px;margin-bottom:6px}
.step h4{margin:0 0 7px;font-size:15px}
.step p{margin:0 0 7px;color:var(--mut);font-size:13px}
pre{background:#0e1119;border:1px solid var(--line);border-radius:8px;padding:11px 12px;
overflow:auto;font:12.5px/1.6 ui-monospace,Menlo,monospace;color:#cdd6e6;margin:6px 0 0}
pre .c{color:#5b6880}
.note{background:rgba(240,169,75,.07);border:1px solid rgba(240,169,75,.28);
border-radius:10px;padding:12px 14px;color:#e6c793;font-size:13px;margin:10px 0}
details{margin-top:8px}
summary{cursor:pointer;color:var(--mut);font-size:12.5px;padding:4px 0}
summary:hover{color:var(--tx)}
.toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(20px);
background:#1b2a22;border:1px solid rgba(94,230,168,.45);color:var(--ok);padding:9px 18px;
border-radius:9px;font-size:13.5px;opacity:0;pointer-events:none;transition:.22s;z-index:99}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
"""

# ============================================================ JS
JS = r"""
function toast(m){var t=document.getElementById('toast');t.textContent=m;
t.classList.add('show');clearTimeout(t._h);t._h=setTimeout(function(){t.classList.remove('show')},1600);}
function flash(b){var o=b.textContent;b.textContent='已复制';b.classList.add('ok');
setTimeout(function(){b.textContent=o;b.classList.remove('ok')},1300);}

/* ---------- 颜色工具 ---------------------------------------------------------
   页面上的深色不是单元格自己带的：.sh td 是透明的，深色靠外层 .pkg 的 #12151d 透出来，
   开头行是 rgba(94,230,168,.04) 近乎全透明。直接把 computed style 交给 WPS 会得到
   rgba(0,0,0,0) → 白底。所以必须沿祖先链把半透明背景一层层合成成不透明色。 */
/* 页面调色板兜底：getComputedStyle 在某些环境拿不到自定义属性，补一层已知值 */
var VARS = {'--bg':'#0b0d12','--bg2':'#12151d','--card':'#161a24','--line':'#242a38',
  '--tx':'#e8ecf4','--mut':'#93a0b8','--dim':'#6b7891',
  '--ok':'#5ee6a8','--warn':'#f0a94b','--bad':'#ff6b81'};

/* 把 var(--x) 展开成真实色值。WPS 不认 CSS 变量，漏出去就是默认黑字。 */
function resolveVars(s, el){
  var out = String(s || '');
  for (var i = 0; i < 6 && out.indexOf('var(') !== -1; i++) {
    out = out.replace(/var\(\s*(--[A-Za-z0-9_-]+)\s*(?:,\s*([^)]*?))?\)/g, function(all, name, fb){
      var v = '';
      var node = el;
      while (!v && node && node.nodeType === 1) {
        try { v = (window.getComputedStyle(node).getPropertyValue(name) || '').trim(); } catch (e) {}
        node = node.parentElement;
      }
      if (!v && document.documentElement) {
        try { v = (window.getComputedStyle(document.documentElement).getPropertyValue(name) || '').trim(); } catch (e) {}
      }
      return v || VARS[name] || (fb ? String(fb).trim() : '') || '';
    });
  }
  return out;
}
/* style="..." 是用双引号包起来的，值里再出现双引号会提前闭合属性，
   后面所有声明（padding / border / 对齐）会被整段吞掉 —— 必须换成单引号。 */
function q(v){ return String(v == null ? '' : v).replace(/"/g, "'"); }

function parseColor(s){
  var str = String(s || '').trim();
  var m = str.match(/rgba?\(([^)]+)\)/);
  if (m) {
    var p = m[1].split(',').map(function(x){ return parseFloat(x); });
    return { r:p[0], g:p[1], b:p[2], a:(p.length > 3 ? p[3] : 1) };
  }
  var h = str.match(/^#([0-9a-f]{3}|[0-9a-f]{6})$/i);
  if (h) {
    var t = h[1];
    if (t.length === 3) t = t[0]+t[0]+t[1]+t[1]+t[2]+t[2];
    return { r:parseInt(t.slice(0,2),16), g:parseInt(t.slice(2,4),16), b:parseInt(t.slice(4,6),16), a:1 };
  }
  return null;
}
function hex2(c){ return ('0' + Math.max(0, Math.min(255, Math.round(c))).toString(16)).slice(-2); }
function toHex(c){ return '#' + hex2(c.r) + hex2(c.g) + hex2(c.b); }
function effectiveBg(el){
  var stack = [], n = el;
  while (n && n.nodeType === 1) {
    var raw = window.getComputedStyle(n).backgroundColor;
    var c = parseColor(resolveVars(raw, n));
    if (c && c.a > 0.001) stack.push(c);
    n = n.parentElement;
  }
  /* 最底层按页面底色起算（不是白纸）：万一 var() 全没解析出来，也还是深色而不是刺眼白底 */
  var out = { r:11, g:13, b:18 };
  for (var i = stack.length - 1; i >= 0; i--) {        /* 从最外层往里合 */
    var c = stack[i];
    out = { r: c.r*c.a + out.r*(1-c.a), g: c.g*c.a + out.g*(1-c.a), b: c.b*c.a + out.b*(1-c.a) };
  }
  return out;
}

/* 把节点树里「眼睛看到的」文字样式全部烘成 inline style。
   页面的颜色来自 CSS class（.zh{color:var(--mut)} 之类），WPS 没有样式表，
   不烘就全变默认黑字；同时把 class / id 摘掉，避免 WPS 拿未知 class 套默认表格样式。 */
function flattenText(root){
  var nodes = [root];
  Array.prototype.forEach.call(root.querySelectorAll('*'), function(n){ nodes.push(n); });
  nodes.forEach(function(n){
    if (String(n.tagName).toLowerCase() === 'button') { n.remove(); return; }
    var cs = window.getComputedStyle(n), st = [];
    var col = parseColor(resolveVars(cs.color, n));
    st.push('color:' + (col ? toHex(col) : q(cs.color)));
    st.push('font-size:' + q(cs.fontSize));
    /* 只接受正常的字体栈："X, Y, sans-serif" 或单个无空格族名。
       像 "depends on user agent" 这种无逗号又带空格的脏值直接丢掉，免得污染整条 style。 */
    var ff = String(cs.fontFamily || '');
    if (ff && (ff.indexOf(',') !== -1 || ff.indexOf(' ') === -1)) st.push('font-family:' + q(ff));
    if (cs.lineHeight && cs.lineHeight !== 'normal') st.push('line-height:' + q(cs.lineHeight));
    if (cs.fontWeight && cs.fontWeight !== '400' && cs.fontWeight !== 'normal') st.push('font-weight:' + q(cs.fontWeight));
    if (cs.whiteSpace && cs.whiteSpace !== 'normal') st.push('white-space:' + q(cs.whiteSpace));
    n.setAttribute('style', st.join(';'));
    n.removeAttribute('class');
    n.removeAttribute('id');
  });
}

/* 重建一张干净的表格：不带 class / id / CSS 变量 / 嵌套外壳。
   这是老版本 generate_report.py 里那套 tblToHtml 的思路——实测 WPS 能吃下。 */
function tblToHtml(el){
  var bg = effectiveBg(el);
  var bgh = toHex(bg);
  var out = ['<table border="1" cellspacing="0" cellpadding="0" bgcolor="' + bgh + '" bordercolor="#242a38"'
    + ' style="border-collapse:collapse;width:100%;background-color:' + bgh + ';'
    + 'font-family:-apple-system,\'PingFang SC\',\'Microsoft YaHei\',sans-serif">'];
  var rowIdx = 0;
  Array.prototype.forEach.call(el.querySelectorAll('tr'), function(tr){
    var tag = (rowIdx === 0) ? 'th' : 'td';
    var cells = [];
    Array.prototype.forEach.call(tr.children, function(cell){
      var cs = window.getComputedStyle(cell);
      var cb = effectiveBg(cell), cbh = toHex(cb);
      var clone = cell.cloneNode(true);
      flattenText(clone);
      var cellCol = parseColor(resolveVars(cs.color, cell));
      var st = [
        'background-color:' + cbh,
        'color:' + (cellCol ? toHex(cellCol) : q(cs.color)),
        'font-size:' + q(cs.fontSize),
        'font-family:' + q(cs.fontFamily),
        'padding:' + q(cs.padding),
        'border:1px solid #2b3346',
        'text-align:' + (cs.textAlign || 'left'),
        'vertical-align:' + (cs.verticalAlign || 'top')
      ];
      cells.push('<' + tag + ' bgcolor="' + cbh + '" bordercolor="#2b3346" style="' + st.join(';') + '">'
        + clone.innerHTML + '</' + tag + '>');
    });
    out.push('<tr>' + cells.join('') + '</tr>');
    rowIdx++;
  });
  out.push('</table>');
  return out.join('');
}

/* 写剪贴板：优先 ClipboardItem（真 HTML）；失败就退化到 contentEditable + Range 选中
   再 execCommand —— 这条路同样能带上 HTML（老版本就是这么兜底的），
   比塞 textarea 只给纯文本强得多。 */
function writeClip(html, text, done, fail){
  function fbRich(){
    var div = document.createElement('div');
    div.contentEditable = 'true';
    div.style.cssText = 'position:fixed;left:-9999px;top:0;opacity:0';
    div.innerHTML = html;
    document.body.appendChild(div);
    var range = document.createRange();
    range.selectNodeContents(div);
    var sel = window.getSelection();
    sel.removeAllRanges(); sel.addRange(range);
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
    sel.removeAllRanges();
    document.body.removeChild(div);
    return ok;
  }
  if (window.ClipboardItem && navigator.clipboard && navigator.clipboard.write) {
    try {
      navigator.clipboard.write([new ClipboardItem({
        'text/html': new Blob([html], {type:'text/html'}),
        'text/plain': new Blob([text], {type:'text/plain'})
      })]).then(done, function(){ fbRich() ? done() : (fail && fail()); });
      return;
    } catch (e) {}
  }
  fbRich() ? done() : (fail && fail());
}

/* 富文本复制整张表 */
function copyRich(el, label){
  var html = tblToHtml(el);
  var text = el.innerText || el.textContent || '';
  function done(){ flash(el._btn || document.createElement('b')); toast((label||'') + ' 已复制（带样式）'); }
  writeClip(html, text, done, function(){ toast('复制失败，请手动选中'); });
}

/* 富文本复制单条提示词：包成单格表格（WPS 认单元格底色，不认 <div> 底色） */
function copyPromptRich(text, label){
  var e = function(s){return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');};
  var BG = '#12151d', BD = '#2b3346';
  var html =
    '<table border="1" cellspacing="0" cellpadding="0" bgcolor="' + BG + '" bordercolor="' + BD + '"'
  + ' style="border-collapse:collapse;width:100%;background-color:' + BG + ';'
  + 'font-family:-apple-system,\'PingFang SC\',\'Microsoft YaHei\',sans-serif"><tr>'
  + '<td bgcolor="' + BG + '" bordercolor="' + BD + '"'
  + ' style="background-color:' + BG + ';color:#cdd6e6;padding:14px 16px;border:1px solid ' + BD + ';'
  + 'font-family:Menlo,Consolas,monospace;font-size:13px;line-height:1.65;'
  + 'white-space:pre-wrap;word-break:break-word;vertical-align:top">'
  + '<div style="color:#5b6880;font-size:11px;letter-spacing:1px;margin-bottom:10px;'
  + 'font-family:-apple-system,PingFang SC,sans-serif">' + e(label||'提示词') + '</div>'
  + e(text)
  + '</td></tr></table>';
  function done(){ toast((label||'提示词') + ' 已复制（带暗色样式）'); }
  writeClip(html, text, done, function(){ toast('复制失败'); });
}

document.addEventListener('click', function(ev){
  var b = ev.target.closest('.cp, .mini, .tblcp');
  if (!b) return;
  var t = b.getAttribute('data-target');
  if (t) { var el = document.getElementById(t); if (el){ el._btn=b; copyRich(el, b.getAttribute('data-label')||'内容'); } return; }
  var s = b.getAttribute('data-text');
  if (s) { copyPromptRich(s, b.getAttribute('data-label')||'提示词'); flash(b); }
});
"""

# ============================================================ 组件
def pbox(label, text, bid):
    return (f'<div class="pbox"><div class="lb">{esc(label)}</div>'
            f'<button class="cp" data-text="{esc(text)}" data-label="{esc(label)}">复制</button>'
            f'<div class="txt" id="{bid}">{esc(text)}</div></div>')


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
    out = '<div class="note" style="font-size:12.5px;white-space:pre-line">' + esc(THUMB_RULES) + '</div><div class="thumbs">'
    for th in thumbs:
        ov = "".join(f"<span>{esc(x)}</span>" for x in th.get("overlay", []))
        out += f'''<div class="th">
          <h4>{esc(th["name"])}{'<span class="pill pick">首选</span>' if th['id'] == 1 else ''}</h4>
          <div class="concept">{esc(th["concept"])}</div>
          <div class="ov">{ov}</div>
          <div class="why"><b>为什么能点：</b>{esc(th["why"])}</div>
          {pbox("生图提示词 · 英文（整段复制，直接喂给生图工具）", th["prompt_en"], f"thm-{th['id']}")}
        </div>'''
    return out + "</div>"


CAM_LABEL = {
    "face":          ("露脸", "#5ee6a8", "能看清她的脸，占画面上三分之一"),
    "profile":       ("侧脸", "#5ee6a8", "侧脸可读，身体转向一侧"),
    "over-shoulder": ("过肩", "#f0a94b", "从她肩后拍，能看到肩线、后脑或下颌边"),
    "hands":         ("手部", "#6b7891", "只有手和前臂，身体在画外但能感觉到"),
    "back":          ("背影", "#f0a94b", "从背后拍，看得到背和后脑"),
    "silhouette":    ("剪影", "#f0a94b", "逆光轮廓，脸在阴影里不可读"),
}


def shots_block(shots, ns):
    """开头 = 分镜表的前 N 行（按 sec==1 自动判定）。不再单独渲染，保留表格加高亮。"""
    hook_ids = {s["id"] for s in shots if s["sec"] == 1}
    rows = ""
    for s in shots:
        is_hook = s["id"] in hook_ids
        cls = " hook" if is_hook else ""
        kind = s.get("cam", "hands")
        label, color, hint = CAM_LABEL.get(kind, CAM_LABEL["hands"])
        cam_cell = (f'<span class="campill" title="{esc(hint)}" '
                    f'style="color:{color};border-color:{color}44">{label}</span>'
                    f'<div class="she">{esc(s.get("she", ""))}</div>')
        rows += f'''<tr class="{cls.strip()}">
          <td class="id">{esc(s["id"])}{'<span class="hooktag">开头</span>' if is_hook else ''}</td>
          <td class="win">{esc(s["window"])}</td>
          <td class="en">{esc(s["en"])}<div class="zh">{esc(s["zh"])}</div></td>
          <td class="vi">{esc(s["visual"])}<div style="margin-top:4px;color:#5b6880">{esc(s["emotion"])}</div></td>
          <td class="mo">{esc(s["motion"])}</td>
          <td class="cam">{cam_cell}</td>
          <td class="pr"><div>{esc(s["img_en"])}</div>
            <button class="mini" data-text="{esc(s['img_en'])}" data-label="图片提示词 · {esc(s['id'])}">复制图片</button></td>
          <td class="pr"><div>{esc(s["vid_en"])}</div>
            <button class="mini" data-text="{esc(s['vid_en'])}" data-label="视频提示词 · {esc(s['id'])}">复制视频</button></td>
        </tr>'''
    return f'''<table class="sh" id="shots-{ns}"><thead><tr>
      <th>镜号</th><th>时间</th><th>口播 英文 / 中文</th><th>画面 / 节奏</th><th>动效</th>
      <th>她在画面里</th><th>图片提示词</th><th>视频提示词</th></tr></thead><tbody>{rows}</tbody></table>'''


def framework_block(p):
    """一句话讲清楚这条视频用什么讲法。框架不展开、不列表格。"""
    return (f'<div class="framework"><b>本片框架：</b>{esc(p["framework_one_liner"])}</div>')


def package_block(p):
    key = p["channel_key"]
    c1, c2 = ACCENT.get(key, ("#7c5cff", "#22d3ee"))
    hook_count = len([s for s in p["shots"] if s["sec"] == 1])
    return f'''
<section class="pkg" style="--c1:{c1};--c2:{c2}" id="pkg-{key}">
  <div class="pkg-head">
    <div>
      <div class="pkg-label">🎬 {esc(p["channel_label"])}</div>
      <div class="pkg-topic">{esc(p["topic"])}<span class="cn">{esc(p["topic_cn"])}</span></div>
    </div>
    <div style="text-align:right;color:var(--mut);font-size:13px">
      <div>{esc(p["duration"])}　·　{p["shot_count"]} 镜　·　{p["word_count"]} 词</div>
      <div style="color:var(--dim);font-size:12px;margin-top:3px">开头 {hook_count} 镜（已高亮）</div>
    </div>
  </div>

  {framework_block(p)}

  <div class="sec"><span class="n">1</span>标题（5 选 1 · 同一内容的 5 个不同封面文案）</div>
  <div class="subhint">5 个标题讲的都是同一条视频。选 1 个发，剩下的进 A/B 测试。</div>
  {titles_block(p["titles"])}

  <div class="sec"><span class="n">2</span>缩略图（3 选 1 · 同一视频的 3 种封面构图）</div>
  <div class="subhint">3 张都是这条视频的封面。3 张都生一遍，挑点击率最高的那张。</div>
  {thumbs_block(p["thumbs"])}

  <div class="sec"><span class="n">3</span>全部分镜（{p["shot_count"]} 镜 · 绿色左边框就是开头）</div>
  <div class="hint">按镜号顺序生图。每个镜头的图片 / 视频提示词都是「角色卡 + 镜头描述 + 风格圣经」的长版，可直接整段复制喂给生图 / 生视频工具。</div>
  <button class="mini tblcp" data-target="shots-{key}" data-label="分镜表" style="margin-bottom:9px">📋 复制整张分镜表（带样式，粘进 WPS / 飞书 / 微信都带暗色底）</button>
  {shots_block(p["shots"], key)}

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
</section>'''


def workflow_block(specs):
    chans = "、".join(esc(s["channel_label"].split("(")[0].strip()) for s in specs)
    total = sum(s["shot_count"] for s in specs)
    return f'''
<section class="pkg" style="--c1:#5ee6a8;--c2:#22d3ee">
  <div class="pkg-head"><div>
    <div class="pkg-label">⚙️ 出片流程</div>
    <div class="pkg-topic">三步出片<span class="cn">本次共 {total} 个镜头（{chans}）</span></div>
  </div></div>

  <div class="note" style="margin-bottom:14px">
    <b>关于 Remotion——它就是出片工具，不是「做完视频再用 Remotion 后期」：</b><br>
    传统流程：先拍 / 录 → 剪映 / Premiere 剪辑 → 字幕 → 输出。<br>
    本流程：<b>Remotion 一步做完全部三件事</b>（按口播时长自动对位 + 字幕 + 转场 + 镜头推拉），
    你只负责前面两步——给它图和文，剩下的它生成 MP4。不用打开任何剪辑软件。
  </div>

  <div class="steps">
    <div class="step"><div class="k">STEP 1</div><h4>生图</h4>
      <p>按「镜号顺序」把每个镜头的<b>图片提示词</b>复制进生图工具，
      保存为 <code>public/&lt;频道&gt;/F01.png</code> …… </p>
      <p style="color:var(--dim)">同一频道一次性批量生，风格最稳。图里不要有字——
      字幕是第 3 步自动叠的。</p></div>
    <div class="step"><div class="k">STEP 2</div><h4>生视频（可选）</h4>
      <p>想让画面动起来的镜头，把<b>视频提示词</b>配合第 1 步那张图一起喂给生视频工具（图生视频），
      存成同名 <code>.mp4</code>。</p>
      <p style="color:var(--dim)">不想做就跳过——只有图也能出片，Remotion 会自动做推拉镜头。</p></div>
    <div class="step"><div class="k">STEP 3</div><h4>Remotion 一键成片</h4>
      <p>Remotion 直接读你做好的图 + 文，生成 MP4。它就是视频编辑器。</p>
      <pre><span class="c"># 先装依赖（只做一次）</span>
cd remotion &amp;&amp; npm install
<span class="c"># 一键成片</span>
npm run finance     <span class="c"># → out/finance.mp4</span>
npm run ai          <span class="c"># → out/ai.mp4</span></pre>
      <p style="color:var(--dim);margin-top:9px">图还没生完也能先渲一条看节奏——
      缺的图会用镜号占位块顶替。</p></div>
  </div>

  <details><summary>手动版（不用 Remotion）</summary>
    <div class="card" style="margin-top:9px;color:var(--mut);font-size:13px">
      把图片按镜号拖进剪映 / CapCut，每张拉到「时间」栏标注的时长，
      加一个「缓慢放大」的关键帧（开头 100%、结尾 112%），
      配旁白音轨，字幕用软件的自动识别。效果差 10%，工作量多 3 倍。
    </div>
  </details>
</section>'''


# ============================================================ 渲染
def render(specs, out_path):
    today = datetime.date.today().isoformat()
    body = "\n".join(package_block(s) for s in specs)
    total = sum(s["shot_count"] for s in specs)
    words = sum(s["word_count"] for s in specs)
    html = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>POV 成片包 · {today}</title><style>{CSS}</style></head><body>
<div class="wrap">
  <h1>POV 成片包 · {today}</h1>
  <div class="lead">{total} 个镜头 / {words} 词 / 两个频道 · 全部画面由 AI 生成，无需录屏、无需准备素材</div>
  <div class="date">使用顺序：选标题 → 生缩略图 → 按分镜表生图 → 丢进 remotion/ → 一键出片</div>
  {body}
  {workflow_block(specs)}
</div>
<div class="toast" id="toast"></div>
<script>{JS}</script>
</body></html>'''
    with io.open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    return out_path


def main():
    specs = [pov_fin.build(), pov_ai.build()]
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        HERE, "output", f"pov-{datetime.date.today().isoformat()}.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    p = render(specs, out)

    # 同时导出 JSON，供 Remotion 工程读取
    jp = os.path.join(HERE, "remotion", "src", "shots.json")
    os.makedirs(os.path.dirname(jp), exist_ok=True)
    with io.open(jp, "w", encoding="utf-8") as f:
        json.dump(specs, f, ensure_ascii=False, indent=1)

    for s in specs:
        print(f'  {s["channel_key"]:8s} {s["shot_count"]:3d} 镜 / {s["word_count"]:4d} 词 / {s["duration"]}')
    print("HTML :", p)
    print("JSON :", jp)
    print("bytes:", os.path.getsize(p))


if __name__ == "__main__":
    main()