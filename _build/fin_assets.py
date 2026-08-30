# -*- coding: utf-8 -*-
"""金融频道（@TheMoneyMoo 风格）实操素材清单 —— 讲故事向，零外部素材。

设计原则（用户原话：「金融频道我实际上只想讲故事，如果也有实际案例需要
去找很多素材就很麻烦」）：

  1. **不晒证件**。不需要真实账单、不需要登录银行 App、不需要 401(k) 计划
     文件。这些东西观众找不到，你也不该晒。
  2. **需要展示的"文件"，我直接写好内容**。你复制 → 粘进任意编辑器 →
     截图。看起来是一份账单，实际上是一段你完全掌控的文字。
  3. **每个数字都能被复算**。所有金额都由 `_build/fin_numbers.py` 实算产出，
     改任何输入就重跑那个脚本，不要手改数字。
  4. **三个人物撑起整支视频**。同一个 $8,000 / 每月 $500，只改利率，
     这样"利率才是变量"这件事不用解释就能看见。
  5. **凡是提到某个网站长什么样，必须真的打开过那个网站**。
     本文件的 G.19 与 Investor.gov 部分，是 2026-08-27 实际抓取页面后
     逐字记录的；页面会改版，用之前请自己再核对一次（见 f3-1 / f3-3 开头）。

虚构人物：Maya（22% 卡债）/ Devon（7% 车贷）/ Priya（3.5% 学生贷）
"""

HOST_NOTE = (
    "金融频道的人物插画一律用 3D 卡通奶牛吉祥物（海军蓝马甲 / 书房），"
    "不出现真人，不出现任何真实金融机构的界面截图。"
)

IMG_SUFFIX_EN = ", clean minimal 3D illustration, soft studio lighting, shallow depth of field, no text, no logos, --ar 16:9 --v 6.0"
IMG_SUFFIX_ZH = "，干净的极简 3D 插画，柔和棚拍灯光，浅景深，无文字，无标志，--ar 16:9 --v 6.0"

# 这次核对页面的日期。每次重录都要重新核对，并把这一行改成新的日期。
VERIFIED_ON = "2026-08-27"


# ================================================================ 卡 1 开场
OPENING_CARD = """开场 9 秒 —— 屏幕上只出现一个数字

  22%

下面一行小字（字号要能在手机上看清）：

  This is a guaranteed cost.
  The market has never guaranteed me anything.

中文对照（如果你做中文版）：
  这是一个确定的成本。
  市场从来没有向我保证过任何事。

----------------------------------------------------------------
为什么开场不放账单截图：
  1. 观众第一反应是「他是不是在晒别人的账单」，信任先掉一半
  2. 真实账单打码会糊，反而看不清重点
  3. 一个数字比一屏文字有力

如果你一定要有"实物感"，拿一张纸手写一个 22%，用手举到镜头前。
手写的比打印的更可信，因为它明显不是模板。

----------------------------------------------------------------
这个 22% 不是编的（出品前请自己再核一次）：
  Federal Reserve G.19 · Terms of Credit 表
  「Commercial bank interest rates → Credit card plans
    → Accounts assessed interest」
  2026 年 5 月 = 22.15%
  见 f3-2 数据快照，里面有完整出处和核对日期。
"""

OPENING_CARD_IMG_EN = (
    "A single large number 22% rendered in bold dark charcoal typography, centered on a warm cream "
    "background, a thin terracotta underline beneath it, generous negative space, editorial poster design, "
    "no other text, no charts, no people"
) + IMG_SUFFIX_EN

OPENING_CARD_IMG_ZH = (
    "一个巨大的数字 22%，用深炭黑色粗体字呈现，居中放在暖奶油色背景上，"
    "下方一道细的陶土色下划线，大量留白，杂志海报式排版，无其他文字，无图表，无人物"
) + IMG_SUFFIX_ZH


# ================================================================ 卡 2 三问表
THREE_QUESTIONS = """THE THREE QUESTIONS — 抄这张表，三个空格自己填

  #   问题                                    Your number    Example    这个数从哪来
  -------------------------------------------------------------------------------
  1   Highest interest rate right now?        ______         22%        账单上的 Purchase APR
  2   Extra cash you can put in monthly?      ______         $500       预算表，不是"感觉"
  3   Does your employer match anything?      ______         50% up to  计划文件里的
                                                            6% of pay  Employer Contributions 段
  -------------------------------------------------------------------------------

填表规则（说给观众听）：
  · 第 2 格必须是"多出来的钱"，不是"全部闲钱"。
    留不出 emergency buffer 就去还债，下一笔意外会让你再刷回去。
  · 第 3 格只有两个答案：有，或者没有。
    "好像有"要打电话问清楚，这是全片回报率最高的一通电话。
  · 三个格子填完，后面全是算术。填不完，后面全是猜。

----------------------------------------------------------------
Example 列是示例，Your number 列留空给观众。
这两列必须同时出现在屏幕上 —— 观众要有地方写自己的数。
"""


