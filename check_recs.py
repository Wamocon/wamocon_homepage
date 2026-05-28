import re, sys

files = [
    ('page57874143.html', '360-Booster DE'),
    ('page59165009.html', '360-Booster EN'),
    ('page57876515.html', 'Cooperation DE'),
    ('page59165443.html', 'Cooperation EN'),
    ('page57882423.html', 'Contact DE'),
    ('page59169775.html', 'Contact EN'),
    ('page59452125.html', 'Privacy DE'),
    ('page59452361.html', 'Privacy EN'),
    ('page61093859.html', 'Imprint DE'),
    ('page61094143.html', 'Imprint EN'),
    ('page64750211.html', 'Employee Reviews DE'),
    ('page69503661.html', 'Azubi DE'),
    ('page70444849.html', 'Azubi EN'),
]

for fname, label in files:
    try:
        with open(fname, encoding='utf-8') as f:
            c = f.read()
        recs = re.findall(r'<div id="(rec\d+)"', c)
        print(f'{label}: {len(recs)} recs: {recs[:8]} ...')
    except Exception as e:
        print(f'{label}: ERROR {e}')
