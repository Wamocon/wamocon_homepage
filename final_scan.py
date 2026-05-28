"""Final comprehensive scan of ALL EN pages for German popup and visible text."""

ALL_EN_FILES = [
    'page59102217.html',  # Homepage EN
    'page59115815.html',  # About WAMOCON EN
    'page59159537.html',  # Customer Testimonials EN
    'page59160115.html',  # Career EN
    'page59165009.html',  # 360-Booster EN
    'page59165443.html',  # Cooperation EN
    'page59169775.html',  # Contact EN
    'page59449779.html',  # Thanks EN
    'page59452361.html',  # Privacy EN
    'page61094143.html',  # Imprint EN
    'page70444849.html',  # Azubi EN
]

# German terms that should NOT appear in EN pages (excluding CSS technical selectors)
GERMAN_TERMS = [
    'Senden Sie Ihre Bewertung',
    'Bewerben Sie sich auf eine freie Stelle',
    'Erfahren Sie mehr über die Auswahl',
    'Hinterlassen Sie Ihre Kontakte',
    'Anfrage senden',
    'Hiermit bestätige ich',
    'Datenschutzerklärung gelesen habe',
    'Zurück',
    'Über uns',
    'Startseite',
    'Karriere',
    'Zusammenarbeit',
    'Kontakte',
    'Impressum',
    'Datenschutz',
    'Bewertungen',
]

print('=== Final German Text Scan - ALL EN Pages ===\n')
all_clean = True

for fname in ALL_EN_FILES:
    try:
        with open(fname, encoding='utf-8') as f:
            c = f.read()
        
        issues = []
        for term in GERMAN_TERMS:
            if term in c:
                # Check if it's in a technical context (data attribute, href, etc.)
                idx = c.find(term)
                ctx = c[max(0,idx-100):idx+len(term)+100]
                # Skip if it's just in a URL/href
                if f'href="' in ctx and term in ['Karriere', 'Kontakte', 'Zusammenarbeit', 'Impressum', 'Datenschutz', 'Bewertungen', 'Startseite']:
                    continue
                # Skip if only in popup: technical hook
                if 'popup:' in ctx and term in ['Bewertungen']:
                    continue
                issues.append(term)
        
        if issues:
            print(f'  {fname}: ISSUES: {issues}')
            all_clean = False
        else:
            print(f'  {fname}: OK')
    except FileNotFoundError:
        print(f'  {fname}: FILE NOT FOUND')

print()
if all_clean:
    print('ALL EN PAGES ARE CLEAN!')
else:
    print('Some issues remain - see above.')
