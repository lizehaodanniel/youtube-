# -*- coding: utf-8 -*-
"""给每个镜头生成一张 SVG 占位图，这样 Remotion 工程在「图还没生完」时也能直接渲染。

生成后你只要把真图存成同名 .png 覆盖掉即可（png 优先级高于 svg）。

用法（在项目根目录）：
    python3 make_placeholders.py
"""
import io
import os
import sys
import html

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "_build"))
import pov_ai  # noqa: E402
import pov_fin  # noqa: E402

PALETTE = {
    "finance": ("#16232B", "#2C3F4A", "#E8A54B"),
    "ai": ("#0B0E14", "#151B29", "#22D3EE"),
}


def svg_for(shot, channel):
    bg, mid, accent = PALETTE[channel]
    ident = shot["id"]
    visual = shot["visual"]
    # 中文可能很长，简单按字数换行
    lines, cur = [], ""
    for ch in visual:
        cur += ch
        if len(cur) >= 22:
            lines.append(cur)
            cur = ""
    if cur:
        lines.append(cur)
    lines = lines[:4]
    tspans = "".join(
        f'<tspan x="960" dy="{0 if i == 0 else 52}">{html.escape(l)}</tspan>'
        for i, l in enumerate(lines)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{bg}"/>
      <stop offset="55%" stop-color="{mid}"/>
      <stop offset="100%" stop-color="{accent}" stop-opacity="0.55"/>
    </linearGradient>
  </defs>
  <rect width="1920" height="1080" fill="url(#g)"/>
  <rect x="0" y="0" width="1920" height="1080" fill="none" stroke="{accent}" stroke-opacity="0.18" stroke-width="8"/>
  <text x="960" y="452" text-anchor="middle" font-family="Helvetica,Arial,sans-serif"
        font-size="150" font-weight="800" fill="#ffffff" fill-opacity="0.92"
        letter-spacing="-3">{ident}</text>
  <text x="960" y="560" text-anchor="middle"
        font-family="PingFang SC,Microsoft YaHei,Helvetica,Arial,sans-serif"
        font-size="40" font-weight="500" fill="#ffffff" fill-opacity="0.62">{tspans}</text>
  <text x="960" y="700" text-anchor="middle" font-family="Menlo,monospace"
        font-size="27" fill="#ffffff" fill-opacity="0.34">public/{channel}/{ident}.png</text>
</svg>'''


def sync_assets():
    """扫描 public/ 里每个镜头到底有哪些素材，写进 remotion/src/assets.ts。

    关键：运行时绝不探测文件是否存在。Remotion 的 <Img>/<OffthreadVideo>
    遇到 404 会挂住（delayRender 超时在 React 之外抛出，错误边界接不住），
    整条渲染会直接失败。所以素材清单必须在构建期算好。
    """
    entries = {}
    total_new = 0
    for pkg in (pov_fin.build(), pov_ai.build()):
        key = pkg["channel_key"]
        d = os.path.join(HERE, "remotion", "public", key)
        os.makedirs(d, exist_ok=True)
        for s in pkg["shots"]:
            ident = s["id"]
            mp4 = os.path.join(d, ident + ".mp4")
            png = os.path.join(d, ident + ".png")
            svg = os.path.join(d, ident + ".svg")
            if os.path.exists(mp4):
                entries[ident] = ("mp4", key)
            elif os.path.exists(png):
                entries[ident] = ("png", key)
            else:
                if not os.path.exists(svg):
                    with io.open(svg, "w", encoding="utf-8") as f:
                        f.write(svg_for(s, key))
                    total_new += 1
                entries[ident] = ("svg", key)

    lines = "\n".join(
        f"  '{k}': {{ kind: '{v[0]}', src: staticFile('{v[1]}/{k}.{v[0]}') }},"
        for k, v in sorted(entries.items())
    )
    ts = (
        "// 由 make_placeholders.py 自动生成，不要手改。\n"
        "// 每次新增 / 替换素材后重跑：python3 make_placeholders.py\n"
        "import {staticFile} from 'remotion';\n\n"
        "export type AssetKind = 'mp4' | 'png' | 'svg';\n\n"
        "export const ASSETS: Record<string, {kind: AssetKind; src: string}> = {\n"
        f"{lines}\n"
        "};\n\n"
        "export const getAsset = (id: string) => ASSETS[id] ?? null;\n"
    )
    out = os.path.join(HERE, "remotion", "src", "assets.ts")
    with io.open(out, "w", encoding="utf-8") as f:
        f.write(ts)
    return entries, total_new


def main():
    entries, new = sync_assets()
    from collections import Counter
    c = Counter(v[0] for v in entries.values())
    print(f'  素材清单：{c["mp4"]} 个 mp4 / {c["png"]} 张 png / {c["svg"]} 张占位 svg')
    if new:
        print(f'  新建占位图 {new} 张')
    print("  写在 remotion/src/assets.ts")
    if c["png"] + c["mp4"] < len(entries):
        print("  → 还有镜头用的是占位图。把真图存成 public/<频道>/<镜号>.png 后，"
              "重跑本脚本即可自动切换。")


if __name__ == "__main__":
    main()
