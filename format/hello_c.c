/* (UNUSED) 
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

// First part is the flag stuff... Just ignore this.	
	
	char str[80];
	char flag[100];
    FILE *fp; 
	
	// Read in the flag
    fp = fopen("flag.txt","r");
    while (fgets(flag, 100, fp) != NULL);
   
	
	strncpy(str,argv[1],80);
	str[80] = 0; // Null byte to end the string

	//printf("Hello World!\n"); 
	// Instead of printing hello world, we print your input!
	printf(str); 
	
	return 0; 
}
