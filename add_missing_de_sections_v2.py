"""
add_missing_de_sections_v2.py
Extracts missing sections from English page, translates them to German,
and inserts them into index.html using the CORRECT English source text.
"""
import re

base = r'c:\Users\Yash Bhesaniya\OneDrive - WAMOCON GmbH\Desktop\WMC\wamocon_homepage'

with open(base + r'\page59102217.html', encoding='utf-8') as f:
    en = f.read()
with open(base + r'\index.html', encoding='utf-8') as f:
    de = f.read()

print(f'English page: {len(en)} chars')
print(f'German page: {len(de)} chars')

def extract_block(html, block_id):
    start = html.find(f'<div id="{block_id}"')
    if start < 0:
        return None
    next_match = re.search(r'<div id="rec', html[start + 20:])
    end = (start + 20 + next_match.start()) if next_match else len(html)
    return html[start:end]

def T(html, pairs):
    for en_text, de_text in pairs:
        html = html.replace(en_text, de_text)
    return html

# ── 380: "Qualitätssicherung durch erfahrene IT-Tester" ──────────────────────
b380 = extract_block(en, 'rec832623380')
b380 = T(b380, [
    ('Quality assurance by experienced IT &nbsp; testers', 'Qualitätssicherung durch erfahrene IT&#8209;Tester'),
    ('Quality assurance by experienced IT testers', 'Qualitätssicherung durch erfahrene IT-Tester'),
    ("With WAMOCON, you don't have to worry about the quality of your IT testers. Our carefully selected specialists understand your requirements and deliver customized solutions that make your projects secure and successful - whether for long-term permanent positions or flexible project tasks. Trust in our experience and let us work together to find the perfect solution for your team.",
     'Mit WAMOCON müssen Sie sich keine Sorgen um die Qualität Ihrer IT-Tester machen. Unsere sorgfältig ausgewählten Spezialisten verstehen Ihre Anforderungen und liefern maßgeschneiderte Lösungen, die Ihre Projekte sicher und erfolgreich machen – ob für langfristige Festanstellungen oder flexible Projektaufgaben. Vertrauen Sie auf unsere Erfahrung und lassen Sie uns gemeinsam die perfekte Lösung für Ihr Team finden.'),
    ('Learn more', 'Erfahren Sie mehr'),
    ('Why IT testers from WAMOCON?', 'Warum IT-Tester von WAMOCON?'),
    ('Customized solutions for your specific requirements', 'Maßgeschneiderte Lösungen für Ihre spezifischen Anforderungen'),
    ('Flexibility for permanent positions and projects', 'Flexibilität bei Festanstellungen und Projekten'),
    ('Reliable selection of experts who exceed your expectations', 'Zuverlässige Auswahl von Experten, die Ihre Erwartungen übertreffen'),
    ('Efficiency and quality at every stage of the project', 'Effizienz und Qualität in jedem Projektschritt'),
    ('Rely on our expertise in the placement of qualified IT specialists and ensure the success of your IT projects.', 'Vertrauen Sie auf unsere Expertise in der Vermittlung qualifizierter IT-Spezialisten und sichern Sie den Erfolg Ihrer IT-Projekte.'),
    ('Request advice now and ensure project success!', 'Jetzt Beratung anfordern und Projekterfolg sichern!'),
    ('Our IT experts keep up to date with the latest developments in test management through regular training.', 'Unsere IT-Experten bleiben durch regelmäßige Fortbildungen im Testmanagement immer auf dem neuesten Stand.'),
    ('We deliver fast results, precise execution and a practical approach to ensure the success of your project.', 'Wir liefern schnelle Ergebnisse, präzise Ausführung und einen praxisnahen Ansatz für Ihren Projekterfolg.'),
    ('We use automation, artificial intelligence and machine learning to make your processes more efficient and future-proof.', 'Mit Automatisierung, künstlicher Intelligenz und maschinellem Lernen gestalten wir Ihre Prozesse effizienter und zukunftssicher.'),
    ('Continuous training for quality that exceeds your expectations and sets standards.', 'Ständige Weiterbildung für Qualität, die Ihre Erwartungen übertrifft und Maßstäbe setzt.'),
    ('40 years of experience. Passion for IT quality. Tailor-made solutions and experts who make your projects secure and successful. Rely on quality and a family approach that makes the difference.', '40 Jahre Erfahrung. Leidenschaft für IT-Qualität. Maßgeschneiderte Lösungen und Experten, die Ihre Projekte sicher und erfolgreich machen. Setzen Sie auf Qualität und einen familiären Ansatz, der den Unterschied macht.'),
    ('Why WAMOCON?', 'Warum WAMOCON?'),
])
print(f'Block 380: {len(b380)} chars')

