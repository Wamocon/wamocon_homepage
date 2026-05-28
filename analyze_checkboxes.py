import re

with open('page70444849.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the checkbox section rec1088201426
sec_start = content.find('id="rec1088201426"')
sec_end = content.find('<!-- /T396 -->', sec_start)
section = content[sec_start:sec_end]

# Find style end to get HTML part
style_end = section.find('</style>')
html_part = section[style_end + 8:]

# Find all elements
elems = re.findall(r"data-elem-id='(\d+)'", html_part)
print(f'Elements in checkbox section: {len(elems)}')

# Get element details
for eid in elems:
    idx = html_part.find(f"data-elem-id='{eid}'")
    context = html_part[idx:idx+800]
    top = re.search(r'data-field-top-value="(\d+)"', context)
    left = re.search(r'data-field-left-value="([^"]*)"', context)
    w = re.search(r'data-field-width-value="(\d+)"', context)
    elem_type = re.search(r"data-elem-type='([^']*)'", context)
    etype = elem_type.group(1) if elem_type else '?'
    
    # Get text content if it's a text element
    text_content = ''
    if etype == 'text':
        text_match = re.search(r'<div[^>]*>([^<]+)</div>', context)
        if text_match:
            text_content = text_match.group(1)[:30]
    
    print(f'  {eid} ({etype}): top={top.group(1) if top else "?"}, left={left.group(1) if left else "?"}, w={w.group(1) if w else "?"} {text_content}')

# Also extract CSS positions
print('\n=== CSS positions ===')
css_rules = re.findall(r'#rec1088201426 \.tn-elem\[data-elem-id="(\d+)"\]\{([^}]*)\}', section)
for eid, css in css_rules:
    top = re.search(r'top:(\d+)px', css)
    left = re.search(r'left:calc\(50% - 600px \+ (\d+)px\)', css)
    if not left:
        left = re.search(r'left:(\d+)px', css)
    w = re.search(r'width:(\d+)px', css)
    print(f'  {eid}: top={top.group(1) if top else "?"}, left={left.group(1) if left else "?"}, w={w.group(1) if w else "?"}')
