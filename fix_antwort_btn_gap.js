const fs = require('fs');

let p578 = fs.readFileSync('page57822475.html', 'utf8');

const blocks = ['822437204', '1050675716', '822437573'];

blocks.forEach(id => {
  // Update the padding-top of the t-rec div
  let divRegex = new RegExp(`(<div id="rec${id}" class="r t-rec t-rec_pt_)30(_t-rec_pb_45"[\\s\\S]*?style="padding-top:)30px(;padding-bottom:45px;)`, 'g');
  p578 = p578.replace(divRegex, `$145$245px$3`);
});

fs.writeFileSync('page57822475.html', p578, 'utf8');
console.log('Fixed page57822475.html Antwort buttons gap');
