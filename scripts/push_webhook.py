#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
push_webhook.py — 把热点看台报告推送到企微/飞书机器人
用法:
    python3 push_webhook.py <report_html_path> [summary_json]

- 读取同目录 config.json 的 webhook_url / webhook_type。
- webhook_url 仍为占位符时，只打印提示并退出（不报错）。
- wecom: 发 Markdown 摘要；若 HTML 文件存在，再上传并发送文件。
- feishu: 发 text 摘要（飞书自定义机器人文件上传需 tenant，脚本内仅发文本）。
- 任何网络异常都优雅降级，打印但不以非零码退出，避免定时任务硬失败。
纯标准库（urllib）。
"""
import json
import sys
import os
import urllib.request
import urllib.error
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), "r", encoding="utf-8") as f:
        return json.load(f)


def is_placeholder(v):
    return (not v) or str(v).startswith("YOUR_")


def http_post(url, payload, is_json=True, files=None):
    data = None
    headers = {"User-Agent": "WorkBuddy-Hotspot/1.0"}
    if files:
        # 简易 multipart（用于企微文件上传）
        boundary = "----wbhotspotboundary"
        body = b""
        for fk, fv in files.items():
            body += f"--{boundary}\r\n".encode()
            body += f'Content-Disposition: form-data; name="{fk}"; filename="{os.path.basename(fv)}"\r\n'.encode()
            body += b"Content-Type: application/octet-stream\r\n\r\n"
            with open(fv, "rb") as fh:
                body += fh.read()
            body += b"\r\n"
        body += f"--{boundary}--\r\n".encode()
        headers["Content-Type"] = f"multipart/form-data; boundary={boundary}"
        data = body
    else:
        if is_json:
            headers["Content-Type"] = "application/json; charset=utf-8"
            data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", "ignore")


def build_markdown(spec, html_path, report_url=""):
    date = spec.get("date", datetime.now().strftime("%Y-%m-%d"))
    rtype = "每日选题推荐" if spec.get("type", "daily") == "daily" else "月度爆款选题盘点"
    lines = [f"## 📡 {rtype} · {date}", ""]
    for p in spec.get("panels", []):
        lines.append(f"**{p.get('label','')}** （{p.get('handle','')}）")
        # 新 schema：直接列出筛选表中 verdict 以「做」开头的选题
        for r in p.get("screening", []):
            verdict = r.get("verdict", "")
            if verdict.startswith("做"):
                lines.append(f"- ✅ {r.get('topic','')}　→　{verdict}")
        lines.append("")
    if report_url:
        lines.append(f"🌐 完整排版报告（点开看）：{report_url}")
    else:
        lines.append(f"📄 完整报告（含信号/趋势/痛点/筛选表/比例）：{html_path}")
    lines.append("> 由 WorkBuddy AI 自动生成 · 灵感选题用途")
    return "\n".join(lines)


def send_wecom(webhook, spec, html_path):
    # 1) Markdown 摘要
    md = build_markdown(spec, html_path)
    http_post(webhook, {"msgtype": "markdown", "markdown": {"content": md}})
    print("✅ 企微 Markdown 摘要已发送")
    # 2) 上传并发送 HTML 文件
    if html_path and os.path.exists(html_path):
        try:
            from urllib.parse import urlparse, parse_qs
            key = parse_qs(urlparse(webhook).query).get("key", [None])[0]
            if key:
                up = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={key}&type=file"
                res = http_post(up, None, is_json=False, files={"media": html_path})
                media_id = json.loads(res).get("media_id")
                if media_id:
                    http_post(webhook, {"msgtype": "file", "file": {"media_id": media_id}})
                    print("✅ 企微 HTML 文件已发送")
        except Exception as e:
            print(f"⚠️ 企微文件发送跳过：{e}")


def send_feishu(webhook, spec, html_path, report_url=""):
    md = build_markdown(spec, html_path, report_url)
    # 飞书自定义机器人 text 类型
    resp = http_post(webhook, {"msg_type": "text", "content": {"text": md}})
    print(f"📨 飞书返回: {resp}")
    print("✅ 飞书 text 摘要已发送")


def main():
    if len(sys.argv) < 2:
        print("用法: python3 push_webhook.py <report_html_path> [summary_json]", file=sys.stderr)
        sys.exit(1)
    html_path = sys.argv[1]
    summary_path = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        cfg = load_config()
    except Exception as e:
        print(f"⚠️ 无法读取 config.json：{e}")
        sys.exit(0)

    webhook = cfg.get("webhook_url", "")
    wtype = cfg.get("webhook_type", "wecom")
    report_url = cfg.get("report_url", "")
    if is_placeholder(webhook):
        print("⏭️ webhook_url 仍为占位符，跳过推送（仅生成报告）。请在 config.json 填入真实 Webhook 后重试。")
        sys.exit(0)

    spec = {}
    if summary_path and os.path.exists(summary_path):
        with open(summary_path, "r", encoding="utf-8") as f:
            spec = json.load(f)

    try:
        if wtype == "feishu":
            send_feishu(webhook, spec, html_path, report_url)
        else:
            send_wecom(webhook, spec, html_path)
    except urllib.error.URLError as e:
        print(f"⚠️ 推送网络错误（已降级）：{e}")
    except Exception as e:
        print(f"⚠️ 推送异常（已降级）：{e}")


if __name__ == "__main__":
    main()
