"""Check 'Über uns' in navigation across EN pages."""
import re

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
        if 'Über uns' in c:
            idx = c.find('Über uns')
            ctx = c[max(0,idx-100):idx+100]
            ctx = ' '.join(ctx.split())
            print(f'{fname}: {repr(ctx[:200])}')
    except FileNotFoundError:
        pass
