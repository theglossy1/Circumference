const http = require('http');

const server = http.createServer(function (req, res) {
  if (req.url === '/live') {
    res.writeHead(200, {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive'
    });
    res.write('retry: 5000\n');

    const interval = setInterval(() => {
      res.write('data: ' + new Date() + '\n\n');
    }, 1000);

    req.on('end', () => clearInterval(interval));
    return;
  }

  // Normal requests
  return res.end();
});

server.listen(3000);