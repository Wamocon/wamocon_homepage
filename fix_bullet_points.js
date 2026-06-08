const fs = require('fs');

let html = fs.readFileSync('page57475469.html', 'utf8');

// The fields we want to target are those containing the bullet points.
// We can just use string replacement or a more flexible regex.
// Since we know the bullet points start with `<strong style="color: rgb(244, 14, 14);">- </strong>`, 
// we can find all `t-card__descr` divs and replace their content if they have bullet points.

const regex = /(<div class="t-card__descr t-descr t-descr_sm"[^>]*>)([\s\S]*?)(<\/div>)/g;

html = html.replace(regex, (match, p1, p2, p3) => {
    if (p2.includes('- </strong>')) {
        // First, clean up any previous failed attempts
        let content = p2.replace(/<div style="padding-left: 15px; text-indent: -15px;">/g, '')
                        .replace(/<\/div>/g, '');
        
        // Split by `<br />`, `<br>`, etc.
        let items = content.split(/<br\s*\/?>/i);
        
        // Wrap each item
        let newContent = items.map(item => {
            if (item.trim() === '') return '';
            return `<div style="padding-left: 15px; text-indent: -15px; margin-bottom: 5px;">${item.trim()}</div>`;
        }).join('');
        
        return p1 + '\n' + newContent + '\n' + p3;
    }
    return match;
});

fs.writeFileSync('page57475469.html', html, 'utf8');
console.log('Fixed bullet points indentation in page57475469.html');
