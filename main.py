from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST", "HEAD"])
def webhook():
    print("== Incoming request ==")
    print("Method:", request.method)
    print("Args:", request.args)
    print("JSON:", request.get_json(silent=True))

    # ✅ 处理 eBay Marketplace Account Deletion webhook 的验证请求
    if request.method == "GET":
        challenge = request.args.get("challenge_code")
        if challenge:
            print("✅ Verification success")
            return challenge, 200
        else:
            print("❌ Verification failed")
            return "Verification failed", 403

    # ✅ 处理 eBay 推送的 webhook 内容
    elif request.method == "POST":
        data = request.get_json(silent=True)
        print("📦 Received POST data:", data)
        return "OK", 200

    # ✅ eBay 用 HEAD 请求检测服务存活
    elif request.method == "HEAD":
        return "OK", 200

    return "Unsupported method", 405

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

