const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

for (const file of files) {
  let html = fs.readFileSync(file, 'utf8');
  let changed = false;

  // Find the Facebook icon specifically in the footer which has left-value="202"
  // It has href pointing to facebook
  const fbFooterRegex = /<div class='t396__elem tn-elem[^>]*data-elem-type='image'[^>]*data-field-top-value="([0-9]+)"[^>]*data-field-left-value="202"[\s\S]*?href="[^"]*facebook\.com/g;
  
  let fbMatch;
  while ((fbMatch = fbFooterRegex.exec(html)) !== null) {
    const correctTop = fbMatch[1];
    
    // Get the res-320 top value for Facebook
    const fbResMatch = html.substring(fbMatch.index, fbMatch.index + 500).match(/data-field-top-res-320-value="([0-9]+)"/);
    const correctRes320 = fbResMatch ? fbResMatch[1] : null;

    // Now fix the LinkedIn icon which has left-value="242"
    const liRegex = /(<div class='t396__elem tn-elem[^>]*data-elem-type='image'[^>]*data-field-top-value=")[0-9]+("[^>]*data-field-left-value="242"[\s\S]*?href="https:\/\/de\.linkedin\.com\/company\/wamocon-gmbh")/g;
    
    html = html.replace(liRegex, (m, p1, p2) => {
      changed = true;
      console.log(`Fixed ${file}: top to ${correctTop}`);
      return p1 + correctTop + p2;
    });

    if (correctRes320) {
      const liResRegex = /(<div class='t396__elem tn-elem[^>]*data-elem-type='image'[^>]*>[\s\S]*?data-field-top-res-320-value=")[0-9]+("[\s\S]*?data-field-left-res-320-value="212"[\s\S]*?href="https:\/\/de\.linkedin\.com\/company\/wamocon-gmbh")/g;
      html = html.replace(liResRegex, (m, p1, p2) => {
        changed = true;
        console.log(`Fixed ${file}: res320 to ${correctRes320}`);
        return p1 + correctRes320 + p2;
      });
    }
  }

  if (changed) {
    fs.writeFileSync(file, html, 'utf8');
  }
}
