import re

with open('page59102217.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all CSS rules for rec832623379 elements
rules = re.findall(r'#rec832623379 \.tn-elem\[data-elem-id=.(\d+).\]\{([^}]*)\}', content)
print(f'Found {len(rules)} element rules for rec832623379')

# Show elements with large width (box shapes)
print('\n=== Elements with width >= 350px ===')
for eid, css in rules:
    w = re.search(r'width:(\d+)px', css)
    h = re.search(r'height:(\d+)px', css)
    if w and int(w.group(1)) >= 350:
        w_val = w.group(1)
        h_val = h.group(1) if h else 'auto'
        print(f'  Element {eid}: {w_val}x{h_val}')

# Find element 1724080449067 specifically
print('\n=== Element 1724080449067 (previously modified) ===')
match = re.search(r'#rec832623379 \.tn-elem\[data-elem-id=.1724080449067.\]\{([^}]*)\}', content)
if match:
    print(f'  CSS: {match.group(1)[:200]}')
else:
    print('  Not found with this pattern')
    # Try alternate pattern
    match = re.search(r'\[data-elem-id=.1724080449067.\]\{([^}]*)\}', content)
    if match:
        print(f'  Found with alt pattern: {match.group(1)[:200]}')

# Find the data-field-height for element 1724080449067 in HTML
print('\n=== HTML data attributes for 1724080449067 ===')
match = re.search(r'data-elem-id="1724080449067"[^>]*', content)
if match:
    attrs = match.group(0)[:500]
    print(f'  {attrs}')

# Find shape elements in this section
print('\n=== Shape type elements in rec832623379 ===')
sec_start = content.find('id="rec832623379"')
sec_end = content.find('id="rec832623383"') if content.find('id="rec832623383"') > sec_start else sec_start + 50000
section = content[sec_start:sec_end]
shapes = re.findall(r'data-elem-id="(\d+)"[^>]*data-elem-type="shape"', section)
print(f'  Shape IDs: {shapes}')

# Get CSS for each shape
for sid in shapes:
    match = re.search(rf'#rec832623379 \.tn-elem\[data-elem-id="{sid}"\]\{{([^}}]*)\}}', content)
    if match:
        css = match.group(1)
        w = re.search(r'width:(\d+)px', css)
        h = re.search(r'height:(\d+)px', css)
        top = re.search(r'top:(\d+)px', css)
        print(f'  Shape {sid}: width={w.group(1) if w else "?"}, height={h.group(1) if h else "?"}, top={top.group(1) if top else "?"}')
