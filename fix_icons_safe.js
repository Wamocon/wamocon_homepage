const fs = require('fs');

const dir = './';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

for (const file of files) {
    let html = fs.readFileSync(file, 'utf8');
    
    // Find Instagram icon to get base Top values
    const instaRegex = /<div class='t396__elem tn-elem(?:(?!<div class='t396__elem tn-elem).)*?href="[^"]*instagram[^"]*"(?:(?!<div class='t396__elem tn-elem).)*?group_316\.svg(?:(?!<div class='t396__elem tn-elem).)*?<\/a>\s*<\/div>/is;
    const instaMatch = instaRegex.exec(html);
    if (!instaMatch) continue;
    
    // Extract Top values from Instagram icon
    const topMatch = /data-field-top-value="([^"]*)"/.exec(instaMatch[0]);
    const top320Match = /data-field-top-res-320-value="([^"]*)"/.exec(instaMatch[0]);
    const top480Match = /data-field-top-res-480-value="([^"]*)"/.exec(instaMatch[0]);
    const top960Match = /data-field-top-res-960-value="([^"]*)"/.exec(instaMatch[0]);
    
    if (!topMatch) continue;
    
    const top = topMatch[1];
    const top320 = top320Match ? top320Match[1] : '';
    const top480 = top480Match ? top480Match[1] : '';
    const top960 = top960Match ? top960Match[1] : '';

    let modified = false;
    
    const blockRegex = /<div class='t396__elem tn-elem(?:(?!<div class='t396__elem tn-elem).)*?href="([^"]+)"(?:(?!<div class='t396__elem tn-elem).)*?<\/a>\s*<\/div>/gis;
    
    html = html.replace(blockRegex, (match, href) => {
        let left, left320, left960;
        
        if (href.includes('youtube') && match.includes('group_317.svg')) {
            left = "162"; left320 = "152"; left960 = "152";
        } else if (href.includes('facebook') && match.includes('facebook_5968764_1.svg')) {
            left = "202"; left320 = "182"; left960 = "192";
        } else if (href.includes('linkedin') && match.includes('frame_9.svg')) {
            left = "242"; left320 = "212"; left960 = "232";
        } else if (href.includes('instagram') && match.includes('group_316.svg')) {
            left = "282"; left320 = "242"; left960 = "272";
        } else {
            return match; // Not a social icon
        }
        
        modified = true;
        let newDiv = match;
        
        // Replace Tops
        newDiv = newDiv.replace(/data-field-top-value="[^"]*"/, `data-field-top-value="${top}"`);
        if (top320) newDiv = newDiv.replace(/data-field-top-res-320-value="[^"]*"/, `data-field-top-res-320-value="${top320}"`);
        if (top480) newDiv = newDiv.replace(/data-field-top-res-480-value="[^"]*"/, `data-field-top-res-480-value="${top480}"`);
        if (top960) newDiv = newDiv.replace(/data-field-top-res-960-value="[^"]*"/, `data-field-top-res-960-value="${top960}"`);
        
        // Replace Lefts
        newDiv = newDiv.replace(/data-field-left-value="[^"]*"/, `data-field-left-value="${left}"`);
        if (newDiv.includes('data-field-left-res-320-value=')) {
            newDiv = newDiv.replace(/data-field-left-res-320-value="[^"]*"/, `data-field-left-res-320-value="${left320}"`);
        } else {
            newDiv = newDiv.replace(/(data-field-left-value="[^"]*")/, `$1 data-field-left-res-320-value="${left320}"`);
        }
        
        if (newDiv.includes('data-field-left-res-960-value=')) {
            newDiv = newDiv.replace(/data-field-left-res-960-value="[^"]*"/, `data-field-left-res-960-value="${left960}"`);
        } else {
            newDiv = newDiv.replace(/(data-field-left-value="[^"]*")/, `$1 data-field-left-res-960-value="${left960}"`);
        }
        
        return newDiv;
    });
    
    if (modified) {
        fs.writeFileSync(file, html);
        console.log(`Fixed icons safely in ${file}`);
    }
}
