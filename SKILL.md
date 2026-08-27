---
name: youtube-hotspot-dashboard
description: This skill builds the 「每日热点看台」(Daily Hotspot Dashboard) — a per-channel YouTube topic-recommendation report (5-section methodology) with two full 成片包 (production packages) pinned at the top. Triggers on phrases like "每日热点看台", "热点看台", "每日选题推荐", "选题推荐报告", "置顶成片包", "YouTube 选题看台", "daily topic report", "生成选题报告". Use when the deliverable is a ready-to-publish HTML report (one report covering multiple YouTube channels) plus deployable webhook push. For the topic-research methodology per channel use youtube-finance-topic-finder; for writing the individual 成片包 (hook variants + per-beat word counts) use viral-short-script.
agent_created: true
---

# 每日热点看台 · YouTube 选题报告 + 置顶成片包生成器

This skill produces a finished, multi-channel **YouTube topic-recommendation report** in HTML, with **two complete 成片包 pinned at the top** (one per channel), then deploys it and pushes a summary to a group chat (Feishu/Lark or WeCom).

The whole pipeline was extracted from a real working setup for two channels:
- **AI · 科技数码** `@AIcheatcodeplaybook` (casual hoodie creator persona)
- **金融 · 财经商业（美国观众）** `@TheMoneyMoo` (finance-educator persona, shirt, study)

## When to use

Invoke this skill when the user asks to:
- Generate a **daily or monthly** YouTube topic-recommendation report covering one or more channels.
- Produce the "热点看台" dashboard — signals → trends → pain points → screening → ratio, per channel.
- Pin **complete 成片包** (production packages) at the top of that report for the selected topics.
- Deploy the report to a public link and/or push a digest to Feishu/WeCom.

## Architecture — three cooperating skills

This skill orchestrates the end-to-end pipeline. The two heavy-lifting sub-skills are referenced, not duplicated:

