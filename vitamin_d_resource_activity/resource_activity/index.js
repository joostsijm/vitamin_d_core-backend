const express = require('express');
const mongoose = require('mongoose');

const app = express();

var bodyParser = require('body-parser');

app.use(bodyParser.json());

app.use(bodyParser.urlencoded({
   extended: true
}));

app.use(express.urlencoded({ extended: false }));

// Connect to MongoDB
mongoose
    .connect('mongodb://mongo:27017/vitamin-d', { useNewUrlParser: true })
    .then(() => console.log('MongoDB Connected'))
    .catch(err => console.log(err));

// routes
require('./routes')(app);

const port = 80;
app.listen(port, () => console.log('Server running...'));
