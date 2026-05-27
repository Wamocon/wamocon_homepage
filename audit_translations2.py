import re

base = r'c:\Users\Yash Bhesaniya\OneDrive - WAMOCON GmbH\Desktop\WMC\wamocon_homepage'
with open(base + r'\page59102217.html', encoding='utf-8') as f:
    en = f.read()

ls = en.index('rec-leon-apps')
le = en.index('rec832623391', ls)
sec = en[ls:le]

# Find heading context
idx = sec.index('Wir entwickeln')
print('Heading area:')
print(sec[idx-20:idx+200])
print()

# Find branch title context
m = re.search(r'leon-branch-title', sec)
if m:
    print('Branch title area:')
    print(sec[m.start()-10:m.start()+300])
else:
    print('No leon-branch-title found')

# Show Büro context
idx2 = sec.index('Büro &amp; Produktivität')
print()
print('Category context:')
print(sec[idx2-200:idx2+100])
