/*
compile: gcc xor.c -o xor
Encrypted String: %$1C2}~*Ve=;_{\_^:/
*/
#include <stdio.h> 
#include <string.h>
char key[] = "hAC1K5?NaTionHmmmmmm"; // 20 characters

// Takes in a string
// Best encryption ever! 
char* encrypt(char* input){
	static char enc[20];
	for(int index = 0; (index < strlen(input)) && (index < 20); index++){
		enc[index] = input[index] ^ key[index]; // xors the string 
		printf("Char: %d: %c : %c \n", enc[index], key[index], input[index]);
	}
	printf("Full Enc String: %s\n", enc);
	return enc; 
}

// Remove in final version
char* decrypt(char* output){
	static char dec[20];
	for(int index= 0; (index < strlen(output)) && (index < 20); index++){
		dec[index] = output[index] ^ key[index];
	}
	
	return dec; 
}

int main(int argc, char *argv[]) 
{    
	if(argc != 2){
		puts("Requires a string of input");
		return 0;
	}
	
	char* enc = encrypt(argv[1]);
	
	//char* dec = decrypt(enc); 
	
    //printf("Decrypted String: %s\n", dec);
    return 0; 
}


