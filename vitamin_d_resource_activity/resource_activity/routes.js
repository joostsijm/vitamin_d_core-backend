module.exports = function(app){

    const Activity = require('./models/Activity');

    app.post('/', (req, res) => {
        const activity = new Activity({ 
            datetime: req.body.datetime,
            distance: req.body.distance
        });
        activity.save()
            .then(activity => res.redirect('/'))
            .catch(err => res.status(400).json({ msg: 'Error saving' }));
    });

    app.get('/', (req, res) => {
        res.setHeader('Content-Type', 'application/json');
        // TODO only find future 
        Activity.find()
            .then(activities => res.end(
                JSON.stringify( activities )
            ))
            .catch(err => res.status(404).json({ msg: 'No results found' }));
    });

    app.get('/history', (req, res) => {
        res.setHeader('Content-Type', 'application/json');
        // TODO only find past 
        Activity.find()
            .then(activities => res.end(JSON.stringify( activities )))
            .catch(err => res.status(404).json({ msg: 'No activities found' }));
    });
}
