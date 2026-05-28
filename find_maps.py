import re

with open('page70444849.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Look for map-related content
terms = ['t117', 'rec_type_map', 'data-record-type="117"', 'class="t-map', 'googleapis', 'initMap', 'gm-err']
for term in terms:
    idx = c.find(term)
    if idx >= 0:
        print(f'{term} at {idx}:')
        print(f'  {c[max(0,idx-50):idx+150]}')
        print()
    else:
        print(f'{term}: not found')

# Also check for the footer section that has the map - look after rec819180409
sec_start = c.find('id="rec819180409"')
sec_end = c.find('<!-- /T396 -->', sec_start)
# What comes after this section?
after = c[sec_end:sec_end+2000]
print('\n=== Content after footer section (first 500 chars) ===')
print(after[:500])

# Check the footer/bottom bar section
footer_idx = c.find('t-footer')
if footer_idx >= 0:
    print(f'\n=== Footer widget at {footer_idx} ===')
    print(c[footer_idx:footer_idx+200])

# Check for the actual Google Maps script loading
# In the page59102217.html (EN homepage), the maps work - what does it use?
with open('page59102217.html', 'r', encoding='utf-8') as f:
    en = f.read()
maps_idx = en.find('maps.googleapis.com')
if maps_idx >= 0:
    print(f'\n=== EN Homepage Maps script ===')
    print(en[maps_idx-100:maps_idx+300])
