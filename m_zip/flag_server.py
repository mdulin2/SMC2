import logging   
import os  
from decode import unzip # Unzip function
import glob
import shutil
from http.server import BaseHTTPRequestHandler, HTTPServer

class Server(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

	# The main request 
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  
		
        
		# Transferring the zip file 
        self.save_file(post_data)

		# unzip 
        self.unzip_local()
        # Check to see if a files exists in /flag location. If so, send back the actual flag...
        flag = self.check_flag()
        if(flag): 
            path = "::::FLAG:::: flg{manscape_mansaving}" 
        else: 
            path = "/" 

        self._set_response()
        self.wfile.write("POST request for {}".format(path).encode('utf-8'))
		
	# Saves all of the files sent via curl as the zip file. 
    def save_file(self, content):
        zip_file = "transfer.zip"
		
        # Create target Directory if do not exist.
        if not os.path.exists(zip_file):
            os.mkdir(zip_file) 
		
        if not os.path.exists("/flag"):
            os.mkdir("/flag") 
			
		# Parse content from the content file 
        content_file = content.split('Content-Disposition: form-data; name="file"; filename=".content"')[1]
        content_file = content_file.split('----------')[0]
        content_file = "\n".join(content_file.split('\n')[3:])		
        f = open(zip_file + '/' + '.content', "w") 
        f.write(content_file) 
        f.close() 
		
		# Parse content for the huffman file
        huffman_file = content.split('Content-Disposition: form-data; name="file"; filename=".huffman.key"')[1]
        huffman_file = huffman_file.split('----------')[0]
        huffman_file = "\n".join(huffman_file.split('\n')[3:-2])
        f = open(zip_file + '/' + '.huffman.key', "w") 
        f.write(huffman_file) 
        f.close()        
		
		# Parse and save the content the hiearchy file 
        hiearchy_file = content.split('Content-Disposition: form-data; name="file"; filename=".hiearchy.key"')[1]
        hiearchy_file = hiearchy_file.split('----------')[0]
        hiearchy_file = "\n".join(hiearchy_file.split('\n')[3:])
        f = open(zip_file + '/' + '.hiearchy.key', "w") 
        f.write(hiearchy_file) 
        f.close() 
	
    # Unzip the gotten file into the directory here2
    def unzip_local(self): 
        unzip("transfer.zip", "here2") 
		
	# See if there is a file in the hidden /flag location :) 
    def check_flag(self): 
        if(len(os.listdir("/flag")) > 0): 
			# The file exists
			flag = True 
        else: 
            flag = False 
			
		# Cleans this up for the next user to call this to use. 
        remove_dir = "/flag/*"
        to_remove = glob.glob(remove_dir) 
        for item in to_remove:

            # Directory
            if(os.path.isdir(item)):
                shutil.rmtree(item)
            # File 
            else: 
                os.remove(item)
		
        return flag 
		
def run(server_class=HTTPServer, handler_class=Server, port=8082):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    from sys import argv
    run() 
	
# How to send a file 
# Need to just do this automatically...
''' 
curl -X POST 127.0.0.1:8082 -F 'file=@test.zip/.content' -F 'file=@test.zip/.huffman.key' -F 'file=@test.zip/.hiearchy.key'
'''