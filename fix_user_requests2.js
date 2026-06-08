const fs = require('fs');

// Fix 3: page57475469.html bullet points indentation (properly this time)
let p57 = fs.readFileSync('page57475469.html', 'utf8');

// Undo the previous wrapping if it exists
p57 = p57.replace(/style="padding-left: 15px; text-indent: -15px;"/g, '');

// Now we need to parse the innerHTML of those two description blocks and replace `<br />` with a div separator
// The block 1: Softwarelösungen und Beratung
let block1Regex = /(<div class="t-card__descr t-descr t-descr_sm" field="li_descr__2514642172360">\s*)([\s\S]*?)(<\/div>)/;
p57 = p57.replace(block1Regex, (match, p1, p2, p3) => {
    // Only replace if it contains bullet points (it has <strong style="color: rgb(244, 14, 14);">- )
    if (p2.includes('- </strong>')) {
        let newP2 = '<div style="padding-left: 15px; text-indent: -15px;">' + p2.split(/<br\s*\/?>/).join('</div><div style="padding-left: 15px; text-indent: -15px;">') + '</div>';
        return p1 + newP2 + p3;
    }
    return match;
});

// The block 2: Karrierebooster
let block2Regex = /(<div class="t-card__descr t-descr t-descr_sm" field="li_descr__2514642172361">\s*)([\s\S]*?)(<\/div>)/;
p57 = p57.replace(block2Regex, (match, p1, p2, p3) => {
    // Only replace if it contains bullet points
    if (p2.includes('- </strong>')) {
        let newP2 = '<div style="padding-left: 15px; text-indent: -15px;">' + p2.split(/<br\s*\/?>/).join('</div><div style="padding-left: 15px; text-indent: -15px;">') + '</div>';
        return p1 + newP2 + p3;
    }
    return match;
});

fs.writeFileSync('page57475469.html', p57, 'utf8');
console.log('Fixed page57475469.html bullet indentation properly');

// Fix 4: page57822475.html form scale (with the correct IDs)
let p578 = fs.readFileSync('page57822475.html', 'utf8');

// Reduce form inputs for 1724154836182
// height: 60 -> 40
p578 = p578.replace(
  /(data-elem-id='1724154836182'[^>]*data-field-inputheight-value=")60(")/g,
  '$140$2'
);
// font size: 18 -> 14
p578 = p578.replace(
  /(data-elem-id='1724154836182'[^>]*data-field-inputfontsize-value=")18(")/g,
  '$114$2'
);
// margin bottom: 20 -> 10
p578 = p578.replace(
  /(data-elem-id='1724154836182'[^>]*data-field-inputmargbottom-value=")20(")/g,
  '$110$2'
);
// button height: 60 -> 40
p578 = p578.replace(
  /(data-elem-id='1724154836182'[^>]*data-field-buttonheight-value=")60(")/g,
  '$140$2'
);

// We also need to fix the custom <style> tag at the bottom of the page which forces 50px input height!
// <style>#rec822446072 .tn-elem[data-elem-id="1724154836182"] .t-input{height:50px !important;}
p578 = p578.replace(
  /#rec822446072 \.tn-elem\[data-elem-id="1724154836182"\] \.t-input\{height:50px !important;\}/g,
  '#rec822446072 .tn-elem[data-elem-id="1724154836182"] .t-input{height:40px !important; font-size:14px !important;}'
);
p578 = p578.replace(
  /#rec822446072 \.tn-elem\[data-elem-id='1724154836182'\] \.t-input\{height:52px !important;\}/g,
  '#rec822446072 .tn-elem[data-elem-id="1724154836182"] .t-input{height:40px !important; font-size:14px !important;}'
);
p578 = p578.replace(
  /#rec822446072 \.tn-elem\[data-elem-id="1724154836182"\] \.t-input-group\{margin-bottom:12px !important;\}/g,
  '#rec822446072 .tn-elem[data-elem-id="1724154836182"] .t-input-group{margin-bottom:10px !important;}'
);

fs.writeFileSync('page57822475.html', p578, 'utf8');
console.log('Fixed page57822475.html form scale correctly');
