with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix the call number
html = html.replace('href="tel:+919666576797"', 'href="tel:+919825744216"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
