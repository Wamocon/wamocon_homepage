const fs = require('fs');

function updateGermanPage(file) {
  let html = fs.readFileSync(file, 'utf8');

  const records = ['822437204', '1050675716', '822437573'];
  for (const rec of records) {
    const divStart = html.indexOf(`<div id="rec${rec}"`);
    if (divStart !== -1) {
      const divEnd = html.indexOf('>', divStart);
      let divString = html.substring(divStart, divEnd + 1);
      divString = divString.replace('t-rec_pb_0', 't-rec_pb_45');
      divString = divString.replace('padding-bottom:0px;', 'padding-bottom:45px;');
      html = html.substring(0, divStart) + divString + html.substring(divEnd + 1);
    }
  }

  fs.writeFileSync(file, html, 'utf8');
  console.log(`Updated padding in ${file}`);
}

function updateEnglishPage(file) {
  let html = fs.readFileSync(file, 'utf8');

  const records = ['833141512', '833141515'];
  for (const rec of records) {
    const divStart = html.indexOf(`<div id="rec${rec}"`);
    if (divStart !== -1) {
      const divEnd = html.indexOf('>', divStart);
      let divString = html.substring(divStart, divEnd + 1);
      divString = divString.replace('t-rec_pb_0', 't-rec_pb_45');
      divString = divString.replace('padding-bottom:0px;', 'padding-bottom:45px;');
      html = html.substring(0, divStart) + divString + html.substring(divEnd + 1);
    }
  }

  fs.writeFileSync(file, html, 'utf8');
  console.log(`Updated padding in ${file}`);
}

updateGermanPage('page57822475.html');
updateEnglishPage('page59160115.html');
