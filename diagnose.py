"""diagnose.py - Check what's actually in the file after translation"""
import re

base = r'c:\Users\Yash Bhesaniya\OneDrive - WAMOCON GmbH\Desktop\WMC\wamocon_homepage'

with open(base + r'\index.html', encoding='utf-8') as f:
    de = f.read()

# Check the blocks we added
b380_start = de.find('<div id="rec832623380"')
b381_start = de.find('<div id="rec832623381"')
b382_start = de.find('<div id="rec832623382"')
b388_start = de.find('<div id="rec832623388"')

print(f'Block 380 at: {b380_start}')
print(f'Block 381 at: {b381_start}')
print(f'Block 382 at: {b382_start}')
print(f'Block 388 at: {b388_start}')

# Check actual headings in added blocks
if b380_start > 0:
    # Get first 3000 chars of section 380 and strip styles
    s = de[b380_start:b380_start+3000]
    s = re.sub(r'<style[^>]*>.*?</style>', '', s, flags=re.DOTALL)
    s = re.sub(r'<script[^>]*>.*?</script>', '', s, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', s)
    text = re.sub(r'\s+', ' ', text).strip()
    print(f'\nBlock 380 text preview:\n  {text[:500]}')

if b381_start > 0:
    s = de[b381_start:b381_start+2000]
    s = re.sub(r'<style[^>]*>.*?</style>', '', s, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', s)
    text = re.sub(r'\s+', ' ', text).strip()
    print(f'\nBlock 381 text preview:\n  {text[:400]}')

if b382_start > 0:
    s = de[b382_start:b382_start+2000]
    s = re.sub(r'<style[^>]*>.*?</style>', '', s, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', s)
    text = re.sub(r'\s+', ' ', text).strip()
    print(f'\nBlock 382 text preview:\n  {text[:400]}')

# Check if Warum WAMOCON is in the file
for search in ['Warum WAMOCON', 'Über WAMOCON', 'WAMOCONs IT-Projekte', 'Vorteile der', 'Wer sind unsere']:
    idx = de.find(search)
    print(f'\n"{search}" at: {idx}')
    if idx > 0:
        print(f'  Context: {de[idx:idx+100]}')
