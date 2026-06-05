const fs = require('fs');

function updateGermanPage(file) {
  let html = fs.readFileSync(file, 'utf8');

  // Change wmc-antwort-btn styles
  html = html.replace(/width: 160px;/g, 'width: 200px;');
  html = html.replace(/height: 48px;/g, 'height: 55px;');
  html = html.replace(/line-height: 48px;/g, 'line-height: 55px;');
  html = html.replace(/font-size: 14px;/g, 'font-size: 16px;');

  // Change padding for the three records
  const records = ['822437204', '1050675716', '822437573'];
  for (const rec of records) {
    const regex = new RegExp(`(<div id="rec${rec}" class="r t-rec[^\"]*t-rec_pb_)0("(?=[\\s\\S]*?padding-bottom:)0px;)`, 'g');
    html = html.replace(regex, `$145$245px;`);
  }

  fs.writeFileSync(file, html, 'utf8');
  console.log(`Updated ${file}`);
}

function updateEnglishPage(file) {
  let html = fs.readFileSync(file, 'utf8');

  // Change padding for the two records
  const records = ['833141512', '833141515'];
  for (const rec of records) {
    const regex = new RegExp(`(<div id="rec${rec}" class="r t-rec[^\"]*t-rec_pb_)0("(?=[\\s\\S]*?padding-bottom:)0px;)`, 'g');
    html = html.replace(regex, `$145$245px;`);
  }
  
  // The english button already has 200 width and 55 height.

  fs.writeFileSync(file, html, 'utf8');
  console.log(`Updated ${file}`);
}

updateGermanPage('page57822475.html');
updateEnglishPage('page59160115.html');
