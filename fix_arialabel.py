"""Fix aria-label for popuptitle_822549340 in Thanks/Privacy/Imprint EN pages."""

SPECIAL_FILES = [
    'page59449779.html',  # Thanks EN
    'page59452361.html',  # Privacy EN  
    'page61094143.html',  # Imprint EN
]

OLD = 'aria-label="Erfahren Sie mehr über die Auswahl von IT-Testern"'
NEW = 'aria-label="Find out more about selecting IT testers"'

for fname in SPECIAL_FILES:
    with open(fname, encoding='utf-8') as f:
        c = f.read()
    if OLD in c:
        c = c.replace(OLD, NEW)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'{fname}: Fixed aria-label')
    else:
        print(f'{fname}: Not found')
