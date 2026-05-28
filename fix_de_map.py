import re

# Check DE Kontakt page
with open('page57882423.html', 'r', encoding='utf-8') as f:
    c = f.read()

title = re.search(r'<title>(.*?)</title>', c)
print(f'page57882423 title: {title.group(1)[:60] if title else "?"}')
has_map = 't-map' in c
print(f't-map: {has_map}')
if has_map:
    idx = c.find('t_appendGoogleMap')
    if idx >= 0:
        print(f'Map call: {c[idx:idx+150]}')
    # Fix this page too
    print('Fixing this page too...')
    
    MAPS_IFRAME = '''<iframe
src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2560.5!2d8.5688471!3d50.1356347!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47bd091d6124e9bb%3A0x52380d9835417f84!2sWAMOCON%20ACADEMY%20GmbH!5e0!3m2!1sde!2sde!4v1"
width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'''

    map_idx = c.find('t-map-lazyload')
    rec_start = c.rfind('<div id="rec', 0, map_idx)
    rec_id_match = re.search(r'<div id="(rec\d+)"', c[rec_start:rec_start+50])
    rec_id = rec_id_match.group(1) if rec_id_match else None
    
    next_rec = c.find('<div id="rec', rec_start + 10)
    section = c[rec_start:next_rec]
    
    style_match = re.search(r'style="([^"]*)"', section[:200])
    section_style = style_match.group(1) if style_match else ''
    class_match = re.search(r'class="([^"]*)"', section[:200])
    section_class = class_match.group(1) if class_match else 'r t-rec'
    
    new_section = f'''<div id="{rec_id}" class="{section_class}" style="{section_style}" data-record-type="117"> <!-- T117 -->
<div class="t117">
<div class="t117__wrapper" style="height:300px;">
{MAPS_IFRAME}
</div>
</div>
</div>
'''
    c = c[:rec_start] + new_section + c[next_rec:]
    with open('page57882423.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'Fixed {rec_id} map in DE Kontakt page')
