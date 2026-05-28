import re

with open('page70444849.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix 1: Telefon: -> Telephone: (only in the footer section rec819180409)
sec_start = c.find('id="rec819180409"')
sec_end = c.find('<!-- /T396 -->', sec_start)

# Replace within the section only
section = c[sec_start:sec_end]

# Fix Telefon: -> Telephone:
old_telefon = ">Telefon:<"
new_telefon = ">Telephone:<"
if old_telefon in section:
    section = section.replace(old_telefon, new_telefon)
    print('Fixed: Telefon: -> Telephone:')
else:
    # Try alternate pattern
    old_telefon = "'>Telefon:</div>"
    new_telefon = "'>Telephone:</div>"
    if old_telefon in section:
        section = section.replace(old_telefon, new_telefon)
        print('Fixed: Telefon: -> Telephone: (alt pattern)')
    else:
        print('Telefon: pattern not found')
        # Find exact context
        idx = section.find('Telefon')
        if idx >= 0:
            print(f'  Context: {section[idx-20:idx+30]}')

# Fix Contact -> Contacts (heading)
old_contact = "'>Contact</div>"
new_contact = "'>Contacts</div>"
if old_contact in section:
    section = section.replace(old_contact, new_contact)
    print('Fixed: Contact -> Contacts')
else:
    # Try finding exact pattern
    idx = section.find('>Contact<')
    if idx >= 0:
        print(f'  Contact context: {section[idx-5:idx+20]}')
        section = section[:idx] + '>Contacts<' + section[idx+len('>Contact<'):]
        print('Fixed: Contact -> Contacts (via >Contact<)')
    else:
        print('Contact heading not found')
        # Search more broadly
        contact_positions = [m.start() for m in re.finditer('Contact', section)]
        for p in contact_positions[:5]:
            print(f'  Contact at: {section[max(0,p-10):p+20]}')

c = c[:sec_start] + section + c[sec_end:]
with open('page70444849.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Done!')
