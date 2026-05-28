"""Compare DE vs EN for pages 3-7. Extract text and find German text in English pages."""
from html.parser import HTMLParser
import sys

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.texts = []
        self.skip_tags = {'script', 'style', 'meta', 'link', 'head'}
        self.skip_depth = 0
    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self.skip_depth += 1
    def handle_endtag(self, tag):
        if self.skip_depth > 0 and tag in self.skip_tags:
            self.skip_depth -= 1
    def handle_data(self, data):
        if self.skip_depth == 0:
            d = data.strip()
            if d:
                self.texts.append(d)

def extract_text(fname):
    with open(fname, encoding='utf-8') as f:
        c = f.read()
    p = TextExtractor()
    p.feed(c)
    return p.texts

pages = [
    ('3 Customer Testimonials', 'page57489943.html', 'page59159537.html'),
    ('4 Career',                'page57822475.html', 'page59160115.html'),
    ('5 360-Booster',           'page57874143.html', 'page59165009.html'),
    ('6 Cooperation',           'page57876515.html', 'page59165443.html'),
    ('7 Contact',               'page57882423.html', 'page59169775.html'),
    ('8 Thanks',                'page59449639.html', 'page59449779.html'),
    ('9 Privacy Policy',        'page59452125.html', 'page59452361.html'),
    ('10 Imprint',              'page61093859.html', 'page61094143.html'),
    ('12 Azubi',                'page69503661.html', 'page70444849.html'),
]

# German words that indicate untranslated German text
# (common German-only words that won't appear in English)
german_indicators = [
    'und', 'die', 'der', 'das', 'ist', 'ein', 'eine', 'mit', 'von',
    'für', 'sich', 'auf', 'bei', 'durch', 'nach', 'über', 'oder',
    'werden', 'haben', 'können', 'wir', 'sie', 'ihr', 'den', 'dem',
    'einen', 'einer', 'eines', 'als', 'auch', 'noch', 'nicht', 'werden',
    'Wir', 'Über', 'Für', 'Bei', 'Von', 'Und', 'Die', 'Das', 'Der'
]

def likely_german(text):
    """Returns True if the text likely contains untranslated German content."""
    if len(text) < 15:
        return False
    count = sum(1 for w in german_indicators if (' ' + w + ' ') in (' ' + text + ' '))
    # If 2+ German function words found, likely German
    return count >= 2

for page_name, de_file, en_file in pages:
    print(f'\n{"="*60}')
    print(f'PAGE {page_name}')
    print(f'{"="*60}')
    try:
        en_texts = extract_text(en_file)
        suspected_german = [(i, t) for i, t in enumerate(en_texts) if likely_german(t)]
        if suspected_german:
            print(f'FOUND {len(suspected_german)} possibly untranslated texts in EN:')
            for idx, t in suspected_german[:20]:
                print(f'  [{idx}] {repr(t[:120])}')
        else:
            print('  All text appears to be in English (no obvious German detected)')
    except FileNotFoundError:
        print(f'  EN file not found: {en_file}')
