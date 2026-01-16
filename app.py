import requests
from flask import Flask, render_template

app = Flask(__name__)

ACCESS_TOKEN = "YOUR_INSTAGRAM_ACCESS_TOKEN"
INSTAGRAM_USER_ID = "loeghaven"

def get_instagram_photos():
    url = f"https://graph.instagram.com/{INSTAGRAM_USER_ID}/media"
    params = {
        "fields": "id,media_type,media_url,permalink",
        "access_token": ACCESS_TOKEN,
        "limit": 9
    }

    response = requests.get(url, params=params)
    print(f"Response {response.status_code}")
    data = response.json()

    photos = []
    for item in data.get("data", []):
        if item["media_type"] == "IMAGE":
            photos.append({
                "url": item["media_url"],
                "link": item["permalink"]
            })

    return photos

@app.route("/")
def home():
    photos = get_instagram_photos()
    return render_template("index.html", title="My Text Site", photos=photos)

@app.route("/changelog")
def changelog():
    changes = [
        {
            "version": "1.0",
            "date": "2026-01-16",
            "items": ["Version 1.0!\n\nVelkommen til :-)"]
        }
    ]

    return render_template("changelog.html", title="Changelog", changes=changes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)