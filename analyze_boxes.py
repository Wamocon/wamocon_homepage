import re

with open('page59102217.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the style block for rec832623379
idx = content.find('#rec832623379 .t396__artboard')
style_start = content.rfind('<style>', 0, idx)
style_end = content.find('</style>', idx)
style = content[style_start:style_end+8]

# Find all element CSS rules in this section (desktop only, before first @media)
first_media = style.find('@media')
desktop_css = style[:first_media] if first_media > 0 else style

# Extract all element rules
elems = re.findall(r'#rec832623379 \[data-elem-id="(\d+)"\]\{([^}]*)\}', desktop_css)
print(f"Found {len(elems)} elements in rec832623379 desktop CSS\n")

# Show elements that have border-style (these are the box outlines)
print("=== Elements with border-style (box outlines) ===")
for eid, css in elems:
    if 'border-style' in css:
        w = re.search(r'width:(\d+)px', css)
        h = re.search(r'height:(\d+)px', css)
        print(f"  Element {eid}: width={w.group(1) if w else '?'}px, height={h.group(1) if h else '?'}px")
        if 'border-color' in css:
            bc = re.search(r'border-color:([^;]+)', css)
            print(f"    border-color: {bc.group(1) if bc else '?'}")

print("\n=== All elements with width > 300px ===")
for eid, css in elems:
    w = re.search(r'width:(\d+)px', css)
    h = re.search(r'height:(\d+)px', css)
    if w and int(w.group(1)) > 300:
        print(f"  Element {eid}: width={w.group(1)}px, height={h.group(1) if h else 'auto'}px")

# Now find the shape element 1724080449067 that we previously modified
print("\n=== Element 1724080449067 (AI box shape) ===")
match = re.search(r'#rec832623379 \[data-elem-id="1724080449067"\]\{([^}]*)\}', desktop_css)
if match:
    print(f"  CSS: {match.group(1)}")
else:
    # Try in full style
    match = re.search(r'#rec832623379 \[data-elem-id="1724080449067"\]\{([^}]*)\}', style)
    if match:
        print(f"  CSS: {match.group(1)}")
    else:
        print("  Not found!")

# Find ALL shape elements (background shapes for the 3 boxes)
print("\n=== Looking for shape elements (tn-atom with background) ===")
# Find in HTML the shape divs
shape_matches = re.findall(r'data-elem-id="(\d+)"[^>]*data-elem-type="shape"', content[content.find('id="rec832623379"'):content.find('id="rec832623379"')+50000])
print(f"Shape elements: {shape_matches}")

# Get their CSS
for sid in shape_matches:
    match = re.search(rf'#rec832623379 \[data-elem-id="{sid}"\]\{{([^}}]*)\}}', desktop_css)
    if match:
        css = match.group(1)
        w = re.search(r'width:(\d+)px', css)
        h = re.search(r'height:(\d+)px', css)
        print(f"  Shape {sid}: width={w.group(1) if w else '?'}px, height={h.group(1) if h else '?'}px")
