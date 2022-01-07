const express = require('express');
const app = express();
const fs = require('fs');

app.listen(3000, () => console.log('listening at 3000'));
app.use(express.static('html'));
app.use(express.json({limit: '10mb'}));





