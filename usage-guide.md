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


# Usage Guide: Frontend Dashboard Template

This document contains the HTML and JavaScript code for the dashboard frontend of the Price Tracker app.

---

## Dashboard Template (`templates/dashboard.html`)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Price Tracker Dashboard</title>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            if ('Notification' in window && Notification.permission !== 'granted') {
                Notification.requestPermission();
            }
        });

        async function addItem() {
            const url = document.getElementById('url').value;
            const discount = document.getElementById('discount').value;
            const res = await fetch('/add', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ url, discount })
            });
            const data = await res.json();
            alert(data.message);
            location.reload();
        }
    </script>
</head>
<body>
    <h1>Tracked Items</h1>
    <input type="text" id="url" placeholder="Product URL">
    <input type="number" id="discount" placeholder="Discount %">
    <button onclick="addItem()">Track Item</button>
    <hr>
    {% for item in items %}
        <div>
            <h3>{{ item.name }}</h3>
            <p>Site: {{ item.site }}</p>
            <p>Original: ${{ item.original_price }}</p>
            <p>Current: ${{ item.current_price }}</p>
            <p>Discount Threshold: {{ item.discount_threshold }}%</p>
            <p>Last Checked: {{ item.last_checked }}</p>
            <a href="/cart/{{ item.id }}">Add to Cart</a>
        </div>
        <hr>
    {% endfor %}
</body>
</html>
