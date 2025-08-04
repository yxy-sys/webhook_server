from flask import Flask, request, Response
import os

app = Flask(__name__)

# 请将此处的 token 替换为你在 eBay 配置页面填写的 Verification Token
VERIFY_TOKEN = "ebay_webhook_verify_token_20250804_3qrn_fulfillment_ready"

@app.route("/", methods=["GET", "HEAD"])
def webhook():
    mode = request.args.get("hub.mode")
    verify_token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if request.method == "HEAD":
        # eBay 会先发 HEAD 请求检测地址是否存在
        return Response(status=200)

    if mode == "subscribe" and verify_token == VERIFY_TOKEN and challenge:
        return Response(challenge, status=200)
    else:
        return Response("Verification failed", status=403)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
