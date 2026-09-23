import re
html = open("index.html", encoding="utf-8").read()

pattern = r'(<section id="fleet".*?<div class="text-center max-w-3xl mx-auto )mb-16(">\s*<h2)'
html = re.sub(pattern, r'\g<1>mb-8\g<2>', html, flags=re.DOTALL)

open("index.html", "w", encoding="utf-8").write(html)
print("Done")
