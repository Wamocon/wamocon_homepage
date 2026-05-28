"""
Fix all pages:
1. Add missing (Junior-)Tester sections to local DE Career page
2. Fix Career EN page translation issues
3. Fix popup aria-labels in all EN pages (Senden Sie / Bewerben Sie)
4. Fix Azubi EN 'Jetzt bewerben!' button
5. Fix Career EN accordion items (Was bieten wir, Letter description)
"""

# --- Part 1: Add missing blocks to German Career page ---
missing_blocks_de = """
<div id="rec1050677701" class="r t-rec t-rec_pt_0 t-rec_pt-res-480_0 t-rec_pb_15 t-rec_pb-res-480_30" style="padding-top:0px;padding-bottom:15px;background-color:#101010; " data-record-type="30" data-bg-color="#101010" data-animationappear="off"> <!-- T015 --> <div class="t015"> <div class="t-container t-align_left"> <div class="t-col t-col_11 "> <h2 class="t015__title t-title t-title_lg" field="title">(Junior-)Tester</h2> </div> </div> </div> <style> #rec1050677701 .t015__uptitle{text-transform:uppercase;}#rec1050677701 .t015__title{font-size:22px;line-height:1.2;color:#ffffff;font-weight:700;padding-top:0px;padding-bottom:20px;font-family:'Poppins';}@media screen and (max-width:480px),(orientation:landscape) and (max-height:480px){#rec1050677701 .t015__title{font-size:18px;}}#rec1050677701 .t015__descr{font-size:16px;line-height:1.3;color:#ffffff;font-weight:400;padding-top:0px;padding-bottom:0px;font-family:'Poppins';}@media screen and (max-width:480px),(orientation:landscape) and (max-height:480px){#rec1050677701 .t015__descr{font-size:14px;}}</style> </div>
<div id="rec1050627181" class="r t-rec t-rec_pt_0 t-rec_pt-res-480_0 t-rec_pb_0 t-rec_pb-res-480_0" style="padding-top:0px;padding-bottom:0px;background-color:#101010; " data-animationappear="off" data-record-type="849" data-bg-color="#101010"> <!-- t849--> <div class="t849"> <div class="t-container"> <div class="t-item t-col t-col_12"> <div class="t849__accordion" data-accordion="false"> <div class="t849__wrapper"> <div class="t849__header " style="border-top: 1px solid #ff0b00"> <button type="button" class="t849__trigger-button " aria-controls="accordion1_1050627181" aria-expanded="false"> <span class="t849__title t-name t-name_xl" field="li_title__2668223938370">Kurzbeschreibung</span> <svg class="t849__icon" role="presentation" focusable="false" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"> <circle cx="20" cy="20" r="20" stroke-width="0"></circle> <g class="t849__lines" stroke-width="1px" fill="none"> <path d="M9 20H31"></path> <path d="M20 9V31"></path> </g> </svg> </button> </div> <div class="t849__content" id="accordion1_1050627181" hidden=""> <div class="t849__textwrapper"> <div class="t849__text t-descr t-descr_sm" field="li_descr__2668223938370">In der Rolle des IT-Beraters als Tester wirst du intensiv geschult, um Anforderungen aus User Storys und technischen Dokumenten zu verstehen und zielgerichtet im Kundensystem umzusetzen. Du führst Kunden sicher durch alle Phasen des Softwarelebenszyklus – ob klassisch oder agil – und gewährleistest dabei höchste Produktqualität. Durch deinen Beitrag stellst du sicher, dass alle Anforderungen präzise erfüllt und hochwertige Ergebnisse erzielt werden.</div> </div> </div> </div> </div> </div> <div class="t-item t-col t-col_12"> <div class="t849__accordion" data-accordion="false"> <div class="t849__wrapper"> <div class="t849__header " style="border-top: 1px solid #ff0b00"> <button type="button" class="t849__trigger-button " aria-controls="accordion2_1050627181" aria-expanded="false"> <span class="t849__title t-name t-name_xl" field="li_title__2668223938371">Aufgaben</span> <svg class="t849__icon" role="presentation" focusable="false" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"> <circle cx="20" cy="20" r="20" stroke-width="0"></circle> <g class="t849__lines" stroke-width="1px" fill="none"> <path d="M9 20H31"></path> <path d="M20 9V31"></path> </g> </svg> </button> </div> <div class="t849__content" id="accordion2_1050627181" hidden=""> <div class="t849__textwrapper"> <div class="t849__text t-descr t-descr_sm" field="li_descr__2668223938371">Du entwickelst strukturierte Testfälle nach standardisierten Methoden und führst diese in verschiedenen Testphasen (System-, Integrations-, Abnahme- und Regressionstests) durch. Abweichungen dokumentierst du präzise mithilfe kundenspezifischer Testwerkzeuge und sorgst für eine kontinuierliche Statusüberwachung. Sobald Fehler behoben sind, führst du Re-Tests durch, um die Korrekturen zu validieren und den Fortschritt transparent zu halten.</div> </div> </div> </div> </div> </div> <div class="t-item t-col t-col_12"> <div class="t849__accordion" data-accordion="false"> <div class="t849__wrapper"> <div class="t849__header " style="border-top: 1px solid #ff0b00"> <button type="button" class="t849__trigger-button " aria-controls="accordion3_1050627181" aria-expanded="false"> <span class="t849__title t-name t-name_xl" field="li_title__2668223938372">Anforderungen</span> <svg class="t849__icon" role="presentation" focusable="false" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"> <circle cx="20" cy="20" r="20" stroke-width="0"></circle> <g class="t849__lines" stroke-width="1px" fill="none"> <path d="M9 20H31"></path> <path d="M20 9V31"></path> </g> </svg> </button> </div> <div class="t849__content" id="accordion3_1050627181" hidden=""> <div class="t849__textwrapper"> <div class="t849__text t-descr t-descr_sm" field="li_descr__2668223938372">Du bist sprachlich versiert in Deutsch und Englisch, arbeitest gerne im Team und kommunizierst offen mit deinen Kolleg. Du bist neugierig auf neue Herausforderungen, lernst schnell, arbeitest eigenständig und bringst eine starke IT-Affinität sowie Begeisterung für Technologie mit.</div> </div> </div> </div> </div> </div> <div class="t-item t-col t-col_12"> <div class="t849__accordion" data-accordion="false"> <div class="t849__wrapper"> <div class="t849__header " style="border-top: 1px solid #ff0b00"> <button type="button" class="t849__trigger-button " aria-controls="accordion4_1050627181" aria-expanded="false"> <span class="t849__title t-name t-name_xl" field="li_title__2668223938373">Was bieten wir</span> <svg class="t849__icon" role="presentation" focusable="false" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"> <circle cx="20" cy="20" r="20" stroke-width="0"></circle> <g class="t849__lines" stroke-width="1px" fill="none"> <path d="M9 20H31"></path> <path d="M20 9V31"></path> </g> </svg> </button> </div> <div class="t849__content" id="accordion4_1050627181" hidden=""> <div class="t849__textwrapper"> <div class="t849__text t-descr t-descr_sm" field="li_descr__2668223938373">Bei WAMOCON erwarten dich eine erstklassige IT-Testausbildung und vielfältige Entwicklungsmöglichkeiten. Wir bereiten dich optimal darauf vor, komplexe Kundenanforderungen souverän zu meistern. Gleichzeitig fördern wir deine Fähigkeiten in Priorisierung, Zeitmanagement und Risikobewertung – alles essenzielle Kompetenzen für deinen Erfolg in der IT-Branche.<br><br><ul><li data-list="bullet">Vorteil Nr. 1: Exzellentes Fachwissen &amp; Persönliche Weiterentwicklung</li><li data-list="bullet">Vorteil Nr. 2: Vielfältige Schulungen &amp; Trainings</li><li data-list="bullet">Vorteil Nr. 3: Spannende Projekteinsätze</li><li data-list="bullet">Vorteil Nr. 4: Individuelle Mentor-Betreuung</li><li data-list="bullet">Vorteil Nr. 5: Option auf ein Studium</li><li data-list="bullet">Vorteil Nr. 6: Attraktives Gehalt: 2000,- € Brutto</li><li data-list="bullet">Vorteil Nr. 7: State-of-the-Art IT-Ausrüstung</li><li data-list="bullet">Vorteil Nr. 8: Expertenwissen in Produktentwicklung</li><li data-list="bullet">Vorteil Nr. 9: Familiäre Unternehmenskultur</li></ul></div> </div> </div> </div> </div> <div class="t849__border" style="height: 1px; background-color: #ff0b00"></div> </div> </div> </div> <style>#rec1050627181 .t849__icon {fill:#101010;stroke:#ff0b00;}#rec1050627181 .t849__title{font-size:18px;line-height:1.3;color:#ffffff;font-weight:600;font-family:'Poppins';}#rec1050627181 .t849__text{font-size:14px;line-height:1.3;color:#ffffff;font-weight:300;font-family:'Poppins';}</style> <script type="text/javascript">t_onReady(function() {t_onFuncLoad('t849_init',function() {t849_init('1050627181');});});</script> </div>
<div id="rec1050675716" class="r t-rec t-rec_pt_30 t-rec_pb_0" style="padding-top:30px;padding-bottom:0px;background-color:#101010;" data-animationappear="off" data-record-type="396" data-bg-color="#101010"> <!-- T396 --> <div class="t396"> <div class="t396__artboard rendered" data-artboard-recid="1050675716" data-artboard-height="55"> <div class="t396__carrier"></div> <div class="t396__filter"></div> <div class="t396__elem tn-elem" data-elem-id="1730977252774" data-elem-type="button"> <a class="tn-atom" href="#popup:Antwort">Antwort</a> </div> </div> </div> <script>t_onFuncLoad('t396_initialScale',function() {t396_initialScale('1050675716');});t_onReady(function() {t_onFuncLoad('t396_init',function() {t396_init('1050675716');});});</script> <!-- /T396 --> </div>
<div id="rec1050684351" class="r t-rec t-rec_pt_0 t-rec_pt-res-480_0 t-rec_pb_15 t-rec_pb-res-480_30" style="padding-top:0px;padding-bottom:15px;background-color:#101010;" data-record-type="30" data-bg-color="#101010" data-animationappear="off"> <!-- T015 --> <div class="t015"> <div class="t-container t-align_left"> <div class="t-col t-col_11 "> </div> </div> </div> <style>#rec1050684351 .t015__title{font-size:22px;line-height:1.2;color:#ffffff;font-weight:700;font-family:'Poppins';}</style> </div>
"""

