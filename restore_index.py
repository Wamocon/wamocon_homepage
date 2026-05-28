"""restore_and_redo.py - Restore index.html to original state then re-apply correct translations"""
import re

base = r'c:\Users\Yash Bhesaniya\OneDrive - WAMOCON GmbH\Desktop\WMC\wamocon_homepage'

with open(base + r'\index.html', encoding='utf-8') as f:
    de = f.read()

print(f'Current index.html size: {len(de)}')
print(f'Has rec832623380: {"rec832623380" in de}')

# The script added blocks 380-389 BEFORE rec819175753
# We need to remove those added blocks
# Find the start of added content (rec832623380 block)
added_start = de.find('<div id="rec832623380"')
if added_start > 0:
    # Find where rec819175753 starts after the added blocks
    rec819_after = de.find('<div id="rec819175753"', added_start)
    print(f'Added blocks: chars {added_start} to {rec819_after}')
    # Remove the added blocks (keep everything before and from rec819175753 onwards)
    de_restored = de[:added_start] + de[rec819_after:]
    print(f'Restored size: {len(de_restored)}')
    with open(base + r'\index.html', 'w', encoding='utf-8') as f:
        f.write(de_restored)
    print('Restored index.html to original state')
else:
    print('No added blocks found - index.html is already in original state')
    de_restored = de
    print(f'Size: {len(de_restored)}')
