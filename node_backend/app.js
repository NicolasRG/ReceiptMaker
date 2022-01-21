const express = require("express");
const bodyParser = require("body-parser");
const fileSystem = require("fs");
const path = require("path");
const cors = require("cors");
const spawn = require("child_process").spawn;


const app = express();
const PORT = process.env.PORT || 80;
const corsOptions = {
  origin: 'http://localhost:8080',
  optionsSuccessStatus: 200 // some legacy browsers (IE11, various SmartTVs) choke on 204
}
app.options('*', cors());

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*"); // update to match the domain you will make the request from
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});


//logging 
app.use(function(req, res, next){
    console.log(req.ip , req.path, req.body);
    next();
  });
  
app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true })); //


//spawn python scripts process
app.post('/spawnPython', function(req, res){
  console.log("Spawning script");
  console.log(req.body.items);
  /*const json = JSON.stringify([
  {"Item":"Carrot",
   "Price": "23.00",
   "Quantity": "1"}, 
  {"Item":"Potato",
  "Price": "2.00",
  "Quantity": "2"}]);*/
  
  const scriptPath = path.join(__dirname, '../Backend(temp)/callable.py'); 
  const process = spawn('python', [
          scriptPath,
          req.body.items]);

  process.stdout.on('data', function(data){

    console.log("done");
    /* return local pdf*/
    const filePath = path.join(__dirname, 'Tet.pdf');
    console.log(filePath);
    const stat =  fileSystem.statSync(filePath);

    res.writeHead(200, {
      'Content-Type': 'application/pdf',
      'Content-Length' : stat.size
    });
    
    const readStream = fileSystem.createReadStream(filePath);
    readStream.pipe(res);
  });

});

app.listen(PORT);

console.log("Starting server on: "+PORT);