# ================================================================ 卡 3 官方数据页
G19_WALKTHROUGH = f"""FEDERAL RESERVE G.19 — 逐字操作路径（{VERIFIED_ON} 实抓核对）

----------------------------------------------------------------
【最重要的一个坑，先说】

  不要打开 https://www.federalreserve.gov/releases/g19/
  那个页面只是"发布日历"—— 一列按年份排的日期链接，没有任何利率表格。
  在它上面找不到 Credit Card Plans，你会以为是自己眼花了。

  要打开的是【当期发布页】，URL 长得像这样（末尾是发布日期 YYYYMMDD）：
      https://www.federalreserve.gov/releases/g19/20260807

  怎么从日历页进到发布页：
    打开 /releases/g19/ → 找 "Release Dates" 区块 → 点当年那一行里
    带星号的月份链接（星号 = 当期）→ 就到了发布页。
    或者直接从上面的日历页点进去，然后把地址栏那一串日期抄下来。

----------------------------------------------------------------
【发布页上，你要找的东西，逐字记录】

  1. 页面标题：Consumer Credit - G.19
  2. 紧挨着标题下面：
        Release Date: August 7, 2026
        June 2026                     ← 这是【数据月份】
     注意两个日期不一样：发布日是 8 月 7 日，数据月份是 6 月。
     视频里要圈出来的是【数据月份】，不是发布日。

  3. 往下滚，找这张表（这是全页唯一一张含信用卡利率的表）：
        Consumer Credit Outstanding
     表下方有一行小字：
        Terms of Credit
     再下面一行：
        Not seasonally adjusted. Percent except as noted.

  4. 在 Terms of Credit 区块里，先有一个分组标题：
        Commercial bank interest rates        ← 带脚注 5

  5. 在这个分组下面，行标签逐字是：

        New car loans 60-month
        New car loans 72-month
        Credit card plans
            All accounts                      ← 缩进一层
            Accounts assessed interest        ← 缩进一层，【用这一行】
        Personal loans 24-month

----------------------------------------------------------------
【两个口径的区别 —— 这段是脚注 5 的原文，直接念也行】

  "For credit card accounts, the rate for all accounts is the stated
   APR averaged across all credit card accounts at all reporting banks.
   The rate for accounts assessed interest is the annualized ratio of
   total finance charges at all reporting banks to the total average
   daily balances against which the finance charges were assessed
   (excludes accounts for which no finance charges were assessed)."

  翻成人话：
    All accounts            = 所有卡的平均名义 APR，包括那些每月清干净、
                              一分利息都没付的卡。这些人把平均值拉低了。
    Accounts assessed interest = 真正付了利息的那些卡，用「总利息 ÷ 总日均余额」
                              算出来的实际利率。

  你如果每个月都留余额（也就是会付利息），要看的是下面那个。
  这也是为什么视频里说 22% 而不是 14.6%——两个都是官方数，
  但只有下面那个是你自己会遇到的数。

----------------------------------------------------------------
【列怎么读】

  表头是：2021 2022 2023 2024 2025 | 2025 Q2 Q3 Q4 | 2026 Q1 Q2p | Aprr Mayr Junp
  最后三列是最近三个月的月度值，带 r = revised（修正）、p = preliminary（初值）。

  信用卡两行在月度列里很多是 n.a.（not available）—— 信用卡利率是
  【季度】调查的，不是每个月都有。所以最稳的做法是念季度值：
    2026 Q2p（初值）= 22.15%
  或者念最近有数的月度值：
    Mayr = 22.15%

  视频里说 "twenty-two percent"，取的就是这个数。

----------------------------------------------------------------
【录屏前必做的三件事】

  □ 打开当期发布页，确认今天的数字还是 22% 上下。
    如果已经变了，改口播里的数字，别硬套旧的。
  □ 把数据月份（不是发布日）圈出来给观众看。
  □ 把 URL 完整留在地址栏里，停留至少 3 秒，够暂停抄下来。

----------------------------------------------------------------
【页面会变的几种情况，遇到了怎么办】

  · 表格折叠起来了（页面上有 "- Show More"）→ 点开它。
  · 当月发布页还没出 → 用上一期，并在口播里说"最新一期是 X 月的数据"。
  · URL 结构改了 → 从 /releases/g19/ 日历页重新点进去，别猜 URL。
  · 实在找不到那两行 → 别硬念数字。改成"我把链接放简介里，
    你自己去看 Accounts assessed interest 那一行"，然后继续往下讲。
    念一个你没找到出处的数字，比跳过这一段危险得多。
"""

DATA_SNAPSHOT = f"""DATA SNAPSHOT — 数据快照（{VERIFIED_ON} 抓取，出品前必须重核）

  来源    Federal Reserve · Consumer Credit - G.19
  发布页  https://www.federalreserve.gov/releases/g19/20260807
  发布日  August 7, 2026
  数据月  June 2026
  表格    Terms of Credit · Commercial bank interest rates（脚注 5）
  单位    Percent, not seasonally adjusted, annual percentage rate (APR)

----------------------------------------------------------------
  行标签                                   2026 Q1    2026 Q2p    May 2026
  -----------------------------------------------------------------------
  New car loans, 60-month                    7.53       7.14        7.14
  New car loans, 72-month                    7.53       6.97        6.97
  Credit card plans · All accounts           21.52     20.94        n.a.
  Credit card plans · Accounts assessed      21.52     22.15       22.15
  Personal loans, 24-month                   11.36     11.86       11.86
  -----------------------------------------------------------------------
  （n.a. = not available；信用卡两行的月度值很多月份没有，是季度调查）

----------------------------------------------------------------
【这三个数，就是视频里三个人的利率】

  Maya  22%    ← Credit card plans · Accounts assessed interest = 22.15%
                 官方口径、官方表格、官方脚注。这是全片最硬的一个数。

  Devon  7%    ← New car loans, 60-month = 7.14%
                 同样是这张表。所以"7% 的车贷"不是编的，
                 是同一份文件里往下数两行就有的数。

  Priya  3.5%  ← ⚠️ 这个数【不在 G.19 里】。G.19 只统计商业银行的消费信贷，
                 联邦学生贷款利率由教育部按学年设定，要另外查。
                 发布前请自行核对当期联邦学生贷款利率；
                 核对不到就把 Priya 换成另一个有出处的利率，
                 或者在口播里明说"这是假设值"。

----------------------------------------------------------------
【为什么要把快照单独存一份】

  这些数每个月都会变。你今天录的 22.15%，三个月后可能变成 21% 或 24%。
  观众两个月后看到视频，看到的是旧数字 —— 这没关系，
  但你自己必须知道那是哪个月的旧数字。

  所以这份快照要和你的工程文件放在一起，并且写清抓取日期。
  下次重录，先更新这一份，再改口播。
"""

CALC_WALKTHROUGH = f"""INVESTOR.GOV 复利计算器 — 逐字字段清单（{VERIFIED_ON} 实抓核对）

  网址 https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator
  标题 Compound Interest Calculator | Investor.gov
  出品 美国证券交易委员会（SEC）旗下，免费、无广告、不采集个人信息

----------------------------------------------------------------
【页面上到底有几个输入框 —— 是六个，不是四个，而且分四步】

  Step 1: Initial Investment
      Initial Investment
      说明文字：Amount of money that you have available to invest initially.

  Step 2: Contribute
      Monthly Contribution
      说明：Amount that you plan to add to the principal every month,
            or a negative number for the amount that you plan to
            withdraw every month.
      Length of Time in Years                ← ⚠️ 单位是【年】，不是月

  Step 3: Interest Rate
      Estimated Interest Rate
      说明：Your estimated annual interest rate.
      Interest rate variance range
      说明：Range of interest rates (above and below the rate set above)
            that you desire to see results for.

  Step 4: Compound It
      Compound Frequency
      选项（五个，逐字）：Annually / Semiannually / Quarterly / Monthly / Daily
      说明：Times per year that interest will be compounded.

  页面顶部还有一行：*** DENOTES A REQUIRED FIELD

----------------------------------------------------------------
【三个最容易翻车的地方】

  1. "Length of Time" 是【年】。
     我们整支视频算的是 20 个月和 17 个月。
     20 个月 = 1.667 年，17 个月 = 1.417 年。
     如果你直接填 20，算出来的是二十年的结果，会大得离谱。
     → 要么填 1.67，要么干脆不用这个算还债（见下面第 2 条）。

  2. 这个计算器算的是【钱生钱】，不是【还债】。
     它算不出"多久还清、一共付多少利息"。
     还债那一半必须用还款计算器，或者照 fin_numbers.py 的算法手算。
     → 屏幕上如果要同时出现两边，左边是还款计算器的结果，
       右边是这个计算器的结果，中间画一条线分开，
       并且标注：left = paying off debt, right = investing instead。

  3. "Interest rate variance range" 那一项，很多人忘了它存在。
     填了之后结果会多出上下两档区间 —— 这其实是好事，
     正好用来说明"7% 是假设，实际可能在 X 和 Y 之间"。
     → 建议填 3（显示 4% 到 10% 的区间），
       这是全片把"假设"两个字讲清楚最省力的一帧。

----------------------------------------------------------------
【建议的填法（对应视频里的 Maya 案例）】

  Initial Investment .......... 0
  Monthly Contribution ........ 500
  Length of Time in Years ..... 1.67          （= 20 个月）
  Estimated Interest Rate ..... 7
  Interest rate variance range  3
  Compound Frequency .......... Monthly

  这样出来的期末值约 $10,574，和 fin_numbers.py 算的一致。
  如果你填出来的数对不上，先检查 Length of Time 是不是填成了 20，
  以及 Compound Frequency 是不是选了 Annually（默认很可能是它）。

----------------------------------------------------------------
【录屏建议】

  这个页面很干净，适合全屏录。要点：
  · 逐格填，光标每跳一格停 0.5 秒，别一口气填完
  · 填到 Estimated Interest Rate 时，就地弹出红色批注
    "assumption, not a forecast"
  · 结果出来后，把结果面板和输入面板一起截进同一张图
  · 页面会改版。录之前先打开一次，确认字段名字还是这几个。
"""

