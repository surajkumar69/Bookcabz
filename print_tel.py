import re
html = open("index.html", encoding="utf-8").read()
print(re.findall(r'href="tel:[^"]+"', html))
