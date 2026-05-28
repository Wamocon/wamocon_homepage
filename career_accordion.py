import re

with open('page59160115.html', encoding='utf-8') as f:
    c = f.read()

# Find all accordion items with their field IDs and titles
items = re.findall(r'field="li_title__([0-9]+)">([^<]+)<', c)
print('Career EN accordion titles with field IDs:')
for field_id, title in items:
    print('  ID=' + field_id + ': ' + repr(title.strip()))

print()
with open('page57822475.html', encoding='utf-8') as f:
    de = f.read()
de_items = re.findall(r'field="li_title__([0-9]+)">([^<]+)<', de)
print('Career DE accordion titles with field IDs:')
for field_id, title in de_items:
    print('  ID=' + field_id + ': ' + repr(title.strip()))
