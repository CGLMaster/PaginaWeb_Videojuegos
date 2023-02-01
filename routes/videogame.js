"use strict";
const express = require('express');
const router = express.Router();

const Videogame = require('../models/videogame');
const games = require('../API/games.json');

/* GET users listing. */
router.get('/', async(request, response) => {
    const newGames = await Videogame.find({rating: {$gt:88}, first_release_date : {$gt: 1640991600}, aggregated_rating_count: {$gt: 8}}).sort({first_release_date : -1}).limit(4);
    const topGames = await Videogame.find({rating: {$gt:80}, first_release_date : {$gt: 1640991600}, aggregated_rating_count: {$gt: 8}}).sort({first_release_date : -1}).limit(15);
    response.render("main", {"newGames" : newGames, "topGames": topGames});
    //response.json(videogames);
});


module.exports = router;
