from flask import Flask, request, Response
import requests

app = Flask(__name__)

# Your proxy address (hosted on Heroku)
PROXY_URL = "https://road-runner-proxy-be-7216c3dea3c7.herokuapp.com:80"

@app.route("/browse")
def browse():
    target_url = request.args.get("url")
    if not target_url:
        return "Please provide a ?url parameter", 400

    try:
        # Make request via your proxy
        resp = requests.get(target_url, proxies={"http": PROXY_URL, "https": PROXY_URL}, timeout=10)
        return Response(resp.content, status=resp.status_code, content_type=resp.headers.get("Content-Type", "text/html"))
    except Exception as e:
        return f"Error fetching URL: {str(e)}", 500

@app.route("/")
def home():
    return """
    <h2>Web Proxy</h2>
    <form action="/browse">
        <input name="url" placeholder="https://example.com" style="width: 300px;">
        <button type="submit">Go</button>
    </form>
    """
    
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
