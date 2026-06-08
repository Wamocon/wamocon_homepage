const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

for (const file of files) {
  let html = fs.readFileSync(file, 'utf8');
  let changed = false;

  const textRegex = /#rec[0-9]+ \.t420__text\s*\{\s*font-size:\s*10px;\s*line-height:\s*1\.2;\s*color:\s*#ffffff;\s*font-weight:\s*300;\s*font-family:\s*'Poppins';\s*\}/g;
  
  if (textRegex.test(html)) {
    html = html.replace(/(#rec[0-9]+) \.t420__text\s*\{\s*font-size:\s*10px;\s*line-height:\s*1\.2;\s*color:\s*#ffffff;\s*font-weight:\s*300;\s*font-family:\s*'Poppins';\s*\}/g, 
                        `$1 .t420__text {
          font-size: 16px;
          line-height: 1.45;
          color: #ffffff;
          font-weight: 300;
          font-family: 'Poppins';
          margin-top: 16px;
        }`);
                        
    html = html.replace(/(#rec[0-9]+) \.t420__descr\s*\{\s*font-size:\s*12px;\s*line-height:\s*1\.3;\s*color:\s*#ffffff;\s*font-weight:\s*300;\s*font-family:\s*'Poppins';\s*\}/g,
                        `$1 .t420__descr {
          font-size: 24px;
          line-height: 1.35;
          color: #ffffff;
          font-weight: 300;
          font-family: 'Poppins';
        }`);

    html = html.replace(/(#rec[0-9]+) \.t420__logo\s*\{\s*font-size:\s*20px;\s*color:\s*#ffffff;\s*text-transform:\s*uppercase;\s*\}/g,
                        `$1 .t420__logo {
          font-size: 20px;
          color: #ffffff;
          text-transform: uppercase;
          max-width: 130px !important;
        }`);

    changed = true;
    console.log(`Fixed tiny footer CSS globally in ${file}`);
  }

  if (changed) {
    fs.writeFileSync(file, html, 'utf8');
  }
}
