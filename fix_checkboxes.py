import re

with open('page70444849.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The issue: Row 1 has consistent gaps but Row 2 has checkboxes too close to text
# Row 1: text left=-55 (Cover Letter), left=554 (CV/Resume), checkboxes at left=22, 624
# Row 2: text left=-39 (School Certificates), left=531 (Internships), checkboxes at left=20, 622
#
# Fix: Move row 2 text positions to match row 1's pattern, and align checkboxes

fixes = [
    # (element_id, old_left_value, new_left_value)
    ('1748013367595', '-39', '-55'),    # School Certificates text: align with Cover Letter
    ('1748013367598', '531', '554'),    # Internships text: align with CV/Resume
    ('1748013367600', '20', '22'),      # School Certificates checkbox: align with Cover Letter checkbox
    ('1748013367602', '622', '624'),    # Internships checkbox: align with CV/Resume checkbox
]

for eid, old_left, new_left in fixes:
    # Fix CSS: left:calc(50% - 600px + Xpx)
    old_css = f'#rec1088201426 .tn-elem[data-elem-id="{eid}"]'
    idx = content.find(old_css)
    if idx >= 0:
        rule_end = content.find('}', idx)
        rule = content[idx:rule_end+1]
        old_left_css = f'left:calc(50% - 600px + {old_left}px)'
        new_left_css = f'left:calc(50% - 600px + {new_left}px)'
        if old_left_css in rule:
            new_rule = rule.replace(old_left_css, new_left_css)
            content = content[:idx] + new_rule + content[rule_end+1:]
            print(f'CSS fixed {eid}: left {old_left} -> {new_left}')
        else:
            print(f'WARNING: CSS left value {old_left} not found in rule for {eid}')
            print(f'  Rule: {rule}')
    else:
        print(f'WARNING: CSS rule not found for {eid}')

    # Fix HTML data-field-left-value
    html_pattern = f"data-elem-id='{eid}'"
    idx = content.find(html_pattern)
    if idx >= 0:
        context = content[idx:idx+800]
        old_attr = f'data-field-left-value="{old_left}"'
        new_attr = f'data-field-left-value="{new_left}"'
        if old_attr in context:
            abs_pos = idx + context.find(old_attr)
            content = content[:abs_pos] + new_attr + content[abs_pos + len(old_attr):]
            print(f'HTML fixed {eid}: left-value {old_left} -> {new_left}')
        else:
            print(f'WARNING: HTML data-field-left-value="{old_left}" not found for {eid}')
    else:
        print(f'WARNING: HTML element {eid} not found')

# Also fix responsive CSS for these elements
# Check what responsive rules exist
print('\n=== Checking responsive rules ===')
for eid, old_left, new_left in fixes:
    # Find responsive rules
    responsive_rules = re.findall(rf'@media[^{{]*\{{[^}}]*#rec1088201426 \.tn-elem\[data-elem-id="{eid}"\] \{{([^}}]*)\}}', content)
    for rule in responsive_rules:
        if f'+ {old_left}px' in rule:
            print(f'  {eid} has responsive rule with old left {old_left}: {rule[:100]}')

with open('page70444849.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\nDone! Checkbox alignment fixed.')
