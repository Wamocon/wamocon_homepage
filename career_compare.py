"""Compare live site sections with local DE pages for pages 3-12."""
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

# Career page comparison
career_live = ['rec822376498', 'rec822373160', 'rec822380795', 'rec822387989',
               'rec822392682', 'rec822394785', 'rec1050682186', 'rec1050677701',
               'rec1050627181', 'rec1050675716', 'rec1050684351', 'rec822436396',
               'rec822450728', 'rec822450772', 'rec822446072']

career_de = get_recs('page57822475.html')
print('=== CAREER: Live vs Local DE ===')
for rec in career_live:
    status = 'IN DE' if rec in career_de else 'MISSING FROM DE'
    print('  ' + rec + ': ' + status)

print()
print('Local DE Career sections:')
for r in career_de:
    print('  ' + r)
