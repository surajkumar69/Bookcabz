html = open('index.html', encoding='utf-8').read()
print('fleet section count:', html.count('id="fleet"'))
print('Sedan AC h4 count:', html.count('Sedan AC</h4>'))
