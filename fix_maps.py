import re

# The Google Maps iframe embed for WAMOCON ACADEMY GmbH location
# This works without an API key and on any domain/local files
MAPS_IFRAME = '''<iframe
src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2560.5!2d8.5688471!3d50.1356347!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47bd091d6124e9bb%3A0x52380d9835417f84!2sWAMOCON%20ACADEMY%20GmbH!5e0!3m2!1sen!2sde!4v1"
width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'''

def fix_map_in_page(filepath, desc):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the map section
    map_idx = content.find('t-map-lazyload')
    if map_idx < 0:
        print(f'{desc}: No t-map-lazyload found')
        return
    
    # Find the rec section containing the map
    rec_start = content.rfind('<div id="rec', 0, map_idx)
    rec_id_match = re.search(r'<div id="(rec\d+)"', content[rec_start:rec_start+50])
    rec_id = rec_id_match.group(1) if rec_id_match else None
    print(f'{desc}: Map in section {rec_id}')
    
    # Find the complete section boundaries
    # The map section starts with <div id="recXXX" and ends with </div> before the next section
    # Find the section end - look for the closing pattern
    # Tilda map sections have this structure:
    # <div id="recXXX" class="r t-rec ..."> <!-- T117 --> ... </div>
    
    # Find the next rec section or end marker
    next_rec = content.find('<div id="rec', rec_start + 10)
    if next_rec < 0:
        next_rec = content.find('</div>', map_idx + 500)
    
    # The section typically ends with </div> </div> </div> before the script section
    # Let's find the complete map block
    section = content[rec_start:next_rec]
    
    # Build replacement - keep the same div wrapper structure but replace content with iframe
    # Extract the section styling (padding, background)
    style_match = re.search(r'style="([^"]*)"', section[:200])
    section_style = style_match.group(1) if style_match else ''
    class_match = re.search(r'class="([^"]*)"', section[:200])
    section_class = class_match.group(1) if class_match else 'r t-rec'
    
    # Create replacement section with iframe
    new_section = f'''<div id="{rec_id}" class="{section_class}" style="{section_style}" data-record-type="117"> <!-- T117 -->
<div class="t117">
<div class="t117__wrapper" style="height:300px;">
{MAPS_IFRAME}
</div>
</div>
</div>
'''
    
    # Replace the old section
    content = content[:rec_start] + new_section + content[next_rec:]
    
    # Also remove the tilda-map script reference if it's now unused
    # (keep it in case other sections use it)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'{desc}: Map replaced with iframe embed successfully')

# Fix EN Contacts page
fix_map_in_page('page59169775.html', 'EN Contacts')

# Fix DE Mitarbeiter page  
fix_map_in_page('page64750211.html', 'DE Mitarbeiter')

print('\nDone! Maps replaced with embed iframes that work without API key restrictions.')
