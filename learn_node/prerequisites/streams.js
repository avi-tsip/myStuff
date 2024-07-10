const {createReadStream} = require("fs");

const stream = createReadStream("../content/bigFile.txt", {
    highWaterMark: 90000, // changes the number of bytes in each stream
    encoding: 'utf8' // changes the encoding of the output
} );

stream.on('data', (result) => {
    console.log(result)
}) 

stream.on('error', (err) => {
    console.log(err)
}) 
