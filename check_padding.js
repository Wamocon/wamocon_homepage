const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

for (const file of files) {
  const html = fs.readFileSync(file, 'utf8');
  if (html.includes('popup:Antwort')) {
    console.log(file, 'contains popup:Antwort');
    const records = html.split('<div id="rec');
    for (const rec of records) {
      if (rec.includes('popup:Antwort')) {
        const idMatch = /^(\d+)"/.exec(rec);
        const paddingMatch = /padding-bottom:(\d+px)/.exec(rec);
        console.log('  Rec ID:', idMatch ? idMatch[1] : '?', 'Padding bottom:', paddingMatch ? paddingMatch[1] : '?');
      }
    }
  }
}
