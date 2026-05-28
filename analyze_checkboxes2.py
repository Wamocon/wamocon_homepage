import re

with open('page70444849.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the checkbox section rec1088201426
sec_start = content.find('id="rec1088201426"')
sec_end = content.find('<!-- /T396 -->', sec_start)
section = content[sec_start:sec_end]

# Get ALL CSS rules including the left:calc patterns
print('=== Full CSS for each element ===')
css_rules = re.findall(r'#rec1088201426 \.tn-elem\[data-elem-id="(\d+)"\]\{([^}]*)\}', section)
for eid, css in css_rules:
    print(f'\n{eid}:')
    print(f'  {css}')

# Get text content for text elements
print('\n\n=== Text content ===')
style_end = section.find('</style>')
html_part = section[style_end + 8:]

for eid in ['1748005174504', '1748005191742', '1748013367595', '1748013367598']:
    idx = html_part.find(f"data-elem-id='{eid}'")
    if idx >= 0:
        context = html_part[idx:idx+2000]
        # Find text content
        text_match = re.search(r"<div[^>]*class='[^']*tn-atom[^']*'[^>]*>(.*?)</div>", context, re.DOTALL)
        if text_match:
            print(f'{eid}: {text_match.group(1)[:100]}')
        else:
            # Try alternate pattern
            text_match = re.search(r'tn-atom[^>]*>(.*?)</div>', context, re.DOTALL)
            if text_match:
                print(f'{eid}: {text_match.group(1)[:100]}')
            else:
                print(f'{eid}: text not found')
                print(f'  context: {context[:300]}')
