"""Fix remaining German text in EN page popup sections."""
import re

EN_FILES = [
    'page59159537.html',  # Customer Testimonials
    'page59160115.html',  # Career
    'page59165009.html',  # 360-Booster
    'page59165443.html',  # Cooperation
    'page59169775.html',  # Contact
    'page59449779.html',  # Thanks
    'page59452361.html',  # Privacy
    'page61094143.html',  # Imprint
    'page70444849.html',  # Azubi
]

# Fixes for ALL EN pages (popup titles for rec822554336 and rec822556468)
FIXES_ALL = [
    # popuptitle_822554336: Send your review
    (
        'id="popuptitle_822554336">Senden Sie Ihre Bewertung<',
        'id="popuptitle_822554336">Send your review<'
    ),
    # popuptitle_822556468: Apply for a vacant position
    (
        'id="popuptitle_822556468">Bewerben Sie sich auf eine freie Stelle<',
        'id="popuptitle_822556468">Apply for a vacant position<'
    ),
]

# Fixes for Thanks, Privacy, Imprint pages only (rec822549340 still in German)
THANKS_PRIVACY_IMPRINT = ['page59449779.html', 'page59452361.html', 'page61094143.html']
FIXES_SPECIAL = [
    # popuptitle_822549340
    (
        'id="popuptitle_822549340">Erfahren Sie mehr über die Auswahl von IT-Testern<',
        'id="popuptitle_822549340">Find out more about selecting IT testers<'
    ),
    # t702__descr text
    (
        '>Hinterlassen Sie Ihre Kontakte, unter denen wir Sie kontaktieren können<',
        '>Leave your contacts where we can contact you<'
    ),
]

# Submit button and consent text fixes for Thanks/Privacy/Imprint
# These appear multiple times, so we need to replace in context of rec822549340 section

def fix_file(fname):
    with open(fname, encoding='utf-8') as f:
        c = f.read()
    
    original = c
    changes = []
    
    # Apply fixes for all pages
    for old, new in FIXES_ALL:
        if old in c:
            c = c.replace(old, new)
            changes.append(f'Fixed: {old[:50]}...')
    
    # Apply fixes for special pages
    if fname in THANKS_PRIVACY_IMPRINT:
        for old, new in FIXES_SPECIAL:
            if old in c:
                c = c.replace(old, new)
                changes.append(f'Fixed special: {old[:50]}...')
    
    if c != original:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'{fname}: {len(changes)} fixes applied')
        for ch in changes:
            print(f'  {ch}')
    else:
        print(f'{fname}: No changes needed')

for fname in EN_FILES:
    fix_file(fname)
