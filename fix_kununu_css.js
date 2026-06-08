const fs = require('fs');

function updateKununuCSS(file) {
  let html = fs.readFileSync(file, 'utf8');

  // Update knn-grid max-width
  html = html.replace(
    /max-width:\s*1200px;[\s\S]*?margin:\s*0 auto;[\s\S]*?padding:\s*0 24px;/g,
    'max-width: 1400px;\n          margin: 0 auto;\n          padding: 0 24px;'
  );

  // Update knn-card dimensions
  html = html.replace(
    /flex:\s*1 1 320px;[\s\S]*?max-width:\s*380px;[\s\S]*?min-width:\s*280px;/g,
    'flex: 1 1 260px;\n          max-width: 350px;\n          min-width: 240px;'
  );

  fs.writeFileSync(file, html, 'utf8');
  console.log(`Updated Kununu CSS in ${file} with Regex`);
}

updateKununuCSS('page57822475.html');
