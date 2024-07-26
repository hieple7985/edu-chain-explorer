const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = process.env.PORT || 5000;

app.use(bodyParser.json());
app.use('/api', require('./routes/api'));

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
