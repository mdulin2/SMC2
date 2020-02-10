#!/bin/bash 

curl -X POST $1 -F "file=@$2/.content" -F "file=@$2/.huffman.key" -F "file=@$2/.hiearchy.key"
