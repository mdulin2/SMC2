# General 

Korean food is a react website with a node express.js backend. On the site, you can register a user, login and search for korean food dishes.  
The goal is to become the admin user on the site.  
## Organization
- Challenge.md: What is given to the contestants 
- Solution.md: How to solve the challenge 
- backend/: The backend for the application 
- client/: The frontend for the application 

## Using the application 

- This is a react application with a express backend. 
- First add the username, password and database name to all the express files are configuration. 
- Run auth.sql and koreanFood.sql to seed the database
- backend: 
	- Run 'npm install' to install all of the packages 
	- Run 'npm start' to run the backend 
- frontend: 
	- Run 'yarn' to install all of the packages
	- Run 'yarn start' to run the frontend 
	- The frontend has three routes: 
		- /login  - login as a user
		- /register  - create a user
		- /korenFood (while authenticated) - query korean food 