# Load German Career page
with open('page57822475.html', encoding='utf-8') as f:
    de_career = f.read()

# Find end of rec1050682186 and insert new blocks before rec822436396
insert_marker = '<div id="rec822436396"'
idx = de_career.find(insert_marker)
if idx < 0:
    print('ERROR: rec822436396 not found in DE career page')
else:
    # Insert the new blocks before rec822436396
    new_content = de_career[:idx] + missing_blocks_de + '\n' + de_career[idx:]
    with open('page57822475.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('DE Career: Added 4 missing sections (Junior-Tester) before rec822436396')

print()

# --- Part 2: Fix Career EN page issues ---
with open('page59160115.html', encoding='utf-8') as f:
    en_career = f.read()

changes = 0

def fix(content, old, new, label):
    global changes
    idx = content.find(old)
    if idx < 0:
        print('NOT FOUND: ' + label)
        return content
    result = content[:idx] + new + content[idx+len(old):]
    print('FIXED: ' + label)
    changes += 1
    return result

# Fix "Was bieten wir" -> "What we offer" (first occurrence, for the existing job listing)
en_career = fix(en_career, 
    'field="li_title__5773642176293">Was bieten wir</span>',
    'field="li_title__5773642176293">What we offer</span>',
    'Career EN: Was bieten wir -> What we offer')

# Fix "Letter description" -> "Requirements" 
en_career = fix(en_career,
    'field="li_title__5773642176292">Letter description</span>',
    'field="li_title__5773642176292">Requirements</span>',
    'Career EN: Letter description -> Requirements')

# Also add (Junior-)Tester section to EN page with translations
# First check if it already exists
if 'rec1050677701' in en_career:
    print('NOTE: rec1050677701 already in EN career page')
else:
    # Add English version of the (Junior-)Tester job listing
    # Find insertion point: before the 2nd job listing (the Testautomatisierer one)
    # This would be before whatever block corresponds to the Testautomatisierer heading in EN
    # We need to find the English equivalent block
    # Looking at EN recs: rec833136005 through rec833136012
    # The junior tester section should go BEFORE the testautomatisierer section in EN
    # We need to find the Testautomatisierer heading in EN
    tester_auto_marker = '(Junior-) Testautomatisierer'
    ta_idx = en_career.find(tester_auto_marker)
    if ta_idx < 0:
        print('WARNING: Testautomatisierer heading not found in EN')
    else:
        # Find the rec div start before this heading
        div_start = en_career.rfind('<div id="rec', 0, ta_idx)
        print('Found Testautomatisierer at char ' + str(ta_idx) + ', rec div at ' + str(div_start))

with open('page59160115.html', 'w', encoding='utf-8') as f:
    f.write(en_career)
print('Career EN: ' + str(changes) + ' fixes applied')

print()

# --- Part 3: Fix popup aria-labels in ALL EN pages ---
en_pages = [
    'page59159537.html',  # Customer Testimonials
    'page59160115.html',  # Career
    'page59165009.html',  # 360-Booster
    'page59165443.html',  # Cooperation
    'page59169775.html',  # Contact
    'page59449779.html',  # Thanks
    'page59452361.html',  # Privacy Policy
    'page61094143.html',  # Imprint
    'page70444849.html',  # Azubi
]

popup_fixes = [
    ('aria-label="Senden Sie Ihre Bewertung"', 'aria-label="Send your review"', 'popup: Senden -> Send review'),
    ('aria-label="Bewerben Sie sich auf eine freie Stelle"', 'aria-label="Apply for a vacant position"', 'popup: Bewerben -> Apply'),
]

for fname in en_pages:
    with open(fname, encoding='utf-8') as f:
        content = f.read()
    
    file_changes = 0
    for old, new, label in popup_fixes:
        if old in content:
            content = content.replace(old, new)
            file_changes += 1
    
    if file_changes > 0:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print('FIXED ' + str(file_changes) + ' popup labels in ' + fname)
    else:
        print('NO popup changes needed in ' + fname)

print()

# --- Part 4: Fix Azubi EN "Jetzt bewerben!" -> "Apply now!" ---
with open('page70444849.html', encoding='utf-8') as f:
    azubi_en = f.read()

if 'Jetzt bewerben!' in azubi_en:
    azubi_en = azubi_en.replace('Jetzt bewerben!', 'Apply now!')
    with open('page70444849.html', 'w', encoding='utf-8') as f:
        f.write(azubi_en)
    print('FIXED: Azubi EN: Jetzt bewerben! -> Apply now!')
else:
    print('Azubi EN: Jetzt bewerben! not found')
