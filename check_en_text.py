"""check_en_text.py - Check actual English text in the blocks"""
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
    """Extract visible text, skipping CSS and script blocks"""
    # Remove style blocks
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL)
    # Remove script blocks
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
    # Remove tags
    text = re.sub(r'<[^>]+>', ' ', html)
    # Clean whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:2000]

for bid in ['rec832623380', 'rec832623381', 'rec832623382', 'rec832623383', 'rec832623388', 'rec832623389']:
    b = extract_block(en, bid)
    if b:
        text = get_visible_text(b)
        print(f'\n=== Block {bid} ===')
        print(text[:1000])
    else:
        print(f'\n=== Block {bid}: NOT FOUND ===')
