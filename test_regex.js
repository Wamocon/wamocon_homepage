const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const regex = /<div class='t396__elem tn-elem(?:(?!<div class='t396__elem tn-elem).)*?href="[^"]*instagram[^"]*"(?:(?!<div class='t396__elem tn-elem).)*?group_316\.svg(?:(?!<div class='t396__elem tn-elem).)*?<\/a>\s*<\/div>/is;
console.log('Regex matched:', regex.test(html));

const blockRegex = /<div class='t396__elem tn-elem(?:(?!<div class='t396__elem tn-elem).)*?href="([^"]+)"(?:(?!<div class='t396__elem tn-elem).)*?<\/a>\s*<\/div>/gis;
let match;
while ((match = blockRegex.exec(html)) !== null) {
  if (match[1].includes('instagram') || match[1].includes('youtube') || match[1].includes('facebook') || match[1].includes('linkedin')) {
    console.log('Block matched:', match[1]);
  }
}
