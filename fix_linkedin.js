const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

for (const file of files) {
  let html = fs.readFileSync(file, 'utf8');
  let changed = false;

  if (html.includes('data-field-top-value="403" data-field-left-value="242"')) {
    html = html.replace(/data-field-top-value="403" data-field-left-value="242"/g, 'data-field-top-value="370" data-field-left-value="242"');
    changed = true;
  }
  
  // also check top-res-320-value for the same icon
  // Facebook has: data-field-top-res-320-value="348" data-field-left-res-320-value="182"
  // LinkedIn currently has: data-field-top-res-320-value="343" data-field-left-res-320-value="212"
  if (html.includes('data-field-top-res-320-value="343"\n            data-field-left-res-320-value="212"')) {
    html = html.replace(/data-field-top-res-320-value="343"\n            data-field-left-res-320-value="212"/g, 'data-field-top-res-320-value="348"\n            data-field-left-res-320-value="212"');
    changed = true;
  }
  // Let's also do a more generic replace for 343 and 212 if the newlines are different
  else if (html.includes('data-field-top-res-320-value="343"') && html.includes('data-field-left-res-320-value="212"')) {
    html = html.replace(/data-field-top-res-320-value="343"(\s*?)data-field-left-res-320-value="212"/g, 'data-field-top-res-320-value="348"$1data-field-left-res-320-value="212"');
    changed = true;
  }

  if (changed) {
    fs.writeFileSync(file, html, 'utf8');
    console.log(`Fixed LinkedIn in ${file}`);
  }
}
