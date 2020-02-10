## Info 

### Structure: 
	- Challenge.md: What is given to the players 
	- Solution.md: The solution for the challenge 
	- decode.py: The unzip script 
	- encode2.py: The zip script 
	- m_zip.py: The CLI for the implementation 
	- flag_server.py: Takes a user chosen m_zip and submits it to a given IP: 
		- Usage: ``python flag_server.py``
	- send_zip.sh: How to send a zip file. 
		- Usage: ./send_zip.sh <IP> <ZIP_FILE>
	- test_folder: A folder that has been used for testing the m_zip functions. 
	

### Notes 
- This will only work with python2 because of the print statements 
- This is a directory traversal challenge. I expect this to be difficult as a fair amount of reverse engineering the format is required. Additionally, once the format is understood, the students still need to find the vuln. 