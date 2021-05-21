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

// Connect to MongoDB
app.get('/user', (request, response) => {
    // Optionally the request above could also be done as
    axios.get('http://resource_user/user')
        .then(function (api_response) {
            response.render('user', { api_response } )
        })
        .catch(function (error) {
            console.log(error);
        });
});

app.post('/user', (request, response) => {
    axios.post('http://resource_user/user', request.body)
        .then(response.redirect('/user'))
        .catch(function (error) {
            console.log(error);
        });
});

const port = 80;
app.listen(port, () => console.log('Server running...'));
