#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
可重跑的数字脚本 —— 每日热点看台 2026-09-03 成片包用数
改输入重跑即可，不要在 JSON 里手改数字。

用法: python3 _build/finance_math_2026_09_03.py
"""
from dataclasses import dataclass


def fv_annuity(pmt, rate, years):
    """期末付年金终值。"""
    return pmt * (((1 + rate) ** years - 1) / rate)


def months_to_payoff(bal, apr, monthly_pmt, cap=1200):
    """
    按月计息，返回 (月数, 总利息, 期末余额)。
    月供覆盖不了利息 -> 负摊销，返回 (None, None, 期末余额)。
    """
    r = apr / 12.0
    bal = float(bal)
    paid_interest = 0.0
    for m in range(1, cap + 1):
        interest = bal * r
        paid_interest += interest
        bal = bal + interest - monthly_pmt
        if bal <= 0:
            return m, paid_interest, 0.0
    return None, None, bal


def pmt_to_payoff(bal, apr, months):
    """给定期限，求所需月供。"""
    r = apr / 12.0
    return bal * r / (1 - (1 + r) ** (-months))


# ---------------------------------------------------------------- 场景参数
SALARY          = 60_000      # 年薪
CONTRIB_PCT     = 0.06        # 个人缴款比例
MATCH_RATE      = 0.50        # 雇主配比（每缴 1 元配 0.5 元）
MATCH_CAP_PCT   = 0.06        # 配比上限（薪金的 6%）
LOAN_AMOUNT     = 15_000      # 401(k) 贷款本金
LOAN_YEARS      = 5           # 还款年限（IRS 上限 5 年）
CC_APR          = 0.249       # 信用卡年利率
CC_MONTHLY      = 300         # 现在每月还信用卡的钱
RETURN          = 0.07        # 组合年化假设
HORIZON         = 30          # 到退休的总年限

# ---------------------------------------------------------------- 1. 配比损失
annual_contrib = SALARY * CONTRIB_PCT
annual_match   = SALARY * min(CONTRIB_PCT, MATCH_CAP_PCT) * MATCH_RATE
repay_per_year = LOAN_AMOUNT / LOAN_YEARS
# 假设：为凑出还款现金流，把缴款从 6% 砍到刚好少 repay_per_year
cut_pct        = repay_per_year / SALARY
new_contrib    = annual_contrib - repay_per_year
new_match      = SALARY * min(new_contrib / SALARY, MATCH_CAP_PCT) * MATCH_RATE
match_lost_yr  = annual_match - new_match

# 5 年内少进账户的钱（个人缴款 + 雇主配比）
lost_inflow_yr = repay_per_year + match_lost_yr
# 这 5 年的钱如果留在账户里，到第 30 年末值多少
fv_each = []
for k in range(1, LOAN_YEARS + 1):
    fv_each.append(lost_inflow_yr * ((1 + RETURN) ** (HORIZON - k)))
fv_lost = sum(fv_each)

# ---------------------------------------------------------------- 2. 利率套利 + 负摊销
m, tot_int, end_bal = months_to_payoff(LOAN_AMOUNT, CC_APR, CC_MONTHLY)
cc_years   = m / 12 if m else float("nan")
first_int  = LOAN_AMOUNT * CC_APR / 12          # 首月利息
pmt_60mo   = pmt_to_payoff(LOAN_AMOUNT, CC_APR, LOAN_YEARS * 12)
total_60mo = pmt_60mo * LOAN_YEARS * 12
# 同期 15,000 留在 401(k) 里的机会成本（按 RETURN 计，5 年）
opp_cost_5y = LOAN_AMOUNT * ((1 + RETURN) ** LOAN_YEARS - 1)
spread_pts  = (CC_APR - RETURN) * 100

# ---------------------------------------------------------------- 3. 费率拖累
def fee_drag(bal, r_gross, fee, years):
    return bal * (1 + r_gross) ** years - bal * (1 + r_gross - fee) ** years

drag_100 = fee_drag(100_000, 0.07, 0.0100, 30)
drag_025 = fee_drag(100_000, 0.07, 0.0025, 30)

# ---------------------------------------------------------------- 4. QPLO 现金缺口
OFFSET       = 15_000    # 被 offset 的贷款余额
WITHHOLD     = 0.20      # IRC 3405(c) 强制预扣
cash_in_hand = OFFSET * (1 - WITHHOLD)
gap_to_roll  = OFFSET - cash_in_hand

# ---------------------------------------------------------------- 输出
if __name__ == "__main__":
    print("=" * 66)
    print("每日热点看台 2026-09-03 · 成片包数字（全部由本脚本算出）")
    print("=" * 66)
    print(f"年薪 {SALARY:,} · 缴款 {CONTRIB_PCT:.0%} · 配比 {MATCH_RATE:.0%}(上限{MATCH_CAP_PCT:.0%})")
    print(f"贷款 {LOAN_AMOUNT:,} / {LOAN_YEARS}年 · 信用卡 APR {CC_APR:.1%} · 月供 {CC_MONTHLY}")
    print(f"组合假设 {RETURN:.0%} · 期限 {HORIZON}年")
    print("-" * 66)
    print(f"[1] 年个人缴款            = {annual_contrib:>12,.0f}")
    print(f"[1] 年雇主配比            = {annual_match:>12,.0f}")
    print(f"[1] 年还款额              = {repay_per_year:>12,.0f}")
    print(f"[1] 每年损失配比          = {match_lost_yr:>12,.0f}")
    print(f"[1] 每年少进账户合计      = {lost_inflow_yr:>12,.0f}")
    print(f"[1] 5年后到第{HORIZON}年的终值 ≈ {fv_lost:>12,.0f}   <-- 视频里的数")
    print("-" * 66)
    print(f"[2] 信用卡 {LOAN_AMOUNT:,} @ {CC_APR:.1%}")
    print(f"[2]   首月利息                = {first_int:>12,.2f}")
    print(f"[2]   月供 {CC_MONTHLY} vs 首月利息 {first_int:,.2f} -> ", end="")
    if m is None:
        _, _, bal_12 = months_to_payoff(LOAN_AMOUNT, CC_APR, CC_MONTHLY, cap=12)
        _, _, bal_60 = months_to_payoff(LOAN_AMOUNT, CC_APR, CC_MONTHLY, cap=60)
        print(f"负摊销：还了 12 个月余额 {bal_12:,.0f}，还了 60 个月余额 {bal_60:,.0f}   <-- 视频里的数")
    else:
        print(f"{m} 个月 ({cc_years:.1f} 年)还清，总利息 {tot_int:,.0f}")
    print(f"[2]   要在 {LOAN_YEARS} 年还清所需月供 = {pmt_60mo:>12,.2f}")
    print(f"[2]   {LOAN_YEARS} 年总支出 = {total_60mo:,.0f}，其中利息 = {total_60mo - LOAN_AMOUNT:,.0f}")
    print(f"[2] 同期留在401(k)的机会成本(5年@{RETURN:.0%}) = {opp_cost_5y:,.0f}")
    print(f"[2] 利率差 = {spread_pts:.1f} 个百分点   <-- 套利成立的前提")
    print("-" * 66)
    print(f"[3] 10万本金 30年：费率 1.00% 拖累 = {drag_100:,.0f}")
    print(f"[3] 10万本金 30年：费率 0.25% 拖累 = {drag_025:,.0f}")
    print(f"[3] 两者差额                        = {drag_100 - drag_025:,.0f}")
    print("-" * 66)
    print(f"[4] offset {OFFSET:,} 被预扣 {WITHHOLD:.0%} 后到手 = {cash_in_hand:,.0f}")
    print(f"[4] 想全额 rollover 需自补现金缺口   = {gap_to_roll:,.0f}   <-- 视频里的数")
    print("=" * 66)
