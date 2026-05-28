import re

with open('page59102217.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all elements in rec832623379 section with top >= 400 (row 2)
text_elems = re.findall(r'#rec832623379 \.tn-elem\[data-elem-id="(\d+)"\]\{([^}]*)\}', content)
print('Row 2 elements (top >= 400px):')
for eid, css in text_elems:
    top_m = re.search(r'top:(\d+)px', css)
    left_m = re.search(r'left:calc\(50% - 600px \+ (\d+)px\)', css)
    if top_m and int(top_m.group(1)) >= 400:
        w = re.search(r'width:(\d+)px', css)
        h = re.search(r'height:(\d+)px', css)
        top_val = top_m.group(1)
        left_val = left_m.group(1) if left_m else '?'
        w_val = w.group(1) if w else 'auto'
        h_val = h.group(1) if h else 'auto'
        print(f'  {eid}: top={top_val}, left={left_val}, w={w_val}, h={h_val}')

# Also check what's in row 1 to compare
print('\nRow 1 elements (top 100-380px):')
for eid, css in text_elems:
    top_m = re.search(r'top:(\d+)px', css)
    left_m = re.search(r'left:calc\(50% - 600px \+ (\d+)px\)', css)
    if top_m and 100 <= int(top_m.group(1)) <= 380:
        w = re.search(r'width:(\d+)px', css)
        h = re.search(r'height:(\d+)px', css)
        top_val = top_m.group(1)
        left_val = left_m.group(1) if left_m else '?'
        w_val = w.group(1) if w else 'auto'
        h_val = h.group(1) if h else 'auto'
        print(f'  {eid}: top={top_val}, left={left_val}, w={w_val}, h={h_val}')

# Check the border/atom CSS for the box elements to understand their borders
print('\nBorder CSS for box elements:')
for eid in ['1724080305746','1724080305756','1724080305760','1724080449061','1724080449067','1724080449073']:
    match = re.search(rf'#rec832623379 \.tn-elem\[data-elem-id="{eid}"\] \.tn-atom\{{([^}}]*)\}}', content)
    if match:
        print(f'  {eid} .tn-atom: {match.group(1)[:150]}')
