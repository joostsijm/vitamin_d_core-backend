const express = require('express');
const axios = require('axios');

const app = express();

var bodyParser = require('body-parser');

app.use(bodyParser.json());

app.use(bodyParser.urlencoded({
   extended: true
}));

app.set('view engine', 'ejs');

app.use(express.urlencoded({ extended: false }));

// Connect to MongoDB
app.get('/', (req, res) => {
    res.render('index')
});

app.get('/user', (req, res) => {
    // get user data
    axios.get('http://resource_user/user')
        .then(function (api_res) {
            // TODO: parse data correctly
            res.json({
                'email': api_res.body.email,
                'firstname': api_res.body.firstname,
                'lastname': api_res.body.lastname,
                'password': api_res.body.password,
                'birthdate': api_res.body.birthdate,
                'gender': api_res.body.gender,
                'lenght': api_res.body.lenght,
                'weight': api_res.body.weight,
                'dressed': api_res.body.dressed,
            })
        })
        .catch(function (error) {
            console.log(error);
        });
});

app.post('/user', (req, res) => {
    // Register new user
    post_data = {
        // TODO: format data correctly
        'geslacht': req.body.gender,
        'voornaam': req.body.firstname,
        'achternaam': req.body.lastname,
        'username': req.body.email,
        'password': req.body.password,
        'geboortedatum': req.body.birthdate,
        'lengte': req.body.lenght,
        'gewicht': req.body.weight,
        'gewichtpositie': req.body.dressed,
    }
    
    axios.post('http://resource_user/user', post_data)
        .then(res.sendStatus(200))
        .catch(function (error) {
            console.log(error);
            res.sendStatus(400);
        });
});

app.post('/login', (req, res) => {
    // login user
    post_data = {
        'email': req.body.email,
        'password': password,
    }
    
    // TODO: get correct resource user route
    axios.post('http://resource_user/login', post_data)
        .then(function (api_res) {
            // TODO: return correct session
            res.json({
                'session': 'zero',
            })
        })
        .catch(function (error) {
            console.log(error);
            res.sendStatus(400);
        });
});

app.post('/activity/', (req, res) => {
    // login user
    post_data = {
        'datetime': req.body.datetime,
        'distance': req.body.distance,
    }
    
    axios.post('http://resource_activity/', post_data)
        .then(function (api_res) {
            res.sendStatus(200);
        })
        .catch(function (error) {
            console.log(error);
            res.sendStatus(400);
        });
});

app.get('/activity/', (req, res) => {
    // get activity data
    axios.get('http://resource_activity/')
        .then(function (activity) {
            res.json({
                'id': activity.body.id,
                'datetime': activity.body.datetime,
                'distance': activity.body.distance,
            })
        })
        .catch(function (error) {
            console.log(error);
        });
});

app.get('/activity/history', (req, res) => {
    // get activity data
    axios.get('http://resource_activity/history')
        .then(function (activity) {
            res.json({
                'id': activity.body.id,
                'datetime': activity.body.datetime,
                'distance': activity.body.distance,
            })
        })
        .catch(function (error) {
            console.log(error);
        });
});

const port = 80;
app.listen(port, () => console.log('Server running...'));
