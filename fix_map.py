import sys
import re

def fix_map_coordinates(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    changes = 0
    
    # Fix map center coordinates from Moscow (55.751979, 37.617499) to Eschborn (50.1356347, 8.5688471)
    if 'data-map-x="55.751979" data-map-y="37.617499"' in text:
        text = text.replace(
            'data-map-x="55.751979" data-map-y="37.617499"',
            'data-map-x="50.1356347" data-map-y="8.5688471"'
        )
        changes += 1
        print(f"  Fixed map center coordinates (Moscow -> Eschborn)")
    
    # Also check for any other wrong coordinates
    if 'data-map-x="55.75' in text:
        print(f"  WARNING: Still has Moscow-like coordinates")
    
    if changes > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"  Saved with {changes} changes")
    else:
        # Check if map already has correct coords
        if 'data-map-x="50.1356' in text:
            print(f"  Already has correct Eschborn coordinates")
        elif 'separateMap' in text:
            # Find what coords it has
            match = re.search(r'data-map-x="([^"]+)" data-map-y="([^"]+)"', text)
            if match:
                print(f"  Has coordinates: x={match.group(1)}, y={match.group(2)}")
            else:
                print(f"  No map coordinates found")
        else:
            print(f"  No map section found")

if __name__ == '__main__':
    pages = sys.argv[1:]
    for page in pages:
        print(f"\nProcessing: {page}")
        fix_map_coordinates(page)
