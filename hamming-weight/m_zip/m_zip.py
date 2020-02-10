from encode2 import zip
from decode import unzip 
import sys 
	
# The main CLI for the zip and unzip.
def main(): 

	if(len(sys.argv) < 3): 
		print "Usage: python m_zip zip|unzip <zip_file_name> <files_or_folders_to_zip>"
		
	# Zipping 
	if(sys.argv[1] == 'zip'): 
		print "Zipping..." 
		print "Zipping to", sys.argv[2]
		
		# Main zip encoding call 
		# This takes in the zips file name and all of the files/folders to zip in
		zip(sys.argv[3:], sys.argv[2])
		print "Finished zipping..."
		
	# Unzipping
	elif(sys.argv[1] == 'unzip'): 
			
		print "Unzipping..." 
		print "Unzipping ", sys.argv[2]
		# This takes in the zip files file name and the output location of the zip files content 
		print unzip(sys.argv[2], sys.argv[3]) 
		print "Finish unzipping to", sys.argv[2]
	else: 
		print "Usage: python m_zip zip|unzip <zip_file_name> <files_or_folders_to_zip>"
	
	
main() 