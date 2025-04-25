from flask import Flask, request, Response
import requests
import os

app = Flask(__name__)

# Set this to your proxy app URL (another Heroku app)
PROXY_URL = "http://road-runner-proxy-be-7216c3dea3c7.herokuapp.com:80"

@app.route("/")
def home():
    return """
    <h2>Web Proxy Browser</h2>
    <form action="/browse">
        <input name="url" placeholder="https://example.com" style="width: 300px;">
        <button type="submit">Go</button>
    </form>
    """

@app.route("/browse")
def browse():
    target_url = request.args.get("url")
    if not target_url:
        return "Please provide a ?url=...", 400

    try:
        print(f"Fetching: {target_url} via proxy {PROXY_URL}")

        resp = requests.get(
            target_url,
            proxies={
                "http": PROXY_URL,
                "https": PROXY_URL
            },
            verify=False,
            timeout=10
        )

        return Response(
            resp.content,
            status=resp.status_code,
            content_type=resp.headers.get("Content-Type", "text/html")
        )

    except Exception as e:
        return f"<h3>Error fetching URL:</h3><pre>{str(e)}</pre>", 500

# Run the app using Heroku's dynamic PORT
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
