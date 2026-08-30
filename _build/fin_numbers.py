# -*- coding: utf-8 -*-
"""金融频道数字核算：所有写进素材清单的数字都在这里算出来，可被复算验证。

原则：任何一个数字出现在视频里之前，先在这里跑一遍。
如果脚本输出和素材里写的对不上，以脚本为准。

运行：python3 _build/fin_numbers.py
"""


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
            return None  # 月供不够覆盖利息，永远还不清
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


def main():
    print("=" * 74)
    print("案例对比：余额 $8,000，月供 $500，只改 APR")
    print("=" * 74)
    print(f"{'CASE':<8}{'APR':>7}{'月数':>7}{'总利息':>12}{'首月利息':>11}{'首月本金':>11}")
    results = {}
    for label, apr in (("A", 22.0), ("B", 7.0), ("C", 3.5)):
        res = payoff(8000, apr, 500)
        months, ti, fi, fp = res
        results[label] = (months, ti, fi, fp)
        print(f"{label:<8}{apr:>6.1f}%{months:>7}{ti:>12,.2f}{fi:>11,.2f}{fp:>11,.2f}")

    print()
    print("=" * 74)
    print("同一笔 $500/月，如果拿去投资而不是还债（假设年化 7%，非保证）")
    print("=" * 74)
    for label in ("A", "B", "C"):
        months = results[label][0]
        fv = future_value(500, 7.0, months)
        contributed = 500 * months
        gain = fv - contributed
        print(f"  Case {label}: 投 {months} 个月 → 本金 ${contributed:,}  期末 ${fv:,.0f}  收益 ${gain:,.0f}")

    print()
    print("=" * 74)
    print("差额：还 Case A 的债 vs 拿去投资（同 7% 假设）")
    print("=" * 74)
    ma, tia, fia, _ = results["A"]
    fv_a = future_value(500, 7.0, ma)
    print(f"  还债：省下利息 ${tia:,.0f}（这是确定的，账单上写着 APR）")
    print(f"  投资：{ma} 个月预期收益 ${fv_a - 500 * ma:,.0f}（假设 7%，可能更高也可能更低）")
    print(f"  差值：${tia - (fv_a - 500 * ma):,.0f} —— 还债方多出来的部分，就是「确定性溢价」")

    print()
    print("=" * 74)
    print("401(k) match：50% of the first 6% of eligible pay")
    print("=" * 74)
    for salary in (48000, 60000, 85000):
        monthly = salary / 12
        defer6 = monthly * 0.06
        match_mo = defer6 * 0.5
        print(f"  年薪 ${salary:,} → 月薪 ${monthly:,.0f} → 自缴 6% = ${defer6:,.0f}/月 → 公司配 ${match_mo:,.0f}/月 = ${match_mo * 12:,.0f}/年")
    print("  关键点：这是一笔立刻到账的 50%，任何市场回报在第一天都比不过它。")

    print()
    print("=" * 74)
    print("0% 余额转账陷阱：转 $8,000，手续费 3%，促销期 18 个月")
    print("=" * 74)
    fee = 8000 * 0.03
    print(f"  转账手续费 3% = ${fee:,.0f}（一次性，立刻就欠着）")
    print(f"  实际成本折算年化：${fee:,.0f} ÷ $8,000 ÷ 1.5 年 = {fee / 8000 / 1.5 * 100:.2f}% / 年")
    print(f"  对照：留在 22% APR 的卡上，18 个月利息远高于 ${fee:,.0f}")
    print("  → 只有当「促销期内还得清」成立时，这笔手续费才划算。")

    print()
    print("=" * 74)
    print("复利：每月 $200，年化 7%，不同年限")
    print("=" * 74)
    for years in (10, 20, 30):
        fv = future_value(200, 7.0, years * 12)
        print(f"  {years:>2} 年：本金 ${200 * years * 12:>7,} → 期末 ${fv:>10,.0f} （收益 ${fv - 200 * years * 12:>9,.0f}）")

    print()
    print("=" * 74)
    print("最小还款陷阱：$8,000 @ 22% APR，只还最低（2% 余额或 $25 取大）")
    print("=" * 74)
    r = 0.22 / 12
    bal = 8000.0
    months = 0
    ti = 0.0
    while bal > 0.005 and months < 1200:
        interest = bal * r
        pmt = max(bal * 0.02, 25.0)
        if pmt <= interest:
            print(f"  第 {months} 个月后月供已无法覆盖利息 —— 债务进入只增不减状态")
            break
        bal = bal + interest - pmt
        ti += interest
        months += 1
    print(f"  按 2% 最低还款：约 {months} 个月（{months / 12:.1f} 年），总利息 ${ti:,.0f}")


if __name__ == "__main__":
    main()
