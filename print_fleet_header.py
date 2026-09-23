import re
html = open("index.html", encoding="utf-8").read()
match = re.search(r'<section id="fleet".*?<div class="grid ', html, re.DOTALL | re.IGNORECASE)
if match:
    print(match.group(0))
