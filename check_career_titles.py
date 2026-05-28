import re

# Career page - find all accordion/list titles
with open('page59160115.html', encoding='utf-8') as f:
    career_en = f.read()

print('=== CAREER EN: List/accordion titles ===')
titles = re.findall(r'field="li_title__\d+">\s*([^<]+?)\s*<', career_en)
for t in titles:
    t = t.strip()
    if t:
        print(repr(t))

print()
# Azubi page
with open('page70444849.html', encoding='utf-8') as f:
    azubi_en = f.read()

print('=== AZUBI EN: List/accordion titles ===')
titles2 = re.findall(r'field="li_title__\d+">\s*([^<]+?)\s*<', azubi_en)
for t in titles2:
    t = t.strip()
    if t:
        print(repr(t))

idx = azubi_en.find('Jetzt bewerben')
if idx >= 0:
    print('Jetzt bewerben context:')
    print(repr(azubi_en[max(0, idx-100):idx+200]))
