const fs = require('fs');

// Fix 1: index.html logo alignment
let indexHtml = fs.readFileSync('index.html', 'utf8');
indexHtml = indexHtml.replace(
  /(<div class='t396__elem tn-elem tn-elem__7949872291734179185165' data-elem-id='1734179185165'[^>]*data-field-top-value=")340(")/,
  '$1325$2'
);
indexHtml = indexHtml.replace(
  /(data-elem-id='1734179185165'[^>]*data-field-top-res-960-value=")340(")/,
  '$1325$2'
);
fs.writeFileSync('index.html', indexHtml, 'utf8');
console.log('Fixed index.html logo alignment');

// Fix 2: page69503661.html email text size
let p69 = fs.readFileSync('page69503661.html', 'utf8');
p69 = p69.replace(
  /(#rec1051682921 \.tn-elem\[data-elem-id="1723632233996"\] \.tn-atom \{\s*vertical-align: middle;\s*color: #ffffff;\s*font-size:\s*)40px/g,
  '$1 26px'
);
p69 = p69.replace(
  /(@media screen and \(max-width:1199px\) \{\s*#rec1051682921 \.tn-elem\[data-elem-id="1723632233996"\] \.tn-atom \{\s*font-size:\s*)35px/g,
  '$1 24px'
);
p69 = p69.replace(
  /(@media screen and \(max-width:639px\) \{\s*#rec1051682921 \.tn-elem\[data-elem-id="1723632233996"\] \.tn-atom \{\s*font-size:\s*)30px/g,
  '$1 20px'
);
p69 = p69.replace(
  /(@media screen and \(max-width:479px\) \{\s*#rec1051682921 \.tn-elem\[data-elem-id="1723632233996"\] \.tn-atom \{\s*font-size:\s*)25px/g,
  '$1 18px'
);
fs.writeFileSync('page69503661.html', p69, 'utf8');
console.log('Fixed page69503661.html email text size');

// Fix 3: page57475469.html bullet points indentation
let p57 = fs.readFileSync('page57475469.html', 'utf8');
p57 = p57.replace(
  /<div class="t-card__descr t-descr t-descr_sm" field="li_descr__2514642172360">/g,
  '<div class="t-card__descr t-descr t-descr_sm" field="li_descr__2514642172360" style="padding-left: 15px; text-indent: -15px;">'
);
p57 = p57.replace(
  /<div class="t-card__descr t-descr t-descr_sm" field="li_descr__2514642172361">/g,
  '<div class="t-card__descr t-descr t-descr_sm" field="li_descr__2514642172361" style="padding-left: 15px; text-indent: -15px;">'
);
// Also let's fix any other bullet point lists if there are any others in that section
// Wait, replacing it exactly by field id is safe.
fs.writeFileSync('page57475469.html', p57, 'utf8');
console.log('Fixed page57475469.html bullet indentation');

// Fix 4: page57822475.html form scale
let p578 = fs.readFileSync('page57822475.html', 'utf8');

// Reduce main heading font size (1723632233996)
p578 = p578.replace(
  /(#rec822446072 \.tn-elem\[data-elem-id="1723632233996"\] \.tn-atom \{\s*color: #ffffff;\s*font-size:\s*)40px/g,
  '$1 30px'
);
// Reduce description text font size (1723632248635)
p578 = p578.replace(
  /(#rec822446072 \.tn-elem\[data-elem-id="1723632248635"\] \.tn-atom \{\s*color: #ffffff;\s*font-size:\s*)20px/g,
  '$1 16px'
);
// Reduce sub-heading font size (1730978083630)
p578 = p578.replace(
  /(#rec822446072 \.tn-elem\[data-elem-id="1730978083630"\] \.tn-atom \{\s*color: #ffffff;\s*font-size:\s*)24px/g,
  '$1 18px'
);

// Reduce form inputs
// height: 60 -> 40
p578 = p578.replace(
  /(data-elem-id='1723632233999'[^>]*data-field-inputheight-value=")60(")/g,
  '$140$2'
);
// font size: 18 -> 14
p578 = p578.replace(
  /(data-elem-id='1723632233999'[^>]*data-field-inputfontsize-value=")18(")/g,
  '$114$2'
);
// margin bottom: 20 -> 10
p578 = p578.replace(
  /(data-elem-id='1723632233999'[^>]*data-field-inputmargbottom-value=")20(")/g,
  '$110$2'
);
// button height: 60 -> 40
p578 = p578.replace(
  /(data-elem-id='1723632233999'[^>]*data-field-buttonheight-value=")60(")/g,
  '$140$2'
);
fs.writeFileSync('page57822475.html', p578, 'utf8');
console.log('Fixed page57822475.html form scale');

