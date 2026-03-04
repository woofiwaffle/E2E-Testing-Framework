// -------------------- Imports --------------------
const express = require('express');
const path = require('path');
const morgan = require('morgan');


// -------------------- App init --------------------
const app = express();
const port = 3000;


/* -------------------- Helpers -------------------- */
const ok = (res, data = null, message = 'ok') =>
  res.json({ status: 'success', message, data });

const fail = (res, code, message) =>
  res.status(code).json({ status: 'error', message });

const asyncHandler = fn => (req, res, next) =>
  Promise.resolve(fn(req, res, next)).catch(next);


/* -------------------- Middleware & Security -------------------- */
app.disable('x-powered-by');
app.use(morgan('dev'));
app.use(express.json({ limit: '100kb' }));
app.use(express.urlencoded({ extended: true }));


/* -------------------- In-memory Database -------------------- */
let items = [
  { id: 1, name: 'Item 1' },
  { id: 2, name: 'Item 2' },
  { id: 3, name: 'Item 3' }
];


/* -------------------- Healthcheck -------------------- */
app.get("/healthz", (req, res) => {
  res.status(200).send("OK");
});



// <-------------------- Demo APIs -------------------->
app.post('/api/echo', (req, res) => {
  const text = req.body?.text || '';
  ok(res, text, 'echo');
});

app.get('/api/toast', (req, res) => {
  ok(res, null, 'toast shown');
});


/* -------------------- Items API -------------------- */
app.get('/api/items', asyncHandler(async (req, res) => {
  ok(res, items);
}));

app.post('/api/items', asyncHandler(async (req, res) => {
  if (!req.body.name) return fail(res, 400, 'Name required');
  const nextId = 
    items.length > 0
      ? Math.max(...items.map(i => i.id)) + 1
      : 1;

  const item = { 
    id: nextId, 
    name: req.body.name 
  };
  items.push(item);
  ok(res, item, 'Item added');
}));

app.put('/api/items/:id', asyncHandler(async (req, res) => {
  const item = items.find(i => i.id === parseInt(req.params.id));
  if (!item) return fail(res, 404, 'Item not found');
  item.name = req.body.name;
  ok(res, item, 'Item updated');
}));

app.delete('/api/items/:id', asyncHandler(async (req, res) => {
  items = items.filter(i => i.id !== parseInt(req.params.id));
  ok(res, null, 'Item deleted');
}));


/* -------------------- API 404 -------------------- */
app.use('/api', (req, res) => {
  fail(res, 404, 'API endpoint not found');
});


/* -------------------- Static -------------------- */
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (_, res) =>
  res.sendFile(path.join(__dirname, 'public/index.html'))
);


/* -------------------- Error Handler -------------------- */
app.use((err, req, res, next) => {
  console.error(err);
  fail(res, 500, 'Internal Server Error');
});


// <-------------------- Server start -------------------->
app.listen(port, () =>
  console.log(`http://localhost:${port}`)
);