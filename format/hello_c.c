/*
Hey there, this is the second program after I wrote hello world!
This time, it just prints the users input! :) 
Compile: 
./
Call: 
./hello_c <user input>
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int main(int argc, char *argv[]){

	char str[100];
    FILE *fp; 
	
	// Read in the flag
    fp = fopen("flag.txt","r");
    while (fgets(str, 100, fp) != NULL);
   
	
	//printf("Hello World!\n"); 
	// Instead of printing hello world, we print your input!
	printf(argv[1]); 
	
	return 0; 
}