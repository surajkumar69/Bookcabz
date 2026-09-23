import re
html = open('index.html', encoding='utf-8').read()
match = re.search(r'<div class="grid [^>]+>.*?(?=</section>)', html, flags=re.DOTALL)
if match:
    print(match.group(0)[:1000])
