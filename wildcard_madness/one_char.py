'''
This challenge is meant to abuse wildcard characters(literal:"*[]?") 
A solution is `python one_char.py "/???/c?? ./????.???"`
But, there are many, many ways to solve this challenge.

Only a single alphabetic character can be used character is allowed in this use case. 
'''

import os
import sys

def find_characters(inp):
    count = 0
    for char in inp:
        if(char.isalpha()):
            count += 1 
    return count 

if(find_characters(sys.argv[1]) > 1):
    print("Too many characters!")

else:
    os.system(sys.argv[1]) 


