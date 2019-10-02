## Organization 
- Challenge.md: The challenge info for the player 
- Solution.md: The solution for the challenge, as well as the theory behind it. 
- Solve.py: A solution to the challenge that was written. 
- client.c: The client that the user can use to interact with the server. 
- server.c: The server that makes the passcode attempts 
- deploy.py: A script to deploy multiple servers on the bigger server. 

## Deployment 
- Only a single connection can be made at a time. So, the client and server have a dynamic IP address and port that can be used. 
- To deploy this, use a script to deploy the server to something like 20 ports. 
- To take it down: Run 'pkill -9 server'. This will kill all instances of the server process. 