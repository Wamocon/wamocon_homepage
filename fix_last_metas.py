import re
base = r'c:\Users\Yash Bhesaniya\OneDrive - WAMOCON GmbH\Desktop\WMC\wamocon_homepage'
with open(base + r'\page59102217.html', encoding='utf-8') as f:
    en = f.read()

en = en.replace('<p class="leon-meta">E-Mobilität</p>', '<p class="leon-meta">E-Mobility</p>')
en = en.replace('<p class="leon-meta">Mobilität / Sicherheit</p>', '<p class="leon-meta">Mobility / Safety</p>')

with open(base + r'\page59102217.html', 'w', encoding='utf-8') as f:
    f.write(en)

# Verify
ls = en.index('rec-leon-apps')
le = en.index('rec832623391', ls)
metas = re.findall(r'class="leon-meta">(.+?)</p>', en[ls:le])
german = [m for m in metas if re.search(r'[äöüÄÖÜß]', m)]
print('Remaining German metas:', german if german else 'None')
print('Done!')
