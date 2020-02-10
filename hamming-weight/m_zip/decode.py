import os

'''
Gets the huffman table from the file.

Parameters: 
	- filename: The huffman table 
- Returns: 
	- A huffman table within a dictionary
Returns a dictionary of letter to bits mapping
'''
def import_key(filename):
    huffman_table = {}
    file_content = open(filename, "r")
    for line in file_content.readlines():
        line = line.strip("\n")
        line = line.split(" ")
        if(line[0] == '\\n'):
            line = ['\n', line[1]]
        elif(line[0] == '\s'):
            line = [' ', line[1]]
        elif(line[0] == '\\t'):
            line = ['\t', line[1]]
        huffman_table[line[1]] = line[0]

    return huffman_table

''' 
Gets the content (meat) of the files from the .content file or the .hiearchy.key file

Parameters: 	
	- The content file name 
Returns: 
	- A list of lists where index 0 is the number of the file and index 1 is the compressed content.
'''
def import_file(filename): 

	imported_content = []
	full_file_content = open(filename, "r").read().split("\n") 
	for line in full_file_content:
		line = line.split(' ') 
		if(len(line) != 2): 
			continue
		
		num = line[0]
		file_content = line[1]
		
		imported_content.append(file_content)
		
	return imported_content
	
# Helper function for import key
# Gets next character found in the binit stream.
def get_substring(string, encode_dict):
    substring = ""
    for i in range(len(string)):
        substring += string[i]
        if(substring in encode_dict):
            return substring, i

# For decoding the huffman encoding
# encode_dict is the huffman table, compressed_text is the string of 1s and 0s.
def decode(encode_dict, compressed_text):

    message = ""
    while compressed_text != "":
        substring, amount = get_substring(compressed_text, encode_dict)
        message += encode_dict[substring] 
        #message += encode_dict.keys()[encode_dict.values().index(substring)]
        compressed_text = compressed_text[amount+1:]
    return message

'''
Iterates over all of the files in order to create a uncompressed version of the structure

Parameters: 
	- filename: The m_zipped file 
	- final_location: The location to write the zip file to
Returns: 
	- Nothing 
'''
def unzip(filename, final_location): 

	bit_dict = import_key(filename + "/" + ".huffman.key")
	file_content = import_file(filename + "/" + ".content")

	hiearchy = import_file(filename + "/" + ".hiearchy.key") 
	
	'''
	tmp_folders = []
	for index in range(len(dict.fromkeys(hiearchy))):
		tmp_folders.append(hiearchy[index])
		
	tmp_folders.sort(key = lambda x: len(x.split('/')))
	hiearchy = tmp_folders
	'''
	
	# First thing we do is create the folders (if they do not exist
	if(not os.path.isdir(final_location)):
		os.mkdir(final_location) 
	
	print hiearchy
	for index in range(len(file_content)):
		
		# Validates that the type in the content file is a directory
		if(file_content[index] != 'D'): 
			continue
			
		# Removes the zip prefix on the folder with string black magic
		folder = "/".join(hiearchy[index].split('/')[1:])
		
		write_location = final_location + '/' + folder
		
		if(not os.path.isdir(write_location)):
			os.mkdir(write_location) 
	
	# Create the files in the correct directories
	for index in range(len(file_content)): 

		# Validates that the type in the content file is NOT a directory
		if(file_content[index] == 'D'): 
			continue
		
		file_name = "/".join(hiearchy[index].split('/')[1:])
		write_location = final_location + '/' + file_name
		print "Decoding file ", write_location
		create_decoded_file(bit_dict, write_location, file_content[index])

'''
Decodes the compressed file 
'''
def create_decoded_file(bit_dict, file_name, content): 
	uncompressed_output = decode(bit_dict, content) 
	
	f = open(file_name , "w")
	f.write(uncompressed_output) 
	f.close() 
	
def main(): 
	filename = 'max.zip'
	bit_dict = import_key(filename + "/" + ".huffman.key")
	file_content = import_file(filename + "/" + ".content")
	hiearchy_content = import_file(filename + "/" + ".hiearchy.key") 
    
	tmp_folders = list(dict.fromkeys(folders))
	tmp_folders.sort(key = lambda x: len(x.split('/')))
	hiearchy_content = tmp_folders
	
	print hiearchy_content
	
	unzip(bit_dict, hiearchy_content, file_content, "final_folder")

#main() 



