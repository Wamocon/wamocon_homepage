"""Fix translation issues in English About page (page59115815.html)"""
import re

filename = 'page59115815.html'
with open(filename, encoding='utf-8') as f:
    content = f.read()

original = content
changes = 0

def replace_once(c, old, new, label):
    global changes
    idx = c.find(old)
    if idx < 0:
        print(f'NOT FOUND: {label}')
        return c
    result = c[:idx] + new + c[idx+len(old):]
    print(f'FIXED: {label}')
    changes += 1
    return result

# 1. Fix "1100+" typo → "100+"
content = replace_once(
    content,
    '>1100+ customers worldwide.</span>',
    '>100+ customers worldwide.</span>',
    '1100+ typo → 100+'
)

# 2. Fix "Wissen, das wächst." → "Knowledge that grows."
content = replace_once(
    content,
    '>Wissen, das wächst.</span>',
    '>Knowledge that grows.</span>',
    'Wissen das wächst → Knowledge that grows'
)

# 3. Fix Olga's title "Management Assistant und Softwaretesterin" → "Management Assistant and Software Tester"
content = replace_once(
    content,
    'Management Assistant und Softwaretesterin',
    'Management Assistant and Software Tester',
    "Olga's title (German → English)"
)

# 4. Fix Maanik's title "Testautomatisierer mit KI-Spezialisierung" → "Test automation engineer with AI specialization"
content = replace_once(
    content,
    'Testautomatisierer mit KI-Spezialisierung',
    'Test automation engineer with AI specialization',
    "Maanik's title (German → English)"
)

# 5. Fix Yash's bio (entirely in German → English)
yash_de = (
    'Yash Bhesaniya ist ein erfahrener Data Scientist mit einer starken akademischen Basis und praktischer '
    'Erfahrung in der Erkennung von Anomalien und der Extraktion versteckter Merkmale aus Daten. Er verfügt '
    'über fundierte Kenntnisse in statistischer Analyse, maschinellem Lernen, Deep Learning und generativer KI. '
    'Seine technischen Fähigkeiten umfassen Python, Power BI, Datenbankmanagement und SQL, sowie Erfahrung mit '
    'Bibliotheken wie Pandas, Numpy und Pytorch.<br /><br />Mit seiner Erfahrung in IT-Projekten hat Yash an der '
    'Entwicklung von Anwendungen zur Anomalieerkennung und Wissensgraph-Extraktion mitgewirkt. Er hat erfolgreich '
    'ein Tool zur Visualisierung von Wissensgraphen für Hella entwickelt und Anomalien in NASAs Bearing Sensor-Daten '
    'mit LSTM-Modellen erkannt. Zudem hat er eine Android-Anwendung für sichere Online-Transaktionen entworfen.'
    '<br /><br />In seinem aktuellen Projekt konzentriert sich Yash darauf, KI-Technologien in die Testautomatisierung '
    'zu integrieren, um die Effizienz und Qualität der Tests zu verbessern. Seine Stärken als AI-Entwickler liegen '
    'in der Fähigkeit zur Problemlösung, der innovativen Anwendung von KI-Methoden und der kontinuierlichen '
    'Optimierung von Prozessen.'
)
yash_en = (
    'Yash Bhesaniya is an experienced data scientist with a strong academic background and practical experience '
    'in anomaly detection and extracting hidden features from data. He has solid knowledge of statistical analysis, '
    'machine learning, deep learning and generative AI. His technical skills include Python, Power BI, database '
    'management and SQL, as well as experience with libraries such as Pandas, NumPy and PyTorch.<br /><br />'
    'With his experience in IT projects, Yash has been involved in the development of applications for anomaly '
    'detection and knowledge graph extraction. He has successfully developed a knowledge graph visualization tool '
    'for Hella and detected anomalies in NASA\'s Bearing Sensor data using LSTM models. He also designed an Android '
    'application for secure online transactions.<br /><br />In his current project, Yash focuses on integrating AI '
    'technologies into test automation to improve the efficiency and quality of tests. His strengths as an AI '
    'developer lie in his problem-solving ability, the innovative application of AI methods and the continuous '
    'optimization of processes.'
)
content = replace_once(content, yash_de, yash_en, "Yash's full German bio → English")

# 6. Fix 2018 milestones (German → English)
milestones_2018_de = (
    ' Demonstration des SAP-Testautomatisierungskonzepts\u2028bei einem führenden deutschen Versicherungsunternehmen'
    '<br /> Einführung der SAP BASS-Lösung für Einsparungen bei einem deutschen Softwareunternehmen'
    '<br /> Weiterentwicklung und Betreuung eines Konstruktionssystems in einem führenden deutschen\u2028Verkehrsunternehmen'
)
milestones_2018_en = (
    ' - Demonstration of the SAP test automation concept at a leading German insurance company'
    '<br /> - Introduction of the SAP BASS savings solution at a German software company'
    '<br /> - Further development and maintenance of a design system at a leading German transportation company'
)
content = replace_once(content, milestones_2018_de, milestones_2018_en, '2018 milestones (German → English)')

# 7. Fix popup aria-label "Senden Sie Ihre Bewertung" → "Send your review"
content = replace_once(
    content,
    'aria-label="Senden Sie Ihre Bewertung"',
    'aria-label="Send your review"',
    'Popup aria-label: Senden Sie Ihre Bewertung → Send your review'
)

# 8. Fix popup aria-label "Bewerben Sie sich auf eine freie Stelle" → "Apply for a vacant position"
content = replace_once(
    content,
    'aria-label="Bewerben Sie sich auf eine freie Stelle"',
    'aria-label="Apply for a vacant position"',
    'Popup aria-label: Bewerben Sie sich → Apply for a vacant position'
)

print(f'\nTotal changes: {changes}')

if changes > 0:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Saved.')
else:
    print('Nothing to save.')
