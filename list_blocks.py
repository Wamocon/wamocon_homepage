import re
base = r'c:\Users\Yash Bhesaniya\OneDrive - WAMOCON GmbH\Desktop\WMC\wamocon_homepage'
with open(base + r'\index.html', encoding='utf-8') as f:
    de = f.read()
# Find all block IDs with their data-record-type
sections = re.findall(r'<div id="(rec\d+)"[^>]*data-record-type="(\d+)"', de)
print('German homepage block order:')
for i, (rid, rtype) in enumerate(sections):
    print(f'  {i+1}. {rid} (type {rtype})')
print(f'Total: {len(sections)} blocks')

# Also check for specific live site sections
live_sections = ['rec818326948', 'rec818885604']
print()
for s in live_sections:
    print(f'Live section {s} present in DE: {s in de}')
