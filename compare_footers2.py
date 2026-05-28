import re

with open('page59102217.html', 'r', encoding='utf-8') as f:
    en_home = f.read()

with open('page70444849.html', 'r', encoding='utf-8') as f:
    trainee = f.read()

# Get the full footer section content for both
# EN Homepage: rec832623391
en_sec_start = en_home.find('id="rec832623391"')
en_sec_end = en_home.find('<!-- /T396 -->', en_sec_start)
en_footer = en_home[en_sec_start:en_sec_end]

# Trainee: rec819180409
tr_sec_start = trainee.find('id="rec819180409"')
tr_sec_end = trainee.find('<!-- /T396 -->', tr_sec_start)
tr_footer = trainee[tr_sec_start:tr_sec_end]

# Extract ALL text content from both
print("=== EN Homepage Footer - All text ===")
en_all = re.findall(r"class='tn-atom'[^>]*>(.+?)</div>", en_footer, re.DOTALL)
for t in en_all:
    clean = re.sub(r'<[^>]+>', '', t).strip()
    if clean:
        print(f"  {clean[:80]}")

print("\n=== Trainee Footer - All text ===")
tr_all = re.findall(r"class='tn-atom'[^>]*>(.+?)</div>", tr_footer, re.DOTALL)
for t in tr_all:
    clean = re.sub(r'<[^>]+>', '', t).strip()
    if clean:
        print(f"  {clean[:80]}")

# Check phone number and email differences
print("\n=== Phone numbers ===")
en_phone = re.search(r'tel:([^"]+)', en_footer)
tr_phone = re.search(r'tel:([^"]+)', tr_footer)
print(f"EN: {en_phone.group(1) if en_phone else 'not found'}")
print(f"TR: {tr_phone.group(1) if tr_phone else 'not found'}")

print("\n=== Email ===")
en_email = re.search(r'mailto:([^"]+)', en_footer)
tr_email = re.search(r'mailto:([^"]+)', tr_footer)
print(f"EN: {en_email.group(1) if en_email else 'not found'}")
print(f"TR: {tr_email.group(1) if tr_email else 'not found'}")

# Check Saturday hours
print("\n=== Looking for Saturday ===")
if 'Saturday' in en_footer:
    print("EN has Saturday hours")
else:
    print("EN does NOT have Saturday hours")
if 'Saturday' in tr_footer:
    print("TR has Saturday hours")
else:
    print("TR does NOT have Saturday hours")

# Check the links (Google Maps, social media)
print("\n=== Google Maps link ===")
en_maps = re.search(r'google\.com/maps[^"]*', en_footer)
tr_maps = re.search(r'google\.com/maps[^"]*', tr_footer)
print(f"EN: {'yes' if en_maps else 'no'}")
print(f"TR: {'yes' if tr_maps else 'no'}")
