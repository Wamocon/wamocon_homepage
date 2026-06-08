const fs = require('fs');

let p578 = fs.readFileSync('page57822475.html', 'utf8');

const blocks = ['822437204', '1050675716', '822437573'];

blocks.forEach(id => {
  // Regex to match the entire CSS block for #recID .wmc-antwort-btn
  let cssRegex = new RegExp(`(#rec${id} \\.wmc-antwort-btn \\{[\\s\\S]*?\\})`, 'g');
  
  p578 = p578.replace(cssRegex, (match) => {
    if (match.includes(':hover')) return match; 
    
    // We update to 280px width, 65px height, and ensure it's block with 0 margin.
    return `#rec${id} .wmc-antwort-btn {
          display: block !important;
          box-sizing: border-box;
          width: 280px !important;
          max-width: 100%;
          height: 65px !important;
          line-height: 65px !important;
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
console.log('Fixed page57822475.html Antwort button alignment and made it bigger');
