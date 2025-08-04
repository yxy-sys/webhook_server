from flask import Flask, request

app = Flask(__name__)

# 用户指定的 Verification Token
VERIFY_TOKEN = "ebay_webhook_verify_token_20250804_3qrn_fulfillment_ready"

@app.route("/", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200
    else:
        return "Verification failed", 403

@app.route("/", methods=["POST"])
def handle_webhook():
    data = request.json
    print("Received webhook:", data)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
