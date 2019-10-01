// PORT=3001 node bin/www
// each file is its own route!
var express = require("express");
var router = express.Router();
var mysql = require("mysql");
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
        if (err) return resolve(err);
        resolve();
      });
    });
  }
}

// returns a promise of a query
async function foodQuery(food_name) {
  const query =
    "SELECT * FROM korean_food WHERE food_name LIKE '%" + food_name + "%';";

  var database = new Database();

  // Might want to send an error message here...
  var rows = await database.query(query);
  console.log("Rows:", rows);
  database.close();
  return rows;
}

/* GET foods listing. */
router.post("/", async function(req, res, next) {
	// Auth: 
	const authenticated = await auth.checkSession(req.cookies.session);
	if(authenticated === false){
		res.status(400); 
		res.send({});
		return; 
	} 

	// Do not want to empty search. Just return blank array.
	// If there's a malicious search, just send back an empty array.
	// If admin user, then return the flag...
	const food_name = req.body.food_name;
	if(food_name === '' || food_name.includes("'") || food_name.includes("\\") || food_name.includes('--')){
		res.send([{}]);
		return;
	}

	const foodResponse = await foodQuery(food_name);
	
	// Adds the flag if this is the admin user. 
	const flag = "flg{some_flag}"
	if(authenticated.username === 'admin'){
		const food_obj = {"food_id" : "-1", "food_name" : "FLAG!", "price" : "♾", "description" : flag }; 
		foodResponse.push(food_obj);
	}
	
	res.send(foodResponse);
});

module.exports = router;
