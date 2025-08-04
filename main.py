from flask import Flask, request, Response

app = Flask(__name__)

# 替换为你在 eBay 页面设置的 Verification Token
EXPECTED_VERIFY_TOKEN = "ebay_webhook_verify_token_20250804_3qrn_fulfillment_ready"

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # 用于 eBay 验证 webhook endpoint
        verify_token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        mode = request.args.get("hub.mode")

        if verify_token == EXPECTED_VERIFY_TOKEN and mode == "subscribe":
            return Response(challenge, status=200, mimetype="text/plain")
        else:
            return Response("Unauthorized", status=401)

    elif request.method == "POST":
        # 实际收到 eBay 通知的处理逻辑（目前仅日志记录）
        print("Received POST:", request.json)
        return Response("Received", status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

