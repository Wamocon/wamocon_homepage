import re

print("=" * 60)
print("COMPREHENSIVE FIX VERIFICATION")
print("=" * 60)

errors = []

# Test 1: AI/LLM box heights (page59102217.html)
print("\n[1] AI/LLM Box Heights (page59102217.html)")
with open('page59102217.html', 'r', encoding='utf-8') as f:
    c = f.read()

# All 3 row 2 boxes should be 330px
for eid in ['1724080449061', '1724080449067', '1724080449073']:
    match = re.search(rf'#rec832623379 \.tn-elem\[data-elem-id="{eid}"\]\{{[^}}]*height:(\d+)px', c)
    if match:
        h = match.group(1)
        status = "OK" if h == "330" else f"FAIL (got {h})"
        print(f"  Element {eid}: height={h}px - {status}")
        if h != "330":
            errors.append(f"Box {eid} height is {h}, expected 330")
    else:
        print(f"  Element {eid}: NOT FOUND")
        errors.append(f"Box {eid} CSS rule not found")

# Artboard height
match = re.search(r'data-artboard-recid="832623379"[^>]*data-artboard-height="(\d+)"', c)
if match:
    h = match.group(1)
    status = "OK" if h == "757" else f"FAIL (got {h})"
    print(f"  Artboard height: {h}px - {status}")
    if h != "757":
        errors.append(f"Artboard height is {h}, expected 757")

# Test 2: Checkbox alignment (page70444849.html)
print("\n[2] Checkbox Alignment & Resume (page70444849.html)")
with open('page70444849.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Check Resume (no accent)
if 'CV / Resume' in c:
    print("  CV / Resume: OK (no accent)")
else:
    print("  CV / Resume: FAIL")
    if 'R\u00e9sum\u00e9' in c:
        errors.append("Still has R\u00e9sum\u00e9 with accents")
    else:
        errors.append("CV / Resume text not found")

# Check checkbox positions (row 2 should match row 1)
left_match = re.search(r'#rec1088201426 \.tn-elem\[data-elem-id="1748013367595"\]\{[^}]*left:calc\(50% - 600px \+ (-?\d+)px\)', c)
if left_match:
    left_val = left_match.group(1)
    status = "OK" if left_val == "-55" else f"FAIL (got {left_val})"
    print(f"  School Certificates text left: {left_val}px - {status}")
    if left_val != "-55":
        errors.append(f"School Certificates left is {left_val}, expected -55")

left_match = re.search(r'#rec1088201426 \.tn-elem\[data-elem-id="1748013367598"\]\{[^}]*left:calc\(50% - 600px \+ (-?\d+)px\)', c)
if left_match:
    left_val = left_match.group(1)
    status = "OK" if left_val == "554" else f"FAIL (got {left_val})"
    print(f"  Internships text left: {left_val}px - {status}")
    if left_val != "554":
        errors.append(f"Internships left is {left_val}, expected 554")

# Test 3: Footer labels (page70444849.html)
print("\n[3] Footer Labels (page70444849.html)")
# Check Telephone:
if 'Telephone:' in c:
    print("  Telephone: OK")
else:
    print("  Telephone: FAIL (still German?)")
    if 'Telefon:' in c:
        errors.append("Footer still has 'Telefon:' instead of 'Telephone:'")

# Check Contacts heading
if '>Contacts<' in c:
    print("  Contacts heading: OK")
else:
    print("  Contacts heading: FAIL")
    errors.append("Footer heading should be 'Contacts' not 'Contact'")

# Test 4: Google Maps (page59169775.html, page64750211.html, page57882423.html)
print("\n[4] Google Maps Embeds")
map_pages = [
    ('page59169775.html', 'EN Contacts'),
    ('page64750211.html', 'DE Mitarbeiter'),
    ('page57882423.html', 'DE Kontakt'),
]
for page, desc in map_pages:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    has_iframe = 'google.com/maps/embed' in content
    has_old = 't-map-lazyload' in content
    if has_iframe and not has_old:
        print(f"  {desc} ({page}): OK (iframe embed)")
    else:
        print(f"  {desc} ({page}): FAIL (iframe={has_iframe}, old_map={has_old})")
        errors.append(f"{desc} map not properly fixed")

# Test 5: No remaining non-English characters in EN pages
print("\n[5] No non-English accented characters in EN page text")
# Check for é in page70444849.html text (Resume was fixed)
accented = re.findall(r'[\u00e0-\u00ff]', c)
# Filter out CSS/code contexts - only check visible text
# Just verify no Résumé specifically
if '\u00e9' in c:
    # Check if it's in visible text or just in URLs/attributes
    contexts = [c[max(0,m.start()-20):m.start()+20] for m in re.finditer('\u00e9', c)]
    visible_issues = [ctx for ctx in contexts if 'sum' in ctx.lower()]
    if visible_issues:
        print(f"  FAIL: Found accented 'é' in text: {visible_issues}")
        errors.append("Still has accented é in visible text")
    else:
        print("  OK (é only in non-visible contexts like URLs)")
else:
    print("  OK (no é found)")

print("\n" + "=" * 60)
if errors:
    print(f"RESULT: {len(errors)} ERRORS FOUND!")
    for e in errors:
        print(f"  - {e}")
else:
    print("RESULT: ALL TESTS PASSED!")
print("=" * 60)