RECALC_NOTE = """怎么自己复算（也给观众）

  方式一：手算（视频里最有说服力）
    每月利息 = 剩余本金 × (APR ÷ 12)
    每月本金 = 月供 − 每月利息
    重复到本金归零，数一下跑了几个月

    例（Case A 第一个月）：
      $8,000 × (22% ÷ 12) = $8,000 × 0.018333 = $146.67   ← 利息
      $500 − $146.67 = $353.33                             ← 真正还掉的本金
      剩余本金 = $8,000 − $353.33 = $7,646.67
    这样跑 20 次，本金归零，总利息 $1,556。

  方式二：用 Investor.gov 的复利计算器
    只适用于"钱生钱"那一半。还债那一半用它算不出来。
    字段清单见 f3-3，注意 Length of Time 的单位是【年】。

  方式三：跑本项目自带的脚本
    python3 _build/fin_numbers.py
    改脚本顶部的 balance / apr / payment，重跑。

----------------------------------------------------------------
录屏建议：
  三个案例不要各录一遍完整操作，太慢。
  录一遍 Case A 的完整手算（20 个月那串数字滚动出现），
  Case B / C 直接切到结果表，说一句"同样的算法，只改利率"。
  观众要看的是方法，不是看你按二十次计算器。
"""


# ================================================================ 卡 4 三个人
PERSONAS = """THREE PEOPLE, ONE NUMBER — 三个人，同一个数字

三个人都欠 $8,000，每个月都能多拿出 $500。唯一的区别是利率。
利率一变，答案就变 —— 这就是整支视频要说的事。

三个人的利率都来自同一张官方表格（Federal Reserve G.19 · Terms of Credit），
见 f3-2 数据快照。

----------------------------------------------------------------
MAYA · 32 岁 · 设计师
  欠什么  信用卡，$8,000
  利率    22% APR
          （G.19：Credit card plans · Accounts assessed interest = 22.15%）
  她的话  "我每个月还五百，感觉永远还不完。"
  实算    20 个月还清，总利息 $1,556
  首月    $500 里有 $146.67 是利息，只有 $353.33 真正还了本金
  另一条路 把这 $500 拿去投资 20 个月（假设 7%）：期末 $10,574，赚 $574
  差额    $1,556 − $574 = $982
          → 还债多出来的这 $982，就是「确定性溢价」
  答案    先还债。没有悬念。

  如果按 22.15%（官方精确值）算：20 个月，总利息 $1,569，差额 $995。
  结论不变。视频里说 22% 是为了好记，两个数都能站得住。

----------------------------------------------------------------
DEVON · 45 岁 · 有两辆车
  欠什么  车贷，$8,000
  利率    7% APR
          （G.19：Commercial bank interest rates · New car loans 60-month = 7.14%）
  他的话  "利率不算高，是不是该去投资？"
  实算    17 个月还清，总利息 $423
  另一条路 同样 17 个月投出去（假设 7%）：赚 $408
  差额    $423 − $408 = $15
          → 两条路几乎打平。这时候决定因素不是算术，是别的东西。
  答案    打平。看第 3 格（公司配不配）来打破僵局。
          如果公司配 50%，先拿满 match —— 那是立刻到账的 50%。

  按 7.14%（官方精确值）算：17 个月，总利息 $432，差额 $24。
  还是打平。这个结论对"到底是 7% 还是 7.14%"不敏感 —— 正因为不敏感，
  才值得在视频里说"打平"。

----------------------------------------------------------------
PRIYA · 29 岁 · 研究生刚毕业
  欠什么  学生贷，$8,000
  利率    3.5% APR
          ⚠️ 这个数不在 G.19 里。G.19 只统计商业银行消费信贷。
             联邦学生贷款利率由教育部按学年设定，要另外查。
             发布前请核对当期利率；核对不到就在口播里明说"这是假设值"。
  她的话  "大家都说低息贷款慢慢还，把钱拿去投资。"
  实算    17 个月还清，总利息 $205
  另一条路 同样 17 个月投出去（假设 7%）：赚 $408
  差额    $408 − $205 = $203，投资方多
          → 数学上投资赢，但只赢 $203，而且这个 7% 是我假设的。
  答案    数学上投资略赢。但"略赢"要押上的是确定性。
          如果她这笔钱三年内要用（买房、生小孩），答案立刻反转。

----------------------------------------------------------------
三个人摆在一起，观众自己就能看出规律：
  利率越高 → 还债越划算
  利率越低 → 越接近打平，越要靠"这笔钱什么时候要用"来定

这条规律比任何一句结论都记得住。
"""

MAYA_IMG_EN = (
    "A 3D animated cartoon cow character in a navy-blue vest sitting at a tidy desk, looking worried, "
    "a single credit card statement face down on the desk, a calculator showing a large number, "
    "warm study lamplight, soft shadows, concerned but not despairing expression"
) + IMG_SUFFIX_EN
MAYA_IMG_ZH = (
    "一只 3D 卡通奶牛角色穿深蓝马甲坐在整洁的书桌前，神情担忧，桌上反扣着一张信用卡账单，"
    "计算器上显示一个大数字，温暖的台灯光，柔和阴影，忧虑但不绝望的表情"
) + IMG_SUFFIX_ZH

