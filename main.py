
from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "ebay_webhook_verify_token_20250804_3qrn_fulfillment_ready"
"  # 用户指定的 Verification Token

@app.route("/", methods=["GET"])
def verify():
    challenge = request.args.get("challenge_code")
    verify_token = request.args.get("verify_token")
    if verify_token == VERIFY_TOKEN:
        return challenge, 200
    return "Unauthorized", 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
