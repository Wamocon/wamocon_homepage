const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

for (const file of files) {
  let html = fs.readFileSync(file, 'utf8');
  let changed = false;

  // Find facebook top value
  const fbRegex = /<div class='t396__elem tn-elem[^>]*data-elem-type='image'[^>]*data-field-top-value="([0-9]+)"[^>]*>[\s\S]*?<a class='tn-atom'[^>]*href="[^"]*facebook\.com/;
  const fbMatch = html.match(fbRegex);

  if (fbMatch) {
    const correctTop = fbMatch[1];
    
    // Find linkedin icon block
    const liBlockRegex = /(<div class='t396__elem tn-elem[^>]*data-elem-type='image'[^>]*data-field-top-value=")([0-9]+)("[^>]*data-field-left-value="242"[\s\S]*?href="https:\/\/de\.linkedin\.com\/company\/wamocon-gmbh")/g;
    
    html = html.replace(liBlockRegex, (match, p1, p2, p3) => {
      if (p2 !== correctTop) {
        changed = true;
        console.log(`Fixing ${file}: changing top from ${p2} to ${correctTop}`);
        return p1 + correctTop + p3;
      }
      return match;
    });

    // Also let's fix the responsive ones based on Facebook's values
    // Find Facebook's top-res values
    const fbRes320Match = html.match(/<div class='t396__elem tn-elem[^>]*data-elem-type='image'[^>]*>[\s\S]*?data-field-top-res-320-value="([0-9]+)"[\s\S]*?<a class='tn-atom'[^>]*href="[^"]*facebook\.com/);
    if (fbRes320Match) {
      const correctRes320 = fbRes320Match[1];
      const liResRegex = /(<div class='t396__elem tn-elem[^>]*data-elem-type='image'[^>]*>[\s\S]*?data-field-top-res-320-value=")([0-9]+)("[\s\S]*?data-field-left-res-320-value="212"[\s\S]*?href="https:\/\/de\.linkedin\.com\/company\/wamocon-gmbh")/g;
      
      html = html.replace(liResRegex, (match, p1, p2, p3) => {
        if (p2 !== correctRes320) {
          changed = true;
          console.log(`Fixing ${file} res320: changing from ${p2} to ${correctRes320}`);
          return p1 + correctRes320 + p3;
        }
        return match;
      });
    }
  }

  if (changed) {
    fs.writeFileSync(file, html, 'utf8');
  }
}