DEVON_IMG_EN = (
    "A 3D animated cartoon cow character in a navy-blue vest standing beside two small cars in a driveway, "
    "holding a loan document, thoughtful expression, late afternoon light, tidy suburban background"
) + IMG_SUFFIX_EN
DEVON_IMG_ZH = (
    "一只 3D 卡通奶牛角色穿深蓝马甲站在车道上两辆小汽车旁，手里拿着一份贷款文件，若有所思的表情，"
    "傍晚光线，整洁的郊区背景"
) + IMG_SUFFIX_ZH

PRIYA_IMG_EN = (
    "A 3D animated cartoon cow character in a navy-blue vest at a standing desk, a graduation certificate "
    "on the wall behind, a laptop showing a rising chart, calm confident expression, morning light"
) + IMG_SUFFIX_EN
PRIYA_IMG_ZH = (
    "一只 3D 卡通奶牛角色穿深蓝马甲站在升降桌前，身后墙上挂着毕业证书，"
    "笔记本电脑上显示一条上升的曲线，平静自信的表情，清晨光线"
) + IMG_SUFFIX_ZH


# ================================================================ 卡 4 计算表
CASE_TABLE = """CASE COMPARISON — 三个案例（数字已实算，可复算）

输入（三个案例只有利率不同）：
  Balance          $8,000
  Monthly payment  $500
  Only the APR changes.

  案例   人物      APR     还清月数   总利息     首月利息   首月本金   同额投资(假设7%)   结论
  ------------------------------------------------------------------------------------------
  A      Maya      22.0%     20      $1,556     $146.67    $353.33      $10,574        还债赢 $982
  B      Devon      7.0%     17      $  423     $ 46.67    $453.33      $ 8,908        几乎打平
  C      Priya      3.5%     17      $  205     $ 23.33    $476.67      $ 8,908        投资赢 $203

"同额投资"列 = 把同一个 $500 拿去投资同样月数，按年化 7% 假设的期末价值。
差额 = 总利息 − 投资收益。正数说明还债划算，负数说明投资划算（数学上）。

----------------------------------------------------------------
如果用 G.19 的官方精确值（22.15% / 7.14%），结论完全不变：

  A  Maya   22.15%  →  20 个月，$1,569，差额 $995   （还债赢）
  B  Devon   7.14%  →  17 个月，$  432，差额 $ 24   （还是打平）
  C  Priya   3.5%   →  17 个月，$  205，差额 −$204  （投资略赢）

  这两个版本你用哪个都行。视频里用整数版（22% / 7%）更好记，
  但你要能说出"官方值是 22.15%"，别被人抓住说你瞎编。

----------------------------------------------------------------
复算方法（你可以在视频里把这段念出来，也可以放屏幕角落）：

  每月利息 = 剩余本金 × (APR ÷ 12)
  每月本金 = 月供 − 每月利息
  重复到本金归零，数一下跑了几个月

  例（Case A 第一个月）：
    $8,000 × (22% ÷ 12) = $8,000 × 0.018333 = $146.67  ← 利息
    $500 − $146.67 = $353.33                            ← 真正还掉的本金
    剩余本金 = $8,000 − $353.33 = $7,646.67
  这样跑 20 次，本金归零，总利息 $1,556。

本项目的 `_build/fin_numbers.py` 就是这段算法，改任何输入重跑即可。
别手改这张表里的数字 —— 改输入，重跑脚本。

----------------------------------------------------------------
必须同时出现在屏幕上的两句话：
  · 22% 是写在官方表格里的，是确定的
  · 7% 是我假设的，是预期的
这两句话不在，这张表就是在误导人。
"""

CHART_IMG_EN = (
    "A clean side-by-side bar chart on a dark background: three pairs of bars labelled 22%, 7%, 3.5%, "
    "one bar in each pair showing total interest paid in terracotta, the other showing assumed investment "
    "gain in teal, a thin dotted line marking where the two bars are equal, minimal gridlines, "
    "no readable numbers, editorial data visualization"
) + IMG_SUFFIX_EN
CHART_IMG_ZH = (
    "一张干净的并排条形图，深色背景：三组条形分别标注 22%、7%、3.5%，"
    "每组的左条用陶土色表示总利息，右条用青绿色表示假设投资收益，"
    "一条细虚线标出两者相等的位置，极简网格线，无可读数字，杂志级数据可视化"
) + IMG_SUFFIX_ZH


# ================================================================ 卡 5 三个陷阱（示例条款）
SAMPLE_OFFER = """SAMPLE DOCUMENT 1 / 3 — 0% 促销 offer（我写的，随便截图）

------------------------------------------------------------
                    NORTHGATE CREDIT UNION
               Visa Platinum — Balance Transfer Offer
------------------------------------------------------------

  0% introductory APR on balance transfers for 18 months
  from the date of your first transfer.

  Balance transfer fee:
      3% of the amount of each transfer,
      minimum $10.

  After the introductory period ends:
      Purchase and Balance Transfer APR: 21.99% variable

  Minimum payment:
      2% of the balance, or $25, whichever is greater.

  Late payment penalty: up to $41.
------------------------------------------------------------
THIS IS A FICTIONAL DOCUMENT CREATED FOR A TUTORIAL VIDEO.
------------------------------------------------------------

三个要圈的字段（视频里用红框）：

  1. 促销截止：18 months from the date of your first transfer
     → 不是从你申请那天算，是从第一笔转账到账那天算。差一周就是一周。

  2. 手续费：3% of the amount of each transfer, minimum $10
     → $8,000 转过去，立刻先欠 $240。这不是利息，是确定的成本。
     → $240 ÷ $8,000 ÷ 1.5 年 = 每年 2.00%
     → 所以对 Maya 来说，付 $240 换 18 个月免息，远比留在 22% 上划算。
       前提是：18 个月内还得清。

  3. 促销后利率：21.99% variable
     → 这才是真正的陷阱。18 个月后还剩多少，就按 21.99% 重新开始滚。
     → 很多人第 19 个月发现余额比转账时还高，就是因为没在第 18 个月还清。

  上面三个数（$240 / 2.00% / 18 个月）都由 fin_numbers.py 实算，不是估的。
"""

