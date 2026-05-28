"""Fix the HTML data attribute for the AI box height."""
with open('page59102217.html', 'r', encoding='utf-8') as f:
    text = f.read()

old = """data-elem-id='1724080449067' data-elem-type='shape' data-field-top-value="418" data-field-left-value="819" data-field-height-value="237" """
new = """data-elem-id='1724080449067' data-elem-type='shape' data-field-top-value="418" data-field-left-value="819" data-field-height-value="330" """

count = text.count(old)
print(f"Found HTML attr: {count}")
if count >= 1:
    text = text.replace(old, new)
    with open('page59102217.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed HTML data-field-height-value 237->330")
else:
    # Try to find a shorter match
    idx = text.find("data-elem-id='1724080449067'")
    if idx >= 0:
        snippet = text[idx:idx+300]
        print(f"Element found at {idx}: {snippet[:200]}")
