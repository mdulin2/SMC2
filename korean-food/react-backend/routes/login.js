// PORT=3001 node bin/www
// each file is its own route!
var express = require("express");
var router = express.Router();
var mysql = require("mysql");
var pbkdf2 = require('pbkdf2');
var rand = require('csprng');
const auth = require('./auth');

class Database {
  constructor(config) {
    this.connection = mysql.createConnection({
      host: "localhost",
      user: "root",
      password: "Airjordan23",
      database: "injection"
    });
  }
  query(sql, args) {
    return new Promise((resolve, reject) => {
      this.connection.query(sql, args, (err, rows) => {
        if (err) return reject(err);
        resolve(rows);
      });
    });
  }
  close() {
    return new Promise((resolve, reject) => {
      this.connection.end(err => {
        if (err) return reject(err);
        resolve();
      });
    });
  }
}

// returns a promise of a query
async function loginQuery(username, password) {
  const query =
    "SELECT * FROM Login WHERE username =" +
     mysql.escape(username) +
    " AND password = " +
     mysql.escape(password) +
    ";";

  var database = new Database();

  // Might want to send an error message here...
  var rows = await database.query(query);
  database.close();
  return rows;
}

// Login for the user. Will return either "" or a valid session ID.
async function login(username, password) {
  const query_info = await loginQuery(username, password);
  if (query_info.length === 0) {
    return "";
  } else {
	 
	const username = query_info[0].username; 
    return username;
  }
}

/* GET users listing. */
router.post("/", async function(req, res, next) {

  const username = req.body.username;
  const password = req.body.password;

  // Hashes the password, with a static salt value.
  const derivedKey = pbkdf2.pbkdf2Sync(password, 'somesalt...', 1, 32, 'sha512').toString('base64');
  const loginResponse = await login(username, derivedKey);
  
  if(loginResponse === ""){
     res.send(loginResponse);
  }
  else {
	const cookie = await auth.createSession(username,Buffer.from(username).toString('base64'));
	
	// console.log(await auth.checkSession(cookie));
	res.cookie('session', cookie);
	res.send(loginResponse);
  }
});

// API for checking if the user has access to a spefific page. 
router.post("/authorize", async function(req,res){
	const check = await auth.checkSession(req.cookies.session);

	if(check === false){
		res.status(403); 
		res.send(false);
	}else{
		res.status(200); 
		res.send(true);		
	}
	return; 
	
});

// API for logging out the user. 
router.post("/logout", async function(req,res){
	res.clearCookie('session'); 
	res.send({});
	return; 
});

module.exports = router;