SAMPLE_STATEMENT = """SAMPLE DOCUMENT 2 / 3 — 账单的利率段（我写的，随便截图）

------------------------------------------------------------
                    NORTHGATE CREDIT UNION
                     Monthly Statement
------------------------------------------------------------
  Account ending                          •••• 4417
  Statement period                   Jun 12 – Jul 11
  New balance                              $8,000.00
  Minimum payment due                        $160.00
  Payment due date                            Aug 06
------------------------------------------------------------
  INTEREST CHARGE CALCULATION

  Balance type              APR            Interest charged
  ---------------------------------------------------------
  Purchases               21.99% (V)              $146.67
  Balance transfers        0.00%                    $0.00
  Cash advances           27.24% (V)                $0.00
------------------------------------------------------------
  (V) = variable rate, may change with the Prime Rate
------------------------------------------------------------
THIS IS A FICTIONAL DOCUMENT CREATED FOR A TUTORIAL VIDEO.
------------------------------------------------------------

要圈的两个地方：

  绿框 → Purchases 21.99%
     这才是你日常刷卡产生的债的利率。整支视频说的 22% 就是这一格。

  红框 → Cash advances 27.24%
     这是预借现金的利率，比消费高 5 个百分点以上。
     很多人以为自己欠的是 22%，结果因为取过一次现金，
     那部分一直按 27.24% 在滚。

  还有一句容易漏的：(V) = variable rate
     意味着这个 22% 会跟着 Prime Rate 变。
     所以它「确定」，指的是「此刻确定」，不是「永远确定」。
     （这一句正好呼应 f3-2 里"这些数据每个月都会变"。）

------------------------------------------------------------
最低还款那一栏也要给一秒镜头：
  Minimum payment due $160，而 New balance 是 $8,000。
  如果只还最低（2% 余额），按 fin_numbers.py 实算：
  要还约 100 年，总利息 $75,989。
  前 12 个月一共付掉约 $1,744 利息，本金只减少 $159 —— 一年下来几乎原地不动。
"""

SAMPLE_SAVINGS = """SAMPLE DOCUMENT 3 / 3 — 储蓄账户页面（我写的，随便截图）

------------------------------------------------------------
              NORTHGATE CREDIT UNION — Savings
------------------------------------------------------------
  Account: Everyday Savings •••• 8820
  APY (Annual Percentage Yield) ............  4.00%
  Interest earned this year ................    $61.22
  Current balance .........................  $3,050.00
------------------------------------------------------------
THIS IS A FICTIONAL DOCUMENT CREATED FOR A TUTORIAL VIDEO.
------------------------------------------------------------

绿框圈住：APY 4.00%

要说的那句话：
  "你的存款在赚 4%，你的卡在收 22%。
   这中间 18 个百分点的差，是真实存在的。
   这不是哪个更划算的问题 —— 这是两个不同量级的问题。"

------------------------------------------------------------
一个常见的反驳，提前准备：
  观众会想「那我把存款全部拿去还卡债不就行了？」
  答：不行。清空 emergency fund 去还债，下一笔意外支出会让你
      再把卡刷回来，而且那时是新消费、没有免息期。
      顺序是：先留 buffer，再谈还债。这也是卡 7 五步的第一步。
"""


# ================================================================ 卡 6 401(k)
SAMPLE_PLAN_DOC = """SAMPLE DOCUMENT — 401(k) 计划条款（我写的，不用去找真文件）

------------------------------------------------------------
           RIVERSIDE MANUFACTURING 401(k) PLAN
              Summary Plan Description (excerpt)
------------------------------------------------------------

  SECTION 6 — EMPLOYER CONTRIBUTIONS

  6.1  Matching Contributions.
       The Employer will contribute to your account
       an amount equal to 50% of your Elective Deferrals,
       up to 6% of your Eligible Compensation for each
       pay period.

  6.2  Example.
       If your Eligible Compensation is $5,000 per month
       and you defer 6% ($300), the Employer contributes
       $150 for that period.

  6.3  Vesting.
       Matching Contributions vest according to the
       following schedule:
           Less than 1 year of service .......  0%
           1 year ...........................  25%
           2 years ..........................  50%
           3 years ..........................  75%
           4 or more years .................. 100%

  SECTION 9 — FEES
  9.1  Administrative fee: $18 per quarter, deducted
       from your account.
  9.2  Fund expense ratios: ranging from 0.04% to 0.62%
       annually, depending on the fund selected.

------------------------------------------------------------
THIS IS A FICTIONAL DOCUMENT CREATED FOR A TUTORIAL VIDEO.
------------------------------------------------------------

要圈的三处：
  1. 「50% of your Elective Deferrals, up to 6%」← 匹配公式
  2. Vesting 表 ← 什么时候才真正属于你
  3. Fees 段 ← 0.04% 到 0.62%，差 15 倍，长期差别巨大

注意 6.2 里的数字：月薪 $5,000 × 6% = $300 自缴，公司配 $150。
这个算式是可以直接在镜头前手算出来的，不用计算器 —— 因为它是乘一半。
"""

IRS_2026 = f"""IRS 2026 年限额（{VERIFIED_ON} 实抓核对，每年会调）

  来源  IRS · Retirement topics - 401(k) and profit-sharing plan
        contribution limits
  网址  https://www.irs.gov/retirement-plans/plan-participant-employee/
        retirement-topics-401k-and-profit-sharing-plan-contribution-limits

----------------------------------------------------------------
  · 员工自缴上限（elective deferral，2026 年）............ $24,500
  · SIMPLE 401(k) 自缴上限（2026 年）..................... $17,000
  · 50 岁及以上追加（catch-up，2026 年）.................. $ 8,000
  · 60–63 岁的更高追加额（SECURE 2.0，2026 年）........... $11,250
  · 年度总缴款上限（annual additions，2026 年）........... $72,000
    （含 catch-up 为 $80,000；60–63 岁最高 $83,250）
  · 计入缴款的薪酬上限（2026 年）........................ $360,000

----------------------------------------------------------------
IRS 页面上还有一句原文，建议在视频里念出来：

  "Your plan's terms may impose a lower limit on elective deferrals."

  翻成人话：上面这些是【国家允许的上限】，不是【你的计划给你的额度】。
  你的公司可以设得更低。所以「先拿满 match」里的"满"，
  指的是满到公司配比的那个点（比如 6%），不是满到 $24,500。

  这也是为什么 f6-1 那份示例条款里那个"50% up to 6%"才是要圈的地方，
  而不是这个 $24,500。

----------------------------------------------------------------
为什么要放这一页：
  观众里一定有人会去查"401(k) 一年最多能存多少"，
  查到 $24,500，然后回来说你讲错了。
  把这张表给他，顺便解释"上限 ≠ 你的额度"，
  一个潜在的差评就变成一个"这个人真懂"的瞬间。

  注意：IRS 每年调一次这些数（COLA）。发布前请重查，
  页面上写的是 "subject to cost-of-living adjustments"。
"""

