# MemeSpin 🎰

A sleek and simple Python Flask web application that generates random memes at the click of a button. Built using the popular public [Meme API](https://meme-api.com/), it dynamically fetches and displays hilarious content with a clean, responsive UI.

## Features ✨
- **One-Click Generation**: Fetch a random meme instantly.
- **Clean Interface**: A modern, beginner-friendly front-end with responsive styling.
- **Loading UI**: Visual feedback lets you know when your fresh meme is being fetched.
- **Graceful Error Handling**: Manages network connection or API errors safely without breaking the app.

## Project Structure 📂
```text
MemeSpin/
├── app.py               # Main Flask application logic (Routing & API fetch)
├── requirements.txt     # Python dependencies
└── templates/
    └── index.html       # Frontend interface with Jinja2 templating
```

## Getting Started 🚀

### Prerequisites
Make sure you have Python 3.7+ installed on your system.

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Soutikkk/MemeSpin.git
   cd MemeSpin
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application:**
   ```bash
   python app.py
   ```

4. **View the App:**
   Open your browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Technologies Used 🛠
- **Backend:** Python, Flask, Requests
- **Frontend:** HTML, Vanilla CSS, JavaScript (Vanilla), Jinja2
- **Data Source:** [Meme-API](https://github.com/D3vd/Meme_Api)

## License 📄
This project is open-source. Feel free to fork, expand, and modify it!
