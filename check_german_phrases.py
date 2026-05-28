import re
en_files = {
    'p3 Testimonials': 'page59159537.html',
    'p4 Career': 'page59160115.html',
    'p5 360-Booster': 'page59165009.html',
    'p6 Cooperation': 'page59165443.html',
    'p7 Contact': 'page59169775.html',
    'p8 Thanks': 'page59449779.html',
    'p9 Privacy': 'page59452361.html',
    'p10 Imprint': 'page61094143.html',
    'p12 Azubi': 'page70444849.html',
}

german_phrases = [
    'Sehr geehrte', 'vielen Dank', 'freue mich', 'mit freundlichen',
    'Senden Sie', 'Bewerben Sie', 'Klicken Sie',
    'Senden Sie Ihre', 'Bewerben Sie sich',
    'Bewerbung', 'Stellenangebot', 'Lebenslauf',
    'Vollzeit', 'Teilzeit', 'Praktikum',
    'Gehalt', 'Vergütung',
    'Anforderungen', 'Aufgaben', 'Kenntnisse',
    'gesucht', 'gesucht wird', 'bieten wir',
    'Ihr Profil', 'Ihre Aufgaben', 'Wir bieten',
    'Bitte bewerben', 'Jetzt bewerben',
]

for name, fname in en_files.items():
    with open(fname, encoding='utf-8', errors='ignore') as f:
        c = f.read()
    found = []
    for phrase in german_phrases:
        if phrase in c:
            found.append(phrase)
    if found:
        print(name + ': FOUND ' + str(found))
    else:
        print(name + ': OK')
