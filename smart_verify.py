base = r'c:\Users\Yash Bhesaniya\OneDrive - WAMOCON GmbH\Desktop\WMC\wamocon_homepage'
with open(base + r'\index.html', encoding='utf-8') as f:
    de = f.read()
print('File size:', len(de))
checks = [
    'Qualitätssicherung</strong>',
    'Warum </span>WAMOCON',
    'Über</span> WAMOCON',
    'Vorteile</span> der Zusammenarbeit',
    'IT-Projekte</span>',
    'Wer sind',
    'IT-Bildungszentrum',
    'Einführung SAP BASS-SPAREN',
    'Jetzt Beratung anfordern',
    'zhKZIDVHLgY',
    'Q_0mtjo8GAU',
    'Wir entwickeln',
    'rec-leon-apps',
    'rec-360-tour',
    'Kontinuierliche Entwicklung im Testmanagement',
    'Über WAMOCON',
    'WAMOCONs IT-Projekte',
]
for s in checks:
    status = 'OK' if s in de else 'FAIL'
    print(status + ': ' + repr(s))
