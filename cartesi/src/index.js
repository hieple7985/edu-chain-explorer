const express = require('express');
const app = express();
const port = process.env.PORT || 4000;

app.get('/', (req, res) => {
  res.send('Hello, this is the Cartesi Rollup off-chain logic!');
});

app.listen(port, () => {
  console.log(`Cartesi Rollup off-chain logic running on port ${port}`);
});