1. **`youtube-finance-topic-finder`** — the 5-section **topic-research methodology** (search-suggestion signals, trend judgment, comment-pain-point → original angles, do/don't screening, content-ratio + compliance). Use it to fill `topic_data.json` per channel.
2. **`viral-short-script`** — the **成片包 generation method** (3 hook variants, per-beat word-count discipline, attention hooks every ~1 min, golden-sentence CTA, A/B thumbnails). Use it to build each `packages.json` entry. **This is the anti-"logic hole" skill: every beat must carry word count ≈ duration × 2.4; a 75-second beat needs ~180 words, never 30.**
3. This skill (`youtube-hotspot-dashboard`) — the **renderer + deployer + pusher** that ties them into one HTML deliverable.

> Rule of thumb: if the task is *researching what to make* → `youtube-finance-topic-finder`; if it's *writing one video's script* → `viral-short-script`; if it's *the whole daily report with pinned packages, deployed and pushed* → this skill.

## The pipeline (run in order)

### Step 0 — Config
Copy `config.example.json` → `config.json`, fill in real values:
- `youtube_api_key` (optional; falls back to WebSearch if blank)
- `webhook_url` + `webhook_type` (`feishu` or `wecom`)
- `report_url` (the public link from the deploy step — appended to the push message so the chat gets a clickable report)
- `timezone` (e.g. `America/New_York`)
- `channels` (handle / label / audience / interests per channel)

### Step 1 — Gather real signals (no API key needed for the core)
Fetch YouTube Autocomplete (real search-dropdown signals, US region):
```
https://suggestqueries.google.com/complete/search?client=youtube&ds=yt&hl=en&gl=US&q=<seed>
```
Seeds come from each channel's `interests`. Pair with `WebSearch` for macro data (FRED, NY Fed, Fed, Fidelity) for the finance channel.

### Step 2 — Build `topic_data.json` (per channel, 5 sections)
See `references/methodology.md` § "topic_data schema" and `references/topic_data.example.json`. Each `panels[]` entry has:
`signals[]` (real dropdown words + insight), `trends[]` (signal, type, saturation note), `painpoints{}` (headline + points + angles[problem/idea/title]), `screening[]` (hot/pain/original/verdict), `ratio{}` (ratios[] + compliance[]).

### Step 3 — Build `packages.json` (the pinned 成片包)
For the top 1–2 "做" topics, write a full 成片包 per channel using `viral-short-script`. Each package:
`channel_key, channel_label, topic, topic_cn, host, host_note, character_card, decision, operator_breakdown, hook, hook_zh, hook_options[3] (痛点暴击 / 反常识悬念 / 利益诱惑), titles[2], script[8 beats × {t,en,zh,viz,demo,img_en,img_zh}], emotion_arc, reference_videos[], source_links[], thumbs[2], description, tags[≥8], chapters[≥8]`.

**CRITICAL — practical-proof discipline:**
Every beat must have a `demo` object. `demo.need=true` means the video must show a real screen recording or physical operation; include `label`, `screen`, `steps[]`, and `proof`. Good AI examples: paste a brief into ChatGPT, manually reject hallucinated claims, build a Canva template, export files, edit a CapCut timeline, calculate time cost. Good finance examples: open the Federal Reserve source, highlight the correct rate field, enter APR/balance/payment in a payoff calculator, compare three cases, read a 401(k) plan's match formula. Do not let the host merely read a list of tools or rules.

**CRITICAL — word-count discipline (the logic-hole rule):**
words ≈ `duration_seconds × 2.4` (~140–160 wpm). Enforce per beat; reject any beat below 80% of target. Example targets: 10s≈30w, 15s≈45w, 45s≈110w, 60s≈150w, 75s≈180w, 90s≈220w. See `references/methodology.md` § "word-count" and the `viral-short-script` skill.

Differentiate `host`/`host_note` per channel so packages don't bleed into one persona (AI = hoodie creator; finance = shirt educator).

### Step 4 — Render the HTML
```
python3 scripts/generate_report.py topic_data.json report.html
```
The renderer **auto-loads `packages.json` from the same directory** as the input and pins both 成片包 above the panels. (Pure stdlib; no pip needed.) Output is a dark-themed, mobile-responsive HTML with a fixed-width script table.

### Step 5 — Deploy to a public link
Use the WorkBuddy **site publish** capability to deploy the report dir to a public `shareLink`. Re-deploying the same dir reuses the sandbox (same URL, content replaced). Put that URL into `config.json → report_url`.

### Step 6 — Push digest to chat
```
python3 scripts/push_webhook.py report.html topic_data.json
```
Sends a Markdown/text digest listing each channel's "做" topics; if `report_url` is set, appends `🌐 完整排版报告（点开看）：<url>`. Degrades gracefully (prints, exits 0) if webhook is a placeholder or network fails — so scheduled runs never hard-fail.

## Automation contract (for scheduled daily/monthly runs)
When wiring this into a recurring automation, the prompt must include:
- Step 1–3 research (signals + trends + pain points + screening + ratio + **成片包 with `hook_options[3]`**).
- The word-count rule verbatim: **"严禁 30 词敷衍 75 秒；每个 beat 词数 ≈ 时长×2.4，低于目标 80% 算不合格"**.
- The good-copy formula (痛点暴击 / 反常识悬念 / 利益诱惑, 黄金 5 秒 → 价值承诺 → 痛点 → 核心 → 金句+CTA, 每 1 分钟一个注意力钩子).
- Step 4 render → Step 5 deploy → Step 6 push.

## Pitfalls to avoid
- **Thin script copy (the #1 logic hole).** A 75-second beat with one sentence of English is impossible to film. Always count words per beat.
- **Concepts without content.** "没有内容只有笼统的文案概念" — every beat must contain specific numbers, scenarios, and a refuted objection, not vague claims.
- **One hook only.** Always provide 3 variants of distinct psychological types.
- **No attention hook mid-video.** Drop a reversal / data disclosure / analogy / guiding question every ~1 minute.
- **Generic CTA.** Replace "thanks for watching" with a specific action + next-week tease.
- **Host drift across packages.** Document per-channel `host_note`.
- **Treating suggestions as fact.** Mark all numbers "教育/演示内容，非投资建议"; verify against first-party sources before publishing.

## Bundled resources
- `scripts/generate_report.py` — stdlib HTML renderer (auto-loads sibling `packages.json`).
- `scripts/push_webhook.py` — Feishu/WeCom webhook pusher (graceful degradation).
- `config.example.json` — config template.
- `references/methodology.md` — full schemas, word-count table, deploy/push details.
- `references/topic_data.example.json` — a real, runnable 2-panel example.
- `references/packages.example.json` — two complete 成片包 (AI + finance) as a reference.
