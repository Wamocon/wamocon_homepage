import re

# Verify page70444849.html (Trainee-FIAE EN)
with open('page70444849.html', 'r', encoding='utf-8') as f:
    c = f.read()

print('=== CHECKBOX CSS LEFT VALUES ===')
for eid, expected in [('1748013367595','-55'),('1748013367598','554'),('1748013367600','22'),('1748013367602','624')]:
    match = re.search(rf'#rec1088201426 \.tn-elem\[data-elem-id=.{eid}.\]\s*\{{([^}}]*)\}}', c, re.DOTALL)
    if match:
        left = re.search(r'left:\s*calc\(50% - 600px \+ (-?\d+)px\)', match.group(1))
        if left:
            val = left.group(1)
            status = 'OK' if val == expected else f'WRONG (got {val}, expected {expected})'
            print(f'  {eid}: left={val}px - {status}')
        else:
            print(f'  {eid}: left pattern not found in CSS')
    else:
        print(f'  {eid}: CSS rule not found')

print()
print('=== RESUME TEXT ===')
if '\u00e9' in c and 'sum' in c:
    print('  FAIL: accented character found')
elif 'CV / Resume' in c:
    print('  OK: CV / Resume (no accent)')
else:
    print('  WARN: CV / Resume text not found')

print()
print('=== FOOTER LABELS ===')
if 'Telefon:' in c:
    print('  FAIL: Still has German Telefon')
else:
    print('  OK: No German Telefon')
if 'Telephone:' in c:
    print('  OK: Has Telephone:')
if '>Contacts<' in c:
    print('  OK: Has Contacts link')

# Verify page59102217.html (EN Homepage boxes)
print()
print('=== EN HOMEPAGE BOXES (page59102217.html) ===')
with open('page59102217.html', 'r', encoding='utf-8') as f:
    h = f.read()

for eid in ['1724080449061','1724080449073','1724080449067']:
    match = re.search(rf'data-elem-id="{eid}"[^>]*data-field-height-value="(\d+)"', h)
    if match:
        print(f'  {eid}: height={match.group(1)}px', 'OK' if match.group(1) == '330' else 'WRONG')
    # Also check CSS
    css_match = re.search(rf'\[data-elem-id="{eid}"\]\{{([^}}]*)\}}', h)
    if css_match:
        height = re.search(r'height:(\d+)px', css_match.group(1))
        if height:
            print(f'    CSS height: {height.group(1)}px', 'OK' if height.group(1) == '330' else 'WRONG')

# Verify Google Maps
print()
print('=== GOOGLE MAPS ===')
for page in ['page59169775.html', 'page57882423.html', 'page64750211.html']:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    has_iframe = 'google.com/maps/embed' in content
    has_old = 't-map-lazyload' in content
    status = 'OK' if has_iframe and not has_old else 'FAIL'
    print(f'  {page}: iframe={has_iframe}, old_map={has_old} - {status}')

print()
print('=== ALL CHECKS COMPLETE ===')
