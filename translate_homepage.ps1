
# translate_homepage.ps1
# Translates missing German sections into English and injects them into page59102217.html

$base = "c:\Users\Yash Bhesaniya\OneDrive - WAMOCON GmbH\Desktop\WMC\wamocon_homepage"
$deFile = "$base\index.html"
$enFile = "$base\page59102217.html"

Write-Host "Reading files..."
$deRaw = [System.IO.File]::ReadAllText($deFile, [System.Text.Encoding]::UTF8)
$enRaw = [System.IO.File]::ReadAllText($enFile, [System.Text.Encoding]::UTF8)

# --- Extract German sections ---
$ls = $deRaw.IndexOf('<div id="rec-leon-apps"')
$le = $deRaw.IndexOf('<div id="rec819175753"', $ls)
$leonDE = $deRaw.Substring($ls, $le - $ls)

$ts = $deRaw.IndexOf('<div id="rec-360-tour"')
$te = $deRaw.IndexOf('<div id="rec819180409"', $ts)
$tourDE = $deRaw.Substring($ts, $te - $ts)

Write-Host "Leon section: $($leonDE.Length) chars"
Write-Host "Tour section: $($tourDE.Length) chars"

# --- Translate Innovation Pipeline ---
$leonEN = $leonDE

# Heading
$leonEN = $leonEN -replace 'Wir entwickeln <span style="color:#ff0b00;">Lösungen</span> für jede Problemstellung', 'We develop <span style="color:#ff0b00;">Solutions</span> for every challenge'

# Intro paragraph - handle multiline
$leonEN = $leonEN -replace 'In aufeinander aufbauenden <strong[\s\S]+?</strong> verwandeln wir konkrete[\s\S]+?bis hin zu E-Commerce und Lifestyle\.', 'In successive <strong style="color:#fff;font-weight:600;">development waves</strong>, we transform concrete challenges into digital products &ndash; from office automation, marketing and AI-driven analysis to real estate, mobility and law through to e-commerce and lifestyle.'

# Category branch titles
$leonEN = $leonEN -replace 'Büro &amp; Produktivität', 'Office &amp; Productivity'
$leonEN = $leonEN -replace 'Marketing, Finanzen &amp; Planung', 'Marketing, Finance &amp; Planning'
$leonEN = $leonEN -replace 'KI, Analyse &amp; Growth', 'AI, Analysis &amp; Growth'
$leonEN = $leonEN -replace 'Immobilien &amp; Handwerk', 'Real Estate &amp; Crafts'
$leonEN = $leonEN -replace 'Mobilität, Familie &amp; Recht', 'Mobility, Family &amp; Law'
$leonEN = $leonEN -replace 'E-Commerce &amp; Marktplatz', 'E-Commerce &amp; Marketplace'
$leonEN = $leonEN -replace 'Lifestyle &amp; Kultur', 'Lifestyle &amp; Culture'

