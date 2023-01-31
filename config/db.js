"use strict";
const mongoose = require('mongoose');

const URLMONGO = "mongodb://localhost:27017/Videojuegos";

module.exports =  () => {
    const connect = function() {
        mongoose.connect(URLMONGO, function(err, db){
            var cursor = db.collection('Videojuegos').find({name:'Injustice: Gods Among Us'});
            console.log(db.collection('Videojuegos'));
            cursor.forEach(function(err, doc){
                if(doc !== null) console.log(doc);
                else db.end();
            })
        });
    }

    connect();
};