const fs = require('fs');
const html = fs.readFileSync('page59160115.html', 'utf8');
const count = (html.match(/popup:Antwort-en/g) || []).length;
console.log(`page59160115.html has ${count} references to popup:Antwort-en`);
