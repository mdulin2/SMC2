/*
gcc -mpreferred-stack-boundary=2 -m32 -ggdb -g -fno-stack-protector auth.c -o auth

Ensure that ASLR is turned off too.
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int validate_serial(){
    printf("Enter a serial number: \n");
    char serial[32];
    fscanf( stdin, "%s", serial);
    return 0;
}

//how to get to this point if validate_serial always returns false?
int do_valid_stuff(){
    printf("Flag!\n");
}

int main( int argc, char *argv[]){
    if(validate_serial()){
        do_valid_stuff();
    }
    else{
        printf("Invalid serial number!\n");
    }
}