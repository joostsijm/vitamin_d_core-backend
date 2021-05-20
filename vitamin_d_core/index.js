const express = require('express');
const axios = require('axios');

const app = express();

app.set('view engine', 'ejs');

app.use(express.urlencoded({ extended: false }));

// Connect to MongoDB
app.get('/', (request, response) => {

    // Optionally the request above could also be done as
    axios.get('http://resource_user/user')
        .then(function (response) {
            response.render('index')
            console.log('response')
            // console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        })
        .then(function () {
            // always executed
        });

});

const port = 80;
app.listen(port, () => console.log('Server running...'));
