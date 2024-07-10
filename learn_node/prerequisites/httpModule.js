const http = require('http');

const server = http.createServer((req, res)=>{
    if (req.url === '/') {
        res.end("welcome to the home page");
    }
    else if (req.url === '/about') {
        res.end('you reached our about page');
    }
    else {
        res.end(`
            <h1>ERROR!</h1>
            <p>the current page is not available</p>
            <a href="/">back home</a>
            `);
    }
})
server.listen(3390);