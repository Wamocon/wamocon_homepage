"""Find all popup titles in English pages to check which ones are still in German."""
import re

def check_popup_titles(fname, label):
    try:
        with open(fname, encoding='utf-8') as f:
            c = f.read()
    except FileNotFoundError:
        print(f'{label}: FILE NOT FOUND')
        return
    
    print(f'\n=== {label} ===')
    
    # Find popup titles using broader pattern
    # data-tilda-popup-title attribute
    popup_titles_attr = re.findall(r'data-tilda-popup-title="([^"]+)"', c)
    if popup_titles_attr:
        print(f'  data-tilda-popup-title attrs: {popup_titles_attr}')
    
    # t702__title divs
    title_divs = re.finditer(r'id="popuptitle_(\d+)"[^>]*>([^<]+)<', c)
    for m in title_divs:
        print(f'  popuptitle_{m.group(1)}: {repr(m.group(2))}')
    
    # Also check t702__descr
    descrs = re.findall(r'class="t702__descr[^"]*">([^<]+)<', c)
    if descrs:
        print(f'  t702__descr texts: {[d[:80] for d in descrs]}')
    
    # Check submit button labels
    submit_labels = re.findall(r'class="t-submit[^"]*"[^>]*>([^<]+)<', c)
    if submit_labels:
        print(f'  Submit labels: {submit_labels}')

pages = [
    ('page59165009.html', '360-Booster EN'),
    ('page59159537.html', 'Customer Testimonials EN'),
    ('page59165443.html', 'Cooperation EN'),
    ('page59169775.html', 'Contact EN'),
    ('page59449779.html', 'Thanks EN'),
    ('page59452361.html', 'Privacy EN'),
    ('page61094143.html', 'Imprint EN'),
    ('page70444849.html', 'Azubi EN'),
    ('page59160115.html', 'Career EN'),
]

for fname, label in pages:
    check_popup_titles(fname, label)
