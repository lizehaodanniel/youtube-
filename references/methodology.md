# 每日热点看台 · 方法与数据 Schema

本文件是 `youtube-hotspot-dashboard` 技能的详细方法说明与数据格式约定。阅读顺序：先看「整体数据流」，再按需查 schema。

---

## 1. 整体数据流

```
[种子词 interests]
   │
   ├─ YouTube Autocomplete API (免 key, gl=US)  → signals / dropdown words
   ├─ WebSearch (宏观/社区)                    → trends / painpoints 佐证
   ▼
topic_data.json   (每频道 5 板块：signals→trends→painpoints→screening→ratio)
   │
   ├─ youtube-finance-topic-finder 方法学   (决定做什么选题)
   ▼
packages.json     (每频道 1–2 个完整成片包，含 hook_options[3])
   │
   ├─ viral-short-script 方法学            (决定单条视频怎么写)
   ▼
generate_report.py topic_data.json report.html   (自动加载同目录 packages.json，置顶渲染)
   │
   ├─ WorkBuddy 站点发布  → 公开 shareLink → report_url
   ▼
push_webhook.py report.html topic_data.json       (推送摘要到飞书/企微)
```

---

## 2. topic_data.json schema

顶层：
```json
{
  "title": "每日热点看台 · 选题推荐",
  "date": "2026-08-26",
  "type": "daily",            // 或 "monthly"
  "subtitle": "（可选）一句话说明",
  "panels": [ /* 每频道一个对象 */ ]
}
```

每个 `panels[]` 对象（= 一个频道）：
```jsonc
{
  "key": "ai",                       // 必须匹配 packages.json 里的 channel_key
  "label": "AI · 科技数码",
  "handle": "@AIcheatcodeplaybook",
  "audience": "（受众描述）",

  "signals": [                       // 板块1：YouTube 搜索建议信号（真实下拉词）
    {
      "topic": "分类名",
      "tags": ["常青", "升温"],       // 可选标签
      "items": ["真实下拉词1", "真实下拉词2"],
      "insight": "（基于下拉词的判断）"
    }
  ],

  "trends": [                        // 板块2：题材热度走向判断
    { "topic":"题材", "signal":"真实信号/下拉词", "type":"Rising / 升温", "note":"是否饱和/注意" }
  ],

  "painpoints": {                    // 板块3：评论区痛点 → 原创角度
    "headline": "（最突出的跨主题痛点一句话）",
    "points": ["痛点1", "痛点2"],
    "angles": [
      { "problem":"原问题", "idea":"原创角度", "title":"建议标题" }
    ]
  },

  "screening": [                     // 板块4：选题筛选表（做/不做）
    { "topic":"选题", "source":"来源", "hot":"是", "pain":"是", "original":"是", "verdict":"做" }
    // verdict: "做" / "做·需强角度" / "不做"
  ],

  "ratio": {                         // 板块5：起步内容比例 + 合规红线
    "ratios": [ { "pct":"60%", "name":"常青需求", "items":"清单" } ],
    "compliance": [ "合规红线1", "合规红线2" ]
  }
}
```

筛选评分维度（用于 `verdict`）：① 近 30 天有热度 ② 有具体痛点 ③ 能提供原创解释/数据。满足 ≥3 项才「做」。

---

## 3. packages.json schema（置顶成片包）

顶层 `{ "packages": [ ... ] }`，每个对象 = 一个频道的一条完整成片包：

