const express = require('express');
const path = require('path');
const body_parser = require('body-parser');
const db = require('./config/db');
const morgan = require('morgan');
const multer = require('multer');

const app = express();
require('./database');

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(express.json());
app.use(body_parser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

//Middlewares
app.use(morgan('dev'));
const storage = multer.diskStorage({
  destination: path.join(__dirname, 'public/images'),
  filename(resquest, file, cb){
    cb(null, new Date().getTime() + file.originalname);
  }
});
app.use(multer({storage}).single());

//Routes
app.use(require('./routes/videogame'));


// Arrancar el servidor
app.listen(3000, function (err) {
  if (err) {
    console.log("ERROR al iniciar el servidor");
  }
  else {
    console.log(`Servidor arrancado en el puerto 3000`);
  }
});

