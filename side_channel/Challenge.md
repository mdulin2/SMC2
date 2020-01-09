## Challenge 

NSA: You've been given the challenge of logging into this unauthorized system; we have taken care of the username for you. Now, it is your job to find the password by WHATEVER means necessary.

How to use: 
- Compile the client file with gcc client.c -o client on gcc 7! Older versions of gcc will not work...
- The passcode is the flag for this challenge. 
- This challenge is quite finky... Each team should have their own ports to connect to on the server. Only use the ports that you are assigned for the team. Only a single connection can be on the server at a time. 
- ./client IP PORT PASSCODE
	- i.e: ./client 127.0.0.1 8080 987654321

- Hint: https://linux.die.net/man/2/time
- Hint: The passcode has 8 characters 
- Hint: Can you spot the difference between the passcodes 987654321 and 19999999?

Given: client.c 
Given server.c with the passcode removed. 
