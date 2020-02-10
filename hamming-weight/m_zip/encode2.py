'''
Huffman Encoding, table creation and decoding file.
https://en.wikipedia.org/wiki/Huffman_coding
'''
import copy
import os 
import sys 

'''
global variables
'''
# The global variable for the bit_dict huffman encoding table 
bit_dict = {}

# The global variable for the folders information. For some reason, the way that I was doing recursion was breaking the other data structure. So, I made this a global variable. 
folders = []


'''
All of the files below are for huffman specific operations
'''
# Compresses the text based upon the huffman encoding.
def encode(text, encode_dict):
    compressed_text = ""
    for char in text:
        compressed_text += str(encode_dict[char])
    return compressed_text

# A helper function for creating the huffman algorithm tree.
# Combines the last two frequentcies into one.
def combine(freq, char_count):
    # assumes a sorted list
    length = len(freq)
    last_item = freq.pop()
    second_to_last = freq.pop()
    new_item = (char_count, last_item[1] + second_to_last[1])
    freq.append(new_item)
    return freq, last_item, second_to_last

# Creates the huffman tree.
def get_key(freq):
    tree = make_tree(sort(freq))
    return bit_dict

''' 
Create the tree to be traversed.
Parameters: 
	- freq:  a list with the setup [(a,b),(a,b)...,(a,b)] where a is the character and b is the frequentcy.
Returns: 
	- A complete huffman table
'''
def make_tree(freq):
    tree = {}
    tree_size = len(freq)
    for elt in freq:
        tree[elt[0]] = elt[1]
    for spot in range(tree_size -1):
        freq, last_item, second_to_last = combine(copy.deepcopy(freq), spot)
        freq = sort(freq)
        tree[spot] = (last_item[0], second_to_last[0])

    x =  traverse_tree(tree, spot)
    return traverse_tree(tree,spot)

''' 
The function for traversing the free.
Parameters: 
	- tree is the tree created in the make tree function.
	- root is the top of the tree.
Returns: 
	- A huffman table

'''
def traverse_tree(tree,root):
    bit_dict[root] = ''
    return traverse_tree_helper(tree, root)

''' 
Helper function for traverse tree.

Parameters: 
	- tree: A huffman tree 
	- spot: The current encoding in 0's and 1's. 
'''
def traverse_tree_helper(tree, spot):
    # Characters will always be the leafs points, while the assigned integers are always the inner nodes.
    if(type(tree[spot]) == float):
        return bit_dict
    else:
        bit_dict[tree[spot][0]] = bit_dict[spot] + '0'
        traverse_tree_helper(tree, tree[spot][0])
        bit_dict[tree[spot][1]] = bit_dict[spot] + '1'
        traverse_tree_helper(tree, tree[spot][1])

''' 
Removes the non-leaf 'numbers' from the key-value mappping.
Parameters: 
	- None (takes in bit_dict as global var) 

Returns: A bit_dict with all of the leafs removed 
'''
def strip_numbers():
    bit_dict_fixed = {}
    for elt in bit_dict:
        if(type(elt) != int):
            bit_dict_fixed[elt] = bit_dict[elt]
    return bit_dict_fixed

''' 
Sorts a list of the format [(a,b)...(a,b)] where it is sorted on b, the frequentcy.
Parameter: 
	- A list of tuples that represents a huffman tree
Returns: 
	- A sorted list of tuples
'''
def sort(inlist):
    for i in range(len(inlist)):
        changed = False
        for j, x in enumerate(inlist[:-i-1]):
            if x[1] <= inlist[j + 1][1]:
                inlist[j], inlist[j + 1] = inlist[j + 1], inlist[j]
                changed = True

        if not changed:
            break
    return inlist


''' 
All of the functions are for zipping the directory properly
'''


