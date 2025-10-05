const express = require('express');
const app = express();
const port = 3000;

app.use(express.static(__dirname + '/public'));
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

app.listen(port, () => {
  console.log(`Demo app running at http://localhost:${port}`);
});