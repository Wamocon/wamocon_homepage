import re

def get_recs(fname):
    with open(fname, encoding='utf-8') as f:
        c = f.read()
    recs = re.findall(r'id=["\'](' + r'rec[0-9a-z-]+)["\']', c)
    seen = set()
    result = []
    for r in recs:
        if r not in seen:
            seen.add(r)
            result.append(r)
    return result

de3 = get_recs('page57489943.html')
en3 = get_recs('page59159537.html')

live_recs = ['rec819412002','rec819418474','rec819424397','rec819423861','rec819425297']

print('=== PAGE 3: Customer Testimonials ===')
print('Live sections check vs DE:')
for rec in live_recs:
    print('  ' + rec + ': ' + ('IN DE' if rec in de3 else 'MISSING FROM DE'))
print()
print('DE rec IDs:')
for r in de3: print('  ' + r)
print()
print('EN rec IDs:')
for r in en3: print('  ' + r)
