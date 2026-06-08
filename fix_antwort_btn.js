const fs = require('fs');

let p578 = fs.readFileSync('page57822475.html', 'utf8');

// For all Antwort buttons, we want to increase the size and add padding-top to their containers.
// The containers are the t-rec blocks.
// We can find them by looking for the wmc-antwort-btn style definitions.
// Actually, I can just replace the CSS for wmc-antwort-btn to use !important, or replace the specific block definitions.
// There are three blocks: #rec822437204, #rec1050675716, #rec822437573.

const blocks = ['822437204', '1050675716', '822437573'];

blocks.forEach(id => {
  // Update the padding-top of the t-rec div
  let divRegex = new RegExp(`(<div id="rec${id}" class="r t-rec[\\s\\S]*?style="padding-top:)0px(;padding-bottom:15px;)`, 'g');
  p578 = p578.replace(divRegex, `$145px$2`);
  
  // Update the width, height, font-size in the CSS
  let cssRegexWidth = new RegExp(`(#rec${id} \\.wmc-antwort-btn \\{[\\s\\S]*?width: )200px(;)`, 'g');
  p578 = p578.replace(cssRegexWidth, `$1260px$2`);
  
  let cssRegexHeight = new RegExp(`(#rec${id} \\.wmc-antwort-btn \\{[\\s\\S]*?height: )55px(;)`, 'g');
  p578 = p578.replace(cssRegexHeight, `$160px$2`);
  
  let cssRegexFont = new RegExp(`(#rec${id} \\.wmc-antwort-btn \\{[\\s\\S]*?font-size: )16px(;)`, 'g');
  p578 = p578.replace(cssRegexFont, `$118px$2`);

  let cssRegexPadding = new RegExp(`(#rec${id} \\.wmc-antwort-btn \\{[\\s\\S]*?padding: )15px 30px(;)`, 'g');
  p578 = p578.replace(cssRegexPadding, `$117px 30px$2`);
});

// Let's also check if the user wanted the button centered or left-aligned. 
// "make sure it has enough and same gap with the component for al l the buttons"
// In the 2nd screenshot the button is left aligned. t-align_left does that.
// BUT wait, in the 1st screenshot, the button was tiny! Why? Because maybe the 1st screenshot is mobile view??
// If it's mobile view, it might have a media query reducing its size!
// Let's check for media queries on wmc-antwort-btn in the HTML.
// There is no media query for wmc-antwort-btn in my previous output, but let me add one just in case, or just trust the new width will scale down via max-width: 100%.

fs.writeFileSync('page57822475.html', p578, 'utf8');
console.log('Fixed page57822475.html Antwort buttons');
