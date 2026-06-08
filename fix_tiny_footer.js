const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

for (const file of files) {
  let html = fs.readFileSync(file, 'utf8');
  let changed = false;

  // We are looking for the tiny footer CSS:
  // font-size: 10px;
  // font-size: 12px;
  
  if (html.includes('#rec819195966 .t420__text') && html.includes('font-size: 10px;')) {
    
    // Replace tiny text styles with the correct ones from page64750211.html
    html = html.replace(/#rec819195966 \.t420__text\s*\{\s*font-size:\s*10px;\s*line-height:\s*1\.2;\s*color:\s*#ffffff;\s*font-weight:\s*300;\s*font-family:\s*'Poppins';\s*\}/g, 
                        `#rec819195966 .t420__text {
          font-size: 16px;
          line-height: 1.45;
          color: #ffffff;
          font-weight: 300;
          font-family: 'Poppins';
          margin-top: 16px;
        }`);
                        
    html = html.replace(/#rec819195966 \.t420__descr\s*\{\s*font-size:\s*12px;\s*line-height:\s*1\.3;\s*color:\s*#ffffff;\s*font-weight:\s*300;\s*font-family:\s*'Poppins';\s*\}/g,
                        `#rec819195966 .t420__descr {
          font-size: 24px;
          line-height: 1.35;
          color: #ffffff;
          font-weight: 300;
          font-family: 'Poppins';
        }`);

    // And fix the logo max-width!
    html = html.replace(/#rec819195966 \.t420__logo\s*\{\s*font-size:\s*20px;\s*color:\s*#ffffff;\s*text-transform:\s*uppercase;\s*\}/g,
                        `#rec819195966 .t420__logo {
          font-size: 20px;
          color: #ffffff;
          text-transform: uppercase;
          max-width: 130px !important;
        }`);

    changed = true;
    console.log(`Fixed tiny footer CSS in ${file}`);
  }

  if (changed) {
    fs.writeFileSync(file, html, 'utf8');
  }
}
