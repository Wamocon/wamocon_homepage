import re

fname = 'page64750211.html'
live_recs_all = ['rec890170051','rec890558230','rec794987227','rec832094056','rec890519809','rec890177821','rec991191421','rec990143356','rec890250250','rec991152491','rec890831551','rec991194106','rec890535031','rec991149021','rec978471051','rec991196436','rec890534974','rec990992166','rec990693936','rec991196876','rec890540353','rec990989376','rec978471826','rec799819339','rec799819366','rec990313966','rec787997778','rec822549340','rec822554336','rec822556468','rec835481654','rec835481655','rec835481656']

with open(fname, encoding='utf-8') as f:
    c = f.read()
local_recs = re.findall('id="(rec[0-9]+)"', c)
print(f'Local DE recs ({len(local_recs)} total):')
print(local_recs)
print()
missing_from_de = [r for r in live_recs_all if r not in local_recs]
extra_in_de = [r for r in local_recs if r not in live_recs_all]
print('Missing from DE:', missing_from_de)
print('Extra in DE (not on live):', extra_in_de)
