const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const uuid = require('uuid');

const ActivitySchema = new Schema({
    _id: {
        type: String,
        default: uuid.v1
    },
    datetime: {
        type: Date,
        required: true
    },
    distance: {
        type: Number,
        required: true
    },
    success: {
        type: Boolean,
    }
});

module.exports = Activity = mongoose.model('Activity', ActivitySchema);
