"""Fix German popup titles in Homepage EN page (page59102217.html)."""
import re

fname = 'page59102217.html'
with open(fname, encoding='utf-8') as f:
    c = f.read()

original = c
fixes = [
    # Popup titles
    ('id="popuptitle_822554336">Senden Sie Ihre Bewertung<', 'id="popuptitle_822554336">Send your review<'),
    ('id="popuptitle_822556468">Bewerben Sie sich auf eine freie Stelle<', 'id="popuptitle_822556468">Apply for a vacant position<'),
    # Aria labels
    ('aria-label="Senden Sie Ihre Bewertung"', 'aria-label="Send your review"'),
    ('aria-label="Bewerben Sie sich auf eine freie Stelle"', 'aria-label="Apply for a vacant position"'),
    # Also check for Erfahren Sie mehr (rec822549340)
    ('id="popuptitle_822549340">Erfahren Sie mehr über die Auswahl von IT-Testern<', 
     'id="popuptitle_822549340">Find out more about selecting IT testers<'),
]

changes = []
for old, new in fixes:
    if old in c:
        c = c.replace(old, new)
        changes.append(f'Fixed: {old[:60]}')

if c != original:
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'{fname}: {len(changes)} fixes')
    for ch in changes:
        print(f'  {ch}')
else:
    print(f'{fname}: No changes needed')

# Also check for other German popup content
for term in ['Senden Sie', 'Bewerben Sie', 'Hinterlassen', 'Anfrage senden', 'Hiermit bestätige']:
    if term in c:
        print(f'STILL FOUND: {term}')
