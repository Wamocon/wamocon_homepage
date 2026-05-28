import re

with open('page59102217.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Change CSS height for elements 1724080449061 and 1724080449073 from 237px to 330px
for eid in ['1724080449061', '1724080449073']:
    old = f'#rec832623379 .tn-elem[data-elem-id="{eid}"]{{z-index:'
    idx = content.find(old)
    if idx >= 0:
        # Find the height:237px in this rule
        rule_end = content.find('}', idx)
        rule = content[idx:rule_end+1]
        new_rule = rule.replace('height:237px', 'height:330px')
        content = content[:idx] + new_rule + content[rule_end+1:]
        print(f'Fixed CSS height for {eid}: 237 -> 330')
    else:
        print(f'WARNING: CSS rule for {eid} not found')

# Fix 2: Change data-field-height-value in HTML for same elements
for eid in ['1724080449061', '1724080449073']:
    old_html = f"data-elem-id='{eid}'"
    idx = content.find(old_html)
    if idx >= 0:
        # Find data-field-height-value="237" near this element
        context_end = idx + 800
        segment = content[idx:context_end]
        old_h = 'data-field-height-value="237"'
        h_pos = segment.find(old_h)
        if h_pos >= 0:
            abs_pos = idx + h_pos
            content = content[:abs_pos] + 'data-field-height-value="330"' + content[abs_pos + len(old_h):]
            print(f'Fixed HTML height-value for {eid}: 237 -> 330')
        else:
            print(f'WARNING: data-field-height-value="237" not found near {eid}')
    else:
        print(f'WARNING: HTML element {eid} not found')

# Fix 3: Update artboard data-artboard-height from 664 to 757
# Find it within the rec832623379 section HTML
sec_start = content.find('id="rec832623379"')
sec_end = content.find('<!-- /T396 -->', sec_start)
# The data-artboard-height is in the HTML div
old_artboard = 'data-artboard-recid="832623379" data-artboard-screens="320,480,640,960,1200" data-artboard-height="664"'
new_artboard = 'data-artboard-recid="832623379" data-artboard-screens="320,480,640,960,1200" data-artboard-height="757"'
if old_artboard in content:
    content = content.replace(old_artboard, new_artboard)
    print('Fixed artboard data-artboard-height: 664 -> 757')
else:
    print('WARNING: artboard height attribute not found (may already be 757)')

# Also need to fix the responsive CSS heights for these elements
# For max-width:1199px
for eid in ['1724080449061', '1724080449073']:
    # Find the responsive rule
    pattern = f'@media screen and (max-width:1199px) {{#rec832623379 .tn-elem[data-elem-id="{eid}"]'
    # Actually, responsive rules are grouped. Let me find them differently.
    pass

# Let's check what responsive heights are set for 1724080449067 (the one we already changed)
# and apply the same to the other two
print('\n=== Checking responsive CSS ===')
responsive_patterns = [
    ('1199px', 'max-width:1199px'),
    ('959px', 'max-width:959px'),
    ('639px', 'max-width:639px'),
    ('479px', 'max-width:479px')
]

for bp_name, bp in responsive_patterns:
    for eid in ['1724080449061', '1724080449067', '1724080449073']:
        # Find the responsive rule for this element
        search = f'@media screen and ({bp})'
        bp_idx = content.find(search)
        while bp_idx >= 0:
            # Check if this media query contains our element
            bp_end = content.find('}}', bp_idx)  # double }} because nested
            if bp_end < 0:
                bp_end = content.find('}', bp_idx + 100)
            segment = content[bp_idx:bp_end+2]
            if f'data-elem-id="{eid}"' in segment:
                h_match = re.search(rf'\[data-elem-id="{eid}"\] \{{([^}}]*)\}}', segment)
                if h_match:
                    css = h_match.group(1)
                    h = re.search(r'height:(\d+)px', css)
                    if h:
                        print(f'  {bp_name} - {eid}: height={h.group(1)}px')
                break
            bp_idx = content.find(search, bp_idx + 1)

with open('page59102217.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\nDone! Main CSS and HTML attributes updated.')
