# -*- coding: utf-8 -*-
"""火柴人故事版《7% 法则》数字核算脚本（@TheMoneyMoo / finance-stick）

原则：视频里出现的每一个数字，都必须在这里算出来。改输入重跑，不手改文案里的数字。
运行：python3 _build/stick_numbers.py

口径（写清楚，方便评论区复核）：
  · 余额 $8,000，月供 $500，只改 APR —— 三个人唯一的区别就是利率
  · 计息方式：按月计息，月末结息（美国信用卡 / 分期贷款的标准口径）
  · 投资对照组：每月月末投入同样的 $500，年化 7%（长期、税前、平均值，非保证）
  · 最低还款：账单常见口径 = 余额的 2% 与 $25 取大者
"""

BALANCE = 8000.0      # 三个人欠的本金，完全相同
PAYMENT = 500.0       # 三个人每月能拿出来的钱，完全相同
MARKET = 7.0          # 投资对照组年化假设（非保证）

CASES = (
    ("MAYA", 22.15),   # 信用卡 APR
    ("DEVON", 7.14),   # 二手车分期 / 商户卡
    ("PRIYA", 3.5),    # 信用合作社的老贷款
)


def payoff(balance, apr, payment):
    """按月计息的还款模拟。返回 (月数, 总利息, 首月利息, 首月本金)。"""
    r = apr / 100.0 / 12.0
    bal = float(balance)
    months = 0
    total_interest = 0.0
    first_interest = None
    first_principal = None
    while bal > 0.005 and months < 1200:
        interest = bal * r
        principal = payment - interest
        if principal <= 0:
            return None
        if first_interest is None:
            first_interest = interest
            first_principal = principal
        bal -= principal
        total_interest += interest
        months += 1
    return months, total_interest, first_interest, first_principal


def future_value(pmt, annual_rate, months, start=0.0):
    """每月月末投入 pmt，年化 annual_rate，共 months 个月的期末价值。"""
    r = annual_rate / 100.0 / 12.0
    fv = float(start)
    for _ in range(months):
        fv = fv * (1 + r) + pmt
    return fv


def invest_gain(pmt, annual_rate, months):
    """同样月供拿去投资，months 个月后的净收益（期末价值 - 累计本金）。"""
    return future_value(pmt, annual_rate, months) - pmt * months


def min_payment_trap(balance, apr, pct=0.02, floor=25.0):
    """只还最低还款额：返回 (月数, 年数, 总利息, 首月还款额)。"""
    r = apr / 100.0 / 12.0
    bal = float(balance)
    months = 0
    total_interest = 0.0
    first_pmt = None
    while bal > 0.005 and months < 2400:
        interest = bal * r
        pmt = max(bal * pct, floor)
        if first_pmt is None:
            first_pmt = pmt
        if pmt <= interest:
            return None                      # 月供覆盖不了利息，债务只增不减
        bal = bal + interest - pmt
        total_interest += interest
        months += 1
    return months, months / 12.0, total_interest, first_pmt


def main():
    print("=" * 78)
    print(f"三个人：本金 ${BALANCE:,.0f}　月供 ${PAYMENT:,.0f}　唯一变量 = APR")
    print("=" * 78)
    print(f"{'角色':<8}{'APR':>8}{'月数':>6}{'总利息':>12}{'首月利息':>11}"
          f"{'投资方收益':>12}{'差额':>10}{'结论':>10}")

    rows = {}
    for name, apr in CASES:
        months, ti, fi, _ = payoff(BALANCE, apr, PAYMENT)
        gain = invest_gain(PAYMENT, MARKET, months)
        diff = ti - gain                       # >0 还债赢，<0 投资赢
        verdict = "还债" if diff > 0 else "投资"
        rows[name] = dict(apr=apr, months=months, interest=ti, first_interest=fi,
                          gain=gain, diff=diff, verdict=verdict)
        print(f"{name:<8}{apr:>7.2f}%{months:>6}{ti:>12,.2f}{fi:>11,.2f}"
              f"{gain:>12,.2f}{diff:>+10,.0f}{verdict:>10}")

    print()
    print("=" * 78)
    print("差额读法：正数 = 还债比投资多出来的钱；负数 = 投资比还债多出来的钱")
    print("=" * 78)
    for name in ("MAYA", "DEVON", "PRIYA"):
        r = rows[name]
        print(f"  {name:<6} 还债省利息 ${r['interest']:,.0f}　vs　投资赚 ${r['gain']:,.0f}"
              f"　→ {r['verdict']}赢 ${abs(r['diff']):,.0f}（{r['months']} 个月）")

    print()
    print("=" * 78)
    print("分界线：还债与投资打平的那个 APR（投资按 7% 假设）")
    print("=" * 78)
    lo, hi = 0.0, 30.0
    for _ in range(200):                       # 二分找打平点
        mid = (lo + hi) / 2
        m, ti, _, _ = payoff(BALANCE, mid, PAYMENT)
        if ti - invest_gain(PAYMENT, MARKET, m) > 0:
            hi = mid
        else:
            lo = mid
    print(f"  打平 APR ≈ {(lo + hi) / 2:.2f}%  —— 所以影片里说的「7% 附近」不是拍脑袋")

    print()
    print("=" * 78)
    print(f"最低还款陷阱：${BALANCE:,.0f} @ 22.15% APR，只还 2%（不足 $25 按 $25）")
    print("=" * 78)
    months, years, ti, first_pmt = min_payment_trap(BALANCE, 22.15)
    print(f"  首次还款额 ${first_pmt:,.2f}")
    print(f"  还清需要 {months:,} 个月 ≈ {years:.0f} 年")
    print(f"  总利息 ${ti:,.0f}（本金只有 ${BALANCE:,.0f}）")

    print()
    print("=" * 78)
    print("401(k) 雇主配比：先拿 match 再谈还债（2026 年个人递延上限 $24,500）")
    print("=" * 78)
    for salary in (48000, 70000, 95000):
        monthly = salary / 12
        defer6 = monthly * 0.06
        match_mo = defer6 * 0.5
        print(f"  年薪 ${salary:,} → 自缴 6% = ${defer6:,.0f}/月 → 公司配 ${match_mo:,.0f}/月"
              f" = ${match_mo * 12:,.0f}/年（立刻到账的 50%）")


if __name__ == "__main__":
    main()
