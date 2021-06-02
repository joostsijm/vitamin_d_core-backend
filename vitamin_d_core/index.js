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
    // TODO: authentication
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
        'email': request.body.email,
        'firstname': request.body.firstname,
        'lastname': request.body.lastname,
        'password': request.body.password,
        'birthdate': request.body.birthdate,
        'gender': request.body.gender,
        'lenght': request.body.lenght,
        'weight': request.body.weight,
        'dressed': request.body.dressed,
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

const port = 80;
app.listen(port, () => console.log('Server running...'));
