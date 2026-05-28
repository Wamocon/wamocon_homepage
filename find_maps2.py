import re

# Check page64750211.html
with open('page64750211.html', 'r', encoding='utf-8') as f:
    c = f.read()

title = re.search(r'<title>(.*?)</title>', c)
print(f'page64750211 title: {title.group(1) if title else "unknown"}')

if 'Startseite' in c:
    print('Language: German (DE)')
if 'Home' in c and 'Startseite' not in c:
    print('Language: English (EN)')

# Find the map section
map_idx = c.find('t-map')
if map_idx >= 0:
    print(f'Map found at {map_idx}')
    rec_idx = c.rfind('id="rec', 0, map_idx)
    rec_match = re.search(r'id="(rec\d+)"', c[rec_idx:rec_idx+30])
    print(f'Map in section: {rec_match.group(1) if rec_match else "?"}')
    # Get map data attributes
    data_map = c[map_idx:map_idx+600]
    key_match = re.search(r'data-map-key="([^"]*)"', data_map)
    print(f'Map API key: {key_match.group(1) if key_match else "not found in nearby context"}')
    # Get bigger context
    map_section_start = c.rfind('<div id="rec', 0, map_idx)
    map_section_end = c.find('</div> </div>', map_idx + 100)
    print(f'\nMap section HTML (500 chars):')
    print(c[map_idx:map_idx+500])

# Also check EN homepage map
print('\n\n=== EN Homepage (page59102217.html) map ===')
with open('page59102217.html', 'r', encoding='utf-8') as f:
    en = f.read()
map_idx = en.find('t-map')
if map_idx >= 0:
    print(f'Map found at {map_idx}')
    data_map = en[map_idx:map_idx+600]
    key_match = re.search(r'data-map-key="([^"]*)"', data_map)
    print(f'Map API key: {key_match.group(1) if key_match else "not found"}')
    print(f'Context: {en[map_idx:map_idx+400]}')
else:
    # The map might use the googleapis.com/maps/api/js script
    api_idx = en.find('maps/api/js')
    if api_idx >= 0:
        print(f'Maps JS API at {api_idx}:')
        print(en[api_idx-50:api_idx+200])
    else:
        print('No map found')

# Check DE homepage (index.html)
print('\n\n=== DE Homepage (index.html) map ===')
with open('index.html', 'r', encoding='utf-8') as f:
    de = f.read()
map_idx = de.find('t-map')
if map_idx >= 0:
    data_map = de[map_idx:map_idx+600]
    key_match = re.search(r'data-map-key="([^"]*)"', data_map)
    print(f'Map API key: {key_match.group(1) if key_match else "not found"}')
    print(f'Context: {de[map_idx:map_idx+400]}')
