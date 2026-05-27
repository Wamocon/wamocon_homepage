"""fix_nav_link.py – Removes the broken Employee Testimonials nav link from page59102217.html"""
import re

base = r'c:\Users\Yash Bhesaniya\OneDrive - WAMOCON GmbH\Desktop\WMC\wamocon_homepage'
en_file = base + r'\page59102217.html'

with open(en_file, encoding='utf-8') as f:
    en = f.read()

# Show context around page64750211.html
idx = en.find('page64750211.html')
print("Before fix:")
print(repr(en[max(0,idx-100):idx+300]))
print()

# Remove the <li>...</li> containing the link (multiline match)
en_new = re.sub(
    r'<li[^>]*>[ \t]*<a[^>]*\nhref="page64750211\.html"[^>]*>[\s\S]*?</a>[ \t]*</li>',
    '',
    en
)

if 'page64750211.html' in en_new:
    print("Still present, trying simpler pattern...")
    # Try simpler: remove from <li to </li> containing page64750211
    en_new = re.sub(
        r'<li[^>]*>[\s\S]*?page64750211\.html[\s\S]*?</li>',
        '',
        en
    )

if 'page64750211.html' in en_new:
    print("Still present after second attempt!")
else:
    print("Successfully removed Employee Testimonials nav link")

print(f"Length change: {len(en)} → {len(en_new)}")

with open(en_file, 'w', encoding='utf-8') as f:
    f.write(en_new)
print("Saved.")
