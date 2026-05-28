import sys

def fix_encoding_v2(filepath):
    """Fix all broken Unicode replacement characters using context-based replacement."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    rc = '\ufffd'
    
    if rc not in text:
        print(f"  No broken characters found")
        return 0
    
    count_before = text.count(rc)
    
    # === Specific known replacements ===
    
    # Copyright
    text = text.replace(f'Copyright {rc} 2026', 'Copyright © 2026')
    text = text.replace(f'Copyright {rc} 2024', 'Copyright © 2024')
    
    # Degree (360°)
    text = text.replace(f'360{rc}', '360°')
    
    # Registered trademark
    text = text.replace(f'ISTQB{rc}', 'ISTQB®')
    
    # Résumé
    text = text.replace(f'R{rc}sum{rc}', 'Résumé')
    
    # Nurzhan
    text = text.replace(f'N{rc}rzhan', 'Nurzhan')
    
    # Laaj dash
    text = text.replace(f'Laaj {rc} a', 'Laaj – a')
    text = text.replace(f'Laaj {rc} ein', 'Laaj – ein')
    
    # Years apostrophe
    text = text.replace(f'years{rc}', "years'")
    
    # Send request arrow
    text = text.replace(f'Send request{rc}', 'Send request')
    text = text.replace(f'Anfrage senden{rc}', 'Anfrage senden')
    
    # Bullets (◆)
    text = text.replace(f'14, 14);">{rc}', '14, 14);">◆')
    
    # Company names
    text = text.replace(f'Telef{rc}nica', 'Telefónica')
    text = text.replace(f'Baden-W{rc}rttemberg', 'Baden-Württemberg')
    
    # === German umlaut patterns (ü, ä, ö, ß) ===
    # These are systematic - the character before/after helps identify
    
    # ü patterns
    umlaut_u_patterns = [
        ('verf' + rc + 'gbar', 'verfügbar'),
        ('Ger' + rc + 'te', 'Geräte'),  # Actually ä
        ('G' + rc + 'ste', 'Gäste'),  # Actually ä
        ('Pr' + rc + 'fung', 'Prüfung'),
        ('Vertr' + rc + 'ge', 'Verträge'),  # ä
        ('f' + rc + 'nf', 'fünf'),
        ('pr' + rc + 'fung', 'prüfung'),
        ('Qualit' + rc + 'ts', 'Qualitäts'),  # ä
        ('gest' + rc + 'tzt', 'gestützt'),
        ('F' + rc + 'higkeit', 'Fähigkeit'),  # ä
        ('Lebensl' + rc + 'uf', 'Lebensläuf'),  # ä
        ('T' + rc + 'glich', 'Tägliche'),  # ä - but in context it's "Täglic"
        ('aktivit' + rc + 'ten', 'aktivitäten'),  # ä
        ('pers' + rc + 'nlich', 'persönlich'),  # ö
        ('zuverl' + rc + 'ssig', 'zuverlässig'),  # ä
        ('S' + rc + 'ulen', 'Säulen'),  # ä
        ('Pl' + rc + 'tz', 'Plätz'),  # ä
        ('n' + rc + 'her', 'näher'),  # ä
        ('rpr' + rc + 'fung', 'rprüfung'),
        ('Vertr' + rc + 'gen', 'Verträgen'),  # ä
        ('K' + rc + 'ndig', 'Kündig'),
        ('fl' + rc + 'chen', 'flächen'),  # ä
        ('tra' + rc + 'en', 'traßen'),  # ß
        ('B' + rc + 'ro', 'Büro'),
        ('f' + rc + 'r ', 'für '),
        ('F' + rc + 'r ', 'Für '),
        ('f' + rc + 'r Arbeit', 'für Arbeit'),
        (' ' + rc + 'ber', ' über'),
        # Address dash
        ('79 ' + rc + ' 81', '79 – 81'),
        ('ly ' + rc + ' cli', 'ly – cli'),
        # Bullet replacement
        ('> ' + rc + ' vis', '> – vis'),
        # Phone number  
        ('904' + rc + '5952', '904-5952'),  # might be an en-dash
    ]
    
    for old, new in umlaut_u_patterns:
        if old in text:
            text = text.replace(old, new)
    
    # Generic remaining: try common German patterns
    # ä (most common broken char in German)
    remaining_patterns = [
        ('st' + rc + 'nd', 'ständ'),
        ('m' + rc + 'ß', 'mäß'),
        ('l' + rc + 'ss', 'läss'),
        ('sch' + rc + 'ft', 'schaft'),  # not umlaut, skip
        ('t' + rc + 't', 'tät'),
        ('s' + rc + 'tz', 'sätz'),
        ('d' + rc + 'rf', 'dürf'),
        ('m' + rc + 'ss', 'müss'),
        ('k' + rc + 'nn', 'könn'),
        ('w' + rc + 'rd', 'würd'),
        ('h' + rc + 'lt', 'hält'),
        ('l' + rc + 'ng', 'läng'),
        ('st' + rc + 'rk', 'stärk'),
        ('l' + rc + 'uf', 'läuf'),
        ('gr' + rc + 'ß', 'größ'),
        ('Geb' + rc + 'ud', 'Gebäud'),
        ('G' + rc + 'ltig', 'Gültig'),
        ('Zug' + rc + 'ng', 'Zugäng'),
        ('R' + rc + 'ck', 'Rück'),
        ('r' + rc + 'ck', 'rück'),
    ]
    
    for old, new in remaining_patterns:
        if old in text:
            text = text.replace(old, new)
    
    count_after = text.count(rc)
    fixed = count_before - count_after
    
    if fixed > 0 or count_after == 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"  Fixed {fixed}/{count_before} broken characters ({count_after} remaining)")
    else:
        print(f"  No patterns matched ({count_before} broken chars remain)")
    
    # Show remaining if any
    if count_after > 0:
        idx = 0
        shown = 0
        while shown < 10:
            i = text.find(rc, idx)
            if i < 0:
                break
            ctx = text[max(0,i-10):min(len(text),i+15)]
            print(f"    Remaining: [{ctx}]")
            idx = i + 1
            shown += 1
    
    return fixed

if __name__ == '__main__':
    pages = sys.argv[1:]
    for page in pages:
        print(f"\nProcessing: {page}")
        fix_encoding_v2(page)