# Product meta tags
$metaMap = @{
    'Urlaubsplanung'           = 'Vacation Planning'
    'Inventar'                 = 'Inventory'
    'KI / Bildung'             = 'AI / Education'
    'Buero / Automatisierung'  = 'Office / Automation'
    'Barrierefreiheit / Compliance' = 'Accessibility / Compliance'
    'KI / Infrastruktur'       = 'AI / Infrastructure'
    'KI / Weiterbildung'       = 'AI / Training'
    'Zusammenarbeit / Lokal'   = 'Collaboration / Local'
    'Finanzen'                 = 'Finance'
    'Hochzeit / Planung'       = 'Wedding / Planning'
    'IT / Backup'              = 'IT / Backup'
    'Einkauf / Planung'        = 'Procurement / Planning'
    'Automotive / Verwaltung'  = 'Automotive / Management'
    'Planung / KI'             = 'Planning / AI'
    'Analyse / Business'       = 'Analysis / Business'
    'Finanzen / Wohnen'        = 'Finance / Housing'
    'Finanzen / Recht'         = 'Finance / Law'
    'Verifizierung / KI'       = 'Verification / AI'
    'IT-Security'              = 'IT Security'
    'HR / Skillmapping'        = 'HR / Skill Mapping'
    'Medical AI / Gesundheit'  = 'Medical AI / Health'
    'KI / Entwicklung'         = 'AI / Development'
    'KI / Prompt-Management'   = 'AI / Prompt Management'
    'Handwerk'                 = 'Crafts &amp; Trades'
    'Wohnen / Gemeinschaft'    = 'Housing / Community'
    'Immobilien / Garten'      = 'Real Estate / Garden'
    'Community / Lokales'      = 'Community / Local'
    'E-Mobilität'              = 'E-Mobility'
    'Familie'                  = 'Family'
    'Recht'                    = 'Law'
    'E-Commerce / KI'          = 'E-Commerce / AI'
    'Prozesse / Intern'        = 'Processes / Internal'
    'Oeffentliche Dienste'     = 'Public Services'
    'Verein / Community'       = 'Club / Community'
    'Familie / Events'         = 'Family / Events'
    'Mobilitaet / Versicherung'= 'Mobility / Insurance'
    'Mobilität / Sicherheit'   = 'Mobility / Safety'
    'Finanzen / Buchhaltung'   = 'Finance / Accounting'
    'E-Commerce / Auktionen'   = 'E-Commerce / Auctions'
    'Inventar / Verwaltung'    = 'Inventory / Management'
    'Genealogie / Kultur'      = 'Genealogy / Culture'
    'Immobilien / Steuern'     = 'Real Estate / Taxes'
    'Recht / Vertraege'        = 'Law / Contracts'
}

