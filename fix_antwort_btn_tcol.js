const fs = require('fs');

let p578 = fs.readFileSync('page57822475.html', 'utf8');

// 1. Force the CSS to have !important
const blocks = ['822437204', '1050675716', '822437573'];

blocks.forEach(id => {
  // Regex to match the CSS block
  let cssRegex = new RegExp(`(#rec${id} \\.wmc-antwort-btn \\{[\\s\\S]*?margin-left: 0;)([\\s\\S]*?width: 260px;)([\\s\\S]*?height: 60px;)([\\s\\S]*?line-height: 60px;)([\\s\\S]*?\\})`, 'g');
  
  p578 = p578.replace(cssRegex, (match, p1, p2, p3, p4, p5) => {
    // Add !important
    let newCss = match.replace(/margin-left: 0;/g, 'margin-left: 0 !important;');
    newCss = newCss.replace(/margin-right: auto;/g, 'margin-right: auto !important;');
    newCss = newCss.replace(/width: 260px;/g, 'width: 260px !important;');
    newCss = newCss.replace(/height: 60px;/g, 'height: 60px !important;');
    newCss = newCss.replace(/line-height: 60px;/g, 'line-height: 60px !important;');
    newCss = newCss.replace(/display: block;/g, 'display: block !important;');
    return newCss;
  });

  // 2. Wrap the button in t-col t-col_12
  // Currently it is:
  // <div class="t-container t-align_left">
  //   <a href="#popup:Antwort" class="wmc-antwort-btn">Antwort</a>
  // </div>
  
  let htmlRegex = new RegExp(`(<div class="t-container t-align_left">\\s*<a href="#popup:Antwort" class="wmc-antwort-btn">Antwort</a>\\s*</div>)`, 'g');
  p578 = p578.replace(htmlRegex, (match) => {
    return `<div class="t-container t-align_left">
        <div class="t-col t-col_12">
          <a href="#popup:Antwort" class="wmc-antwort-btn">Antwort</a>
        </div>
      </div>`;
  });
});

fs.writeFileSync('page57822475.html', p578, 'utf8');
console.log('Fixed page57822475.html Antwort button alignment via t-col_12');
