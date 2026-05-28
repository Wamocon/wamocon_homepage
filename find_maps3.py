import re

# Check all potential contact pages for maps
pages = [
    ('contacts/index.html', 'EN Contacts'),
    ('kontakte/index.html', 'DE Kontakte'),
    ('page70444849.html', 'EN Trainee-FIAE'),
    ('page64750211.html', 'DE Mitarbeiter'),
    ('page59102217.html', 'EN Homepage'),
    ('index.html', 'DE Homepage'),
]

for filepath, desc in pages:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            c = f.read()
        has_tmap = 't-map' in c
        has_api = 'maps/api/js' in c or 'maps.googleapis.com/maps/api' in c
        has_script = 'tilda-map' in c
        title = re.search(r'<title>(.*?)</title>', c)
        t = title.group(1)[:50] if title else '?'
        print(f'{desc} ({filepath}):')
        print(f'  Title: {t}')
        print(f'  t-map widget: {has_tmap}')
        print(f'  Maps API: {has_api}')
        print(f'  tilda-map script: {has_script}')
        if has_tmap:
            # Get the map data
            idx = c.find('t-map')
            key = re.search(r'data-map-key="([^"]*)"', c[idx:idx+1000])
            zoom = re.search(r'data-map-zoom="([^"]*)"', c[idx:idx+1000])
            print(f'  Map key: {key.group(1) if key else "not found"}')
            print(f'  Map zoom: {zoom.group(1) if zoom else "?"}')
        print()
    except FileNotFoundError:
        print(f'{desc} ({filepath}): FILE NOT FOUND')
        print()
    except UnicodeDecodeError:
        print(f'{desc} ({filepath}): ENCODING ERROR')
        print()

# Also check if there's a map script reference
print('\n=== Checking tilda-map JS files ===')
import glob
for f in glob.glob('js/tilda-map*'):
    print(f'  Found: {f}')
