import re
import sys

def fix_employee_testimonials(filepath):
    """Fix the employee testimonials page to match live version:
    1. Hide Yash and Maanik desktop sections (not on live site)
    2. Hide extra placeholder carousel entries
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    changes = 0
    
    # 1. Hide rec_yash_desktop section (add display:none)
    old_yash = 'id="rec_yash_desktop" class="r t-rec t-rec_pt_60 t-rec_pt-res-480_60 t-rec_pb_0 t-rec_pb-res-480_0 t-screenmin-980px" style="padding-top:60px;padding-bottom:0px;background-color:#101010;"'
    new_yash = 'id="rec_yash_desktop" class="r t-rec t-rec_pt_60 t-rec_pt-res-480_60 t-rec_pb_0 t-rec_pb-res-480_0 t-screenmin-980px" style="display:none;padding-top:60px;padding-bottom:0px;background-color:#101010;"'
    if old_yash in text:
        text = text.replace(old_yash, new_yash)
        changes += 1
        print(f"  Hidden rec_yash_desktop")
    else:
        print(f"  WARNING: rec_yash_desktop not found with expected style")
    
    # 2. Hide rec_maanik_desktop section (add display:none)
    old_maanik = 'id="rec_maanik_desktop" class="r t-rec t-rec_pt_60 t-rec_pt-res-480_60 t-rec_pb_0 t-rec_pb-res-480_0 t-screenmin-980px" style="padding-top:60px;padding-bottom:0px;background-color:#101010;"'
    new_maanik = 'id="rec_maanik_desktop" class="r t-rec t-rec_pt_60 t-rec_pt-res-480_60 t-rec_pb_0 t-rec_pb-res-480_0 t-screenmin-980px" style="display:none;padding-top:60px;padding-bottom:0px;background-color:#101010;"'
    if old_maanik in text:
        text = text.replace(old_maanik, new_maanik)
        changes += 1
        print(f"  Hidden rec_maanik_desktop")
    else:
        print(f"  WARNING: rec_maanik_desktop not found with expected style")
    
    # 3. In Nurzhan carousel (rec890540353), hide the placeholder entries
    # Find and hide entries with "Demnächst verfügbar" placeholder
    # These are carousel items for future videos (Nurzhan 2J, 2.5J, 3J) and wrong (Yash, Maanik)
    # The approach: find each t-col with placeholder and add display:none
    # Pattern: <div class="t-col t-col_4"> <div class="t1061__wrap-video"> <div style="width:100%;padding-top:56.25%;background-color:#1e1e1e;
    placeholder_pattern = r'(<div class="t-col t-col_4">\s*<div class="t1061__wrap-video">\s*<div style="width:100%;padding-top:56\.25%;background-color:#1e1e1e;)'
    placeholder_replace = r'<div class="t-col t-col_4" style="display:none;"> <div class="t1061__wrap-video"> <div style="width:100%;padding-top:56.25%;background-color:#1e1e1e;'
    
    # Count how many placeholders exist
    placeholder_count = len(re.findall(placeholder_pattern, text))
    if placeholder_count > 0:
        text = re.sub(placeholder_pattern, placeholder_replace, text)
        changes += placeholder_count
        print(f"  Hidden {placeholder_count} placeholder carousel entries")
    
    if changes > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"  Saved with {changes} changes")
    else:
        print(f"  No changes needed")
    
    return changes

if __name__ == '__main__':
    pages = sys.argv[1:]
    for page in pages:
        print(f"\nProcessing: {page}")
        fix_employee_testimonials(page)
