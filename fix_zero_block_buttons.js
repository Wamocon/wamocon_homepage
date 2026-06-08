const fs = require('fs');

function fixPage(filename) {
  if (!fs.existsSync(filename)) return;
  let html = fs.readFileSync(filename, 'utf8');
  
  // Replace the wmc-antwort-btn we added earlier if it exists, to clean up our previous attempt
  html = html.replace(/<div class="t-container t-align_left">\s*<div class="t-col t-col_12">\s*<a href="#popup:Antwort" class="wmc-antwort-btn">Antwort<\/a>\s*<\/div>\s*<\/div>/g, '');
  html = html.replace(/<div class="t-container t-align_left">\s*<a href="#popup:Antwort" class="wmc-antwort-btn">Antwort<\/a>\s*<\/div>/g, '');
  
  // Find all CSS blocks for the 1730977252774 element
  // We need to target width, height, and left properties
  
  html = html.replace(/(\.tn-elem\[data-elem-id="1730977252774"\]\s*\{[\s\S]*?)width:\s*200px;/g, '$1width: 260px !important;');
  html = html.replace(/(\.tn-elem\[data-elem-id="1730977252774"\]\s*\{[\s\S]*?)height:\s*55px;/g, '$1height: 60px !important;');
  
  // Fix the line-height for tn-atom inside the button if needed
  html = html.replace(/(\.tn-elem\[data-elem-id="1730977252774"\]\s*\.tn-atom\s*\{[\s\S]*?font-size:\s*16px;)/g, '$1\n          line-height: 60px !important;');
  
  // Replace all the 'left: calc(... + XXpx)' with 'left: calc(...) !important'
  html = html.replace(/(left:\s*calc\(50%\s*-\s*\d+px)\s*\+\s*\d+px\)/g, '$1) !important');
  // Replace any existing left: calc(...) without !important
  html = html.replace(/(left:\s*calc\(50%\s*-\s*\d+px\));/g, '$1 !important;');
  
  // Fix HTML data attributes for Tilda JS initialization (mainly in page59160115.html)
  html = html.replace(/(data-elem-id=['"]1730977252774['"][\s\S]*?)data-field-width-value=['"]200['"]/g, '$1data-field-width-value="260"');
  html = html.replace(/(data-elem-id=['"]1730977252774['"][\s\S]*?)data-field-height-value=['"]55['"]/g, '$1data-field-height-value="60"');
  html = html.replace(/(data-elem-id=['"]1730977252774['"][\s\S]*?)data-field-left-value=['"]20['"]/g, '$1data-field-left-value="0"');
  
  // Also fix responsive left values in HTML
  html = html.replace(/(data-elem-id=['"]1730977252774['"][\s\S]*?)data-field-left-res-320-value=['"]20['"]/g, '$1data-field-left-res-320-value="0"');
  html = html.replace(/(data-elem-id=['"]1730977252774['"][\s\S]*?)data-field-left-res-480-value=['"]20['"]/g, '$1data-field-left-res-480-value="0"');
  html = html.replace(/(data-elem-id=['"]1730977252774['"][\s\S]*?)data-field-left-res-640-value=['"]10['"]/g, '$1data-field-left-res-640-value="0"');
  html = html.replace(/(data-elem-id=['"]1730977252774['"][\s\S]*?)data-field-left-res-960-value=['"]10['"]/g, '$1data-field-left-res-960-value="0"');

  fs.writeFileSync(filename, html, 'utf8');
  console.log('Fixed ' + filename);
}

fixPage('page57822475.html');
fixPage('page59160115.html');
fixPage('page59102217.html'); // Just in case