# ── 381: "Warum WAMOCON?" ─────────────────────────────────────────────────────
b381 = extract_block(en, 'rec832623381')
b381 = T(b381, [
    ('Why WAMOCON?', 'Warum WAMOCON?'),
    ('Our IT experts keep up to date with the latest developments in test management through regular training.', 'Unsere IT-Experten bleiben durch regelmäßige Fortbildungen im Testmanagement immer auf dem neuesten Stand.'),
    ('We deliver fast results, precise execution and a practical approach to ensure the success of your project.', 'Wir liefern schnelle Ergebnisse, präzise Ausführung und einen praxisnahen Ansatz für Ihren Projekterfolg.'),
    ('We use automation, artificial intelligence and machine learning to make your processes more efficient and future-proof.', 'Mit Automatisierung, künstlicher Intelligenz und maschinellem Lernen gestalten wir Ihre Prozesse effizienter und zukunftssicher.'),
    ('Continuous training for quality that exceeds your expectations and sets standards.', 'Ständige Weiterbildung für Qualität, die Ihre Erwartungen übertrifft und Maßstäbe setzt.'),
    ('40 years of experience. Passion for IT quality. Tailor-made solutions and experts who make your projects secure and successful. Rely on quality and a family approach that makes the difference.', '40 Jahre Erfahrung. Leidenschaft für IT-Qualität. Maßgeschneiderte Lösungen und Experten, die Ihre Projekte sicher und erfolgreich machen. Setzen Sie auf Qualität und einen familiären Ansatz, der den Unterschied macht.'),
])
print(f'Block 381: {len(b381)} chars')

# ── 382: "Über WAMOCON" ───────────────────────────────────────────────────────
b382 = extract_block(en, 'rec832623382')
b382 = T(b382, [
    ('About WAMOCON', 'Über WAMOCON'),
    ('For many years, our company has specialized in software testing and quality assurance as well as consulting on software methods. World-renowned and market-leading companies rely on our precise work every day. We pride ourselves on our ability to provide a first-class service and are committed to delivering a high level of expertise to each and every client.',
     'Unser Unternehmen hat sich seit vielen Jahren auf Softwaretests und Qualitätssicherung sowie auf die Beratung zu Softwaremethoden spezialisiert. Weltbekannte und marktführende Unternehmen verlassen sich tagtäglich auf unsere präzise Arbeit. Wir sind stolz auf unsere Fähigkeit, erstklassigen Service zu bieten, und verpflichten uns, jedem einzelnen Kunden ein hohes Maß an Kompetenz zu vermitteln.'),
    ("With WAMOCON's innovative products and services, companies can not only solve existing problems in testing and quality management, but also anticipate future challenges and thus ensure sustainable business development.",
     'Mit den innovativen Produkten und Dienstleistungen von WAMOCON können Unternehmen nicht nur bestehende Probleme im Prüf- und Qualitätsmanagement lösen, sondern auch zukünftige Herausforderungen antizipieren und so eine nachhaltige Geschäftsentwicklung sicherstellen.'),
])
print(f'Block 382: {len(b382)} chars')

