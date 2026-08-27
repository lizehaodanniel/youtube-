# youtube-hotspot-dashboard

「每日热点看台」—— 一个面向多 YouTube 频道的 **每日/每月选题推荐报告 + 置顶成片包** 自动生成器。输入真实搜索下拉词与公开数据，产出一份可发布的深色响应式 HTML 报告（每频道 5 板块选题推荐），并在报告最顶部钉两个**完整成片包**（含 3 个 Hook 备选、句子级英中分栏脚本、逐段实操录屏步骤、来源链接、可借鉴视频链接、图片提示词、A/B 封面、简介/标签/章节）。

> 本仓库同时是一个 WorkBuddy AI **Skill**，可直接放入 `~/.workbuddy-ai/skills/` 使用。

## 适用场景
- 每天/每月给一个或多个 YouTube 频道生成「该做什么视频」的选题报告
- 在报告顶部预置可直接拍摄的完整成片包（脚本 + 钩子 + 封面）
- 把报告部署成公开链接，并推送摘要到飞书/企微群

## 两个协作 Skill（本 Skill 调用它们）
| Skill | 职责 |
|-------|------|
| `youtube-finance-topic-finder` | 单频道的 5 板块选题研究方法（信号/趋势/痛点/筛选/比例） |
| `viral-short-script` | 单条视频的成片包写法（3 Hook 备选、逐 beat 词数纪律、注意力钩子） |

## 快速开始
```bash
# 1. 准备配置
cp config.example.json config.json   # 填入 webhook / report_url / 频道信息

# 2. 准备数据（参考 references/*.example.json）
#    topic_data.json  —— 每频道 5 板块选题推荐
#    packages.json    —— 置顶成片包（与 topic_data.json 同目录）

# 3. 渲染 HTML（纯标准库，无需 pip）
python3 scripts/generate_report.py topic_data.json report.html

# 4. 推送摘要到飞书/企微（可选）
python3 scripts/push_webhook.py report.html topic_data.json
```

## 目录结构
```
youtube-hotspot-dashboard/
├── SKILL.md                       # Skill 主体（方法 + 流程）
├── README.md                      # 本文件
├── config.example.json            # 配置模板
├── scripts/
│   ├── generate_report.py         # 标准库 HTML 渲染器（自动加载同目录 packages.json）
│   └── push_webhook.py            # 飞书/企微 Webhook 推送（优雅降级）
└── references/
    ├── methodology.md             # 完整方法、两个 JSON schema、词数表、部署/推送细节
    ├── topic_data.example.json    # 可运行的 2 频道选题示例
    └── packages.example.json      # 两个完整成片包示例（AI + 金融）
```

## 核心纪律：词数 + 实操证明（防逻辑漏洞）
一个 75 秒的 beat 必须 ~180 词，绝不能用一句话敷衍。每个 beat 低于目标 80% 词数即打回重写。更重要的是：每段必须回答“观众看到什么真实操作、怎么操作、用什么结果验收”。AI 内容要展示 brief → ChatGPT → 人工修改 → Canva/CapCut → 导出 → 报价；金融内容要展示官方数据页 → 账单字段 → 还款/复利计算器 → 案例表 → 计划文件。详见 `references/methodology.md` §3–4。

## 合规
所有数据回到一手来源核实；标注「教育/演示内容，不构成个别投资或工具推荐/收益保证」。

---
由 WorkBuddy AI「每日热点看台」能力沉淀为 Skill · 灵感选题用途
