"""extract_en_blocks.py - Extract missing blocks from the English page for German translation"""
import re

base = r'c:\Users\Yash Bhesaniya\OneDrive - WAMOCON GmbH\Desktop\WMC\wamocon_homepage'
with open(base + r'\page59102217.html', encoding='utf-8') as f:
    en = f.read()

# The missing blocks in the English page that need German equivalents
block_ids = [
    'rec832623380',  # Quality assurance
    'rec832623381',  # Why WAMOCON?
    'rec832623382',  # About WAMOCON
    'rec832623383',  # Advantage of cooperation
    'rec832623384',  # WAMOCONs IT projects
    'rec832623385',  # Project popups
    'rec832623386',
    'rec832623387',
    'rec832623388',  # Who are our customers?
    'rec832623389',  # IT training center
    'rec832623390',  # Continuous development
]

for bid in block_ids:
    start = en.find(f'<div id="{bid}"')
    if start < 0:
        print(f'Block {bid}: NOT FOUND')
        continue
    # Find the next block to know the end
    # Look for the next <div id="rec... after this one
    next_match = re.search(r'<div id="rec[^"]*"', en[start+10:])
    if next_match:
        end = start + 10 + next_match.start()
    else:
        end = len(en)
    content = en[start:end]
    print(f'Block {bid}: {len(content)} chars')
    # Extract text content for display
    text_only = re.sub(r'<[^>]+>', ' ', content).strip()
    text_only = re.sub(r'\s+', ' ', text_only)[:300]
    print(f'  Preview: {text_only}')
    print()
