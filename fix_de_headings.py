"""fix_de_headings.py - Fix German headings in the newly added blocks in index.html"""

base = r'c:\Users\Yash Bhesaniya\OneDrive - WAMOCON GmbH\Desktop\WMC\wamocon_homepage'

with open(base + r'\index.html', encoding='utf-8') as f:
    de = f.read()

print(f'File size: {len(de)}')

# All heading and text fixes using exact HTML
fixes = [
    # ── Block 380: Qualitätssicherung ──────────────────────────────────────
    ('<strong style="color: rgb(244, 14, 14);">Quality</strong><strong> assurance by experienced IT</strong>&nbsp;<strong>testers</strong>',
     '<strong style="color: rgb(244, 14, 14);">Qualitätssicherung</strong><strong> durch erfahrene IT-Tester</strong>'),

    # ── Block 381: Warum WAMOCON? ───────────────────────────────────────────
    ('<span style="color: rgb(244, 14, 14);">Why </span>WAMOCON?',
     '<span style="color: rgb(244, 14, 14);">Warum </span>WAMOCON?'),

    # ── Block 382: Über WAMOCON ─────────────────────────────────────────────
    ('<span style="color: rgb(244, 14, 14);">About</span> WAMOCON',
     '<span style="color: rgb(244, 14, 14);">Über</span> WAMOCON'),

    # ── Block 383: Vorteile der Zusammenarbeit ──────────────────────────────
    ('<span style="color: rgb(244, 14, 14);">Advantage</span> of&nbsp;cooperation',
     '<span style="color: rgb(244, 14, 14);">Vorteile</span> der Zusammenarbeit'),

    # ── Block 384: WAMOCONs IT-Projekte ────────────────────────────────────
    ('WAMOCONs <span style="color: rgb(244, 14, 14);">IT projects</span>',
     'WAMOCONs <span style="color: rgb(244, 14, 14);">IT-Projekte</span>'),

    # ── Block 388: Wer sind unsere Kunden? ─────────────────────────────────
    ('Who are <span style="color: rgb(244, 14, 14);">our</span>&nbsp;<span style="color: rgb(244, 14, 14);">customers?</span>',
     'Wer sind <span style="color: rgb(244, 14, 14);">unsere</span>&nbsp;<span style="color: rgb(244, 14, 14);">Kunden?</span>'),

    # ── Block 389: IT-Bildungszentrum ───────────────────────────────────────
    ('IT training center', 'IT-Bildungszentrum'),

    # ── Also fix "Kontinuierliche Entwicklung" if block 390 was added ────────
    ('<span style="color: rgb(244, 14, 14);">Continuous development </span> in&nbsp;test&nbsp;management',
     '<span style="color: rgb(244, 14, 14);">Kontinuierliche Entwicklung </span> im Testmanagement'),
]

changes = 0
for en_text, de_text in fixes:
    count = de.count(en_text)
    if count > 0:
        de = de.replace(en_text, de_text)
        print(f'  Replaced ({count}x): "{en_text[:60]}" → "{de_text[:60]}"')
        changes += 1
    else:
        print(f'  NOT FOUND: "{en_text[:80]}"')

print(f'\nTotal changes: {changes}')

with open(base + r'\index.html', 'w', encoding='utf-8') as f:
    f.write(de)
print('Saved.\n')

# Verification
checks = [
    ('Qualitätssicherung durch erfahrene IT-Tester', True),
    ('Warum WAMOCON?', True),
    ('Über WAMOCON', True),  # Note: might not need exact heading match
    ('Vorteile der Zusammenarbeit', True),
    ('WAMOCONs IT-Projekte', True),
    ('Wer sind', True),
    ('IT-Bildungszentrum', True),
    ('Einführung SAP BASS-SPAREN', True),
    ('Jetzt Beratung anfordern', True),
    ('IT-Projekte', True),
]
print('Verification:')
for text, should in checks:
    found = text in de
    ok = found == should
    print(f'  [{"OK" if ok else "FAIL"}] "{text}": {"found" if found else "missing"}')
