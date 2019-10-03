# Info

## Setup for the challenge
- Setup a standard Linux OS. 
- Create a user with lower level priviliges than the admin.
- Insert the flag.txt file into the home directory of the new user. 
- As the admin user, add the setuid bit to the date and dd binaries. 
- Make sure that the admin user owns the flag.txt file. 
- Hack the planet :)

## Info 

- Privilege Escalation will always be a thing. From poorly written custom binaries to AWS configurations, these are major issues! For this challenge, there are two binaries that allow for the opening of a textfile, that should not be readable, by abusing the setuid bit. 