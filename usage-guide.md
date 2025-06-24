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
