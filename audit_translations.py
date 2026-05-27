import re

base = r'c:\Users\Yash Bhesaniya\OneDrive - WAMOCON GmbH\Desktop\WMC\wamocon_homepage'
with open(base + r'\page59102217.html', encoding='utf-8') as f:
    en = f.read()

ls = en.index('rec-leon-apps')
le = en.index('rec832623391', ls)  # next section after leon-apps in EN page
sec = en[ls:le]
print(f'Section length: {len(sec)}')
print(f'Has "Wir entwickeln": {"Wir entwickeln" in sec}')
print(f'Has "Office": {"Office" in sec}')
print(f'Has "Büro & Produktivität": {"Büro & Produktivität" in sec}')
print(f'Has "Büro &amp; Produktivität": {"Büro &amp; Produktivität" in sec}')
print(f'Has "Office &amp; Productivity": {"Office &amp; Productivity" in sec}')
print(f'Has "Finance": {"Finance" in sec}')
print(f'Has "Finanzen": {"Finanzen" in sec}')
print(f'Has "Solutions": {"Solutions" in sec}')
print(f'Has "development waves": {"development waves" in sec}')
print()
# Extract leon-branch-title texts
titles = re.findall(r'class="leon-branch-title">(.+?)</span>', sec)
print('Branch titles found:', titles)
# Check for meta tags
metas = re.findall(r'class="leon-meta">(.+?)</p>', sec)
print(f'\nMeta tags (total {len(metas)}):')
for m in metas[:10]:
    print(f'  {m}')
if len(metas) > 10:
    print(f'  ... and {len(metas)-10} more')
