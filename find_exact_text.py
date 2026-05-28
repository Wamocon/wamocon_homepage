"""find_exact_text.py - Find exact HTML for specific strings"""
import re

base = r'c:\Users\Yash Bhesaniya\OneDrive - WAMOCON GmbH\Desktop\WMC\wamocon_homepage'

with open(base + r'\page59102217.html', encoding='utf-8') as f:
    en = f.read()

# Find the exact HTML context for each untranslated string
search_strings = [
    'Why WAMOCON',
    'About WAMOCON',
    'Advantage of',
    'WAMOCONs IT',
    'Who are our',
    'Qualitätssicherung',    # This should be in the file if block 380 was translated
]

for s in search_strings:
    idx = en.find(s)
    if idx > 0:
        print(f'\n=== "{s}" in EN page at {idx} ===')
        # Show 100 chars before and after to see full HTML context
        start = max(0, idx-50)
        end = min(len(en), idx+200)
        print(repr(en[start:end]))
    else:
        print(f'\n=== "{s}": NOT FOUND in EN page ===')

print('\n\n--- Now checking index.html ---')
with open(base + r'\index.html', encoding='utf-8') as f:
    de = f.read()

for s in ['Qualitätssicherung', 'WAMOCONs IT-Projekte', 'Warum WAMOCON']:
    idx = de.find(s)
    print(f'"{s}" in DE page: {idx}')
    if idx > 0:
        print(f'  Context: {repr(de[idx:idx+100])}')