MATCH_TABLE = """EMPLOYER MATCH — 立刻到账的那一半

公式：50% of the first 6% of eligible pay

  年薪       月薪      自缴 6%      公司配/月     公司配/年
  --------------------------------------------------------
  $48,000   $4,000     $240        $120        $1,440
  $60,000   $5,000     $300        $150        $1,800
  $85,000   $7,083     $425        $212        $2,550

----------------------------------------------------------------
为什么它排在还债前面：

  Maya 的卡债是 22%。听起来很急。
  但她只要每月自缴 $300，公司立刻配 $150。

  这 $150 是投进去当天就到账的 50% 回报。
  年化不是 50% —— 是「立刻」，比年化更狠。

  市场上没有任何东西能在第一天给你 50%，
  而 22% 的债是按月计的，一个月只吃掉 1.83%。

  所以顺序是：先拿满 match，再回去打 22% 的债。
  这是全片唯一一个"数学上反直觉但确实正确"的地方，
  值得花 20 秒讲清楚。

----------------------------------------------------------------
反过来，如果公司不配（第 3 格填"没有"）：
  那么 Devon 那种 7% 打平的情况，就直接去还债 ——
  因为少了一个确定的 50%，剩下的就只剩假设的 7%。

  一张表，第三格填什么，决定第二格怎么走。

----------------------------------------------------------------
配套要说的两句（不说会误导）：
  · "拿满"指的是满到公司配比的那个点（示例里是 6%），
    不是满到 IRS 的年度上限。IRS 上限见 f6-3。
  · 公司配的那部分要按 vesting 表逐年归属，
    没待满年限就走，不一定全带走。见 f6-1 的 6.3 节。
"""


# ================================================================ 卡 7 五步顺序
FIVE_STEPS = """THE ORDER — 五步，按顺序来

  1. BUFFER
     先留一小笔应急金（哪怕只有 $1,000）。
     没有它，下一笔意外支出会把你打回原点。

  2. MATCH
     拿满公司的退休金匹配。这是立刻到账的 50%，
     任何债务利率在第一天都比不过它。

  3. HIGH-RATE DEBT
     打掉高息债。经验上 APR 超过你"假设投资回报"的那部分，
     优先级最高 —— 因为它是确定的成本。

  4. LOW-RATE DEBT
     低息债慢慢还。3.5% 的学生贷不值得你牺牲流动性去提前还清。

  5. INVEST
     剩下的才拿去投资。而且这里的 7% 是假设，不是承诺。

----------------------------------------------------------------
为什么是这个顺序（一句话版本）：
  确定的先于假设的，立刻到账的先于远期预期的。

----------------------------------------------------------------
白板建议：
  这五步用手写在白板上，边说边写。
  写字的节奏比打字的节奏更容易让人跟得上，
  而且手写的东西观众会截图。打在 PPT 上的不会。
"""

WHITEBOARD_IMG_EN = (
    "A clean whiteboard with five hand-written numbered lines in dark marker, a simple arrow pointing "
    "down the list, a small doodle of a coffee cup at the top and a small upward chart at the bottom, "
    "warm room light, slightly angled perspective, no printed text"
) + IMG_SUFFIX_EN
WHITEBOARD_IMG_ZH = (
    "一块干净的白板，上面用深色马克笔手写着五行带编号的字，一个简单的箭头沿列表向下指，"
    "顶部画了一个小咖啡杯涂鸦，底部画了一条向上的小曲线，温暖的室内光，略微倾斜的视角，无印刷文字"
) + IMG_SUFFIX_ZH


# ================================================================ 卡 8 收尾
DISCLAIMER = """免责声明 —— 放在片尾，也要放在三问表底部

英文：
  This is educational content, not individualized investment advice.
  The 7% return used throughout is an assumption, not a forecast.
  Your numbers will differ. Check them against your own statements.

中文：
  本视频为教育内容，不构成针对个人的投资建议。
  全片使用的 7% 回报率为假设值，不是预测。
  你的数字会不同，请对照你自己的账单核对。

----------------------------------------------------------------
为什么必须放：
  1. 这是金融内容的合规底线，不是可选项
  2. 放了反而更可信 —— 敢说"这是我的假设"的人，
     比说"市场长期年化 10%"的人可信得多
  3. 它能防止观众把 Maya 的 22% 当成自己的情况照做

放在哪：
  · 三问表底部（观众截图时会一起截走）
  · 视频简介第一行
  · 片尾最后一屏，停留至少 3 秒
"""

SOURCES = f"""SOURCES — 可公开核查的来源（{VERIFIED_ON} 逐条打开核对过）

  1. 信用卡利率 / 车贷利率 / 个人贷利率
     Federal Reserve · Consumer Credit - G.19
     ⚠️ 别贴这个：https://www.federalreserve.gov/releases/g19/
        （这个只是发布日历，上面没有表格）
     ✅ 贴这个（当期发布页，日期会变）：
        https://www.federalreserve.gov/releases/g19/20260807
     → 找 "Terms of Credit" 表 → "Commercial bank interest rates" 分组
     → "Credit card plans" → "Accounts assessed interest" 那一行
     → 完整路径与字段逐字记录见 f3-1

  2. 复利计算
     Investor.gov (U.S. SEC) · Compound Interest Calculator
     https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator
     → 政府站点，免费无广告，不采集个人信息
     → 六个输入框分四步，字段逐字清单见 f3-3
     → 注意：Length of Time 的单位是【年】

  3. 退休金缴款限额
     IRS · 401(k) and profit-sharing plan contribution limits
     https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-401k-and-profit-sharing-plan-contribution-limits
     → 2026 年自缴上限 $24,500，catch-up $8,000
     → 每年随通胀调整，发布前重查（见 f6-3）

----------------------------------------------------------------
用来源的三条规矩：
  · 链接要在画面上停留够久，能被暂停后抄下来
  · 引用的是"数据页面"，不是"某篇文章的观点"
  · 如果某个数据你没找到出处，就说"这是我假设的"，
    不要含糊过去 —— 观众分得清，而且会很在意

----------------------------------------------------------------
每季度要做一次的事：
  G.19 每月 5 日左右更新，IRS 限额每年更新一次。
  把下面三件事做成日历提醒：
    □ 打开 G.19 当期发布页，更新 f3-2 数据快照
    □ 如果信用卡利率变动超过 1 个百分点，重录那 15 秒
    □ 每年 1 月查一次 IRS 限额，更新 f6-3
"""

CTA_COPY = """CTA — 收尾 20 秒（对应实操卡 7 / 8）

  口播（英文）：
    "If you want the three-question sheet, comment the word MATH
     and I'll pin the link. Next week: you have three debts and
     enough extra cash to attack exactly one. Which one?"
     ——别问"大家还想看什么"，问一个具体的、有唯一答案的问题。

  口播（中文）：
    "想要那张三问表的，评论区打 MATH，我把链接置顶。
     下期讲：你有三笔欠款，每个月的钱只够多攻一笔，先攻哪一笔？"

----------------------------------------------------------------
画面要配合的三件事：
  1. 评论框里出现 MATH 四个字母（停留 2 秒，够看清）
  2. 三根高度不同的债务柱，问号浮在最矮那根上方
  3. 最后切回三问表，Your number 三格是空的，等着观众填

----------------------------------------------------------------
不要做的三件事：
  · 不要说"关注我获取更多理财知识" —— 空话
  · 不要承诺"下期解答你的具体情况" —— 那就变成个别投资建议了
  · 不要用夸张表情和爆炸音效 —— 金融内容的信任感来自克制
"""


