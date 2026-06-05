const fs = require('fs');

let html = fs.readFileSync('page64750211.html', 'utf8');

html = html.replace('WAMOCON Academy GmbH', 'WAMOCON GmbH');
html = html.replace('+49 (0) 6196 5838312', '+49 6196 5838311');
html = html.replace('tel:+49061965838312', 'tel:+4961965838311');
html = html.replace('info@test-it-academy.de', 'info@wamocon.com');

fs.writeFileSync('page64750211.html', html);
