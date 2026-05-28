"""Fix all remaining German text in Azubi EN page (page70444849.html)."""

fixes = [
    # Navigation link
    ('>Über uns</a>', '>About us</a>'),
    
    # List items
    ('Persönlicher Mentor während der gesamten Ausbildung.',
     'Personal mentor throughout the entire apprenticeship.'),
    ('Individuelle Förderung und regelmäßiges Feedback.',
     'Individual support and regular feedback.'),
    ('Moderne Büroräume und top ausgestattete Arbeitsplätze in Eschborn.',
     'Modern office spaces and well-equipped workplaces in Eschborn.'),
    ('Regelmäßige Team-Events und gemeinsame Aktivitäten.',
     'Regular team events and joint activities.'),
    ('Kostenlose Getränke, Obst etc.',
     'Free drinks, fruit, etc.'),
    ('Überdurchschnittliche Ausbildungsvergütung',
     'Above-average apprenticeship remuneration'),
    ('Familiäre Umgangsform',
     'Friendly and family-like atmosphere'),
    ('Effiziente Fachliche und Persönliche Entwicklung',
     'Efficient professional and personal development'),
    ('Regelmäßige Leistungsanalysen',
     'Regular performance reviews'),
    
    # Span texts (requirements)
    ('Großes Interesse an IT, Computern und Softwareentwicklung.',
     'Strong interest in IT, computers and software development.'),
    ('Logisches Denkvermögen und analytische Fähigkeiten.',
     'Logical thinking and analytical skills.'),
    ('Teamfähigkeit und Kommunikationsstärke.',
     'Teamwork skills and strong communication abilities.'),
    ('Zuverlässigkeit und sorgfältige Arbeitsweise.',
     'Reliability and careful working style.'),
    ('Erfahrungen mit Betriebssystemen und Office-Anwendungen.',
     'Experience with operating systems and Office applications.'),
]

fname = 'page70444849.html'
with open(fname, encoding='utf-8') as f:
    c = f.read()

original = c
changes = []
for old, new in fixes:
    if old in c:
        c = c.replace(old, new)
        changes.append(f'Fixed: {old[:60]}')
    else:
        print(f'NOT FOUND: {old[:60]}')

if c != original:
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'\n{fname}: {len(changes)} fixes applied')
    for ch in changes:
        print(f'  {ch}')
else:
    print('No changes made')
