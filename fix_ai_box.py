"""Fix AI/LLM box overflow by increasing background shape height."""
with open('page59102217.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Desktop CSS: increase height from 237 to 330 for element 1724080449067
old = '[data-elem-id="1724080449067"]{z-index:12;top:418px;left:calc(50% - 600px + 819px);width:360px;height:237px;'
new = '[data-elem-id="1724080449067"]{z-index:12;top:418px;left:calc(50% - 600px + 819px);width:360px;height:330px;'

count = text.count(old)
print(f"Found desktop CSS rule: {count}")
if count == 1:
    text = text.replace(old, new)
    print("Fixed desktop height 237->330")

# Also fix the HTML data attribute for this element
old2 = 'data-elem-id="1724080449067" data-elem-type="shape" data-field-top-value="418" data-field-left-value="819" data-field-height-value="237"'
new2 = 'data-elem-id="1724080449067" data-elem-type="shape" data-field-top-value="418" data-field-left-value="819" data-field-height-value="330"'
count2 = text.count(old2)
print(f"Found HTML data attr: {count2}")
if count2 >= 1:
    text = text.replace(old2, new2)
    print("Fixed HTML data-field-height-value")

# Increase artboard height as well - find the artboard for rec832623379
# The artboard height is in CSS: #rec832623379 .t396__artboard {height:XXXpx;
import re
# Find current artboard height
m = re.search(r'#rec832623379 \.t396__artboard \{height:(\d+)px;', text)
if m:
    old_h = int(m.group(1))
    new_h = old_h + 93  # add the difference (330-237)
    text = text.replace(f'#rec832623379 .t396__artboard {{height:{old_h}px;', 
                       f'#rec832623379 .t396__artboard {{height:{new_h}px;')
    # Also fix filter and carrier heights
    text = text.replace(f'#rec832623379 .t396__filter {{height:{old_h}px;',
                       f'#rec832623379 .t396__filter {{height:{new_h}px;')
    text = text.replace(f'#rec832623379 .t396__carrier{{height:{old_h}px;',
                       f'#rec832623379 .t396__carrier{{height:{new_h}px;')
    print(f"Fixed artboard height {old_h}->{new_h}")

with open('page59102217.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Done!")
