const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/Videojuegos', {
   useNewUrlParser: true
})
  .then(db => console.log("La base de datos ha sido conectada"))
  .catch(err => console.log("Se ha producido un error al conectarse a la BD"))

