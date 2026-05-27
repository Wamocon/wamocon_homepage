"""final_check.py – Final audit of page59102217.html"""
import re

base = r'c:\Users\Yash Bhesaniya\OneDrive - WAMOCON GmbH\Desktop\WMC\wamocon_homepage'
with open(base + r'\page59102217.html', encoding='utf-8') as f:
    en = f.read()

print("=" * 60)
print("FINAL AUDIT: page59102217.html (English Homepage)")
print("=" * 60)
print(f"File size: {len(en)} bytes\n")

checks = [
    # (description, text_to_find, should_exist)
    ("EN heading 'We develop Solutions'",        'We develop',                          True),
    ("DE heading gone (Wir entwickeln)",         'Wir entwickeln',                      False),
    ("Category: Office & Productivity",          'Office &amp; Productivity',            True),
    ("Category: Marketing, Finance & Planning",  'Marketing, Finance &amp; Planning',   True),
    ("Category: AI, Analysis & Growth",          'AI, Analysis &amp; Growth',            True),
    ("Category: Real Estate & Crafts",           'Real Estate &amp; Crafts',            True),
    ("Category: Mobility, Family & Law",         'Mobility, Family &amp; Law',          True),
    ("Category: E-Commerce & Marketplace",       'E-Commerce &amp; Marketplace',        True),
    ("Category: Lifestyle & Culture",            'Lifestyle &amp; Culture',             True),
    ("DE category gone (Büro & Produktivität)",  'Büro &amp; Produktivität',            False),
    ("360° Office Tour title",                   'Office Tour',                          True),
    ("Start 360° Tour button",                   'Start 360° Tour',                     True),
    ("View counter (not Ansicht)",               'View <strong id',                      True),
    ("Open in Google Maps",                      'Open in Google Maps',                  True),
    ("Start full 360° tour CTA",                 'Start full 360° tour',                True),
    ("rec-leon-apps section present",            'rec-leon-apps',                        True),
    ("rec-360-tour section present",             'rec-360-tour',                         True),
    ("Employee Testimonials nav bug fixed",      'page64750211.html',                   False),
]

all_ok = True
for desc, text, should_exist in checks:
    found = text in en
    ok = found == should_exist
    status = "✓" if ok else "✗"
    if not ok:
        all_ok = False
    label = "present" if found else "absent"
    expected = "present" if should_exist else "absent"
    print(f"  [{status}] {desc}: {label} (expected: {expected})")

print()
print(f"Result: {'ALL CHECKS PASSED' if all_ok else 'SOME CHECKS FAILED'}")

# Count meta tags translated vs German remaining
leon_start = en.index('rec-leon-apps')
leon_end = en.index('rec832623391', leon_start)
sec = en[leon_start:leon_end]
metas = re.findall(r'class="leon-meta">(.+?)</p>', sec)
print(f"\nMeta tags in Innovation Pipeline: {len(metas)} total")
german_metas = [m for m in metas if re.search(r'[äöüÄÖÜß]', m)]
print(f"Still German: {german_metas if german_metas else 'None'}")
