import re

with open('page59102217.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the HTML div tags for the box elements
for eid in ['1724080449061', '1724080449067', '1724080449073']:
    # Find all occurrences 
    positions = [m.start() for m in re.finditer(re.escape('"' + eid + '"'), content)]
    print(f'{eid}: {len(positions)} occurrences')
    
    # Look at the last one (should be the HTML element, not CSS)
    for pos in positions:
        # Find the enclosing tag
        tag_start = content.rfind('<', 0, pos)
        tag_end = content.find('>', pos)
        if tag_start >= 0 and tag_end >= 0:
            tag = content[tag_start:tag_end+1]
            if 'data-field-height' in tag:
                h = re.search(r'data-field-height-value="(\d+)"', tag)
                print(f'  Found HTML tag with height-value: {h.group(1) if h else "none"}')
                break
    else:
        # If no tag has data-field-height, show what we have
        if positions:
            pos = positions[-1]
            tag_start = content.rfind('<', 0, pos)
            tag_end = content.find('>', pos)
            tag = content[tag_start:tag_end+1]
            if len(tag) > 300:
                print(f'  Last tag snippet: {tag[:150]}...{tag[-150:]}')
            else:
                print(f'  Last tag: {tag}')

print('\n\n=== Checking if these are CSS-only elements (no HTML div) ===')
# In Tilda, shape elements might just be inline styles without separate div data attrs
# Let's look for the actual HTML structure in the rec832623379 section
sec_start = content.find('id="rec832623379"')
sec_end = content.find('<!-- /T396 -->', sec_start)
section = content[sec_start:sec_end]

# Find all data-elem-id in the section HTML (not style)
style_end_in_section = section.find('</style>')
html_part = section[style_end_in_section:]

elem_ids = re.findall(r'data-elem-id="(\d+)"', html_part)
print(f'HTML element IDs in rec832623379: {elem_ids[:30]}')

# Check one of the box elements
for eid in ['1724080449061', '1724080449067', '1724080449073']:
    if eid in elem_ids:
        idx = html_part.find(f'data-elem-id="{eid}"')
        snippet = html_part[idx:idx+400]
        print(f'\n{eid} HTML context:')
        print(snippet[:400])
