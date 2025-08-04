from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST", "HEAD"])
def webhook():
    print("== Incoming request ==")
    print("Method:", request.method)
    print("Args:", request.args)
    print("JSON:", request.get_json(silent=True))

    challenge = request.args.get("hub.challenge")
    if request.method == "GET" and challenge:
        return challenge, 200

    if request.method == "POST":
        return "OK", 200

    if request.method == "HEAD":
        return "OK", 200

    return "Unsupported method", 405

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  # Render使用此环境变量
    app.run(host="0.0.0.0", port=port)
