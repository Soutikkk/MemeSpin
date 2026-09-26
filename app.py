```python
from flask import Flask, render_template
import requests


# Create the Flask application
app = Flask(__name__)

# Meme API endpoint
MEME_API_URL = "https://meme-api.com/gimme"


def get_random_meme():
    """
    Fetch a random meme from the meme API.

    Returns:
        tuple: (meme_url, title, error)
    """
    try:
        response = requests.get(MEME_API_URL, timeout=10)
        response.raise_for_status()

        meme_data = response.json()

        meme_url = meme_data.get("url")
        title = meme_data.get("title")

        return meme_url, title, None

    except requests.exceptions.RequestException as error:
        print(f"Error fetching meme: {error}")

        return None, None, "Oops! Couldn't fetch a meme right now. Please try again later."


@app.route("/")
def home():
    """Display the homepage without a meme."""
    return render_template(
        "index.html",
        meme_url=None,
        title=None,
        error=None
    )


@app.route("/generate")
def generate_meme():
    """Fetch and display a random meme."""
    meme_url, title, error = get_random_meme()

    return render_template(
        "index.html",
        meme_url=meme_url,
        title=title,
        error=error
    )


# Start the Flask development server
if __name__ == "__main__":
    app.run(debug=True)
```