''' 
Creates a frequentcy calculation based upon each character in the file.

Parameters:
	- filename: The file being evaluated 
	- char_count: The previous frequency dictionary
Returns: 
	A dictionary of chars(key) : frequentcy(value), key value mapping.

'''
def eval_file(filename, char_count):
    total = 0
    file_content = open(filename, "r")
    for line in file_content.readlines():
        line += '\n'
        for char in line:
            total +=1
            if char in char_count:
                char_count[char] = char_count[char] +1
            else:
                char_count[char] = 1

    # calculates the percentage of the time a character occurs.
    for key in char_count:
        char_count[key] = char_count[key] / float(total)

    return char_count

''' 
Iterate over an entire directory structure to get the correct percentages for the encoding process. Helper function because of the recursion parameter that had to be added

Parameters: 
	- folder_name: The name of the folder 
	- char_count: The dictionary of all characters and their frequency
Returns:
	A dictory of character to likelihood ratio for a given folder

'''
def eval_folder_helper(folder_name, char_count): 
	# Iterate over an entire directory structure to encode everything 
	for (dir_path, dir_names, file_names) in os.walk(folder_name):
		# Recursively call this function in order to go through all directories. 
		for dir in dir_names: 
			char_count = eval_folder_helper(dir, char_count) 
		
		# Run the encoding scheme on each file in the directory 
		for file_name in file_names: 
			char_count = eval_file(dir_path + '/' +  file_name, char_count)
	return char_count
	
# Iterate over an entire directory structure to get the correct percentages for the encoding process
# Returns a dictory of character to likelihood ratio
def eval_folder(folder, char_count = {}): 
	return eval_folder_helper(folder, char_count) 
	
''' 
Decides whether the item in the list is a folder or a file. Depending on the type inserted, the file is either encoded or the directory is traversed. 
Parameters: 
	- A list of file and directory names 
	
Returns: 
	- A dictonary of characters with their corresponding likelihoods
'''
def eval_both(file_or_folder_name): 
		
	char_count = {}
	for element in file_or_folder_name:
		# For directories
		if(os.path.isdir(element)): 
			char_count = eval_folder(element, char_count)
		# A path for files
		else: 
			char_count = eval_file(element, char_count) 
	return char_count
	
# Convert the dictionary into a tree traversable object.
def dict_to_tuple_list(char_count):
    freq_list = []
    for key in char_count:
        freq_list.append((key, char_count[key]))
    return freq_list

''' 
Encodes a single file 
Parameters: 
	- file_name: The file that we are encoding 
	- bit_dict: The huffman encoding table 
	- write_location: The location where the file is being written to. 
'''
def encode_file(file_name, bit_dict, write_location): 
	
	# Get the files contents
	f = open(file_name, "r") 
	content = f.read() 
	f.close() 
	coded = encode(content,bit_dict) 
	
	# Write the file
	print "Compressed file", file_name
	return [coded,write_location]


''' 
Traverses through an entire directory and encodes all of the files. Used as a helper function for recursion
Parameters: 
	- folder_name: Location to be zipped 
	- final_location: The location being written to. 
	- bit_dict: The huffman table used for compression
	- loc_info: A list of a all files compressed
Returns: 
	- loc_info: A list of a all files compressed
'''
# Currently does not save empty folders information...
# Need to do that in order to make this attack more realistic
def encode_folder_helper(folder_name, final_location, loc_info, bit_dict): 
	
	# Iterate over an entire directory structure to encode everything 
	for (dir_path, dir_names, file_names) in os.walk(folder_name):
		# Recursively call this function in order to go through all directories. 
		for dir in dir_names:
			loc_info = loc_info + (encode_folder_helper(folder_name + '/' + dir, final_location + '/' + dir, loc_info, bit_dict))
			
			tmp_loc = final_location + '/' + dir 	
			
			# This is in order to get the directory hiearchy properly. 
			folders.append(tmp_loc) 
				
		# Run the encoding scheme on each file in the directory 
		for file_name in file_names: 
			loc_info = loc_info + encode_file(dir_path + '/' +  file_name, bit_dict, final_location + '/' + file_name)
		
		# os.walk goes down the entire directory hiearchy. However, we do not want this. So, we break here. 
		break 
	return loc_info
	
