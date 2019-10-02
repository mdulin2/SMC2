'''
This is a working solution for the side channel challenge :)
The solution does not take into consideration solving two numbers at the same time (which is possible) or the case of 0. However, the solution works :)
'''
import os
import time

# Calls the client from the CLI. 
# Returns the time taken. 
def run(password):
	start = time.time()
	os.system("./client " + password)
	end = time.time()
	time_taken = end - start
	return time_taken

# Forces a single number. 
def solve_single(loc, current_code, total_time):
	passcode = current_code 
	
	for i in range(10):
		print passcode
		time_taken = run(passcode) 
		# If the time taken on the request is greater than 0.4 seconds, then this was a leak on the passcode. 
		if(total_time + 0.6 <  time_taken):
			print "Found char at index " + str(loc) + " : " + str(i)
			return i, time_taken
			
		passcode = list(passcode) 
		passcode[loc] = str(i+1)
		passcode = "".join(passcode)
		
	return "failed..."
	
# Forces the entire passcode
def solve():

	# 8 characters in the flag. 
	passcode = "00000000" 
	
	# Get a default runtime, with the first character being wrong. 
	total_time = run(passcode)
	for i in range(8):
		char, total_time = solve_single(i,passcode, total_time)
		passcode = list(passcode) 
		passcode[i] = str(char)
		passcode = "".join(passcode)		
	
	# This is the flag!
	print "Final passcode is...", passcode

#solve_single(7,"12348210",7)
solve()
	