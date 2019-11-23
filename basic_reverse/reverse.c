/*
Compile: gcc reverse.c -o reverse -m32
Reversing problem! 
Given the binary, can you login as the user? 

This can be easily done by running `strings reverse`. Only three strings appear; one is the flag, one is the password! 
*/

#include <stdio.h>
#include <string.h>
int main (int argc, char* argv[]) {

    if(argc != 2){
        puts("Use ./reverse password");
        return 1;
    }
    int x = 1 + 2; 

    if(strncmp("potato_bacoN_hamburger", argv[1], 30) == 0){
        printf("flg{N1ce70bHAc5er}\n");
        return 0; 
    }
    
    puts("Good try :)");
    return 1;
}