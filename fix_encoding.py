import sys
import re

def fix_encoding(filepath):
    """Fix broken Unicode replacement characters (U+FFFD) in HTML files."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    original = text
    rc = '\ufffd'  # Unicode replacement character
    
    if rc not in text:
        print(f"  No broken characters found")
        return 0
    
    count_before = text.count(rc)
    
    # Fix specific known patterns:
    
    # Copyright symbol
    text = text.replace(f'Copyright {rc} 2026', 'Copyright © 2026')
    text = text.replace(f'Copyright {rc} 2024', 'Copyright © 2024')
    
    # Degree symbol (360°)
    text = text.replace(f'360{rc}', '360°')
    
    # Registered trademark (ISTQB®)
    text = text.replace(f'ISTQB{rc}', 'ISTQB®')
    
    # German umlauts
    text = text.replace(f'f{rc}r Arbeit', 'für Arbeit')
    text = text.replace(f'Baden-W{rc}rttemberg', 'Baden-Württemberg')
    text = text.replace(f'Telef{rc}nica', 'Telefónica')
    
    # Résumé
    text = text.replace(f'R{rc}sum{rc}', 'Résumé')
    text = text.replace(f'R{rc}sum', 'Résum')
    
    # Nurzhan name (the u was corrupted)
    text = text.replace(f'N{rc}rzhan', 'Nurzhan')
    
    # Em dash / en dash  (Laaj – a)
    text = text.replace(f'Laaj {rc} a', 'Laaj – a')
    text = text.replace(f'Laaj {rc} ein', 'Laaj – ein')
    
    # Apostrophe / special quotes in "years' experience" etc
    text = text.replace(f'years{rc}', "years'")
    text = text.replace(f'Jahre{rc}', "Jahre'")
    
    # Button text - "Send request" with trailing broken char (→ arrow or similar)
    text = text.replace(f'Send request{rc}', 'Send request')
    text = text.replace(f'Anfrage senden{rc}', 'Anfrage senden')
    
    # Bullet points (red diamond ◆ used as list bullets)
    # The pattern is: rgb(244, 14, 14);">�  - this is a decorative bullet
    # These should be the diamond character ◆
    text = text.replace(f'14, 14);">{rc}', '14, 14);">◆')
    
    # Any remaining with common patterns
    text = text.replace(f'f{rc}r', 'für')
    text = text.replace(f'{rc}ber', 'über')  
    text = text.replace(f'f{rc}r', 'für')
    text = text.replace(f'Gef{rc}hl', 'Gefühl')
    text = text.replace(f'{rc}bung', 'übung')
    
    count_after = text.count(rc)
    fixed = count_before - count_after
    
    if fixed > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"  Fixed {fixed}/{count_before} broken characters ({count_after} remaining)")
    else:
        print(f"  No patterns matched ({count_before} broken chars remain)")
    
    return fixed

if __name__ == '__main__':
    pages = sys.argv[1:]
    for page in pages:
        print(f"\nProcessing: {page}")
        fix_encoding(page)