# ── 383: "Vorteile der Zusammenarbeit" ────────────────────────────────────────
b383 = extract_block(en, 'rec832623383')
b383 = T(b383, [
    ('Advantage of&nbsp;cooperation', 'Vorteile der Zusammenarbeit'),
    ('Advantage of cooperation', 'Vorteile der Zusammenarbeit'),
    ('Clear communication', 'Klare Kommunikation'),
    ('Specialist knowledge', 'Fachwissen'),
    ('Partnership', 'Partnerschaft'),
    ('Our customers benefit from constant transparency between the requirements and expectations of&nbsp;both parties. This avoids discrepancies.',
     'Unsere Kunden profitieren von einer ständigen Transparenz zwischen den Anforderungen und Erwartungen beider Parteien. So werden Unstimmigkeiten vermieden.'),
    ('Our customers receive comprehensive expertise in the areas of testing and quality management with high-quality services.',
     'Unsere Kundinnen und Kunden erhalten umfassende Expertise in den Bereichen Testing und Qualitätsmanagement mit qualitativ hochwertigen Dienstleistungen.'),
    ('Our customers gain a relationship of trust with WAMOCON for successful cooperation.',
     'Unsere Kunden gewinnen mit WAMOCON ein Vertrauensverhältnis für eine erfolgreiche Zusammenarbeit.'),
    ('Flexibility and adaptability', 'Flexibilität und Anpassungsfähigkeit'),
    ('Artificial Intelligence (AI / LLM-as-a-Judge)Would you like to find out more about us?', 'Bildung und SchulungMöchten Sie mehr über uns erfahren?'),
    ('Artificial Intelligence (AI / LLM-as-a-Judge)', 'Bildung und Schulung'),
    ('Would you like to find out more about us?', 'Möchten Sie mehr über uns erfahren?'),
    ('Improving the value', 'Verbesserung des Werts'),
    ('Our customers receive added value through higher efficiency, lower costs or improved quality.',
     'Durch höhere Effizienz, geringere Kosten oder verbesserte Qualität erhalten unsere Kunden einen Mehrwert.'),
    ('In order to be able to react to changing requirements and needs, our customers are given absolute flexibility.',
     'Um auf veränderte Anforderungen und Bedürfnisse reagieren zu können, erhalten unsere Kunden absolute Flexibilität.'),
    ('More about the company', 'Mehr zum Unternehmen'),
    ('/about-wamocon', '/uber-wamocon'),
])
print(f'Block 383: {len(b383)} chars')

# ── 384: "WAMOCONs IT-Projekte" ──────────────────────────────────────────────
b384 = extract_block(en, 'rec832623384')
b384 = T(b384, [
    ('WAMOCONs IT projects', 'WAMOCONs IT-Projekte'),
    ('Introduction SAP BASS-SPAREN System', 'Einführung SAP BASS-SPAREN System'),
    ('Introduction of SAP ERP system in 50 countries', 'Einführung SAP ERP-System in 50 Ländern'),
    ('Introduction of SAP ERP system and CRM system', 'Einführung SAP ERP-System und CRM-System'),
    ('Read more', 'Weitere Details'),
])
print(f'Block 384: {len(b384)} chars')

# ── 385-387: Project popups ──────────────────────────────────────────────────
b385 = extract_block(en, 'rec832623385')
b385 = T(b385, [
    ('Implementation of SAP BASS-SPAREN System - iBS Innovative Banking Solutions AG', 'Einführung SAP BASS-SPAREN System - iBS Innovative Banking Solutions AG'),
    ('About the company', 'Über das Unternehmen'),
    ('About the project', 'Über das Projekt'),
    ('iBS, based in Wiesbaden, is a leading company in the financial services sector and specializes in innovative solutions in the area of savings and investment advice.',
     'iBS mit Sitz in Wiesbaden ist ein führendes Unternehmen im Finanzdienstleistungssektor und spezialisiert sich auf innovative Lösungen im Bereich Spar- und Anlageberatung.'),
    ('SAP BASS-SPAREN is an innovative application that enables customers to precisely track their savings goals and plan their financial future with the help of sound data and analysis tools. Using modern technologies such as cloud solutions and data-driven forecasting, it provides a user-friendly platform that enables intuitive management of savings and supports long-term financial security. With SAP BASS-SPAREN, iBS sets a new standard in digital savings and offers users an efficient solution for managing and planning',
     'SAP BASS-SPAREN ist eine innovative Anwendung, die es Kunden ermöglicht, ihre Sparziele präzise zu verfolgen und ihre finanzielle Zukunft mit Hilfe fundierter Daten und Analysetools zu planen. Mit modernen Technologien wie Cloud-Lösungen und datengetriebenem Forecasting bietet es eine benutzerfreundliche Plattform für das intuitive Verwalten von Ersparnissen und unterstützt langfristige finanzielle Sicherheit. Mit SAP BASS-SPAREN setzt iBS einen neuen Standard im digitalen Sparen und bietet Nutzern eine effiziente Lösung zur Verwaltung und Planung'),
    ('Close', 'Schließen'),
])

