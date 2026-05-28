"""Fix remaining German text in Thanks, Privacy, Imprint EN pages - submit buttons and consent text."""
import re

SPECIAL_FILES = [
    'page59449779.html',  # Thanks EN
    'page59452361.html',  # Privacy EN  
    'page61094143.html',  # Imprint EN
]

# German → English fixes
FIXES = [
    # Submit button text
    ('Anfrage senden\xa0', 'Send request\xa0'),
    ('Anfrage senden ', 'Send request '),
    ('Hinterlassen Sie eine Anfrage', 'Leave a request'),
    # Privacy consent text (full sentence)
    (
        'Hiermit bestätige ich, dass ich die ',
        'I hereby confirm that I have read the '
    ),
    (
        '>Datenschutzerklärung</a><span style="color: rgb(113, 113, 113);"> gelesen habe und damit einverstanden bin, dass die WAMOCON GmbH meine Daten, einschließlich personenbezogener Daten, speichern und verarbeiten darf.',
        '>Privacy Policy</a><span style="color: rgb(113, 113, 113);"> and agree that WAMOCON GmbH may store and process my data, including personal data.'
    ),
    # Fix the privacy policy link target from German DE page to English EN page
    ('href="page59452125.html"', 'href="page59452361.html"'),
]

def fix_file(fname):
    with open(fname, encoding='utf-8') as f:
        c = f.read()
    
    original = c
    changes = []
    
    for old, new in FIXES:
        count = c.count(old)
        if count > 0:
            c = c.replace(old, new)
            changes.append(f'Fixed ({count}x): {old[:60]}...')
    
    if c != original:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'{fname}: {len(changes)} fix types applied')
        for ch in changes:
            print(f'  {ch}')
    else:
        print(f'{fname}: No changes needed')

for fname in SPECIAL_FILES:
    fix_file(fname)

# Also check all other EN pages for Anfrage senden / Hinterlassen
OTHER_EN = [
    'page59159537.html',
    'page59160115.html',
    'page59165009.html',
    'page59165443.html',
    'page59169775.html',
    'page70444849.html',
]
print('\n--- Checking other EN pages for remaining issues ---')
for fname in OTHER_EN:
    with open(fname, encoding='utf-8') as f:
        c = f.read()
    issues = []
    for term in ['Anfrage senden', 'Hinterlassen Sie', 'Hiermit bestätige', 'gelesen habe', 'Datenschutzerklärung']:
        if term in c:
            issues.append(term)
    if issues:
        print(f'{fname}: STILL HAS: {issues}')
    else:
        print(f'{fname}: OK')
