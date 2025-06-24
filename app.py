# Full Stack Price Tracker - MVP Architecture Sketch (Python Flask + SQLite + JS Frontend + Push Notifications + Discord Alerts)

from flask import Flask, request, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import requests
from bs4 import BeautifulSoup
import datetime
import threading
import time
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tracked_items.db'
db = SQLAlchemy(app)

# ---- 1. Database Model ----
class TrackedItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    site = db.Column(db.String)
    original_price = db.Column(db.Float)
    current_price = db.Column(db.Float)
    discount_threshold = db.Column(db.Float)
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    last_checked = db.Column(db.DateTime)

# ---- 2. Add Item Route ----
@app.route('/add', methods=['POST'])
def add_item():
    data = request.json
    url = data['url']
    discount = data['discount']
    name, price, site = scrape_product(url)

    item = TrackedItem(
        url=url,
        name=name,
        site=site,
        original_price=price,
        current_price=price,
        discount_threshold=discount
    )
    db.session.add(item)
    db.session.commit()
    return jsonify({"message": "Item tracked successfully!"})

# ---- 3. Scraper Function ----
def scrape_product(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.title.string.strip() if soup.title else "Unknown Item"
    site = url.split("/")[2]
    price = find_price(soup)
    return title, price, site

def find_price(soup):
    price_tags = soup.find_all(string=lambda t: "$" in t)
    for tag in price_tags:
        try:
            price = float(tag.replace("$", "").replace(",", "").strip())
            if price > 0:
                return price
        except:
            continue
    return 9999.99  # fallback price

# ---- 4. Background Price Check ----
def check_prices():
    while True:
        with app.app_context():
            items = TrackedItem.query.all()
            for item in items:
                try:
                    _, new_price, _ = scrape_product(item.url)
                    item.current_price = new_price
                    item.last_checked = datetime.datetime.utcnow()
                    if new_price <= item.original_price * (1 - item.discount_threshold / 100):
                        notify_user(item)
                except Exception as e:
                    print(f"Error checking {item.url}: {e}")
            db.session.commit()
        time.sleep(3600)  # Check every hour

# ---- 5. Notification with Discord Webhook ----
# Replace with your Discord webhook before running
DISCORD_WEBHOOK_URL = 

def notify_user(item):
    print(f"[NOTIFY] {item.name} is now ${item.current_price} ({item.site})")
    try:
        payload = {
            "content": f"🔥 **{item.name}** is now **${item.current_price:.2f}** on {item.site}!\nURL: {item.url}"
        }
        headers = {"Content-Type": "application/json"}
        requests.post(DISCORD_WEBHOOK_URL, headers=headers, data=json.dumps(payload))
    except Exception as e:
        print(f"[ERROR] Failed to send Discord notification: {e}")

# ---- 6. Dashboard Route ----
@app.route('/')
def dashboard():
    items = TrackedItem.query.all()
    return render_template('dashboard.html', items=items)

# ---- 7. Add to Cart Redirect ----
@app.route('/cart/<int:item_id>')
def go_to_cart(item_id):
    item = TrackedItem.query.get(item_id)
    return redirect(item.url)

# ---- 8. Static Files ----
@app.route('/static/<path:path>')
def send_static(path):
    return app.send_static_file(path)

# ---- 9. Frontend Template (dashboard.html in /templates) ----
# You need to create a file named 'dashboard.html' in a 'templates' folder:
"""
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
"""

# ---- Start App and Background Thread ----
if __name__ == '__main__':
    db.create_all()
    thread = threading.Thread(target=check_prices, daemon=True)
    thread.start()
    app.run(debug=True)
