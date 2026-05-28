"""Check shared popup content in EN pages - the form consent text and labels."""
import re

def check_shared_sections(fname, label):
    try:
        with open(fname, encoding='utf-8') as f:
            c = f.read()
    except FileNotFoundError:
        print(f'FILE NOT FOUND: {fname}')
        return
    
    # Find text in the shared popup/footer sections
    shared_ids = ['rec822549340', 'rec822554336', 'rec822556468', 'rec835481654', 'rec835481655', 'rec835481656']
    
    print(f'\n=== {label} ===')
    
    # Find Datenschutzerklarung references (privacy consent text)
    if 'Datenschutzerkl' in c:
        idx = c.find('Datenschutzerkl')
        print(f'  Privacy consent text found at char {idx}:')
        print(f'  {repr(c[max(0,idx-100):idx+200][:300])}')
    
    # Find Hinterlassen
    if 'Hinterlassen' in c:
        idx = c.find('Hinterlassen')
        print(f'  "Hinterlassen" at char {idx}:')
        print(f'  {repr(c[max(0,idx-50):idx+150][:250])}')
    
    # Find popup titles
    popup_titles = re.findall(r'class="t702__title[^"]*"[^>]*>([^<]+)<', c)
    if popup_titles:
        print(f'  Popup titles: {popup_titles}')
    
    # Find submit button text
    submit_texts = re.findall(r'data-tilda-page-type="submit"[^>]*>\s*([^<]+)\s*<', c)
    if submit_texts:
        print(f'  Submit button texts: {submit_texts}')
    
    # Check footer navigation links
    if 'Startseite' in c:
        print(f'  "Startseite" found (footer nav link in German)')
    if 'Über uns' in c:
        print(f'  "Über uns" found')
    if 'Bewertungen' in c:
        print(f'  "Bewertungen" found (= Reviews)')
    
    # Check rec835481654 content (shared footer nav)
    idx_nav = c.find('rec835481654')
    if idx_nav >= 0:
        nav_content = c[idx_nav:idx_nav+1000]
        # Find text in nav
        links = re.findall(r'href="[^"]+">([^<]+)</a>', nav_content)
        print(f'  Footer nav links (rec835481654): {links}')

pages = [
    ('page59165009.html', '360-Booster EN'),
    ('page59159537.html', 'Customer Testimonials EN'),
    ('page59169775.html', 'Contact EN'),
    ('page59449779.html', 'Thanks EN'),
    ('page59452361.html', 'Privacy EN'),
    ('page61094143.html', 'Imprint EN'),
    ('page70444849.html', 'Azubi EN'),
]

for fname, label in pages:
    check_shared_sections(fname, label)