b386 = extract_block(en, 'rec832623386')
b386 = T(b386, [
    ('Introduction of SAP ERP system and CRM system - Lekkerland Deutschland GmbH &amp; Co. KG', 'Einführung SAP ERP-System und CRM-System - Lekkerland Deutschland GmbH &amp; Co. KG'),
    ('About the company', 'Über das Unternehmen'),
    ('About the project', 'Über das Projekt'),
    ('Lekkerland is a leading wholesale company for everyday consumer goods, specializing in convenience. The company offers customized logistics and retail solutions for customers in various sectors, including retail, food service and petrol stations.',
     'Lekkerland ist ein führendes Großhandelsunternehmen für Alltagskonsumgüter, das sich auf Convenience spezialisiert hat. Das Unternehmen bietet maßgeschneiderte Logistik- und Handelslösungen für Kunden in verschiedenen Branchen, darunter Einzelhandel, Gastronomie und Tankstellen.'),
    ('The implementation of SAP ERP and CRM aims to optimize business processes by seamlessly integrating logistics, sales and customer management. This project improves supply chain visibility and increases operational efficiency through process automation and personalized CRM capabilities. The implementation of this technological solution strengthens Lekkerland\'s market position as a leading provider of customized logistics solu',
     'Die Implementierung von SAP ERP und CRM zielt darauf ab, Geschäftsprozesse durch die nahtlose Integration von Logistik, Vertrieb und Kundenmanagement zu optimieren. Dieses Projekt verbessert die Transparenz der Lieferkette und steigert die betriebliche Effizienz durch Prozessautomatisierung und personalisierte CRM-Funktionen. Die Umsetzung dieser technologischen Lösung stärkt Lekkerlandts Marktposition als führender Anbieter maßgeschneiderter Logistiklösungen'),
    ('Close', 'Schließen'),
])

b387 = extract_block(en, 'rec832623387')
b387 = T(b387, [
    ('Implementation of SAP ERP system in 50 countries - Phoenix Contact GmbH', 'Einführung SAP ERP-System in 50 Ländern - Phoenix Contact GmbH'),
    ('About the company', 'Über das Unternehmen'),
    ('About the project', 'Über das Projekt'),
    ('Phoenix Contact is a leading global supplier of components, systems and solutions in the field of electrical engineering, electronics and automation. The company offers innovative products and services for industrial applications and strives for the digitalization and networking of production processes.',
     'Phoenix Contact ist ein weltweit führender Anbieter von Komponenten, Systemen und Lösungen im Bereich Elektrotechnik, Elektronik und Automatisierung. Das Unternehmen bietet innovative Produkte und Dienstleistungen für industrielle Anwendungen und strebt nach Digitalisierung und Vernetzung von Produktionsprozessen.'),
    ('The implementation of the SAP ERP template in 50 countries aims to standardize and optimize global business processes. The introduction of the ERP system will create a uniform and efficient basis for operational activities, enabling the harmonization and simplification of global processes. This large-scale implementation supports the digital transformation and increases the company\'s',
     'Die Implementierung des SAP ERP-Templates in 50 Ländern zielt darauf ab, globale Geschäftsprozesse zu standardisieren und zu optimieren. Die Einführung des ERP-Systems schafft eine einheitliche und effiziente Grundlage für operative Tätigkeiten und ermöglicht die Harmonisierung und Vereinfachung globaler Prozesse. Diese großangelegte Implementierung unterstützt die digitale Transformation und steigert die'),
    ('Close', 'Schließen'),
])

print(f'Block 385: {len(b385)} chars')
print(f'Block 386: {len(b386)} chars')
print(f'Block 387: {len(b387)} chars')

