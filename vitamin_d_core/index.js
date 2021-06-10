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
app.get('/', (request, response) => {
    response.render('index')
});

app.get('/user', (request, response) => {
    // get user data
    axios.get('http://resource_user/user')
        .then(function (api_response) {
            // TODO: parse data correctly
            response.json({
                'email': api_response.body.email,
                'firstname': api_response.body.firstname,
                'lastname': api_response.body.lastname,
                'password': api_response.body.password,
                'birthdate': api_response.body.birthdate,
                'gender': api_response.body.gender,
                'lenght': api_response.body.lenght,
                'weight': api_response.body.weight,
                'dressed': api_response.body.dressed,
            })
        })
        .catch(function (error) {
            console.log(error);
        });
});

app.post('/user', (request, response) => {
    // Register new user
    post_data = {
        // TODO: format data correctly
        'geslacht': request.body.gender,
        'voornaam': request.body.firstname,
        'achternaam': request.body.lastname,
        'username': request.body.email,
        'password': request.body.password,
        'geboortedatum': request.body.birthdate,
        'lengte': request.body.lenght,
        'gewicht': request.body.weight,
        'gewichtpositie': request.body.dressed,
    }
    
    axios.post('http://resource_user/user', post_data)
        .then(response.sendStatus(200))
        .catch(function (error) {
            console.log(error);
            response.sendStatus(400);
        });
});

app.post('/login', (request, response) => {
    // login user
    post_data = {
        'email': request.body.email,
        'password': password,
    }
    
    // TODO: get correct resource user route
    axios.post('http://resource_user/login', post_data)
        .then(function (api_response) {
            // TODO: return correct session
            response.json({
                'session': 'zero',
            })
        })
        .catch(function (error) {
            console.log(error);
            response.sendStatus(400);
        });
});

app.post('/activity/', (request, response) => {
    // login user
    post_data = {
        'datetime': request.body.datetime,
        'distance': request.body.distance,
    }
    
    axios.post('http://resource_activity/', post_data)
        .then(function (api_response) {
            response.sendStatus(200);
        })
        .catch(function (error) {
            console.log(error);
            response.sendStatus(400);
        });
});

app.get('/activity/', (request, response) => {
    // get activity data
    axios.get('http://resource_activity/')
        .then(function (activity) {
            response.json({
                'id': activity.body.id,
                'datetime': activity.body.datetime,
                'distance': activity.body.distance,
            })
        })
        .catch(function (error) {
            console.log(error);
        });
});

app.get('/activity/history', (request, response) => {
    // get activity data
    axios.get('http://resource_activity/history')
        .then(function (activity) {
            response.json({
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
