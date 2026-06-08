const fs = require('fs');

let p578 = fs.readFileSync('page57822475.html', 'utf8');

const blocks = ['822437204', '1050675716', '822437573'];

blocks.forEach(id => {
  // We want to replace display: inline-block; with display: block; margin: 0 auto 0 0;
  // Also ensure width and height and font-size are large enough.
  let regex = new RegExp(`(#rec${id} \\.wmc-antwort-btn \\{[\\s\\S]*?)(display: inline-block;)([\\s\\S]*?\\})`, 'g');
  
  p578 = p578.replace(regex, (match, p1, p2, p3) => {
    // Modify the block to ensure left alignment
    let newCSS = p3;
    newCSS = newCSS.replace(/width: 200px;/g, 'width: 260px;');
    newCSS = newCSS.replace(/height: 55px;/g, 'height: 60px;');
    newCSS = newCSS.replace(/line-height: 55px;/g, 'line-height: 60px;');
    newCSS = newCSS.replace(/font-size: 16px;/g, 'font-size: 18px;');
    
    // Replace inline-block with block + margin
    return p1 + 'display: block;\n          margin-left: 0;\n          margin-right: auto;' + newCSS;
  });
});

fs.writeFileSync('page57822475.html', p578, 'utf8');
console.log('Fixed page57822475.html Antwort button alignment');
