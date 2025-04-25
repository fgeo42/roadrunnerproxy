from flask import Flask, request, Response
import requests
import os

app = Flask(__name__)

# ScraperAPI URL and your API key
SCRAPER_API_URL = "https://api.scraperapi.com/"
SCRAPER_API_KEY = "48ca6046ca5a586225533ce421ccfd39"  # Replace with your actual API key

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
        # Prepare the payload for ScraperAPI
        payload = {
            'api_key': SCRAPER_API_KEY,
            'url': target_url
        }

        print(f"Fetching: {target_url} via ScraperAPI")

        # Make a request to ScraperAPI to fetch the URL
        resp = requests.get(SCRAPER_API_URL, params=payload, timeout=10)

        # Return the response from ScraperAPI to the user
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