foreach ($de in $metaMap.Keys) {
    $en = $metaMap[$de]
    $leonEN = $leonEN -replace ([regex]::Escape('<p class="leon-meta">' + $de + '</p>')), "<p class=`"leon-meta`">$en</p>"
}

# Product descriptions (German → English)
$descMap = @{
    'Digitale Urlaubsantragstellung mit Genehmigungsprozess, Kalender-Anbindung,\s+Email-Benachrichtigungen und Vorlagenverwaltung\.' = 'Digital vacation request submission with approval process, calendar integration, email notifications and template management.'
    'Zentrale Ger&auml;teverwaltung und Inventar-Tracking für Unternehmen mit Zuweisung und\s+Statusverfolgung\.' = 'Central device management and inventory tracking for companies with assignment and status monitoring.'
    'Zentrale Geräteverwaltung und Inventar-Tracking für Unternehmen mit Zuweisung und\s+Statusverfolgung\.' = 'Central device management and inventory tracking for companies with assignment and status monitoring.'
    'KI-gestuetztes Lernmanagementsystem fuer moderne Wissensverteilung, Kursplanung und\s+Fortschrittstracking\.' = 'AI-powered learning management system for modern knowledge distribution, course planning and progress tracking.'
    'Digitaler Assistent fuer Bueroprozesse: Dokumentenverwaltung, Aufgabenverteilung und\s+Kommunikation im Team\.' = 'Digital assistant for office processes: document management, task distribution and team communication.'
    'Lokale KI-Plattform fuer den internen Einsatz im LAN ohne Cloud-Abhaengigkeit\.\s+Datensouveraene Verarbeitung sensibler Unternehmensdaten\.' = 'Local AI platform for internal LAN use without cloud dependency. Data-sovereign processing of sensitive corporate data.'
    'Regionale Datensynchronisation und Zusammenarbeit für lokale Unternehmen\.' = 'Regional data synchronization and collaboration for local businesses.'
    'Zentrale Kampagnenverwaltung mit strukturierter Erstellung, Creative-Workflow und\s+kanalbezogenen KPIs\.' = 'Central campaign management with structured creation, creative workflow and channel-specific KPIs.'
    'Budget- und Finanzverwaltung mit Übersicht über Einnahmen, Ausgaben und Einsparpotenziale\.' = 'Budget and financial management with overview of income, expenses and savings potential.'
    'Dynamische Hochzeits-Budgetkalkulation nach Region und Gästezahl plus CRM für Dienstleister\s+und Checklisten\.' = 'Dynamic wedding budget calculation by region and guest count plus CRM for service providers and checklists.'
    'Planung und Verwaltung von Datensicherungen mit automatisierten Backup-Strategien und\s+Statusübersicht\.' = 'Planning and management of data backups with automated backup strategies and status overview.'
    'Digitale Bedarfsplanung und Beschaffungsmanagement fuer Unternehmen mit Lieferantenverwaltung\s+und Kostenoptimierung\.' = 'Digital demand planning and procurement management for companies with supplier management and cost optimization.'
    'Prüfung und Analyse von Nebenkostenabrechnungen auf Fehler und Einsparpotenziale\.' = 'Review and analysis of utility bill statements for errors and savings potential.'
    'Verwaltung und Kostenübersicht für Verträge, Abos und laufende Kosten\.' = 'Management and cost overview for contracts, subscriptions and ongoing costs.'
    'Content-Verifizierung mit fünf Analyse-Modi: Faktencheck, Bias-Erkennung, KI-Erkennung,\s+Plagiatsprüfung und Qualitätsbewertung\.' = 'Content verification with five analysis modes: fact-checking, bias detection, AI detection, plagiarism check and quality assessment.'
    'Middleware zwischen Mitarbeitenden und KI-Modellen mit DLP, Prompt-Filterung,\s+PII-Anonymisierung und Audit-Logs\.' = 'Middleware between employees and AI models with DLP, prompt filtering, PII anonymization and audit logs.'
    'KI-gestütztes Skill-Mapping: Fähigkeiten aus Lebensläufen und Projektlogs extrahieren und\s+intern matchen\.' = 'AI-powered skill mapping: extract capabilities from CVs and project logs and match them internally.'
    'Tägliche Reflexionsfragen mit Sentiment-Analyse und passenden Mikroaktivitäten für\s+persönliches Wachstum\.' = 'Daily reflection questions with sentiment analysis and matching micro-activities for personal growth.'
    'KI-gestuetzter Pruefungstrainer fuer Berufsausbildung und Zertifizierungen mit adaptiven\s+Lernpfaden und Selbsttests\.' = 'AI-powered exam trainer for vocational training and certifications with adaptive learning paths and self-tests.'
    'Verwaltung, Versionierung und Optimierung von KI-Prompts für Teams\.' = 'Management, versioning and optimization of AI prompts for teams.'
    'Handwerker-Vermittlung und Auftragsverwaltung für schnelle, zuverlässige Reparaturen und\s+Installationen\.' = 'Tradesman placement and job management for fast, reliable repairs and installations.'
    'Digitale Verwaltung von Wohngemeinschaften mit Aufgabenverteilung, Einkaufslisten und\s+transparenter Kostenteilung\.' = 'Digital management of shared apartments with task distribution, shopping lists and transparent cost sharing.'
    'Kartenbasierte Übersicht für Ladesäulen und E-Mobility-Standorte mit Verfügbarkeit und\s+Routenplanung\.' = 'Map-based overview of charging stations and e-mobility locations with availability and route planning.'
    'Standortbasierte Suche nach freien Kita-Plätzen und Betreuungsangeboten in der näheren Umgebung\.' = 'Location-based search for available childcare spots and care services in the local area.'
    'Überprüfung und Optimierung des Schufa-Scores mit konkreten Handlungsempfehlungen und\s+Schritt-für-Schritt-Anleitung\.' = 'Review and optimization of the credit score with concrete recommendations and step-by-step guidance.'
    'Verwaltung und Analyse von Verträgen mit automatischem Fristen-Tracking, Erinnerungen und\s+Kündigungsoptionen\.' = 'Management and analysis of contracts with automatic deadline tracking, reminders and cancellation options.'
    'Verwaltung und Bereinigung veralteter oder inaktiver digitaler Konten zur Reduktion von\s+Angriffsflächen\.' = 'Management and cleanup of outdated or inactive digital accounts to reduce attack surfaces.'
    'KI-gestützter Shopping-Assistent für personalisierte Produktempfehlungen und smarte\s+Kaufentscheidungen im E-Commerce\.' = 'AI-powered shopping assistant for personalized product recommendations and smart purchasing decisions in e-commerce.'
    'Internes Portal zur strukturierten Erfassung, Priorisierung und Verwaltung von Projekt- und\s+Produktanforderungen\.' = 'Internal portal for structured capture, prioritization and management of project and product requirements.'
    'Intelligente Geburtstagsverwaltung mit Erinnerungen, Geschenkideen und personalisierter Planung\s+fuer die ganze Familie\.' = 'Smart birthday management with reminders, gift ideas and personalized planning for the whole family.'
    'Warnsystem für Blitzer, Gefahrenstellen und Tempoüberwachung im Straßenverkehr\.' = 'Warning system for speed cameras, hazard zones and speed monitoring on roads.'
    'KI-gestuetzter Shopping-Assistent fuer smarte Kaufentscheidungen, Preisvergleiche und\s+personalisierte Produktempfehlungen\.' = 'AI-powered shopping assistant for smart purchasing decisions, price comparisons and personalized product recommendations.'
    'Digitale Visitenkarte und Card-Management-Loesung fuer professionelles Networking und\s+Kontaktverwaltung\.' = 'Digital business card and card management solution for professional networking and contact management.'
    'Intelligente Vertragsverwaltung und Kuendigungsmanagement fuer Privatpersonen und kleine\s+Unternehmen\.' = 'Smart contract management and cancellation management for individuals and small businesses.'
}

foreach ($de in $descMap.Keys) {
    $en = $descMap[$de]
    $leonEN = [regex]::Replace($leonEN, $de, $en)
}

# "Coming soon" link titles and placeholder text
$leonEN = $leonEN -replace 'title="Bald verfügbar"', 'title="Coming soon"'
$leonEN = $leonEN -replace 'title="Bald verfuegbar"', 'title="Coming soon"'
$leonEN = $leonEN -replace 'Lorem ipsum dolor sit amet, consectetur adipiscing elit\. Beschreibung wird in Kuerze\s+ergaenzt\.', 'Description coming soon.'
$leonEN = $leonEN -replace 'Lorem ipsum dolor sit amet, consectetur adipiscing elit\. Beschreibung wird in Kuerze ergaenzt\.', 'Description coming soon.'

# Fix remaining open link titles
$leonEN = $leonEN -replace 'title="AWAY öffnen"', 'title="Open AWAY"'
$leonEN = $leonEN -replace 'title="KI Manager LMS oeffnen"', 'title="Open KI Manager LMS"'
$leonEN = $leonEN -replace 'title="Backoffice Assistent oeffnen"', 'title="Open Backoffice Assistant"'
$leonEN = $leonEN -replace 'title="RegioSync öffnen"', 'title="Open RegioSync"'
$leonEN = $leonEN -replace 'title="Marketing Planer öffnen"', 'title="Open Marketing Planner"'
$leonEN = $leonEN -replace 'title="WedBudget öffnen"', 'title="Open WedBudget"'
$leonEN = $leonEN -replace 'title="Bedarfspilot oeffnen"', 'title="Open Bedarfspilot"'
$leonEN = $leonEN -replace 'title="Nebenkostencheck öffnen"', 'title="Open Nebenkostencheck"'
$leonEN = $leonEN -replace 'title="VertragsManager öffnen"', 'title="Open VertragsManager"'
$leonEN = $leonEN -replace 'title="Kompetenzkompass öffnen"', 'title="Open Kompetenzkompass"'
$leonEN = $leonEN -replace 'title="KI-Pruefungstrainer oeffnen"', 'title="Open AI Exam Trainer"'
$leonEN = $leonEN -replace 'title="ARIA oeffnen"', 'title="Open ARIA"'
$leonEN = $leonEN -replace 'title="PromptControl öffnen"', 'title="Open PromptControl"'
$leonEN = $leonEN -replace 'title="Ustafix öffnen"', 'title="Open Ustafix"'
$leonEN = $leonEN -replace 'title="WG-Planer oeffnen"', 'title="Open WG-Planer"'
$leonEN = $leonEN -replace 'title="Ladekompass öffnen"', 'title="Open Ladekompass"'
$leonEN = $leonEN -replace 'title="Kita Radar öffnen"', 'title="Open Kita Radar"'
$leonEN = $leonEN -replace 'title="Schufa Cleaner öffnen"', 'title="Open Schufa Cleaner"'
$leonEN = $leonEN -replace 'title="VertragsPro öffnen"', 'title="Open VertragsPro"'
$leonEN = $leonEN -replace 'title="Geburtstagspilot oeffnen"', 'title="Open Geburtstagspilot"'
$leonEN = $leonEN -replace 'title="Rideproof oeffnen"', 'title="Open Rideproof"'
$leonEN = $leonEN -replace 'title="BlitzerSafe öffnen"', 'title="Open BlitzerSafe"'
$leonEN = $leonEN -replace 'title="BuyRight-AI oeffnen"', 'title="Open BuyRight-AI"'
$leonEN = $leonEN -replace 'title="CanCard oeffnen"', 'title="Open CanCard"'
$leonEN = $leonEN -replace 'title="belegnest oeffnen"', 'title="Open belegnest"'
$leonEN = $leonEN -replace 'title="AhnenEcho oeffnen"', 'title="Open AhnenEcho"'
$leonEN = $leonEN -replace 'title="BaseGuard oeffnen"', 'title="Open BaseGuard"'

Write-Host "Translation complete. EN Leon length: $($leonEN.Length)"

# --- Translate 360° Tour section ---
$tourEN = $tourDE

# Text content
$tourEN = $tourEN -replace '<h2 class="tour360-title"><span>360°</span> Büro Tour</h2>', '<h2 class="tour360-title"><span>360°</span> Office Tour</h2>'
$tourEN = $tourEN -replace 'Erkunden Sie unser Büro virtuell – klicken Sie auf die Vorschau, um die interaktive 360° Ansicht zu starten', 'Explore our office virtually – click on the preview to start the interactive 360° view'
$tourEN = $tourEN -replace 'aria-label="360° Büro Tour starten"', 'aria-label="Start 360° Office Tour"'
$tourEN = $tourEN -replace '<span class="tour360-play-label">360° Tour starten</span>', '<span class="tour360-play-label">Start 360° Tour</span>'
$tourEN = $tourEN -replace 'title="360° Büro Tour"', 'title="360° Office Tour"'
$tourEN = $tourEN -replace 'aria-label="Vorherige Ansicht"', 'aria-label="Previous view"'
$tourEN = $tourEN -replace 'aria-label="Nächste Ansicht"', 'aria-label="Next view"'
$tourEN = $tourEN -replace 'Ansicht <strong id="tour360-cur">1</strong> / <strong>14</strong>', 'View <strong id="tour360-cur">1</strong> / <strong>14</strong>'
$tourEN = $tourEN -replace 'In Google Maps öffnen &#8599;', 'Open in Google Maps &#8599;'
$tourEN = $tourEN -replace 'Vollständige 360° Tour starten &#8599;', 'Start full 360° tour &#8599;'
$tourEN = $tourEN -replace '14 Ansichten · Büro &amp; Außenbereich', '14 views &middot; Office &amp; exterior'

# View labels in JS VIEWS array
$tourEN = $tourEN -replace "label: 'Ansicht 1'", "label: 'View 1'"
$tourEN = $tourEN -replace "label: 'Ansicht 2 .* Außen'", "label: 'View 2 -- Exterior'"
for ($i = 3; $i -le 14; $i++) {
    $tourEN = $tourEN -replace "label: 'Ansicht $i'", "label: 'View $i'"
}

# aria-labels in thumb buttons (generated by JS, using v.label) - no change needed in HTML
# alt text in thumb buttons is also v.label - OK

Write-Host "Tour translation complete. EN Tour length: $($tourEN.Length)"

# --- Inject into English page ---
$insertionPoint = '<div id="rec832623391"'
$insertIdx = $enRaw.IndexOf($insertionPoint)
Write-Host "Insertion point at char: $insertIdx"

if ($insertIdx -lt 0) {
    Write-Error "Could not find insertion point in English page!"
    exit 1
}

# Build the new English page content
$newEN = $enRaw.Substring(0, $insertIdx)
$newEN += "`n" + $leonEN + "`n"
$newEN += $tourEN + "`n"
$newEN += $enRaw.Substring($insertIdx)

Write-Host "New EN page length: $($newEN.Length)"
Write-Host "Original EN page length: $($enRaw.Length)"
Write-Host "Added content: $($newEN.Length - $enRaw.Length) chars"

# Write the updated file
[System.IO.File]::WriteAllText("$base\page59102217.html", $newEN, [System.Text.Encoding]::UTF8)
Write-Host "SUCCESS: page59102217.html updated!"
