from flask import Flask, render_template, request
import requests

# Initialize the Flask application
app = Flask(__name__)

# The public API URL to fetch memes
MEME_API_URL = "https://meme-api.com/gimme"

@app.route("/")
def home():
    """
    Renders the homepage. 
    It passes None to the template so it knows not to show a meme yet.
    """
    return render_template("index.html", meme_url=None, title=None, error=None)

@app.route("/generate")
def generate_meme():
    """
    Fetches a random meme from the API and renders the homepage with the meme data.
    """
    meme_url = None
    title = None
    error = None
    
    try:
        # Fetching a random meme from the API
        response = requests.get(MEME_API_URL)
        
        # Raise an exception if the request was unsuccessful (e.g., 404 or 500)
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Extract the image URL and the title
        meme_url = data.get("url")
        title = data.get("title")
        
    except requests.exceptions.RequestException as e:
        # Handle network or API errors gracefully by showing a friendly message
        error = "Oops! Couldn't fetch a meme right now. Please try again later."
        print(f"Error fetching meme: {e}")
        
    # Render the index.html template, passing the variables using Jinja2
    return render_template("index.html", meme_url=meme_url, title=title, error=error)

if __name__ == "__main__":
    # Run the app in debug mode so changes reflect automatically
    app.run(debug=True)
