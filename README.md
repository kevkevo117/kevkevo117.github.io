#Kevin Gonzalez Projects 


# 💸 Price Tracker App

A full-stack web app that lets users track product prices and get notified via Discord when prices drop below a specified discount threshold.

---

## 🧠 Features

- ✅ Add any product URL and set your desired discount percentage
- ✅ Scrapes the page to extract name, site, and price
- ✅ Periodic (hourly) price checks in the background
- ✅ Sends alerts to your **Discord server** via webhook
- ✅ Web dashboard to view tracked items
- ✅ “Add to Cart” link redirects to the store

---

## 🛠 Technologies Used

- **Python + Flask** (web server)
- **BeautifulSoup** (scraping)
- **SQLite** (lightweight database)
- **JavaScript** (frontend fetch + interactivity)
- **Discord Webhooks** (notifications)

---

## 🖥 How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/price-tracker-app.git
cd price-tracker-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your Discord Webhook
In `app.py`, replace this line:
```python
DISCORD_WEBHOOK_URL = 
```


### 4. Run the app
```bash
python app.py
```

### 5. (Optional) Run the background checker separately
```bash
python worker.py
```

---

## 🗂 Folder Structure

```
price-tracker-app/
├── app.py               # Main Flask app
├── worker.py            # Optional background thread as separate process
├── templates/
│   └── dashboard.html   # HTML dashboard template
├── static/              # (Optional) frontend assets
├── requirements.txt     # Dependencies
├── Procfile             # For deployment
└── README.md            # Project documentation
```

---

## 🚀 Deployment

You can deploy the app to any Python-friendly host like:
- [Render](https://render.com)
- [Railway](https://railway.app)
- [Fly.io](https://fly.io)

For deployment:
- Use `gunicorn` via the `Procfile`
- Add a background worker to run `worker.py`
- Set your `DISCORD_WEBHOOK_URL` as an environment variable

---

## ⚠️ Notes

- Respect site scraping rules — use at your own risk
- This app is intended for **educational use**

---

## ✍️ Author

**Kevin Gonzalez**  
[GitHub Pages](https://kevkevo117.github.io)
