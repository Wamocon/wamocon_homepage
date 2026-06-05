const fs = require('fs');
const html = fs.readFileSync('page64750211.html', 'utf8');
const regex = /<div class='t396__elem tn-elem[^>]*data-elem-type='image'[^>]*data-field-top-value="([0-9]+)"[^>]*data-field-left-value="([0-9]+)"[\s\S]*?href="([^"]+)"[\s\S]*?<img/g;
let match;
while ((match = regex.exec(html)) !== null) {
  const url = match[3];
  if (url.includes('facebook') || url.includes('instagram') || url.includes('youtube') || url.includes('linkedin')) {
    console.log(`Icon: ${url}`);
    console.log(`Top: ${match[1]}, Left: ${match[2]}`);
    const resTop = html.substring(match.index, match.index + 500).match(/data-field-top-res-[0-9]+-value="([0-9]+)"/g);
    console.log(`Responsive Tops: ${resTop ? resTop.join(', ') : 'none'}`);
  }
}
