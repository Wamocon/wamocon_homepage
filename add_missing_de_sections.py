"""
add_missing_de_sections.py
Extracts missing sections from English page (page59102217.html),
translates them to German using live site content, and inserts into index.html
"""
import re

base = r'c:\Users\Yash Bhesaniya\OneDrive - WAMOCON GmbH\Desktop\WMC\wamocon_homepage'

with open(base + r'\page59102217.html', encoding='utf-8') as f:
    en = f.read()
with open(base + r'\index.html', encoding='utf-8') as f:
    de = f.read()

def extract_block(html, block_id):
    """Extract a block and everything up to the next block."""
    start = html.find(f'<div id="{block_id}"')
    if start < 0:
        return None
    # Find end: next <div id="rec...
    next_match = re.search(r'<div id="rec', html[start + 20:])
    end = (start + 20 + next_match.start()) if next_match else len(html)
    return html[start:end]

def translate_block(html, translations):
    """Apply a list of (EN, DE) text replacements."""
    for en_text, de_text in translations:
        html = html.replace(en_text, de_text)
    return html

# ─────────────────────────────────────────────────────────────────────────────
# Block rec832623380 – "Qualitätssicherung durch erfahrene IT-Tester"
# ─────────────────────────────────────────────────────────────────────────────
b380 = extract_block(en, 'rec832623380')
b380 = translate_block(b380, [
    ('Quality assurance by experienced IT &nbsp; testers', 'Qualitätssicherung durch erfahrene IT-Tester'),
    ('Quality assurance by experienced IT testers', 'Qualitätssicherung durch erfahrene IT-Tester'),
    ('<strong>Quality assurance</strong>', '<strong>Qualitätssicherung</strong>'),
    ('<strong>by experienced IT testers</strong>', '<strong>durch erfahrene IT-Tester</strong>'),
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
print(f'Block 380 (Qualitätssicherung): {len(b380)} chars')

# ─────────────────────────────────────────────────────────────────────────────
# Block rec832623381 – "Warum WAMOCON?"
# ─────────────────────────────────────────────────────────────────────────────
b381 = extract_block(en, 'rec832623381')
b381 = translate_block(b381, [
    ('Why WAMOCON?', 'Warum WAMOCON?'),
    ('Our IT experts keep up to date with the latest developments in test management through regular training.', 'Unsere IT-Experten bleiben durch regelmäßige Fortbildungen im Testmanagement immer auf dem neuesten Stand.'),
    ('We deliver fast results, precise execution and a practical approach to ensure the success of your project.', 'Wir liefern schnelle Ergebnisse, präzise Ausführung und einen praxisnahen Ansatz für Ihren Projekterfolg.'),
    ('We use automation, artificial intelligence and machine learning to make your processes more efficient and future-proof.', 'Mit Automatisierung, künstlicher Intelligenz und maschinellem Lernen gestalten wir Ihre Prozesse effizienter und zukunftssicher.'),
    ('Continuous training for quality that exceeds your expectations and sets standards.', 'Ständige Weiterbildung für Qualität, die Ihre Erwartungen übertrifft und Maßstäbe setzt.'),
    ('40 years of experience. Passion for IT quality. Tailor-made solutions and experts who make your projects secure and successful. Rely on quality and a family approach that makes the difference.', '40 Jahre Erfahrung. Leidenschaft für IT-Qualität. Maßgeschneiderte Lösungen und Experten, die Ihre Projekte sicher und erfolgreich machen. Setzen Sie auf Qualität und einen familiären Ansatz, der den Unterschied macht.'),
])
print(f'Block 381 (Warum WAMOCON): {len(b381)} chars')

# ─────────────────────────────────────────────────────────────────────────────
# Block rec832623382 – "Über WAMOCON"
# ─────────────────────────────────────────────────────────────────────────────
b382 = extract_block(en, 'rec832623382')
b382 = translate_block(b382, [
    ('About WAMOCON', 'Über WAMOCON'),
    ('For many years, our company has specialized in software testing and quality assurance as well as consulting on software methods. World-renowned and market-leading companies rely on our precise work every day. We pride ourselves on our ability to provide a first-class service and are committed to delivering a high level of expertise to each and every client.',
     'Unser Unternehmen hat sich seit vielen Jahren auf Softwaretests und Qualitätssicherung sowie auf die Beratung zu Softwaremethoden spezialisiert. Weltbekannte und marktführende Unternehmen verlassen sich tagtäglich auf unsere präzise Arbeit. Wir sind stolz auf unsere Fähigkeit, erstklassigen Service zu bieten, und verpflichten uns, jedem einzelnen Kunden ein hohes Maß an Kompetenz zu vermitteln.'),
    ("With WAMOCON's innovative products and services, companies can not only solve existing problems in testing and quality management, but also anticipate future challenges and thus ensure sustainable business development.",
     'Mit den innovativen Produkten und Dienstleistungen von WAMOCON können Unternehmen nicht nur bestehende Probleme im Prüf- und Qualitätsmanagement lösen, sondern auch zukünftige Herausforderungen antizipieren und so eine nachhaltige Geschäftsentwicklung sicherstellen.'),
])
print(f'Block 382 (Über WAMOCON): {len(b382)} chars')

# ─────────────────────────────────────────────────────────────────────────────
# Block rec832623383 – "Vorteile der Zusammenarbeit"
# ─────────────────────────────────────────────────────────────────────────────
b383 = extract_block(en, 'rec832623383')
b383 = translate_block(b383, [
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
print(f'Block 383 (Vorteile): {len(b383)} chars')

# ─────────────────────────────────────────────────────────────────────────────
# Block rec832623384 – "WAMOCONs IT-Projekte"
# ─────────────────────────────────────────────────────────────────────────────
b384 = extract_block(en, 'rec832623384')
b384 = translate_block(b384, [
    ("WAMOCONs IT projects", "WAMOCONs IT-Projekte"),
    ('Implementation of SAP BASS-SPAREN System', 'Einführung SAP BASS-SPAREN System'),
    ('Implementation of SAP ERP system in 50 countries', 'Einführung SAP ERP-System in 50 Ländern'),
    ('Implementation of SAP ERP system and CRM system', 'Einführung SAP ERP-System und CRM-System'),
    ('More details', 'Weitere Details'),
])
print(f'Block 384 (IT-Projekte): {len(b384)} chars')

# ─────────────────────────────────────────────────────────────────────────────
# Blocks rec832623385-387 – Project popups
# ─────────────────────────────────────────────────────────────────────────────
b385 = extract_block(en, 'rec832623385')
b385 = translate_block(b385, [
    ('Implementation of SAP BASS-SPAREN System - iBS Innovative Banking Solutions AG', 'Einführung SAP BASS-SPAREN System - iBS Innovative Banking Solutions AG'),
    ('About the company', 'Über das Unternehmen'),
    ('iBS, based in Wiesbaden, is a leading company in the financial services sector and specializes in innovative banking solutions. Their products and services are used by major banks and financial institutions worldwide.',
     'iBS mit Sitz in Wiesbaden ist ein führendes Unternehmen im Finanzdienstleistungssektor und spezialisiert sich auf innovative Banklösungen. Ihre Produkte und Dienstleistungen werden von großen Banken und Finanzinstitutionen weltweit eingesetzt.'),
    ('Project description', 'Projektbeschreibung'),
    ('WAMOCON implemented the BASS-SPAREN system for iBS Innovative Banking Solutions AG, covering all test management processes. This system was designed to optimize savings processes and improve the financial performance of banks and savings institutions. WAMOCON was responsible for the entire test management, including planning, execution and reporting of tests.',
     'WAMOCON implementierte das BASS-SPAREN System für iBS Innovative Banking Solutions AG, wobei alle Testmanagementprozesse abgedeckt wurden. Dieses System wurde entwickelt, um Sparprozesse zu optimieren und die finanzielle Leistung von Banken und Sparkassen zu verbessern. WAMOCON war für das gesamte Testmanagement verantwortlich, einschließlich Planung, Durchführung und Berichterstattung von Tests.'),
    ('Close', 'Schließen'),
])

b386 = extract_block(en, 'rec832623386')
b386 = translate_block(b386, [
    ('Introduction of SAP ERP system and CRM system - Lekkerland Deutschland GmbH &amp; Co. KG', 'Einführung SAP ERP-System und CRM-System - Lekkerland Deutschland GmbH &amp; Co. KG'),
    ('About the company', 'Über das Unternehmen'),
    ('Lekkerland is a leading wholesale company for everyday consumer goods, specializing in convenience and petrol station supply. With a network of over 75,000 customers across Europe, Lekkerland connects manufacturers with retailers.',
     'Lekkerland ist ein führendes Großhandelsunternehmen für Alltagskonsumgüter, das sich auf die Versorgung von Tankstellen und Convenience-Stores spezialisiert hat. Mit einem Netzwerk von über 75.000 Kunden in ganz Europa verbindet Lekkerland Hersteller mit dem Handel.'),
    ('Project description', 'Projektbeschreibung'),
    ('WAMOCON successfully implemented an SAP ERP system and a CRM system for Lekkerland Deutschland GmbH. The ERP system was used to integrate and optimize business processes, while the CRM system helped to better manage and expand customer relationships. WAMOCON was responsible for the entire test management, ensuring that all systems met the required standards.',
     'WAMOCON implementierte erfolgreich ein SAP ERP-System und ein CRM-System für Lekkerland Deutschland GmbH. Das ERP-System wurde zur Integration und Optimierung von Geschäftsprozessen eingesetzt, während das CRM-System dabei half, Kundenbeziehungen besser zu verwalten und auszubauen. WAMOCON war für das gesamte Testmanagement verantwortlich und stellte sicher, dass alle Systeme den geforderten Standards entsprachen.'),
    ('Close', 'Schließen'),
])

b387 = extract_block(en, 'rec832623387')
b387 = translate_block(b387, [
    ('Implementation of SAP ERP system in 50 countries - Phoenix Contact GmbH', 'Einführung SAP ERP-System in 50 Ländern - Phoenix Contact GmbH'),
    ('About the company', 'Über das Unternehmen'),
    ('Phoenix Contact is a leading global supplier of components, systems and solutions in the field of electrical engineering, electronics and automation. With around 21,000 employees worldwide, Phoenix Contact serves customers in numerous industries.',
     'Phoenix Contact ist ein weltweit führender Anbieter von Komponenten, Systemen und Lösungen im Bereich Elektrotechnik, Elektronik und Automatisierung. Mit rund 21.000 Mitarbeitern weltweit bedient Phoenix Contact Kunden in zahlreichen Branchen.'),
    ('Project description', 'Projektbeschreibung'),
    ('WAMOCON led the global rollout of an SAP ERP system for Phoenix Contact in 50 countries. This project required precise test management to ensure the seamless integration of the ERP system into the existing processes of Phoenix Contact worldwide. WAMOCON was responsible for the planning, execution and reporting of all test phases.',
     'WAMOCON leitete die globale Einführung eines SAP ERP-Systems für Phoenix Contact in 50 Ländern. Dieses Projekt erforderte ein präzises Testmanagement, um die nahtlose Integration des ERP-Systems in die bestehenden Prozesse von Phoenix Contact weltweit zu gewährleisten. WAMOCON war für die Planung, Durchführung und Berichterstattung aller Testphasen verantwortlich.'),
    ('Close', 'Schließen'),
])

print(f'Block 385 (Popup 1): {len(b385)} chars')
print(f'Block 386 (Popup 2): {len(b386)} chars')
print(f'Block 387 (Popup 3): {len(b387)} chars')

# ─────────────────────────────────────────────────────────────────────────────
# Block rec832623388 – "Wer sind unsere Kunden?"
# ─────────────────────────────────────────────────────────────────────────────
b388 = extract_block(en, 'rec832623388')
b388 = translate_block(b388, [
    ('Who are our customers?', 'Wer sind unsere Kunden?'),
    # Company names don't need translation - they're the same in both languages
])
print(f'Block 388 (Kunden): {len(b388)} chars')

# ─────────────────────────────────────────────────────────────────────────────
# Block rec832623389 – "IT-Bildungszentrum"
# ─────────────────────────────────────────────────────────────────────────────
b389 = extract_block(en, 'rec832623389')
b389 = translate_block(b389, [
    ('IT training center', 'IT-Bildungszentrum'),
    ('Software testers are in greater demand than ever, with an upward trend. As an official partner of the International Software Testing Qualifications Board (ISTQB®), the WAMOCON Academy offers high-quality education and training in software testing.',
     'Softwaretester sind gefragter denn je, Tendenz steigend. Als offizieller Partner des International Software Testing Qualifications Board (ISTQB®) bietet die WAMOCON Akademie hochwertige Aus- und Weiterbildung im Softwaretesten.'),
    ('Participants receive all the resources and knowledge they need for successful certification and an IT career.',
     'Die Teilnehmenden erhalten alle Ressourcen und Kenntnisse, die sie für eine erfolgreiche Zertifizierung und IT-Karriere benötigen.'),
])
print(f'Block 389 (IT-Bildungszentrum): {len(b389)} chars')

# ─────────────────────────────────────────────────────────────────────────────
# Block rec832623390 – "Kontinuierliche Entwicklung im Testmanagement"
# NOTE: This may already be present in DE as rec819175753. Skip if identical.
# ─────────────────────────────────────────────────────────────────────────────
b390 = extract_block(en, 'rec832623390')
b390 = translate_block(b390, [
    ('Continuous development in test management', 'Kontinuierliche Entwicklung im Testmanagement'),
    ('Your development is our drive!', 'Deine Weiterentwicklung ist unser Antrieb!'),
    ('Whether beginner, career changer or professional: With our ISTQB® programs, we take your test management career to the next level.',
     'Ob Einsteiger, Quereinsteiger oder Profi: Mit unseren ISTQB®-Programmen bringen wir deine Testmanagement-Karriere auf das nächste Level.'),
    ('Practice, mentoring, success – your career booster!', 'Praxis, Mentoring, Erfolg – dein Karriere-Turbo!'),
    ('With our programs according to international standards, you will become a sought-after IT specialist. Together we shape your future and that of the IT industry.',
     'Mit unseren Programmen nach internationalen Standards wirst du zur gefragten IT-Fachkraft. Gemeinsam gestalten wir deine Zukunft und die der IT-Branche.'),
    ('Customer satisfaction begins with training.', 'Kundenzufriedenheit beginnt bei der Ausbildung.'),
    ('We promote IT talent so that your customer service not only meets standards, but exceeds them.',
     'Wir fördern IT-Talente, damit dein Kundenservice nicht nur Standards erfüllt, sondern übertrifft.'),
    ('Learn more about the Academy', 'Erfahren Sie mehr über die Akademie'),
])
print(f'Block 390 (Kontinuierliche Entwicklung): {len(b390)} chars')

# ─────────────────────────────────────────────────────────────────────────────
# Now insert all blocks into index.html
# Insert AFTER rec795950036 (IT Services) and BEFORE custom rec-leon-apps section
# In the German page, after rec795950036, the next block is rec819175753 
# But we need to insert BEFORE rec819175753 as well (since rec819175753 = rec832623390)
# 
# Actually: the German page already has rec819175753 = "Kontinuierliche Entwicklung"
# This is the SAME content as EN block rec832623390.
# So we should insert blocks 380-389 BEFORE rec819175753, not block 390.
# ─────────────────────────────────────────────────────────────────────────────

# Find insertion point: just before rec819175753 in index.html
insert_anchor = '<div id="rec819175753"'
insert_idx = de.find(insert_anchor)
print(f'\nInsertion point in index.html at char: {insert_idx}')

if insert_idx < 0:
    print('ERROR: Cannot find insertion point!')
    exit(1)

# Build the blocks to insert (all 9 sections: 380-389)
new_sections = '\n'.join([b380, b381, b382, b383, b384, b385, b386, b387, b388, b389])
total_added = len(new_sections)
print(f'Total content to add: {total_added} chars')

# Insert into the German page
new_de = de[:insert_idx] + new_sections + '\n' + de[insert_idx:]
print(f'New index.html size: {len(new_de)} (was {len(de)})')

# Save
with open(base + r'\index.html', 'w', encoding='utf-8') as f:
    f.write(new_de)
print('\nSaved index.html!')

# Verify
with open(base + r'\index.html', encoding='utf-8') as f:
    verify = f.read()
checks = [
    ('Qualitätssicherung durch erfahrene IT-Tester', True),
    ('Warum WAMOCON?', True),
    ('Über WAMOCON', True),
    ('Vorteile der Zusammenarbeit', True),
    ('WAMOCONs IT-Projekte', True),
    ('Wer sind unsere Kunden?', True),
    ('IT-Bildungszentrum', True),
    ('zhKZIDVHLgY', True),
    ('Q_0mtjo8GAU', True),
]
print('\nVerification:')
all_ok = True
for text, should_exist in checks:
    found = text in verify
    ok = found == should_exist
    print(f"  [{'OK' if ok else 'FAIL'}] '{text}': {'found' if found else 'missing'}")
    if not ok:
        all_ok = False
print(f'\nAll OK: {all_ok}')