# ── 388: "Wer sind unsere Kunden?" ───────────────────────────────────────────
b388 = extract_block(en, 'rec832623388')
b388 = T(b388, [
    ('Who are our &nbsp; customers?', 'Wer sind unsere Kunden?'),
    ('Who are our customers?', 'Wer sind unsere Kunden?'),
])
print(f'Block 388: {len(b388)} chars')

# ── 389: "IT-Bildungszentrum" ─────────────────────────────────────────────────
b389 = extract_block(en, 'rec832623389')
b389 = T(b389, [
    ('IT training center', 'IT-Bildungszentrum'),
    ('Software testers are more in demand than ever, and the trend is rising. As an official partner of the International Software Testing Qualifications Board (ISTQB®), the WAMOCON Academy offers high-quality training and further education in software testing.',
     'Softwaretester sind gefragter denn je, Tendenz steigend. Als offizieller Partner des International Software Testing Qualifications Board (ISTQB®) bietet die WAMOCON Akademie hochwertige Aus- und Weiterbildung im Softwaretesten.'),
    ('Participants receive all the resources and knowledge they need for a successful certification and IT career.',
     'Die Teilnehmenden erhalten alle Ressourcen und Kenntnisse, die sie für eine erfolgreiche Zertifizierung und IT-Karriere benötigen.'),
])
print(f'Block 389: {len(b389)} chars')

# ── 390: "Kontinuierliche Entwicklung im Testmanagement" ─────────────────────
# NOTE: German page already has rec819175753 covering this content.
# We'll still add block 390 from EN page (which has a different ID) to ensure parity,
# but it will be inserted BEFORE rec819175753 which may create duplication.
# Decision: SKIP block 390 - the German rec819175753 already covers this.
# The German page has its own version which should be kept as-is.
print('Block 390: SKIPPED (already covered by rec819175753 in German page)')

# ── Insert all blocks into index.html ────────────────────────────────────────
# Insert BEFORE rec819175753 (which = "Kontinuierliche Entwicklung" in German)
insert_anchor = '<div id="rec819175753"'
insert_idx = de.find(insert_anchor)
print(f'\nInsertion point at: {insert_idx}')

if insert_idx < 0:
    print('ERROR: Cannot find insertion point!')
    exit(1)

# Combine all sections to add
new_sections = '\n'.join([b380, b381, b382, b383, b384, b385, b386, b387, b388, b389])
print(f'Total content to add: {len(new_sections)} chars')

# Insert into German page
new_de = de[:insert_idx] + new_sections + '\n' + de[insert_idx:]
print(f'New index.html: {len(new_de)} chars (was {len(de)})')

with open(base + r'\index.html', 'w', encoding='utf-8') as f:
    f.write(new_de)
print('Saved index.html!\n')

# ── Verification ─────────────────────────────────────────────────────────────
with open(base + r'\index.html', encoding='utf-8') as f:
    verify = f.read()

checks = [
    ('Qualitätssicherung durch erfahrene IT', True),
    ('Warum IT-Tester von WAMOCON', True),
    ('Maßgeschneiderte Lösungen für Ihre spezifischen', True),
    ('Jetzt Beratung anfordern', True),
    ('Warum WAMOCON?', True),
    ('Über WAMOCON', True),
    ('Vorteile der Zusammenarbeit', True),
    ('WAMOCONs IT-Projekte', True),
    ('Einführung SAP BASS-SPAREN', True),
    ('Wer sind unsere Kunden?', True),
    ('IT-Bildungszentrum', True),
    ('zhKZIDVHLgY', True),
    ('Q_0mtjo8GAU', True),
    ('Wir entwickeln', True),         # Innovation Pipeline still there
    ('rec-leon-apps', True),           # custom section still there
    ('rec-360-tour', True),            # 360 tour still there
    ('Kontinuierliche Entwicklung im Testmanagement', True),
]
print('Verification:')
all_ok = True
for text, should_exist in checks:
    found = text in verify
    ok = found == should_exist
    status = 'OK' if ok else 'FAIL'
    print(f'  [{status}] "{text}": {"found" if found else "missing"}')
    if not ok:
        all_ok = False
print(f'\nResult: {"ALL PASSED" if all_ok else "SOME FAILED"}')
