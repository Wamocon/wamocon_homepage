const fs = require('fs');

let html = fs.readFileSync('page57822475.html', 'utf8');

html = html.replace(/max-width: 1400px;/g, 'max-width: 1800px;');
html = html.replace(/max-width: 350px;/g, 'max-width: 450px;');

fs.writeFileSync('page57822475.html', html, 'utf8');
console.log('Updated to 1800px and 450px max-width');
