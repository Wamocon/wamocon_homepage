import re

with open('page59102217.html', 'r', encoding='utf-8') as f:
    content = f.read()

sec_start = content.find('id="rec832623379"')
sec_end_idx = content.find('<!-- /T396 -->', sec_start)
section = content[sec_start:sec_end_idx]
style_end = section.find('</style>')
html_part = section[style_end + 8:]

# Find all elements with single-quote data-elem-id
elems = re.findall(r"data-elem-id='(\d+)'", html_part)
print(f'Found element IDs (single quotes): {elems}')

# Find elements with data-field-height-value
for eid in elems:
    # Find the full tag for this element
    idx = html_part.find(f"data-elem-id='{eid}'")
    # Get surrounding context for height
    context = html_part[idx:idx+600]
    h_match = re.search(r'data-field-height-value="(\d+)"', context)
    if h_match:
        print(f'  {eid}: height-value={h_match.group(1)}')

# Now I need to:
# 1. Change height-value from 237 to 330 for elements 1724080449061 and 1724080449073
# 2. Change the CSS height from 237px to 330px for those same elements
# 3. Also update artboard data-artboard-height from 664 to 757 if not already done

print('\n=== Artboard height in HTML ===')
artboard_match = re.search(r'data-artboard-height="(\d+)"', html_part)
if artboard_match:
    print(f'  data-artboard-height={artboard_match.group(1)}')

# Show which elements are at which positions
print('\n=== Element positions ===')
for eid in elems:
    idx = html_part.find(f"data-elem-id='{eid}'")
    context = html_part[idx:idx+800]
    top = re.search(r'data-field-top-value="(\d+)"', context)
    left = re.search(r'data-field-left-value="([^"]*)"', context)
    h = re.search(r'data-field-height-value="(\d+)"', context)
    w = re.search(r'data-field-width-value="(\d+)"', context)
    elem_type = re.search(r"data-elem-type='([^']*)'", context)
    if top:
        print(f'  {eid} ({elem_type.group(1) if elem_type else "?"}): top={top.group(1)}, left={left.group(1) if left else "?"}, w={w.group(1) if w else "?"}, h={h.group(1) if h else "auto"}')