```jsonc
{
  "channel_key": "ai",               // 匹配 topic_data panels[].key
  "channel_label": "AI · 科技数码 (@AIcheatcodeplaybook)",
  "topic": "英文主标题",
  "topic_cn": "中文副标题",
  "host": "人设描述（口语化）",
  "host_note": "（重要）本包与另一频道人设的差异点，避免 drift",
  "decision": "为什么选这个题（来自哪条下拉词/痛点）",

  "hook": "主用 Hook（英文，黄金前 15 秒）",
  "hook_zh": "主用 Hook 中文",
  "hook_options": [                  // 3 个备选，按类型
    { "type":"痛点暴击", "label":"（戳中什么）", "en":"...", "zh":"..." },
    { "type":"反常识悬念", "label":"...", "en":"...", "zh":"..." },
    { "type":"利益诱惑", "label":"...", "en":"...", "zh":"..." }
  ],

  "titles": ["标题A", "标题B"],       // 2 个炸裂标题

  "script": [                        // 8 个 beat，句子级英中分栏
    {
      "t": "00:00-00:10",            // 时间段
      "en": "英文口播（词数 ≈ 时长×2.4）",
      "zh": "中文翻译",
      "viz": "分镜/情绪（给拍摄看）",
      "img_en": "Midjourney 英文提示词 --ar 16:9 --v 6.0",
      "img_zh": "中文提示词"
    }
    /* ... 共 8 个 beat ... */
  ],

  "emotion_arc": "Hook(...) → 价值承诺 → 痛点 → 核心 → 金句+CTA",
  "thumbs": [                        // A/B 两版封面
    { "ver":"A", "desc":"（视觉概念）", "img_en":"...", "img_zh":"..." },
    { "ver":"B", "desc":"...", "img_en":"...", "img_zh":"..." }
  ],
  "description": "视频简介（含教育/演示免责声明）",
  "tags": ["tag1", "tag2", "...≥8"],
  "chapters": ["00:00 ...", "00:10 ...", "...≥8"]
}
```

---

## 4. 词数纪律（防「逻辑漏洞」核心规则）

**公式：词数 ≈ duration_seconds × 2.4**（约 140–160 wpm 口语节奏）。

| 时段 | 目标词数 | 说明 |
|------|---------|------|
| 10s  | ~30     | Hook |
| 15s  | ~45     | 价值承诺 |
| 45s  | ~110    | 痛点代入 |
| 60s  | ~150    | 核心内容 |
| 75s  | ~180    | 核心内容（最常见翻车点） |
| 90s  | ~220    | 核心内容 |

- 写之前：对每个 beat 先算目标词数；写之后：用字数统计核对。
- **低于目标 80% 的 beat 一律打回重写**——这是「一句英文撑 75 秒」逻辑漏洞的唯一解法。
- 每 ~1 分钟埋一个注意力钩子：反转 / 关键数据披露 / 意想不到的类比 / 引导性提问。

---

## 5. 渲染与部署

### 渲染
```bash
python3 scripts/generate_report.py topic_data.json report.html
```
- 纯标准库，无需 `pip install`。
- 自动在 `topic_data.json` 同目录找 `packages.json` 并置顶渲染两个成片包；也可在 `topic_data.json` 顶层直接放 `"packages":[...]` 覆盖。
- 输出深色响应式 HTML，脚本表用 `table-layout:fixed` + 横向滚动，保证英文/中文分栏不溢出。

### 部署（公开链接）
用 WorkBuddy 站点发布能力，把含 `report.html` 的目录部署为公开 `shareLink`。
- 重复部署同一目录会复用沙箱（同一 URL，内容替换）。
- 把该 URL 填回 `config.json → report_url`。

### 推送
```bash
python3 scripts/push_webhook.py report.html topic_data.json
```
- `feishu`：发 text；若 `report_url` 非空，末尾追加 `🌐 完整排版报告（点开看）：<url>`。
- `wecom`：发 Markdown 摘要，并尝试上传 HTML 文件。
- `webhook_url` 仍为占位符 / 网络异常时：打印提示并以 exit 0 退出，避免定时任务硬失败。

---

## 6. 合规与免责（发布前必读）
- 所有价格 / 能力 / 数据回到一手来源核实（OpenAI、Google、xAI、FRED、Federal Reserve、NY Fed、Fidelity、SEC）。
- 明确标注「教育 / 演示内容，不构成个别投资或工具推荐 / 收益保证」。
- 不把任何频道的播放 / 收益等后台指标当作已知事实，除非该频道本人公开。
