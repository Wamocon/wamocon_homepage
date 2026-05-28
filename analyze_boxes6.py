import re

with open('page59102217.html', 'r', encoding='utf-8') as f:
    content = f.read()

sec_start = content.find('id="rec832623379"')
# Find the T396 end marker
t396_end_marker = '<!-- /T396 -->'
sec_end_idx = content.find(t396_end_marker, sec_start)
section = content[sec_start:sec_end_idx]

# Find the style end
style_end = section.find('</style>')
html_part = section[style_end + 8:]
print(f'HTML part length: {len(html_part)} chars')

# Show first 1000 chars
print('\nFirst 1000 chars of HTML part:')
print(html_part[:1000])

# Find all data-elem-id in html_part
elems = re.findall(r'data-elem-id="(\d+)"', html_part)
print(f'\nFound element IDs in HTML: {elems}')

# Check for data-field-height
heights = re.findall(r'data-field-height-value="(\d+)"', html_part)
print(f'Found height values: {heights}')
