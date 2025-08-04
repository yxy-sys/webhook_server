from flask import Flask, request, jsonify
import hashlib
import os

app = Flask(__name__)

VERIFY_TOKEN = "ebay_webhook_verify_token_20250804_3qrn_fulfillment_ready"
ENDPOINT_URL = os.environ.get("WEBHOOK_URL") or "https://webhook-server-3q1r.onrender.com/"

@app.route("/", methods=["GET", "POST", "HEAD"])
def webhook():
    print("== Incoming request ==")
    print("Method:", request.method)
    print("Args:", request.args)
    print("JSON:", request.get_json(silent=True))

    if request.method == "GET":
        challenge = request.args.get("challenge_code")
        if challenge:
            # 按官方要求生成 challengeResponse
            to_hash = (challenge + VERIFY_TOKEN + ENDPOINT_URL).encode("utf-8")
            resp_hash = hashlib.sha256(to_hash).hexdigest()
            print("✅ Verification success, challengeResponse:", resp_hash)
            return jsonify({"challengeResponse": resp_hash}), 200
        print("❌ Verification failed")
        return "Verification failed", 403

    elif request.method == "POST":
        data = request.get_json(silent=True)
        print("📦 Received POST data:", data)
        return "OK", 200

    elif request.method == "HEAD":
        return "OK", 200

    return "Unsupported method", 405

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
