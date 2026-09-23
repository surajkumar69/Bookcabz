html = open("index.html", encoding="utf-8").read()
html = html.replace('<div class="space-y-2 mb-4">', '<div class="space-y-2 mb-4 mt-auto">')
open("index.html", "w", encoding="utf-8").write(html)
