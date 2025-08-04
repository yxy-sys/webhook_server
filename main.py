from flask import Flask, request

app = Flask(__name__)

# 🛡️ 用于 eBay webhook 验证的 Token（需与你在 eBay Developer 中设定的一致）
VERIFY_TOKEN = "ebay_webhook_verify_token_20250804_3qrn_fulfillment_ready"

@app.route("/", methods=["GET", "POST", "HEAD"])
def webhook():
    print("== Incoming request ==")
    print("Method:", request.method)
    print("Args:", request.args)
    print("JSON:", request.get_json(silent=True))

    # ✅ 处理验证 GET 请求（注册 Webhook 时 eBay 会调用）
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("✅ Verification success")
            return challenge, 200
        else:
            print("❌ Verification failed")
            return "Verification failed", 403

    # ✅ 处理 webhook 推送 POST 请求
    elif request.method == "POST":
        data = request.get_json(silent=True)
        print("📦 Received POST data:", data)
        return "OK", 200

    # ✅ eBay 有时会发送 HEAD 请求检查服务存活
    elif request.method == "HEAD":
        return "OK", 200

    return "Unsupported method", 405

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  # Render 默认使用 PORT 环境变量
    app.run(host="0.0.0.0", port=port)
