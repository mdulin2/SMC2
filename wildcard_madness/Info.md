## Wildcard Maddness 

- Originally this challenge was written with just the Python file and the flag. However, setuid does not work on scripting langauges. 
- Because of this (and not wanting to write a web server) the `startup.sh` will deploy the service by using socat, which will execute with the proper permissions. 

### Files 
- startup.sh: Deploy the service 
- connect.sh: Connect to the service 
- one_char.py: The python script that executes the bash code 
- Challenge.md: The challenge given to the student 
- Solution.md: The solutions for the challenge. 
- flag.txt: The file trying to be printed