"""Fix German popup titles in About WAMOCON EN page (page59115815.html)."""

fname = 'page59115815.html'
with open(fname, encoding='utf-8') as f:
    c = f.read()

fixes = [
    ('id="popuptitle_822554336">Senden Sie Ihre Bewertung<', 'id="popuptitle_822554336">Send your review<'),
    ('id="popuptitle_822556468">Bewerben Sie sich auf eine freie Stelle<', 'id="popuptitle_822556468">Apply for a vacant position<'),
    ('aria-label="Senden Sie Ihre Bewertung"', 'aria-label="Send your review"'),
    ('aria-label="Bewerben Sie sich auf eine freie Stelle"', 'aria-label="Apply for a vacant position"'),
    ('id="popuptitle_822549340">Erfahren Sie mehr über die Auswahl von IT-Testern<',
     'id="popuptitle_822549340">Find out more about selecting IT testers<'),
    ('>Hinterlassen Sie Ihre Kontakte, unter denen wir Sie kontaktieren können<',
     '>Leave your contacts where we can contact you<'),
]

changes = []
original = c
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
    print('No changes')
