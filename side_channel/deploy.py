# The deploy function 
import os 

amount = 20
starting_port = 8080
for i in range(10): 
	os.system("./server" + " " + str(starting_port + i) + "&")
