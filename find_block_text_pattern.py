"""find_block_text_pattern.py - Find how text is stored in Tilda blocks"""
import re

base = r'c:\Users\Yash Bhesaniya\OneDrive - WAMOCON GmbH\Desktop\WMC\wamocon_homepage'
with open(base + r'\page59102217.html', encoding='utf-8') as f:
    en = f.read()

# Find block 381
start = en.find('<div id="rec832623381"')
next_block = re.search(r'<div id="rec', en[start+20:])
end = start + 20 + next_block.start() if next_block else len(en)
b381 = en[start:end]

print(f'Block 381 length: {len(b381)}')

# Look for h2 tags
h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', b381, re.DOTALL)
print(f'H2 tags: {h2s[:5]}')

# Look for "Why" anywhere
why_idx = b381.find('Why')
if why_idx > 0:
    print(f'\n"Why" at {why_idx}:')
    print(repr(b381[max(0,why_idx-20):why_idx+100]))
else:
    print('\n"Why" NOT FOUND in block 381')

# Look for WAMOCON text
wam_idx = b381.find('WAMOCON')
print(f'\n"WAMOCON" at {wam_idx}:')
if wam_idx > 0:
    print(repr(b381[wam_idx:wam_idx+200]))

# Look for data- attributes with text
data_attrs = re.findall(r'data-[a-z]+="([^"]*(?:WAMOCON|Why|About)[^"]*)"', b381)
print(f'\nData attributes with keywords: {data_attrs[:5]}')

# Look for JavaScript content
js_match = re.search(r'<script[^>]*>([\s\S]*?)</script>', b381)
if js_match:
    print(f'\nScript content (first 500 chars):')
    print(js_match.group(1)[:500])
    
# Check what "Why WAMOCON" looks like encoded
print('\n\nSearching for patterns:')
for pattern in [r'Why\s+WAMOCON', r'Why.*WAMOCON', r'WAMOCON\?']:
    matches = re.findall(pattern, b381)
    print(f'  Pattern "{pattern}": {matches[:3]}')
