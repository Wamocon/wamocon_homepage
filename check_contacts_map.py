import re

with open('page59169775.html', 'r', encoding='utf-8') as f:
    c = f.read()

title = re.search(r'<title>(.*?)</title>', c)
print(f'Title: {title.group(1)[:80] if title else "?"}')

has_tmap = 't-map' in c
has_api = 'maps.googleapis' in c
has_script = 'tilda-map' in c
print(f't-map: {has_tmap}, maps API: {has_api}, tilda-map script: {has_script}')

if has_tmap:
    idx = c.find('t-map')
    # Find the rec section
    rec_idx = c.rfind('id="rec', 0, idx)
    rec_match = re.search(r'id="(rec\d+)"', c[rec_idx:rec_idx+30])
    print(f'Map in section: {rec_match.group(1) if rec_match else "?"}')
    
    # Get map details
    context = c[idx:idx+800]
    key = re.search(r'data-map-key="([^"]*)"', context)
    zoom = re.search(r'data-map-zoom="([^"]*)"', context)
    x = re.search(r'data-map-x="([^"]*)"', context)
    y = re.search(r'data-map-y="([^"]*)"', context)
    print(f'Key: {key.group(1) if key else "none"}')
    print(f'Coords: {x.group(1) if x else "?"}, {y.group(1) if y else "?"}')
    print(f'Zoom: {zoom.group(1) if zoom else "?"}')
    
    # Show the full map section HTML
    print(f'\nMap HTML (600 chars):')
    print(context[:600])
else:
    print('NO MAP WIDGET FOUND')
    
    # Check what sections are near the end (where a map would be)
    # Find the contacts section
    contacts_idx = c.rfind('Mergenthalerallee')
    if contacts_idx > 0:
        print(f'\nContacts section found near char {contacts_idx}')
        # What comes after?
        after_contacts = c[contacts_idx:contacts_idx+2000]
        # Look for any map-related content
        for term in ['map', 'iframe', 'embed']:
            if term in after_contacts.lower():
                t_idx = after_contacts.lower().find(term)
                print(f'  Found "{term}" at +{t_idx}: {after_contacts[t_idx:t_idx+100]}')
