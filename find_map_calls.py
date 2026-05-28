import re

# Find where t_appendGoogleMap is called in both pages
pages = [
    ('page59169775.html', 'EN Contacts'),
    ('page64750211.html', 'DE Mitarbeiter'),
]

for filepath, desc in pages:
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    print(f'=== {desc} ({filepath}) ===')
    
    # Find t_appendGoogleMap calls
    idx = c.find('t_appendGoogleMap')
    if idx >= 0:
        print(f'  Call found at {idx}:')
        print(f'  {c[idx:idx+200]}')
    else:
        print('  t_appendGoogleMap NOT called!')
    
    # Find the map section script
    # Look for script blocks near the map section
    map_idx = c.find('t-map')
    if map_idx >= 0:
        # Find the nearest script after the map
        script_idx = c.find('<script', map_idx)
        if script_idx >= 0 and script_idx < map_idx + 2000:
            script_end = c.find('</script>', script_idx)
            script_content = c[script_idx:script_end+9]
            print(f'\n  Script near map ({len(script_content)} chars):')
            print(f'  {script_content[:500]}')
    
    # Also look for arMapMarkers (used by the map init)
    markers_idx = c.find('arMapMarkers')
    if markers_idx >= 0:
        print(f'\n  arMapMarkers at {markers_idx}:')
        print(f'  {c[markers_idx:markers_idx+200]}')
    
    print()
