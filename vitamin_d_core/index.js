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
    axios.post('http://resource_auth/auth', {'session_code': session_code})
        .then(function (auth_res) {
            axios.get('http://resource_user/user/' + auth_res.data.username)
                .then(function (api_res) {
                    res.json({
                        'username': api_res.data.username,
                        'firstname': api_res.data.naamgegevens.voornaam,
                        'lastname': api_res.data.naamgegevens.geslachtsnaam.achternaam,
                        'birthdate': api_res.data.geboortedatum['$date'],
                        'gender': api_res.data.geslacht,
                        'lenght': api_res.data.userdata.lichaamslengte.lengteWaarde,
                        'position': api_res.data.userdata.lichaamslengte.positie,
                        'lenghtdatetime': api_res.data.userdata.lichaamslengte.lengteDatum,
                        'weight': api_res.data.userdata.lichaamsgewicht.gewichtWaarde,
                        'dressed': api_res.data.userdata.lichaamsgewicht.kleding,
                        'weightdatetime': api_res.data.userdata.lichaamsgewicht.gewichtDatum,
                    })
                })
                .catch(function (error) {
                    res.status(error.response.status).send(error.response.data)
                });
        })
        .catch(function (error) {
            res.status(error.response.status).send(error.response.data)
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
        'lengtepositie': req.body.position,
        'gewicht': req.body.weight,
        'gewichtpositie': req.body.dressed,
    }
    
    axios.post('http://resource_user/user', post_data)
        .then(response => {
            if (response.status != 200) {
                console.log(response)
                res.status(response.status).send(response)
            }
            res.status(200).end()
        })
        .catch(error => {
            res.status(error.response.status).send(error.response.data)
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
            res.status(error.response.status).send(error.response.data)
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
            res.status(error.response.status).send(error.response.data)
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
            res.status(error.response.status).send(error.response.data)
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
            res.status(error.response.status).send(error.response.data)
        });
});

app.post('questionnaire', (req, res) => {
    session_code = req.cookies.session_code
    axios.post('http://resource_auth/auth', {'session_code': session_code})
        .then(auth_res => {
            post_data = req.body
            post_data['username'] = auth_res.data.username
            axios.post('http://resource_questionnaire/anwser', post_data)
                .then(api_res => {
                    res.status(200).end()
                })
                .catch(function (error) {
                    res.status(error.response.status).send(error.response.data)
                });
        })
        .catch(function (error) {
            res.status(error.response.status).send(error.response.data)
        });
})

app.get('quetionnaire', (req, res) => {
    session_code = req.cookies.session_code
    axios.post('http://resource_auth/auth', {'session_code': session_code})
        .then(auth_res => {
            axios.get('http://resource_questionnaire/questionnaires/' + auth_res.data.username)
                .then(api_res => {
                    questionnaires = []
                    api_res.data.forEach(questionnaire => {
                        questionnaires.push({
                            'mobility': api_res.data.mobility,
                            'selfcare': api_res.data.selfCare,
                            'usualactivities': api_res.data.usualActivities,
                            'paindiscomfort': api_res.data.painOrDiscomfort,
                            'anxietydepression': api_res.data.anxietyDepression,
                            'todaysHealth': api_res.data.todaysHealth,
                            'datetime': api_res.data.date
                        })
                    })
                    res.json(questionnaires)
                })
                .catch(function (error) {
                    res.status(error.response.status).send(error.response.data)
                });
        })
        .catch(function (error) {
            res.status(error.response.status).send(error.response.data)
        });
})


const port = 80;
app.listen(port, () => console.log('Server running...'));
