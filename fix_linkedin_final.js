const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

for (const file of files) {
  let html = fs.readFileSync(file, 'utf8');
  let changed = false;

  // Let's find the exact Youtube icon that is next to LinkedIn (left=162)
  const blockRegex = /<div class='t396__elem tn-elem[^>]*data-field-left-value="162"[^>]*data-field-top-value="([0-9]+)"[\s\S]*?youtube\.com[\s\S]*?<div class='t396__elem tn-elem/g;
  
  let match = blockRegex.exec(html);
  if (match) {
    const correctTop = match[1];
    
    // Find the correct top-res-320 from the same Youtube block
    const res320Match = html.substring(match.index, match.index + 500).match(/data-field-top-res-320-value="([0-9]+)"/);
    const correctRes320 = res320Match ? res320Match[1] : null;

    // Now fix LinkedIn icon (left=242)
    const liRegex = /(<div class='t396__elem tn-elem[^>]*data-elem-type='image'[^>]*data-field-top-value=")([0-9]+)("[^>]*data-field-left-value="242"[\s\S]*?href="https:\/\/de\.linkedin\.com\/company\/wamocon-gmbh")/g;
    
    html = html.replace(liRegex, (m, p1, p2, p3) => {
      if (p2 !== correctTop) {
        changed = true;
        console.log(`Fixing ${file}: top from ${p2} to ${correctTop}`);
        return p1 + correctTop + p3;
      }
      return m;
    });

    if (correctRes320) {
      const liResRegex = /(<div class='t396__elem tn-elem[^>]*data-elem-type='image'[^>]*>[\s\S]*?data-field-top-res-320-value=")([0-9]+)("[\s\S]*?data-field-left-res-320-value="212"[\s\S]*?href="https:\/\/de\.linkedin\.com\/company\/wamocon-gmbh")/g;
      html = html.replace(liResRegex, (m, p1, p2, p3) => {
        if (p2 !== correctRes320) {
          changed = true;
          console.log(`Fixing ${file}: res320 from ${p2} to ${correctRes320}`);
          return p1 + correctRes320 + p3;
        }
        return m;
      });
    }
  }

  if (changed) {
    fs.writeFileSync(file, html, 'utf8');
  }
}
