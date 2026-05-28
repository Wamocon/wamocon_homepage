import re

# Compare footer sections between EN homepage and trainee page
with open('page59102217.html', 'r', encoding='utf-8') as f:
    en_home = f.read()

with open('page70444849.html', 'r', encoding='utf-8') as f:
    trainee = f.read()

# Find the contacts/footer section in EN homepage
# The section should have rec832623391 (based on element IDs seen earlier like tn-elem__8326233911726050687890)
en_sec_start = en_home.find('id="rec832623391"')
en_sec_end = en_home.find('<!-- /T396 -->', en_sec_start)
en_footer = en_home[en_sec_start:en_sec_end]

# Extract text elements from EN footer
en_texts = re.findall(r"tn-atom[^>]*>([^<]{2,50})<", en_footer)
print("EN Homepage footer labels:")
for t in en_texts:
    if t.strip():
        print(f"  {t.strip()}")

# Now find the equivalent section in trainee page
# Find the section that contains 'Telefon:'
trainee_telefon_idx = trainee.find('Telefon:')
trainee_sec_start = trainee.rfind('id="rec', 0, trainee_telefon_idx)
sec_id_match = re.search(r'id="(rec\d+)"', trainee[trainee_sec_start:trainee_sec_start+30])
trainee_sec_id = sec_id_match.group(1) if sec_id_match else 'unknown'
print(f"\nTrainee footer section: {trainee_sec_id}")

trainee_sec_end = trainee.find('<!-- /T396 -->', trainee_sec_start)
trainee_footer = trainee[trainee_sec_start:trainee_sec_end]

# Extract text elements from trainee footer
trainee_texts = re.findall(r"tn-atom[^>]*>([^<]{2,50})<", trainee_footer)
print("\nTrainee-FIAE footer labels:")
for t in trainee_texts:
    if t.strip():
        print(f"  {t.strip()}")

# Compare the section IDs to see if they're different
print(f"\nEN Homepage footer section ID: rec832623391")
print(f"Trainee footer section ID: {trainee_sec_id}")