# ================================================================ 组装
CARDS = [
    {
        "id": 1,
        "title": "开场：一个数字（不需要账单）",
        "note": "对应实操卡 1（0:00–0:09）。开场只需要一个数字 —— 不放截图、不放打码账单。一个 22% 比一屏文字有力量，而且观众不会怀疑你在晒别人的账单。",
        "items": [
            {
                "no": "f1-1",
                "kind": "image",
                "name": "opening-22-percent.png",
                "spec": "1920 × 1080 · 全屏只有一个数字",
                "brief_zh": "开场数字卡。巨大的 22% 居中，下面一行小字做「确定 vs 假设」的对照。没有任何其他元素。",
                "img_en": OPENING_CARD_IMG_EN,
                "img_zh": OPENING_CARD_IMG_ZH,
            },
            {
                "no": "f1-2",
                "kind": "doc",
                "name": "opening-card-copy.txt",
                "spec": "两行文案 · 中英对照 · 含 22% 的出处",
                "brief_zh": "数字卡上的两行字，以及「为什么不放账单截图」的三条理由，外加这个 22% 在 G.19 上的具体出处。手写这张卡比打印的更可信。",
                "content": OPENING_CARD,
            },
        ],
    },
    {
        "id": 2,
        "title": "三问表（观众可以暂停跟做）",
        "note": "对应实操卡 2（0:15–0:30）。全片唯一的「作业」。这张表必须同时有 Example 列和留空的 Your number 列 —— 观众要有地方写自己的数。",
        "items": [
            {
                "no": "f2-1",
                "kind": "sheet",
                "name": "three-questions.txt",
                "spec": "3 行 × 3 列 · 白板或表格都行",
                "brief_zh": "三问表模板。三行：最高利率 / 每月能多拿多少 / 公司配不配。最后「第 3 格决定第 2 格怎么走」是全片的转折点。",
                "content": THREE_QUESTIONS,
            },
        ],
    },
    {
        "id": 3,
        "title": "官方数据页 + 复利计算器（可复核性）",
        "note": f"对应实操卡 3（1:25–2:17）。这一卡的全部内容都在 {VERIFIED_ON} 实际打开页面逐字记录过。G.19 那个坑一定要看：日历页上没有表格，表格在当期发布页上。",
        "warn": "页面会改版。每次重录前，请自己再打开一次这两个页面，确认字段名和行标签没变，然后把 fin_assets.py 顶部的 VERIFIED_ON 改成当天日期。",
        "items": [
            {
                "no": "f3-1",
                "kind": "doc",
                "name": "g19-walkthrough.txt",
                "spec": "逐字操作路径 · 含两个口径的脚注原文",
                "brief_zh": "G.19 怎么走到那一行。含最重要的一条：别打开 /releases/g19/，那只是发布日历。要打开的是带日期的当期发布页。两个口径的区别附了脚注 5 英文原文。",
                "content": G19_WALKTHROUGH,
            },
            {
                "no": "f3-2",
                "kind": "sheet",
                "name": "data-snapshot.txt",
                "spec": "数据快照 · 含发布日与数据月的区别",
                "brief_zh": "当期数字快照。信用卡计息账户 22.15%、60 期车贷 7.14% —— 就是 Maya 和 Devon 的利率出处。Priya 的 3.5% 不在这张表上，已标红。",
                "content": DATA_SNAPSHOT,
            },
            {
                "no": "f3-3",
                "kind": "doc",
                "name": "investor-gov-calculator.txt",
                "spec": "六个字段逐字清单 · 三个翻车点",
                "brief_zh": "Investor.gov 复利计算器字段清单。最大的坑：Length of Time 单位是【年】不是【月】，填 20 会算成二十年。",
                "content": CALC_WALKTHROUGH,
            },
        ],
    },
    {
        "id": 4,
        "title": "三个人的故事 + 算术（只改利率）",
        "note": "对应实操卡 4（2:26–3:27）。整支视频的骨架。三个人都欠 $8,000、每月都能多还 $500，只有利率不同 —— 这样「利率才是变量」不用解释就能看见。",
        "warn": "Priya 的 3.5% 没有官方出处（G.19 不含联邦学生贷）。发布前请自行核对当期联邦学生贷款利率，或在口播里明说「这是假设值」。Maya 和 Devon 的利率都有出处。",
        "items": [
            {
                "no": "f4-1",
                "kind": "doc",
                "name": "three-personas.txt",
                "spec": "3 个人物档案 · 每个利率都标了出处",
                "brief_zh": "三个人物 + 各自实算结果 + 利率出处。Maya 22%（G.19 计息账户 22.15%）/ Devon 7%（G.19 车贷 7.14%）/ Priya 3.5%（无官方出处，已标红）。",
                "content": PERSONAS,
            },
            {
                "no": "f4-2",
                "kind": "image",
                "name": "persona-maya.png",
                "spec": "Maya · 32 岁 · 22% 卡债",
                "brief_zh": "Maya 的人物插画。桌上一张反扣的账单 + 一个大数字的计算器，神情担忧但不绝望。",
                "img_en": MAYA_IMG_EN,
                "img_zh": MAYA_IMG_ZH,
            },
            {
                "no": "f4-3",
                "kind": "image",
                "name": "persona-devon.png",
                "spec": "Devon · 45 岁 · 7% 车贷",
                "brief_zh": "Devon 的人物插画。车道上两辆车 + 手里的贷款文件，若有所思。",
                "img_en": DEVON_IMG_EN,
                "img_zh": DEVON_IMG_ZH,
            },
            {
                "no": "f4-4",
                "kind": "image",
                "name": "persona-priya.png",
                "spec": "Priya · 29 岁 · 3.5% 学生贷",
                "brief_zh": "Priya 的人物插画。升降桌 + 墙上的毕业证书 + 屏幕上的上升曲线，平静自信。",
                "img_en": PRIYA_IMG_EN,
                "img_zh": PRIYA_IMG_ZH,
            },
            {
                "no": "f4-5",
                "kind": "sheet",
                "name": "case-comparison.txt",
                "spec": "3 案例 × 7 列 · 整数版与官方精确版两套",
                "brief_zh": "三案例对比表。A: 22% → 20 个月 / $1,556；B: 7% → 17 个月 / $423；C: 3.5% → 17 个月 / $205。附 22.15% / 7.14% 的精确版，结论不变。",
                "content": CASE_TABLE,
            },
            {
                "no": "f4-6",
                "kind": "image",
                "name": "comparison-chart.png",
                "spec": "并排条形图 · 无数字版",
                "brief_zh": "对比图表。左右条分别表示「总利息」和「假设投资收益」，虚线标出两者相等的位置 —— 那个交叉点就是全片的转折点。",
                "img_en": CHART_IMG_EN,
                "img_zh": CHART_IMG_ZH,
            },
            {
                "no": "f4-7",
                "kind": "doc",
                "name": "how-to-recalculate.txt",
                "spec": "三种复算方式 + 录屏建议",
                "brief_zh": "复算方法。录屏建议：Case A 完整手算一遍，B/C 直接切结果表 —— 观众要看方法，不是看你按二十次计算器。",
                "content": RECALC_NOTE,
            },
        ],
    },
    {
        "id": 5,
        "title": "三个陷阱（用我写好的示例条款讲）",
        "note": "对应实操卡 5（3:45–4:50）。这一整卡都不需要你去找真实文件。下面三份「示例文档」是我写的内容，你复制到任意编辑器里截图就是一份看起来很真的账单 —— 而且完全在你掌控之下。",
        "warn": "如果你的频道做中文，示例里的机构名 Northgate / Riverside 都是我编的，可以直接改成本地化的名字。重点是那几个字段，不是机构名。",
        "items": [
            {
                "no": "f5-1",
                "kind": "doc",
                "name": "sample-01-zero-percent-offer.txt",
                "spec": "示例 0% 促销 offer",
                "brief_zh": "三处要圈：促销期从「第一笔转账到账日」算起、3% 手续费（$8,000 → 立刻欠 $240，折算 2.00%/年）、促销后 21.99% 才是真陷阱。",
                "content": SAMPLE_OFFER,
            },
            {
                "no": "f5-2",
                "kind": "doc",
                "name": "sample-02-statement-apr.txt",
                "spec": "示例账单的利率段",
                "brief_zh": "绿圈 Purchase APR 21.99%，红圈 Cash Advance 27.24%。还有那句 (V) variable rate —— 22% 是「此刻确定」，不是「永远确定」。",
                "content": SAMPLE_STATEMENT,
            },
            {
                "no": "f5-3",
                "kind": "doc",
                "name": "sample-03-savings-apy.txt",
                "spec": "示例储蓄账户页面",
                "brief_zh": "APY 4% vs 卡上 22%，差的 18 个百分点是两个量级的问题。文末预埋了观众会有的反驳（「那我把存款全还了不就行了」）和回答。",
                "content": SAMPLE_SAVINGS,
            },
        ],
    },
    {
        "id": 6,
        "title": "401(k) match（用示例计划条款讲）",
        "note": "对应实操卡 6（5:00–6:15）。不需要去找真实的计划文件。下面这份示例条款是我写的，复制截图即可。这一卡是全片唯一「数学上反直觉但确实正确」的地方，值得花时间讲。",
        "items": [
            {
                "no": "f6-1",
                "kind": "doc",
                "name": "sample-401k-plan-excerpt.txt",
                "spec": "示例计划条款（含 vesting 与费用段）",
                "brief_zh": "三处要圈：50% up to 6% 的匹配公式、vesting 四年归属表、0.04%–0.62% 的费用区间（差 15 倍）。6.2 节那个 $5,000 × 6% = $300 的算式可以直接在镜头前手算。",
                "content": SAMPLE_PLAN_DOC,
            },
            {
                "no": "f6-2",
                "kind": "sheet",
                "name": "match-table.txt",
                "spec": "三档年薪的匹配金额",
                "brief_zh": "$60,000 年薪 → 自缴 $300/月 → 公司配 $150/月 = $1,800/年。关键是这句：市场没有任何东西能在第一天给你 50%，而 22% 的债一个月只吃掉 1.83%。",
                "content": MATCH_TABLE,
            },
            {
                "no": "f6-3",
                "kind": "doc",
                "name": "irs-2026-limits.txt",
                "spec": "IRS 2026 年限额 · 实抓核对",
                "brief_zh": "2026 年自缴上限 $24,500 / catch-up $8,000 / 60–63 岁 $11,250 / 总缴款 $72,000。重点是 IRS 那句原文：计划条款可以设得更低 —— 上限不等于你的额度。",
                "content": IRS_2026,
            },
        ],
    },
    {
        "id": 7,
        "title": "五步顺序（白板手写）",
        "note": "对应实操卡 6 的收尾段。这五步建议手写 —— 写字的节奏比打字更容易跟上，而且手写的东西观众会截图，打在 PPT 上的不会。",
        "items": [
            {
                "no": "f7-1",
                "kind": "doc",
                "name": "five-steps-order.txt",
                "spec": "5 步 · 按顺序",
                "brief_zh": "buffer → match → high-rate debt → low-rate debt → invest。一句话版本：确定的先于假设的，立刻到账的先于远期预期的。",
                "content": FIVE_STEPS,
            },
            {
                "no": "f7-2",
                "kind": "image",
                "name": "whiteboard-five-steps.png",
                "spec": "白板手写图",
                "brief_zh": "五步白板。手写编号 + 向下的箭头 + 顶部咖啡杯涂鸦 + 底部上升小曲线。",
                "img_en": WHITEBOARD_IMG_EN,
                "img_zh": WHITEBOARD_IMG_ZH,
            },
        ],
    },
    {
        "id": 8,
        "title": "收尾：免责声明 + 可核查来源 + CTA",
        "note": "对应实操卡 7（6:15–6:36）与实操卡 8（6:41–6:53）。这三件直接决定这支视频能不能长期放在频道上。免责声明不是可选项，来源链接必须是真的，CTA 必须是一个具体动作。",
        "warn": "SOURCES 里 G.19 的链接是【当期发布页】（带日期），不是日历页。日历页上没有任何表格 —— 贴错链接会让观众点进去什么都找不到。",
        "items": [
            {
                "no": "f8-1",
                "kind": "doc",
                "name": "disclaimer.txt",
                "spec": "中英双语 · 三处位置",
                "brief_zh": "免责声明。放三问表底部（观众截图会一起截走）+ 视频简介第一行 + 片尾停留 3 秒。敢说「这是我的假设」比说「市场长期年化 10%」可信得多。",
                "content": DISCLAIMER,
            },
            {
                "no": "f8-2",
                "kind": "doc",
                "name": "sources.txt",
                "spec": "3 个真实可查的官方来源 + 季度维护提醒",
                "brief_zh": "Federal Reserve G.19 当期发布页（信用卡 / 车贷利率）、Investor.gov 复利计算器（SEC 官方）、IRS 401(k) 限额页。三条都是逐条打开核对过的真链接。",
                "content": SOURCES,
            },
            {
                "no": "f8-3",
                "kind": "doc",
                "name": "cta-copy.txt",
                "spec": "中英双语 · 三要三不要",
                "brief_zh": "收尾 20 秒的口播与画面配合。核心：问一个具体的、有唯一答案的问题（先攻哪一笔），不要问「还想看什么」。",
                "content": CTA_COPY,
            },
        ],
    },
]
