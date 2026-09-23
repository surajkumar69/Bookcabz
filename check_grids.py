html = open('index.html', encoding='utf-8').read()
import re
match = re.search(r'<section id="fleet".*?</section>', html, flags=re.DOTALL)
print('grid count in fleet:', match.group(0).count('<div class="grid'))
