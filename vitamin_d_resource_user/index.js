const express = require('express');
const mongoose = require('mongoose');

const app = express();

app.use(express.urlencoded({ extended: false }));

// Connect to MongoDB
mongoose
  .connect(
    'mongodb://mongo:27017/vitamin-d',
    { useNewUrlParser: true }
  )
  .then(() => console.log('MongoDB Connected'))
  .catch(err => console.log(err));

const User= require('./models/User');

app.get('/', (req, res) => {
    res.setHeader('Content-Type', 'application/json');
    User.find()
        .then(users => res.end(JSON.stringify( users )))
        .catch(err => res.status(404).json({ msg: 'No users found' }));
});

app.post('/user/add', (req, res) => {
  const newUser = new User({
    name: req.body.name
  });

  newUser.save().then(user => res.redirect('/'));
});

const port = 3000;

app.listen(port, () => console.log('Server running...'));
