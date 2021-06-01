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

const User = require('./models/User');

app.get('/user', (request, response) => {
    response.setHeader('Content-Type', 'application/json');
    User.find()
        .then(users => response.end(JSON.stringify( users )))
        .catch(err => response.status(404).json({ msg: 'No users found' }));
});

app.post('/user', (request, response) => {
    const newUser = new User({ name: request.body.name });
    newUser.save()
        .then(user => response.redirect('/'))
        .catch(err => response.status(400).json({ msg: 'Error saving user' }));
});

const port = 80;
app.listen(port, () => console.log('Server running...'));
