const fs = require('fs');

const processFile = (file, newText) => {
    let html = fs.readFileSync(file, 'utf8');
    const regex = /<span[^>]*>[^<]*(Tatsache|Fakt|fact)[^<]*<\/span>/gi;
    
    let count = 0;
    html = html.replace(regex, (match) => {
        // Double check if it is one of the headings we want to replace
        if (/Interessante\s+Tatsache|interessanter\s+Fakt|Interesting\s+fact/i.test(match)) {
            count++;
            return `<span style="font-weight: 600; font-family: Poppins; font-size: 18px; color: #ffffff;">${newText}</span>`;
        }
        return match;
    });

    console.log(`${file}: replaced ${count} occurrences.`);
    fs.writeFileSync(file, html);
};

processFile('page57475469.html', 'Interessante Tatsache: ');
processFile('page59115815.html', 'Interesting fact: ');
