const fs = require('fs');

let p578 = fs.readFileSync('page57822475.html', 'utf8');

// 1. Fix the HTML wrappers
// Currently it might be: <div class="t-container t-align_left">\s*<a href="#popup:Antwort" class="wmc-antwort-btn">Antwort</a>\s*</div>
// Or it might be wrapped in t-col_12 already. Let's reset it safely.

// First remove any existing t-col_12 wrappers around wmc-antwort-btn so we don't double wrap
p578 = p578.replace(/<div class="t-container t-align_left">\s*<div class="t-col t-col_12">\s*<a href="#popup:Antwort" class="wmc-antwort-btn">Antwort<\/a>\s*<\/div>\s*<\/div>/g, '<div class="t-container t-align_left">\n        <a href="#popup:Antwort" class="wmc-antwort-btn">Antwort</a>\n      </div>');

// Now wrap it correctly
p578 = p578.replace(/<div class="t-container t-align_left">\s*<a href="#popup:Antwort" class="wmc-antwort-btn">Antwort<\/a>\s*<\/div>/g, 
`<div class="t-container t-align_left">
        <div class="t-col t-col_12">
          <a href="#popup:Antwort" class="wmc-antwort-btn">Antwort</a>
        </div>
      </div>`);

// 2. Fix the CSS. We'll find the wmc-antwort-btn css block and completely rewrite it.
const blocks = ['822437204', '1050675716', '822437573'];

blocks.forEach(id => {
  // Regex to match the entire CSS block for #recID .wmc-antwort-btn
  let cssRegex = new RegExp(`(#rec${id} \\.wmc-antwort-btn \\{[\\s\\S]*?\\})`, 'g');
  
  p578 = p578.replace(cssRegex, (match) => {
    // We only want to replace the base style, NOT the :hover block (which is a separate block)
    if (match.includes(':hover')) return match; 
    
    return `#rec${id} .wmc-antwort-btn {
          display: block !important;
          box-sizing: border-box;
          width: 260px !important;
          max-width: 100%;
          height: 60px !important;
          line-height: 60px !important;
          text-align: center;
          color: #ffffff;
          font-size: 18px !important;
          font-family: 'TildaSans', Arial, sans-serif;
          font-weight: 600;
          background-color: #f40e0e;
          text-decoration: none;
          margin: 0 !important;
          transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
        }`;
  });
});

fs.writeFileSync('page57822475.html', p578, 'utf8');
console.log('Fixed page57822475.html Antwort button alignment and size');
