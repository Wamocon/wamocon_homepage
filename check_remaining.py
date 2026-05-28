"""Check context of remaining German terms in EN pages."""
import re

def check_term_context(fname, term, max_occurrences=3):
    with open(fname, encoding='utf-8') as f:
        c = f.read()
    
    positions = [m.start() for m in re.finditer(re.escape(term), c)]
    print(f'{fname}: "{term}" found {len(positions)} times:')
    for i, pos in enumerate(positions[:max_occurrences]):
        context = c[max(0,pos-80):pos+len(term)+80]
        # Simplify context
        context = re.sub(r'\s+', ' ', context)
        print(f'  [{i+1}] ...{context[:200]}...')
    return positions

# Check "Bewertung" in all pages
print('=== "Bewertung" contexts ===')
check_term_context('page59165009.html', 'Bewertung')

print('\n=== Azubi EN remaining terms ===')
for term in ['Über uns', 'Erfahrung', 'Entwicklung', 'Ausbildung']:
    check_term_context('page70444849.html', term, 1)
