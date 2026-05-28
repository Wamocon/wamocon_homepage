"""Find all German text in Azubi EN body content."""
import re

with open('page70444849.html', encoding='utf-8') as f:
    c = f.read()

# Find all li items with German text
li_items = re.findall(r'<li data-list="bullet">([^<]+)</li>', c)
print('All list items:')
for item in li_items:
    print(f'  {repr(item.strip())}')

# Find all span/div text content that might be German
print('\nPotential German span texts:')
span_texts = re.findall(r'<span[^>]*>([^<]{10,200})</span>', c)
for t in span_texts:
    t = t.strip()
    # Simple heuristic: if German chars or German words present
    if any(c in t for c in 'äöüÄÖÜß') or any(w in t for w in ['und ', 'der ', 'die ', 'das ', 'mit ', 'für ', 'bei ', 'von ', 'zu ', 'ist ']):
        print(f'  {repr(t[:150])}')
