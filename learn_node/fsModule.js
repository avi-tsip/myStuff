const {readFileSync} = require('fs');
const {writeFileSync} = require('fs');

const firstFile = readFileSync('../content/firstFile.txt', 'utf8')
const secondFile = readFileSync('../content/secondFile.txt', 'utf8')

writeFileSync('../content/results.txt', `here is the text from both files: ${firstFile}, ${secondFile}`, {flag:'a'})
