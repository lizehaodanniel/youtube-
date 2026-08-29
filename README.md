# StrongBug

> 每日 YouTube 热点看台 · 双频道选题推荐 + 完整成片包生成器

## 这是什么

一个自动化产出「每日选题推荐报告」的 Python 工具，覆盖两个 YouTube 频道：

| 频道 | 定位 | 虚拟主人公（3D 卡通） |
|---|---|---|
| **AI · 科技数码** `@AIcheatcodeplaybook` | AI 工具实战变现 | 3D 卡通年轻女性，棒球帽 + 大耳机，紫红霓虹公寓 |
| **金融 · 美国个人理财** `@TheMoneyMoo` | 美国家庭财务决策 | 3D 卡通奶牛吉祥物（Pixar 风格），深蓝马甲，简洁书房 |

每份报告分 5 块（真实下拉词信号 · 题材热度 · 痛点角度 · 筛选表 · 起步内容比例 + 合规红线），并把两个**完整成片包**置顶（hook / 标题 / 句子级脚本 / 镜头级视频提示词 / 实操卡 / 缩略图 / 简介 / 标签 / 章节）。

## 项目结构

```
.
├── topic_data.json            # 选题数据（信号 / 趋势 / 痛点 / 筛选表 / 比例）
├── packages.json              # 两个完整成片包（生成产物，由 _build/build.py 产出）
├── generate_report.py         # HTML 渲染器（无第三方依赖）
├── push_webhook.py            # 飞书 / 企业微信 推送
├── config.json                # 频道配置 + 飞书 webhook
├── _build/                    # 成片包素材源文件
│   ├── ai_ch1_4.py            #   AI 包第 1-4 章口播句子
│   ├── ai_ch5_6.py            #   AI 包第 5-6 章口播句子
│   ├── ai_ch7_8.py            #   AI 包第 7-8 章口播句子
│   ├── ai_demos.py            #   AI 包 8 张实操卡
│   ├── ai_videos.py           #   AI 包镜头级视频提示词
│   ├── fin_ch1_4.py           #   金融包第 1-4 章口播句子
│   ├── fin_ch5_6.py           #   金融包第 5-6 章口播句子
│   ├── fin_ch7_8.py           #   金融包第 7-8 章口播句子
│   ├── fin_demos.py           #   金融包 8 张实操卡
│   ├── fin_videos.py          #   金融包镜头级视频提示词
│   ├── scan_numbers.py        #   口播数字真实性扫描工具
│   └── build.py               #   把上述源文件合成为 packages.json
├── output/                    # 生成的每日 HTML 报告（默认被 git 忽略）
├── site/                      # 部署用的静态站点（默认被 git 忽略）
└── .workbuddy-ai/             # 本地记忆（默认被 git 忽略）
```

## 用法

```bash
# 1. 重建 packages.json（修改 _build/ 下的源文件后）
python3 _build/build.py

# 2. 生成当日报告
python3 generate_report.py topic_data.json output/daily-2026-08-28.html

# 3. 复制到部署目录
cp output/daily-2026-08-28.html site/index.html

# 4. 推送到飞书
python3 push_webhook.py output/daily-2026-08-28.html topic_data.json
```

部署用 WorkBuddy AI 的 sites 能力，发布后复用同一沙箱 ID。

## 选题信号来源

- **YouTube Autocomplete API**（美国区），用 `https://suggestqueries.google.com/complete/search?client=youtube&ds=yt&hl=en&gl=US&q=<种子词>` 抓取真实下拉词。种子词列表见 `topic_data.json`。
- **公开报道 + 社区讨论**（WebSearch 近似判断，发布前需一手复核）。
- 案例数字均为**情景假设**（示例演算，不是真实成交/真实账户数据）。

## 内容质检（每次交付前必跑）

参见 skill `youtube-package-qa`：

1. **制作指令串台扫描**——口播里不能出现 `screenshot / pause / zoom / circle` 这类给拍摄者的指令
2. **案例数字真实性扫描**——所有 `$ / % / 年限` 都必须可追溯或明确标假设
3. **host 形象一致性**——img / character_card / host / host_note / thumbs 必须全统一；检测真人残留词用 lookbehind 正则 `(?<!as-)\bhands\b`（`hooves-as-hands` 是卡通牛必要表述，不能误判）
4. **视频提示词 mode 分流**——ai-video 可直喂视频模型；screen 镜头建议自己录屏 + AE

## 配置

`config.json` 里的 `webhook_url` 与 `webhook_type` 控制推送目标（飞书 / 企业微信）。两个频道的 `handle` 也在 `config.json` 里改。

## 合规红线（成片包文案必须执行）

- 所有收益数字标注「示例 / 假设」，不写成「保证月入」
- 信用卡 / 401(k) 数字必须发布前到 Federal Reserve / NY Fed / Investor.gov 复核
- host 描述不复刻任何受版权保护的文字（频道名 / t-shirt 印字等）
- 标题中第一人称过去式「I Used」需谨慎——会构成"我做过且成交过"的虚假陈述

## 许可

私有项目。代码与文案供作者本人使用。
