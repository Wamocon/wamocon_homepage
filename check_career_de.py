import re

# Check career DE titles
with open('page57822475.html', encoding='utf-8') as f:
    career_de = f.read()
print('=== CAREER DE: List/accordion titles ===')
titles = re.findall(r'field="li_title__[0-9]+">\s*([^<]+?)\s*<', career_de)
for t in [x.strip() for x in titles if x.strip()]:
    print(repr(t))

# Find 'Was bieten wir' context in EN
with open('page59160115.html', encoding='utf-8') as f:
    career_en = f.read()
idx = career_en.find('Was bieten wir')
print()
print('Was bieten wir context in EN:')
print(repr(career_en[max(0, idx-200):idx+400]))

# Azubi page
with open('page70444849.html', encoding='utf-8') as f:
    azubi_en = f.read()
idx2 = azubi_en.find('Jetzt bewerben')
print()
print('Jetzt bewerben context in Azubi EN:')
print(repr(azubi_en[max(0, idx2-200):idx2+300]))

# Check Azubi DE titles
with open('page69503661.html', encoding='utf-8') as f:
    azubi_de = f.read()
print()
print('=== AZUBI DE: Any button texts ===')
buttons = re.findall(r"href=[\"']([^\"']+)[\"'].*?class=[\"']tn-atom[\"']>([^<]+)<", azubi_de)
for href, text in buttons[:10]:
    print(repr(text.strip()), '->', repr(href))
