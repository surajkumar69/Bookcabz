import re
html = open('index.html', encoding='utf-8').read()
match = re.search(r'<section id="fleet".*?</section>', html, flags=re.DOTALL)
if match:
    fleet_html = match.group(0)
    print('Cards in fleet section:', fleet_html.count('Sedan AC'))
    print('Flex cards:', fleet_html.count('flex flex-wrap justify-center'))
    print('Grid cards:', fleet_html.count('grid grid-cols-1 md:grid-cols-2'))
