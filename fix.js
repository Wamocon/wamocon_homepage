const fs = require('fs');
let html = fs.readFileSync('page59102217.html', 'utf8');

// 1. Fix CSS for Column 2 (left from 239 -> 210)
html = html.replace(/left:calc\(50% - 600px \+ 239px\);/g, 'left:calc(50% - 600px + 210px);');
// 2. Fix HTML for Column 2
html = html.replace(/data-field-left-value="239"/g, 'data-field-left-value="210"');

// 3. Fix CSS for Column 3 (left from 471 -> 400)
html = html.replace(/left:calc\(50% - 600px \+ 471px\);/g, 'left:calc(50% - 600px + 400px);');
// 4. Fix HTML for Column 3
html = html.replace(/data-field-left-value="471"/g, 'data-field-left-value="400"');

// 5. Change text in Column 2
html = html.replace(/>successful IT projects</g, '>successful IT projects<');

// Now let's extract the HTML and CSS for "1723558927084" (35+) and "1723558927089" (reliable partnerships) and duplicate them for Column 4
let elem1_css = html.match(/#rec832623374 \.tn-elem\[data-elem-id="1723558927084"\].*?}/g);
let elem2_css = html.match(/#rec832623374 \.tn-elem\[data-elem-id="1723558927089"\].*?}/g);

let elem1_html = html.match(/<div class='t396__elem tn-elem tn-elem__8326233741723558927084'.*?<\/div>/);
let elem2_html = html.match(/<div class='t396__elem tn-elem tn-elem__8326233741723558927089'.*?<\/div>/);

// Add new elements at the end of the style block and HTML block
if (elem1_css && elem2_css && elem1_html && elem2_html) {
    let new_css1 = elem1_css.map(s => s.replace(/1723558927084/g, '1723558927200').replace(/400px/g, '590px'));
    let new_css2 = elem2_css.map(s => s.replace(/1723558927089/g, '1723558927201').replace(/400px/g, '590px'));

    let new_html1 = elem1_html[0].replace(/1723558927084/g, '1723558927200').replace(/data-field-left-value="400"/g, 'data-field-left-value="590"').replace(/>35\+</g, '>50+<');
    let new_html2 = elem2_html[0].replace(/1723558927089/g, '1723558927201').replace(/data-field-left-value="400"/g, 'data-field-left-value="590"').replace(/>reliable partnerships</g, '>new AI apps<').replace(/width-value="124"/, 'width-value="160"');

    // Inject CSS
    html = html.replace('</style>', new_css1.join('\n') + '\n' + new_css2.join('\n') + '\n</style>');
    // Inject HTML
    html = html.replace(/<\/div>\s*<\/div>\s*<\/div>\s*<script>/, new_html1 + '\n' + new_html2 + '\n</div>\n</div>\n</div>\n<script>');
}

fs.writeFileSync('page59102217.html', html);
console.log('Done replacement');
