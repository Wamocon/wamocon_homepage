import re
import sys

def fix_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    changes = 0
    
    # Fix body tag
    old_body = '<body class="t-body" style="margin:0;">'
    new_body = '<body class="t-body" style="margin:0;background-color:#101010;">'
    if old_body in text:
        text = text.replace(old_body, new_body)
        changes += 1
        print(f"  Fixed body tag")
    
    # Fix allrecords - add style attribute
    old_allrec = 'id="allrecords" data-tilda-export="yes" class="t-records"'
    new_allrec = 'id="allrecords" data-tilda-export="yes" style="background-color:#101010;" class="t-records"'
    if old_allrec in text:
        text = text.replace(old_allrec, new_allrec)
        changes += 1
        print(f"  Fixed allrecords")
    
    # Fix all style=" " occurrences (empty style with just a space)
    # Pattern: style=" " followed by space and data- or >
    count = text.count('style=" "')
    if count > 0:
        text = text.replace('style=" "', 'style="background-color:#101010; "')
        changes += count
        print(f"  Fixed {count} empty style sections")
    
    # Fix style="padding-top:Xpx;padding-bottom:Xpx; " (no background)
    pattern = r'style="(padding-top:\d+px;padding-bottom:\d+px;) "'
    matches = re.findall(pattern, text)
    if matches:
        text = re.sub(pattern, r'style="\1background-color:#101010; "', text)
        changes += len(matches)
        print(f"  Fixed {len(matches)} padding sections without bg")
    
    if changes > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"  Total changes: {changes}")
    else:
        print(f"  No changes needed")
    
    return changes

if __name__ == '__main__':
    pages = sys.argv[1:]
    for page in pages:
        print(f"\nProcessing: {page}")
        fix_page(page)
