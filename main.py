from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST", "HEAD"])
def webhook():
    print("== Incoming request ==")
    print("Method:", request.method)
    print("Args:", request.args)
    print("JSON:", request.get_json(silent=True))

    # ✅ 验证 webhook GET 请求
    if request.method == "GET":
        challenge = request.args.get("hub.challenge")
        if challenge:
            return challenge, 200
        else:
            return "No challenge", 400

    # ✅ webhook 推送事件
    elif request.method == "POST":
        return "OK", 200

    # ✅ eBay webhook 校验用 HEAD 请求
    elif request.method == "HEAD":
        return "OK", 200

    return "Unsupported method", 405

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
