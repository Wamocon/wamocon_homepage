const fs = require('fs');

const dir = './';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

let count = 0;
for (const file of files) {
    let html = fs.readFileSync(file, 'utf8');
    
    // The logo is: <img class="t420__logo t-img" src="images/tild3038-3363-4533-a261-363563393531__tilda_logo_wmc_neu_0.png" imgfield="img" style="max-width: 200px;" alt="">
    if (html.includes('max-width: 200px;') && html.includes('tilda_logo_wmc_neu_0.png')) {
        // We only want to replace the max-width of the logo!
        html = html.replace(/(<img[^>]*tilda_logo_wmc_neu_0\.png[^>]*style="max-width: )200px(;?"[^>]*>)/g, '$1130px$2');
        html = html.replace(/(<img[^>]*tilda_logo_wmc_neu_0\.png[^>]*style="max-width: )220px(;?"[^>]*>)/g, '$1130px$2');
        fs.writeFileSync(file, html);
        count++;
    }
}
console.log(`Fixed logo width in ${count} files`);
