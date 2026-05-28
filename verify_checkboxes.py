import re

with open('page70444849.html', 'r', encoding='utf-8') as f:
    c = f.read()

print("Checkbox element positions:")
elements = {
    '1748013367595': ('School Certificates text', '-55'),
    '1748013367598': ('Internships text', '554'),
    '1748013367600': ('School Cert checkbox', '22'),
    '1748013367602': ('Internships checkbox', '624'),
}

for eid, (desc, expected) in elements.items():
    match = re.search(rf'#rec1088201426 \.tn-elem\[data-elem-id="{eid}"\]\{{([^}}]*)\}}', c)
    if match:
        css = match.group(1)
        left = re.search(r'left:calc\(50% - 600px \+ (-?\d+)px\)', css)
        if left:
            actual = left.group(1)
            status = "OK" if actual == expected else f"MISMATCH (expected {expected})"
            print(f"  {desc} ({eid}): left={actual}px - {status}")
        else:
            print(f"  {desc} ({eid}): left not found in CSS: {css}")
    else:
        print(f"  {desc} ({eid}): CSS rule not found")

# Also verify the HTML data attributes
print("\nHTML data-field-left-value:")
for eid, (desc, expected) in elements.items():
    idx = c.find(f"data-elem-id='{eid}'")
    if idx >= 0:
        context = c[idx:idx+600]
        left_match = re.search(r'data-field-left-value="([^"]*)"', context)
        if left_match:
            actual = left_match.group(1)
            status = "OK" if actual == expected else f"MISMATCH (expected {expected})"
            print(f"  {desc}: left-value={actual} - {status}")
