# POV 一键成片（Remotion）

把生好的图片丢进 `public/`，跑一条命令，出 MP4。

## 三步

```bash
# 1. 装依赖（只做一次）
npm install

# 2. 把图放进去
#    金融频道 → public/finance/F01.png … F60.png
#    AI 频道  → public/ai/A01.png … A42.png
#    文件名必须和报告里的「镜号」一致。
#    想让画面动起来，就把同名 mp4 也丢进去（图生视频），会自动优先用 mp4。

# 3. 成片
npm run finance     # → out/finance.mp4
npm run ai          # → out/ai.mp4
npm run both        # 两条一起
```

## 图还没生完也能先渲

缺图的镜头会自动显示一个带镜号的渐变占位块，所以你可以先渲一条
**占位片**确认节奏和字幕时长，再逐张替换图片。这比生完 60 张才发现节奏不对省事得多。

## 改字幕语言

`src/Root.tsx` 里的 `defaultProps.captionLang`：

| 值 | 效果 |
|---|---|
| `en` | 只显示英文（默认，美国观众） |
| `zh` | 只显示中文 |
| `both` | 英文大字 + 中文小字（自己审片时用） |

## 时长的来源

每个镜头的时长直接来自报告里「时间」列（如 `2:34–2:47`），
`src/shots.ts` 的 `parseWindow` 负责解析，**不需要你手动填任何时长**。
改报告里的时间，重新渲染即可。

## 动效只有 4 种

| 动效 | 参数 | 用在哪 |
|---|---|---|
| `push-in` | scale 1.00 → 1.12 | 揭示 / 强调 / 段落开场 |
| `pull-out` | scale 1.12 → 1.00 | 收束 / 转场前 |
| `drift-right` | x 0 → −60px, scale 1.06 | 列举 / 时间推进 |
| `hold` | scale 1.02 → 1.05 | 重句 / 需要看清数字 |

转场是每个镜头开头 12 帧淡入（交叉溶解），`Root.tsx` 里的 `fadeInFrames` 可调。

## 视频规格

1920×1080 / 30fps。成片时长由最后一镜的时间戳决定 + 1 秒黑场。

## 数据来源

`src/shots.json` 由根目录 `generate_pov.py` 自动生成，**不要手改**。
改内容请改 `_build/pov_fin.py` / `_build/pov_ai.py`，然后重跑：

```bash
cd .. && python3 generate_pov.py
```
