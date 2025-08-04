from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "ebay_webhook_verify_token_20250804_3qrn_fulfillment_ready"

@app.route("/", methods=["GET", "POST", "HEAD"])
def webhook():
    # eBay 验证请求
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if request.method == "GET":
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Verification failed", 403

    # eBay 推送通知请求
    elif request.method == "POST":
        print("Received POST:", request.json)
        return "OK", 200

    # eBay HEAD 请求验证服务器存活
    elif request.method == "HEAD":
        return "OK", 200

    return "Unsupported method", 405

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  # Render使用此环境变量
    app.run(host="0.0.0.0", port=port)
