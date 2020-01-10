#!/usr/bin/python

import os
import sys

print open(__file__,'r').read()

# Only allow a single alphabetic character
def find_characters(inp):
    count = 0
    for char in inp:
        if(char.isalpha()):
            count += 1 
    return count

def main():
    inp = raw_input('>>')
    sys.stdout.flush()  
    if(find_characters(inp) > 1):
        print("Too many characters!")

    # Execute the command
    else:
        os.system('bash -c \''+inp+'\'') 


main() 

