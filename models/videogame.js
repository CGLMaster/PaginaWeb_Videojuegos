"use strict";
const { Double } = require('mongodb');
const mongoose = require('mongoose');
const videogameScheme = new mongoose.Schema(
    {   

        first_release_date:{
            type: Number,
        },
        genres:{
            type: [String]
        },
        involved_companies:{
            type: [String]
        },
        name:{
            type: String,
        },
        platforms:{
            type: [String]
        },
        screenshots:{
            type: [String]
        },
        summary:{
            type: String
        },
        image:{
            type: String,
        },
        cover:{
            type: String,
        },
        rating:{
            type: Number,
        },
        aggregated_rating:{
            type: Number,
        },
        aggregated_rating_count:{
            type: Number,
        }

    }
)

module.exports = mongoose.model('videogame', videogameScheme);