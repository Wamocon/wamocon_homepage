import re

live_sections = {
    '360-Booster': ('page57874143.html', ['rec822469985','rec822469986','rec822475269','rec819180409']),
    'Cooperation': ('page57876515.html', ['rec822490330','rec822547564','rec794987227','rec832094056','rec822547565','rec822490332','rec822510646','rec822490333','rec822511336','rec822512196','rec822513904','rec822515003','rec822518871','rec822526441','rec822524912','rec819180409','rec819195966','rec822490338','rec822490339','rec822549340','rec822554336','rec822556468','rec835481654','rec835481655','rec835481656']),
    'Contact': ('page57882423.html', ['rec822540420','rec822548034','rec794987227','rec832094056','rec822548035','rec822540928','rec832134134','rec819195966','rec822540429','rec822540430','rec822549340','rec822554336','rec822556468','rec835481654','rec835481655','rec835481656']),
    'Privacy': ('page59452125.html', ['rec835493614','rec835493615','rec822549340','rec822554336','rec822556468','rec835481654','rec835481655','rec835481656']),
    'Imprint': ('page61093859.html', ['rec848930418','rec848930419','rec822549340','rec822554336','rec822556468','rec835481654','rec835481655','rec835481656']),
    'Employee Reviews': ('page64750211.html', ['rec890170051','rec890558230','rec794987227','rec832094056','rec890519809','rec890177821','rec991191421','rec990143356','rec890250250','rec991152491','rec890831551','rec991194106','rec890535031','rec991149021','rec978471051','rec991196436','rec890534974','rec990992166','rec990693936','rec991196876','rec890540353','rec990989376','rec978471826','rec799819339','rec799819366','rec990313966','rec787997778','rec822549340','rec822554336','rec822556468','rec835481654','rec835481655','rec835481656']),
    'Azubi': ('page69503661.html', ['rec1051555956','rec1051870721','rec794987227','rec832094056','rec1051556756','rec1051557496','rec1051608911','rec1051638191','rec1052070381','rec1051696341','rec1051734546','rec1059934481','rec1051899696','rec1052066386','rec1051790271','rec1051803131','rec1052135436','rec1051682921','rec819180409','rec819195966','rec1052098211','rec822549340','rec822554336','rec822556468','rec835481654','rec835481655','rec835481656']),
}

for name, (fname, live_recs) in live_sections.items():
    with open(fname, encoding='utf-8') as f:
        c = f.read()
    local_recs = re.findall('id="(rec[0-9]+)"', c)
    missing = [r for r in live_recs if r not in local_recs]
    print(f'=== {name} === ({fname})')
    if missing:
        print(f'  MISSING FROM DE: {missing}')
    else:
        print(f'  ALL {len(live_recs)} live sections present in local DE')
    print()
