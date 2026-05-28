import re

with open('page59102217.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the HTML div elements for the 3 row 2 box shapes
for eid in ['1724080449061', '1724080449067', '1724080449073']:
    # Find the div with this data-elem-id
    pattern = rf'<div[^>]*data-elem-id="{eid}"[^>]*>'
    match = re.search(pattern, content)
    if match:
        tag = match.group(0)
        h_match = re.search(r'data-field-height-value="(\d+)"', tag)
        print(f'{eid}: data-field-height-value={h_match.group(1) if h_match else "NOT FOUND"}')
        # Show relevant attributes
        top_match = re.search(r'data-field-top-value="(\d+)"', tag)
        left_match = re.search(r'data-field-left-value="(\d+)"', tag)
        print(f'  top={top_match.group(1) if top_match else "?"}, left={left_match.group(1) if left_match else "?"}')
    else:
        print(f'{eid}: element not found in HTML')

# Also check the next section after rec832623379 to understand what's below
print('\n=== Section after rec832623379 ===')
idx = content.find('id="rec832623383"')
if idx > 0:
    snippet = content[idx:idx+300]
    print(snippet[:300])
