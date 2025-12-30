const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());
app.use(express.static(__dirname + '/public'));
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

// health check used by docker-compose
app.get('/healthz', (req, res) => {
  res.status(200).json({ status: 'ok' });
});

// simple demo API: echo posted text back
app.post('/api/echo', (req, res) => {
  const text = (req.body && req.body.text) || '';
  res.json({ echo: text });
});

app.listen(port, () => {
  console.log(`Demo app running at http://localhost:${port}`);
});