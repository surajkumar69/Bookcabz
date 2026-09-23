import re
html = open('index.html', encoding='utf-8').read()
match = re.search(r'<section id="fleet".*?</section>', html, flags=re.DOTALL)
if match:
    open('fleet_section.html', 'w', encoding='utf-8').write(match.group(0))
