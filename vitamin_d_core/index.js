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

app.get('/user/', (req, res) => {
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
                        'length': api_res.data.userdata.lichaamslengte.lengteWaarde,
                        'position': api_res.data.userdata.lichaamslengte.positie,
                        'lengthdatetime': api_res.data.userdata.lichaamslengte.lengteDatum['$date'],
                        'weight': api_res.data.userdata.lichaamsgewicht.gewichtWaarde,
                        'dressed': api_res.data.userdata.lichaamsgewicht.kleding,
                        'weightdatetime': api_res.data.userdata.lichaamsgewicht.gewichtDatum['$date'],
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

app.post('/user/', (req, res, next) => {
    // Register new user
    post_data = {
        'geslacht': req.body.gender,
        'voornaam': req.body.firstname,
        'achternaam': req.body.lastname,
        'username': req.body.username,
        'password': req.body.password,
        'geboortedatum': req.body.birthdate,
        'lengte': req.body.length,
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

app.post('/login/', (req, res) => {
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

app.post('/schedule/', (req, res) => {
    // create schedule
    session_code = req.cookies.session_code
    axios.post('http://resource_auth/auth', {'session_code': session_code})
        .then(auth_res => {
            post_data = {
                'username': auth_res.data.username,
                'date': req.body.date,
                'distance': Number(req.body.distance),
                'type': req.body.type,
            }
            axios.post('http://resource_schedule/schedule', post_data)
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
});

app.get('/schedule/', (req, res) => {
    // get schedule data
    session_code = req.cookies.session_code
    axios.post('http://resource_auth/auth', {'session_code': session_code})
        .then(auth_res => {
            axios.get('http://resource_schedule/schedule/' + auth_res.data.username)
                .then(api_res => {
                    schedules = []
                    api_res.data.forEach(schedule => {
                        schedules.push({
                            'date': schedule.date['$date'],
                            'distance': schedule.distance,
                            'type': schedule.activity_type,
                        })
                    })
                    res.json(schedules)
                })
                .catch(function (error) {
                    res.status(error.response.status).send(error.response.data)
                });
        })
        .catch(function (error) {
            res.status(error.response.status).send(error.response.data)
        });
});

app.get('/activity/', (req, res) => {
    // get activity data
    session_code = req.cookies.session_code
    axios.post('http://resource_auth/auth', {'session_code': session_code})
        .then(auth_res => {
            axios.get('http://resource_activity/activity/' + auth_res.data.username)
                .then(api_res => {
                    activities = []
                    api_res.data.forEach(activity => {
                        activities.push({
                            'date': activity.date,
                            'distance': activity.distance,
                            'type': activity.activity_type,
                        })
                    })
                    res.json(activities)
                })
                .catch(function (error) {
                    console.log(error)
                    res.status(error.response.status).send(error.response.data)
                });
        })
        .catch(function (error) {
            res.status(error.response.status).send(error.response.data)
        });
});

app.post('/questionnaire/', (req, res) => {
    session_code = req.cookies.session_code
    axios.post('http://resource_auth/auth', {'session_code': session_code})
        .then(auth_res => {
            post_data = {
                'username': auth_res.data.username,
                'mobility': Number(req.body.mobility),
                'selfcare': Number(req.body.selfcare),
                'usualactivities': Number(req.body.usualactivities),
                'paindiscomfort': Number(req.body.usualactivities),
                'anxietydepression': Number(req.body.anxietydepression),
                'todayshealth': Number(req.body.todayshealth),
            }
            axios.post('http://resource_questionnaire/answer', post_data)
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

app.get('/questionnaire/', (req, res) => {
    session_code = req.cookies.session_code
    axios.post('http://resource_auth/auth', {'session_code': session_code})
        .then(auth_res => {
            axios.get('http://resource_questionnaire/questionnaires/' + auth_res.data.username)
                .then(api_res => {
                    questionnaires = []
                    api_res.data.forEach(questionnaire => {
                        questionnaires.push({
                            'mobility': questionnaire.mobility,
                            'selfcare': questionnaire.selfCare,
                            'usualactivities': questionnaire.usualActivities,
                            'paindiscomfort': questionnaire.painOrDiscomfort,
                            'anxietydepression': questionnaire.anxietyDepression,
                            'todayshealth': questionnaire.todaysHealth,
                            'datetime': questionnaire.date
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
