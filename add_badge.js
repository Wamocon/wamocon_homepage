const fs = require('fs');

const pages = ['page59102217.html', 'page54483969.html', 'index.html'];

for (let page of pages) {
    if (!fs.existsSync(page)) continue;
    
    let html = fs.readFileSync(page, 'utf8');

    // Skip if already added
    if (html.includes('1734181878265')) {
        console.log(`Already added to ${page}`);
        continue;
    }

    // 1. Extract the CSS block for 1734181878266
    let cssRegex = new RegExp('([^}]*#rec\\d+ \\.tn-elem\\[data-elem-id="1734181878266"\\][^{]*\\{[^}]*\\})', 'g');
    let cssMatches = html.match(cssRegex);
    
    // There should be multiple matches for the media queries
    if (cssMatches) {
        let newCssBlocks = cssMatches.map(css => {
            let newCss = css.replace(/1734181878266/g, '1734181878265');
            // Adjust left positions
            newCss = newCss.replace(/1023px/, '932px');
            newCss = newCss.replace(/844px/, '753px');
            newCss = newCss.replace(/542px/, '451px');
            newCss = newCss.replace(/410px/, '345px');
            newCss = newCss.replace(/271px/, '222px');
            return newCss;
        });
        
        // Inject CSS right before </style>
        let styleEndIdx = html.lastIndexOf('</style>');
        if (styleEndIdx !== -1) {
            html = html.substring(0, styleEndIdx) + '\n' + newCssBlocks.join('\n') + '\n' + html.substring(styleEndIdx);
        }
    }

    // 2. Extract the HTML block for 1734181878266
    let htmlRegex = /<div class='t396__elem tn-elem tn-elem__\d+1734181878266'[\s\S]*?<\/div>\s*<\/div>/;
    let htmlMatch = html.match(htmlRegex);
    
    if (htmlMatch) {
        let newHtml = htmlMatch[0].replace(/1734181878266/g, '1734181878265');
        // Replace image src
        newHtml = newHtml.replace(/data-original='[^']*'/, "data-original='images/WMC_UnternehmeNderZukuft_nominiert.webp'");
        newHtml = newHtml.replace(/src='[^']*'/, "src='images/WMC_UnternehmeNderZukuft_nominiert.webp'");
        
        // Adjust inline HTML left positions
        newHtml = newHtml.replace(/data-field-left-value="1023"/, 'data-field-left-value="932"');
        newHtml = newHtml.replace(/data-field-left-res-960-value="844"/, 'data-field-left-res-960-value="753"');
        newHtml = newHtml.replace(/data-field-left-res-640-value="542"/, 'data-field-left-res-640-value="451"');
        newHtml = newHtml.replace(/data-field-left-res-480-value="410"/, 'data-field-left-res-480-value="345"');
        newHtml = newHtml.replace(/data-field-left-res-320-value="271"/, 'data-field-left-res-320-value="222"');

        // Inject new HTML before the existing HTML block
        html = html.replace(htmlMatch[0], newHtml + '\n' + htmlMatch[0]);
    }

    fs.writeFileSync(page, html);
    console.log(`Updated ${page}`);
}
