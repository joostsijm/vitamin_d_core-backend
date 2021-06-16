const express = require('express');
const axios = require('axios');

const app = express();

var cookieParser = require('cookie-parser');
app.use(cookieParser());

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
    session_code = req.cookies.session_code
    axios.post('http://resource_auth/auth', {'session_code': session_cookie})
        .then(function (auth_res) {
            axios.get('http://resource_user/user/' + auth_res.body.username)
                .then(function (api_res) {
                    res.json({
                        'firstname': api_res.body.firstname,
                        'lastname': api_res.body.lastname,
                        'username': api_res.body.username,
                        'password': api_res.body.password,
                        'birthdate': api_res.body.birthdate,
                        'gender': api_res.body.gender,
                        'lenght': api_res.body.lenght,
                        'weight': api_res.body.weight,
                        'dressed': api_res.body.dressed,
                    })
                })
                .catch(function (error) {
                    res.status(500).send(error.message);
                });
        })
        .catch(function (error) {
            res.status(500).send(error.message);
        });
});

app.post('/user', (req, res, next) => {
    // Register new user
    post_data = {
        'geslacht': req.body.gender,
        'voornaam': req.body.firstname,
        'achternaam': req.body.lastname,
        'username': req.body.username,
        'password': req.body.password,
        'geboortedatum': req.body.birthdate,
        'lengte': req.body.lenght,
        'lengtepositie': req.body.lenghtposition,
        'gewicht': req.body.weight,
        'gewichtpositie': req.body.dressed,
    }
    
    axios.post('http://resource_user/user', post_data)
        .then(response => {
            if (response.status != 200) {
                res.status(response.status).send(response.body)
            }
            res.status(200).end()
        })
        .catch(error => {
            res.status(error.response.status).send(error.response.body)
        });

});

app.post('/login', (req, res) => {
    // login user
    post_data = {
        'username': req.body.username,
        'password': req.body.password,
    }
    
    axios.post('http://resource_auth/login', post_data)
        .then(function (api_res) {
            if (api_res.status != 200) {
                res.status(api_res.status).send(api_res.body)
            }
            res.json(api_res.data)
        })
        .catch(function (error) {
            res.status(500).send(error.message);
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
            res.status(500).send(error.message);
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
            res.status(500).send(error.message);
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
            res.status(500).send(error.message);
        });
});

const port = 80;
app.listen(port, () => console.log('Server running...'));
