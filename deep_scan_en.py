"""Deeper scan for German text in English pages - targeting specific German patterns."""
from html.parser import HTMLParser
import re

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

def get_raw(fname):
    with open(fname, encoding='utf-8') as f:
        return f.read()

# German-specific patterns that are very unlikely in English text
german_patterns = [
    # German verb forms / grammar
    r'\bist\s+ein\b',            # "ist ein" = "is a" in German
    r'\bsind\s+\w+\b',           # "sind" = "are"
    r'\bwird\s+\w+\b',           # "wird" = "will be"
    r'\bwurde\s+\w+\b',          # "wurde" = "was"
    r'\bhat\s+\w+\s+\w+\b',      # "hat ... gemacht" pattern
    r'\bkann\s+\w+\b',           # "kann" = "can"
    r'\bSie\s+\w+\b',            # "Sie" formal "you"
    r'\bdurch\s+\w+\b',          # "durch" = "through"
    r'\bnach\s+\w+\b',           # "nach" = "after/to"
    r'\bwird\b',                  # "wird"
    r'\bder\s+[A-ZÄÖÜa-zäöü]+\b', # "der X" German article
    # German-specific words
    r'\bGmbH\s+hat\b',           # "GmbH hat"
    r'\bHerren\b',               # "Herren" = "gentlemen"
    r'\bDamen\b',                # "Damen" = "ladies"
    r'\beinen\s+\w+\b',          # "einen" German article
    r'\beiner\s+\w+\b',          # "einer"
    r'\bsich\s+\w+\b',           # "sich" reflexive
    r'\bunserer\b',              # "unserer" German
    r'\bIhrem\b',                # "Ihrem" formal German
    r'\bIhrer\b',                # "Ihrer" formal German
    r'\bIhre\b',                 # "Ihre" formal German
    r'\bIhnen\b',                # "Ihnen" formal German
    r'\bdass\b',                 # "dass" = "that" in German
    r'\bdaher\b',                # "daher" = "therefore"
    r'\bdabei\b',                # "dabei"
    r'\bdamit\b',                # "damit"
    r'\bdurch\b',                # "durch"
    r'\bwenn\b',                 # "wenn" = "when/if"
    r'\bzur\b',                  # "zur"
    r'\bzum\b',                  # "zum"
    r'\bals\s+[A-Z]\w+\b',      # "als X" German "as"
    r'\bbei\s+\w+\b',            # "bei" = "at/with"
    r'\bsollen\b',               # German modal
    r'\bkönnen\b',               # German modal
    r'\bmüssen\b',               # German modal
    r'\bwollen\b',               # German modal
    r'\bwerden\b',               # German modal
    r'\bsollte\b',               # German conditional
    r'\bkönnten\b',              # German conditional
    r'\bmöchten\b',              # German conditional
    r'\bwären\b',                # German conditional
    r'\bhätten\b',               # German conditional
    r'\bdeshalb\b',              # German "therefore"
    r'\ballerdings\b',           # German "however"
    r'\baußerdem\b',             # German "furthermore"
    r'\bjedoch\b',               # German "however"
    r'\bzusätzlich\b',           # German "additionally"
    r'\bbesonders\b',            # German "especially"
    r'\bregelmäßig\b',           # German "regularly"
    r'\binsbesondere\b',         # German "particularly"
    r'\bbeispielsweise\b',       # German "for example"
    r'\bschließlich\b',          # German "finally"
]

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

for page_name, de_file, en_file in pages:
    print(f'\n{"="*60}')
    print(f'PAGE {page_name}')
    print(f'{"="*60}')
    try:
        en_raw = get_raw(en_file)
        en_texts = extract_text(en_file)
        
        issues = []
        for pattern in german_patterns:
            matches = re.findall(pattern, en_raw)
            if matches:
                issues.append((pattern, matches[:3]))
        
        # Also check for specific German words in text nodes
        german_text_nodes = []
        specific_german = ['Sehr geehrte', 'Herren,', 'Damen und', 'vielen Dank', 
                          'freue mich', 'bin ich', 'habe ich', 'mit freundlichen',
                          'Hochachtungsvoll', 'Liebe Damen', 'Grüße', 'Schreiben',
                          'möchte ich', 'Wir freuen', 'Unternehmen hat']
        for t in en_texts:
            if any(g in t for g in specific_german):
                german_text_nodes.append(t)
        
        if not issues and not german_text_nodes:
            print('  No issues found')
        else:
            if german_text_nodes:
                print(f'  GERMAN TEXT NODES ({len(german_text_nodes)}):')
                for t in german_text_nodes[:10]:
                    print(f'    {repr(t[:120])}')
    except FileNotFoundError:
        print(f'  EN file not found: {en_file}')
