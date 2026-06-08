const fs = require('fs');

function fixPage(filename) {
  if (!fs.existsSync(filename)) return;
  let html = fs.readFileSync(filename, 'utf8');

  // Replace the wmc-antwort-btn we added earlier if it exists
  html = html.replace(/<div class="t-container t-align_left">\s*<div class="t-col t-col_12">\s*<a href="#popup:Antwort" class="wmc-antwort-btn">Antwort<\/a>\s*<\/div>\s*<\/div>/g, '');
  html = html.replace(/<div class="t-container t-align_left">\s*<a href="#popup:Antwort" class="wmc-antwort-btn">Antwort<\/a>\s*<\/div>/g, '');

  // Regex specifically targeting the CSS blocks for the element 1730977252774
  // We match the selector, and then match the block body `{ ... }`
  const regex = /(\.tn-elem\[data-elem-id="1730977252774"\]\s*\{)([\s\S]*?)(\})/g;

  html = html.replace(regex, (match, prefix, body, suffix) => {
    // Modify width, height, and left INSIDE the block
    let newBody = body;
    newBody = newBody.replace(/width:\s*200px;/, 'width: 260px !important;');
    newBody = newBody.replace(/height:\s*55px;/, 'height: 60px !important;');
    newBody = newBody.replace(/left:\s*calc\((50%\s*-\s*\d+px)[\s+0-9px]*\);/g, 'left: calc($1) !important;');
    
    // Also handle line-height and font-size for tn-atom, but that's a different block.
    return prefix + newBody + suffix;
  });

  // Also specifically fix the .tn-atom line-height block
  const atomRegex = /(\.tn-elem\[data-elem-id="1730977252774"\]\s*\.tn-atom\s*\{)([\s\S]*?)(\})/g;
  html = html.replace(atomRegex, (match, prefix, body, suffix) => {
    let newBody = body;
    // We add line-height so the text is vertically centered
    newBody = newBody.replace(/font-size:\s*14px;/, 'font-size: 18px !important;\n          line-height: 60px !important;');
    newBody = newBody.replace(/font-size:\s*16px;/, 'font-size: 18px !important;\n          line-height: 60px !important;');
    return prefix + newBody + suffix;
  });

  // Fix HTML data attributes for Tilda JS initialization (mainly in page59160115.html)
  html = html.replace(/(data-elem-id=['"]1730977252774['"][\s\S]*?)data-field-width-value=['"]200['"]/g, '$1data-field-width-value="260"');
  html = html.replace(/(data-elem-id=['"]1730977252774['"][\s\S]*?)data-field-height-value=['"]55['"]/g, '$1data-field-height-value="60"');
  html = html.replace(/(data-elem-id=['"]1730977252774['"][\s\S]*?)data-field-left-value=['"]\d+['"]/g, '$1data-field-left-value="0"');
  
  // Also fix responsive left values in HTML
  html = html.replace(/(data-elem-id=['"]1730977252774['"][\s\S]*?)data-field-left-res-320-value=['"]\d+['"]/g, '$1data-field-left-res-320-value="0"');
  html = html.replace(/(data-elem-id=['"]1730977252774['"][\s\S]*?)data-field-left-res-480-value=['"]\d+['"]/g, '$1data-field-left-res-480-value="0"');
  html = html.replace(/(data-elem-id=['"]1730977252774['"][\s\S]*?)data-field-left-res-640-value=['"]\d+['"]/g, '$1data-field-left-res-640-value="0"');
  html = html.replace(/(data-elem-id=['"]1730977252774['"][\s\S]*?)data-field-left-res-960-value=['"]\d+['"]/g, '$1data-field-left-res-960-value="0"');

  fs.writeFileSync(filename, html, 'utf8');
  console.log('Fixed ' + filename);
}

fixPage('page57822475.html');
fixPage('page59160115.html');
fixPage('page59102217.html'); // Just in case
