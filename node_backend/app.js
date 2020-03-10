const express = require("express");
const bodyParser = require("body-parser");


const app = express();
const PORT = process.env.PORT || 80;

//logging 
app.use(function(req, res, next){
    console.log(req.ip , req.path);
    next();
  });
  
app.use(bodyParser.urlencoded({extended: true}));


//test route
app.get('/test', function(req, res){
    console.log("test get route");
    res.send("test get route");
});

app.listen(PORT);

console.log("Starting server on: "+PORT);