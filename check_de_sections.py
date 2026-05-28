"""Get section IDs from all local DE pages to compare with live site."""
import re

files = [
    ('3 Customer Testimonials', 'page57489943.html'),
    ('4 Career',                'page57822475.html'),
    ('5 360-Booster',           'page57874143.html'),
    ('6 Cooperation',           'page57876515.html'),
    ('7 Contact',               'page57882423.html'),
    ('8 Thanks DE',             'page59449639.html'),
    ('9 Privacy DE',            'page59452125.html'),
    ('10 Imprint DE',           'page61093859.html'),
    ('11 Employee Reviews',     'page64750211.html'),
    ('12 Azubi DE',             'page69503661.html'),
]

def get_recs(fname):
    with open(fname, encoding='utf-8') as f:
        c = f.read()
    recs = re.findall(r'id=["\'](' + r'rec[0-9a-z-]+)["\']', c)
    seen = set()
    result = []
    for r in recs:
        if r not in seen:
            seen.add(r)
            result.append(r)
    return result

for name, fname in files:
    recs = get_recs(fname)
    content_recs = [r for r in recs if not r.startswith('rec822') and not r.startswith('rec835')]
    print(f'{name}: {len(recs)} total recs. Content: {", ".join(content_recs[:10])}...')
