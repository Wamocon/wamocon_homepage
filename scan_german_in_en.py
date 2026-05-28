"""Compare visible text between DE and EN pages for each section, focusing on German text in EN pages."""
import re

# German words that SHOULD NOT appear in English pages (not CSS/JS keywords)
GERMAN_INDICATORS = [
    'Datenschutz', 'Impressum', 'Deutsch', 'Bewertung', 'Karriere',
    'Zusammenarbeit', 'Kontakte', 'Kontakt', 'Über uns', 'Unternehmen',
    'Erfahrung', 'Möglichkeit', 'Entwicklung', 'Ausbildung', 'Qualität',
    'Beratung', 'Lösung', 'Erfolg', 'Teamarbeit', 'Kenntnisse',
    'Anforderungen', 'Aufgaben', 'Mitarbeiter', 'Leistungen',
    'Wamocon GmbH', 'Jetzt bewerben', 'Mehr erfahren',
    'Schreiben Sie', 'Senden Sie', 'Bewerben Sie',
    'Was bieten wir', 'Kurzbeschreibung',
    'der IT', 'die IT', 'das System',
    'Weiterbildung', 'Zertifizierung', 'Projektmanagement',
    'Testautomatisierer', 'Testmanagement',
    'Hinterlassen', 'Bewertungen',
    'Sie uns', 'für Sie', 'mit uns',
    'Ihrer', 'Ihrem', 'Ihren', 'Ihres',
    'unseren', 'unserer', 'unserem',
    'Hiermit bestätige', 'gelesen habe',
    'Alle Rechte', 'Startseite',
    'Über uns',
]

def find_german_in_file(fname, label):
    try:
        with open(fname, encoding='utf-8') as f:
            c = f.read()
    except FileNotFoundError:
        print(f'  {label}: FILE NOT FOUND')
        return
    
    found = []
    for indicator in GERMAN_INDICATORS:
        if indicator in c:
            # Find the position to get context
            idx = c.find(indicator)
            # Get surrounding text (ignore if in a script/style block)
            context = c[max(0,idx-50):idx+len(indicator)+50]
            # Skip if in style/script
            if '<style' in context or '</style' in context or 'script' in context.lower() or '.css' in context:
                continue
            found.append(indicator)
    
    if found:
        print(f'  {label}: GERMAN FOUND: {found[:15]}')
    else:
        print(f'  {label}: OK - no German indicators found')

pages = [
    ('3 Customer Testimonials', 'page59159537.html'),
    ('5 360-Booster', 'page59165009.html'),
    ('6 Cooperation', 'page59165443.html'),
    ('7 Contact', 'page59169775.html'),
    ('8 Thanks', 'page59449779.html'),
    ('9 Privacy Policy', 'page59452361.html'),
    ('10 Imprint', 'page61094143.html'),
    ('12 Azubi', 'page70444849.html'),
]

for page_name, en_file in pages:
    print(f'Page {page_name}:')
    find_german_in_file(en_file, en_file)
    print()
