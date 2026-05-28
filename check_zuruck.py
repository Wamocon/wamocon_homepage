"""Check for 'Zurück' in all EN pages."""

EN_FILES = [
    'page59159537.html', 'page59160115.html', 'page59165009.html',
    'page59165443.html', 'page59169775.html', 'page59449779.html',
    'page59452361.html', 'page61094143.html', 'page70444849.html',
    'page59102217.html',  # Homepage EN
]

for fname in EN_FILES:
    try:
        with open(fname, encoding='utf-8') as f:
            c = f.read()
        count = c.count('Zurück')
        if count > 0:
            print(f'{fname}: "Zurück" found {count} times')
            idx = c.find('Zurück')
            ctx = c[max(0,idx-50):idx+80]
            print(f'  Context: {" ".join(ctx.split())[:200]}')
    except FileNotFoundError:
        pass
