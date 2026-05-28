"""find_all_headings.py - Find exact HTML for all block headings"""
import re

base = r'c:\Users\Yash Bhesaniya\OneDrive - WAMOCON GmbH\Desktop\WMC\wamocon_homepage'
with open(base + r'\page59102217.html', encoding='utf-8') as f:
    en = f.read()

def extract_block(html, block_id):
    start = html.find(f'<div id="{block_id}"')
    if start < 0:
        return None
    next_match = re.search(r'<div id="rec', html[start + 20:])
    end = (start + 20 + next_match.start()) if next_match else len(html)
    return html[start:end]

block_ids = ['rec832623380', 'rec832623381', 'rec832623382', 'rec832623383', 
             'rec832623384', 'rec832623388', 'rec832623389', 'rec832623390']

for bid in block_ids:
    b = extract_block(en, bid)
    if b:
        # Find ALL h1, h2, h3 tags
        headings = re.findall(r'<h[123][^>]*>(.*?)</h[123]>', b, re.DOTALL)
        print(f'\n=== Block {bid} headings ===')
        for h in headings:
            print(f'  {repr(h[:200])}')
        
        # Also find all visible text spans with color
        colored = re.findall(r'<span style="color: [^"]+">([^<]+)</span>', b)
        if colored:
            print(f'  Colored spans: {colored[:5]}')
