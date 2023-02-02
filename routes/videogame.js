"use strict";
const express = require('express');
const router = express.Router();

const Videogame = require('../models/videogame');
const games = require('../API/games.json');

/* GET users listing. */
router.get('/', async(request, response) => {
    let date = parseInt((Date.now() / 1000).toFixed(0))
    console.log(date);
    const bestGames = await Videogame.find({rating: {$gt:88}, first_release_date : {$gt: 1640991600}, aggregated_rating_count: {$gt: 8}}).sort({first_release_date : -1}).limit(4);
    const topGames = await Videogame.find({rating: {$gt:80}, first_release_date : {$gt: 1640991600}, aggregated_rating_count: {$gt: 8}}).sort({first_release_date : -1}).limit(15);
    const shooterGames = await Videogame.find({genres: "Shooter", first_release_date : {$lt: date}, category : 0}).sort({first_release_date : -1}).limit(15);
    const adventureGames = await Videogame.find({genres: "Adventure", first_release_date : {$lt: date}, category : 0}).sort({first_release_date : -1}).limit(15);
    response.render("main", {"bestGames" : bestGames, "topGames": topGames, "shooterGames": shooterGames, "adventureGames": adventureGames});
});


module.exports = router;
