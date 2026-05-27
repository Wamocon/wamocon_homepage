"""fix_en_homepage.py – Fixes remaining untranslated German text in page59102217.html"""

base = r'c:\Users\Yash Bhesaniya\OneDrive - WAMOCON GmbH\Desktop\WMC\wamocon_homepage'
en_file = base + r'\page59102217.html'

with open(en_file, encoding='utf-8') as f:
    en = f.read()

original_len = len(en)
print(f"Original length: {original_len}")

# ── 1. Fix heading (Wir entwickeln) ─────────────────────────────────────────
en = en.replace(
    'Wir entwickeln <span style="color:#ff0b00;">Lösungen</span> für jede Problemstellung',
    'We develop <span style="color:#ff0b00;">Solutions</span> for every challenge'
)

# ── 2. Fix branch / category titles ─────────────────────────────────────────
category_map = {
    'Büro &amp; Produktivität':           'Office &amp; Productivity',
    'Marketing, Finanzen &amp; Planung':  'Marketing, Finance &amp; Planning',
    'KI, Analyse &amp; Growth':           'AI, Analysis &amp; Growth',
    'Immobilien &amp; Handwerk':          'Real Estate &amp; Crafts',
    'Mobilität, Familie &amp; Recht':     'Mobility, Family &amp; Law',
    'E-Commerce &amp; Marktplatz':        'E-Commerce &amp; Marketplace',
    'Lifestyle &amp; Kultur':             'Lifestyle &amp; Culture',
}
for de, eng in category_map.items():
    en = en.replace(de, eng)

# ── 3. Fix any remaining "öffnen" link titles ────────────────────────────────
import re
en = re.sub(r'title="(.+?) öffnen"',  r'title="Open \1"', en)
en = re.sub(r'title="(.+?) oeffnen"', r'title="Open \1"', en)

# ── 4. Fix 360° tour remaining German ────────────────────────────────────────
tour_fixes = {
    '<h2 class="tour360-title"><span>360°</span> Büro Tour</h2>':
        '<h2 class="tour360-title"><span>360°</span> Office Tour</h2>',
    'Erkunden Sie unser Büro virtuell \u2013 klicken Sie auf die Vorschau, um die interaktive 360° Ansicht zu starten':
        'Explore our office virtually \u2013 click on the preview to start the interactive 360° view',
    'aria-label="360° Büro Tour starten"':  'aria-label="Start 360° Office Tour"',
    '<span class="tour360-play-label">360° Tour starten</span>':
        '<span class="tour360-play-label">Start 360° Tour</span>',
    'title="360° Büro Tour"':               'title="360° Office Tour"',
    'aria-label="Vorherige Ansicht"':       'aria-label="Previous view"',
    'aria-label="Nächste Ansicht"':         'aria-label="Next view"',
    'Ansicht <strong id="tour360-cur">1</strong> / <strong>14</strong>':
        'View <strong id="tour360-cur">1</strong> / <strong>14</strong>',
    'In Google Maps öffnen &#8599;':        'Open in Google Maps &#8599;',
    'Vollständige 360° Tour starten &#8599;': 'Start full 360° tour &#8599;',
    '14 Ansichten · Büro &amp; Außenbereich': '14 views &middot; Office &amp; exterior',
}
for de, eng in tour_fixes.items():
    en = en.replace(de, eng)

# Fix JS view labels (Ansicht 1..14)
en = en.replace("label: 'Ansicht 1'", "label: 'View 1'")
for i in range(2, 15):
    en = en.replace(f"label: 'Ansicht {i}'", f"label: 'View {i}'")
# The "Ansicht 2 – Außen" variant
en = re.sub(r"label: 'Ansicht 2[^']*'", "label: 'View 2 -- Exterior'", en)

# ── 5. Fix Employee Testimonials nav link (BUG: points to German page) ──────
# The English nav currently links to page64750211.html (German employee reviews)
# The page has no English equivalent – remove just that nav item
# The nav item looks like: href="page64750211.html" with "Employee Testimonials" or "Mitarbeiter Stimmen" text
# Find and report it
m = re.search(r'<a[^>]+href="page64750211\.html"[^>]*>(.+?)</a>', en)
if m:
    print(f"Found nav link: {m.group(0)[:200]}")
    # Remove or comment the entire <li> containing this link
    en = re.sub(r'<li[^>]*>\s*<a[^>]+href="page64750211\.html"[^>]*>.+?</a>\s*</li>', '', en, flags=re.DOTALL)
    print("Removed Employee Testimonials nav link (German-only page)")
else:
    print("Employee Testimonials nav link not found via href pattern – checking for text...")
    idx = en.find('page64750211.html')
    if idx >= 0:
        print(f"Raw occurrence: {en[max(0,idx-50):idx+200]}")

# ── 6. Verify ─────────────────────────────────────────────────────────────────
checks = {
    'Wir entwickeln':              False,   # should NOT be present
    'We develop':                  True,    # should be present
    'Office &amp; Productivity':   True,
    'AI, Analysis &amp; Growth':   True,
    'Lifestyle &amp; Culture':     True,
    'Office Tour':                 True,
    'Start 360° Tour':             True,
    'View <strong id':             True,
}
print("\nVerification:")
all_ok = True
for text, should_exist in checks.items():
    found = text in en
    status = "OK" if found == should_exist else "FAIL"
    if status == "FAIL":
        all_ok = False
    print(f"  [{status}] '{text}' {'present' if found else 'absent'} (expected: {'present' if should_exist else 'absent'})")

print(f"\nAll OK: {all_ok}")
print(f"New length: {len(en)} (added {len(en)-original_len} chars vs original)")

# Save
with open(en_file, 'w', encoding='utf-8') as f:
    f.write(en)
print("Saved.")
