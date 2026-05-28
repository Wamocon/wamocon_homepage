"""check_en_text2.py - Check actual English text in blocks 384, 385-390"""
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

def get_visible_text(html):
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL)
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', html)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

for bid in ['rec832623384', 'rec832623385', 'rec832623386', 'rec832623387', 'rec832623389', 'rec832623390']:
    b = extract_block(en, bid)
    if b:
        text = get_visible_text(b)
        print(f'\n=== Block {bid} ===')
        print(text[:800])
    else:
        print(f'\n=== Block {bid}: NOT FOUND ===')