''' 
Traverses through an entire directory and encodes all of the files 
Parameters: 
	- folder_name: Location to be zipped 
	- final_location: The location being written to. 
	- bit_dict: The huffman table used for compression
Returns: 
	- file_info: A list of a all files compressed
'''
def encode_folder(folder_name, final_location, bit_dict):
	folders.append(final_location)
	return encode_folder_helper(folder_name, final_location, [], bit_dict) 
	
'''
Zips a given folder 
Parameters: 
	folder_name: The target to zip 
	final_location: The final location of the zip file 
	bit_dict: The huffman table used for encoding 
Returns: 
	Nothing
'''
def zip(file_or_folder_name, final_location): 

	# Create the huffman encoding 
	freq_list = dict_to_tuple_list(eval_both(file_or_folder_name))

	# Create the huffman table 
	encoding = get_key(freq_list)
	bit_dict = strip_numbers()
	
	file_info = []
	# Create the new folder to write to, if not already there.
	if(not os.path.isdir(final_location)):
		os.mkdir(final_location) 
		
	for element in file_or_folder_name:
		# For directories
		if(os.path.isdir(element)): 
			file_info = file_info + (encode_folder(element, final_location + '/' + element,bit_dict))
		# A path for files
		else: 
			file_info = file_info + encode_file(element, bit_dict, final_location + '/' + element)
		
	print "Adding compressed data to the '.content' file" 
	# Writes the content to a file 
	loc_info = write_to_file(final_location, file_info)
	
	print "Adding hiearchy information to the '.hiearchy.key' file" 
	# Writes the file hiearchy to a file 
	add_hiearchy_key(loc_info, final_location) 
	
	print "Outputting the huffman table to '.huffman.key'"
	# Writes the compression huffman table to a file
	output_huffman_table(bit_dict, final_location)
	
''' 
Outputs the huffman table that was used for compression to the directory in the .huffman.key file.
Parameters: 
	- bit_dict: The huffman encoding table 
	- write_location: The location for the huffman table to be written to. 
''' 
def output_huffman_table(bit_dict, write_location):
	f = open(write_location + "/.huffman.key" , "w+")
	for char_key in bit_dict:
		
		char_key_write = char_key
		# Special characters to not break the parsing
		if(char_key == '\n'): 
			char_key_write = "\\n"
		elif(char_key == '\t'):
			char_key_write = "\\t" 
		elif(char_key == ' '): 
			char_key_write = "\s" 
		
		f.write(char_key_write + ' ' + bit_dict[char_key] + '\n')
	f.close() 
	
	
''' 
Adds the hiearchy information in order for the unzip to work properly.
Parameters: 
	- loc_info: All of the files that were encoding 
	- final_location: The zip file being written to. 
Returns: 
	- This hiearchy information is return in the .hiearchy.key at the first level
'''
def add_hiearchy_key(loc_info, final_location): 
	# Turn the folders list into a unique list 
	# Now, need to organize these by amount of slashes in order to fix the decode function.
	tmp_folders = list(dict.fromkeys(folders))
	tmp_folders.sort(key = lambda x: len(x.split('/')))
	
	# Intergrate the folders information with the file information.
	loc_info = loc_info + tmp_folders
	
	f = open(final_location + "/.hiearchy.key" , "w+") 
	counter = 0
	for loc in loc_info:
		f.write(str(counter) + ' ' + loc + '\n') 
		counter += 1
	f.close() 

''' 
Outputs all of the file content into this one file. 
Each newline represents a new file. 
'''
def write_to_file(final_location,file_info): 
	f = open(final_location + "/.content" , "w+") 
	loc_info = []
	
	index = 0
	for index in range(0,len(file_info),2):
		content = file_info[index]
		name = file_info[index + 1]
		f.write(str(index/2) + ' ' + content + "\n") 
		loc_info.append(name) 
	
	# The folders have the content as a 'D'. This ensures that they get referred later in the decoding to the hiearchy file. 
	# Additionally, this gets sorted in order to make the directory creation process simplier. 
	tmp_folders = list(dict.fromkeys(folders))
	
	for folder in tmp_folders: 
		index += 2
		f.write(str(index/2) + ' ' + 'D' + "\n") 
	f.close() 
	
	return loc_info



