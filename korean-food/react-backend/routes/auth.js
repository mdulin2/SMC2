var mysql = require("mysql");

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

module.exports = {
	createSession: async function (username, session) {
	  var database = new Database();

	  // The MySQL.escape is used to prevent SQL Injections
	  // Add the session
	  const query =
		"INSERT INTO Sessions(username,session) VALUES(" + mysql.escape(username) +"," + mysql.escape(session) + ");";
	  var rows = await database.query(query);
	  database.close();
	  return session;
	},
	
	checkSession: async function (session) {
		var database = new Database();	
		const queryCheck = "SELECT * FROM Sessions WHERE session = " + mysql.escape(session);
		
		var rows = await database.query(queryCheck);
		if(rows.length === 0){
			return false; 
		}
		else {
			return {'username': rows[0].username, 'session': rows[0].session}
		}
	}

}