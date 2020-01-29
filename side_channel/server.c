// Modifed from https://www.geeksforgeeks.org/tcp-server-client-implementation-in-c/
// gcc server.c -o server
#include <netdb.h> 
#include <stdio.h>
#include <netinet/in.h> 
#include <stdlib.h> 
#include <string.h> 
#include <sys/socket.h> 
#include <sys/types.h> 
#define MAX 80 
#define SA struct sockaddr 

// Really ensures that the values are the same. 
int sure_equals(char ch, char ch2){
	
	// Ensures that the values really equal each other! 
	for (int iteration = 0; iteration < 15000000; iteration++){
		
		// Compares the two inputted characters
		if(atoi(&ch) != atoi(&ch2)){
			return 0; 
		}
	}
	
	printf("Finish for char: %c \n", ch);
	return 1; 
}

// Does the user have the right password? 
int check_auth(char *attempt, char *password){
	
	// Check the length to match.
	if(strlen(attempt) != 8){
		printf("Not enough characters...\n");
		return 0; 
	}
	
	// Iterates over each character in the array.
	for (int index = 0; index < 8; index ++){
		int result = sure_equals(password[index], attempt[index]);
		
		// If the attempt is wrong, then exit. 
		// This is fast to return earlier! :)
		if(result == 0){
			return 0; 
		}
	}
	return 1;
	
}

// Function designed for chat between client and server. 
void login_wrapper(int sockfd) 
{ 
	
    char password[MAX]; 
    int n; 
	
	// Clear the memory 
	bzero(password, MAX);
	
	// Read the password from the client 
    read(sockfd, password, sizeof(password)); 	

	// The flag! 
	char *pin = "XXXXXXXX";
	int answer = check_auth(password, pin);
	
	// Send flag or not the flag. 
	char* flag; 
	if(answer == 1){
		flag = "Correct";
	}
	else{
		flag = "Invalid"; 
	}
	write(sockfd, flag, sizeof(flag)); 
	return;
} 
  
//\\\//\\\ Ignore this! //\\//\\//
int main(int argc, char* argv[] ) 
{ 
	// 1st parameter should be the port...
	int PORT = atoi(argv[1]);
    int sockfd, connfd, len; 
    struct sockaddr_in servaddr, cli; 
  
    // socket create and verification 
    sockfd = socket(AF_INET, SOCK_STREAM, 0); 
    if (sockfd == -1) { 
        printf("socket creation failed...\n"); 
        exit(0); 
    } 
    else
        printf("Socket successfully created..\n"); 
	
    bzero(&servaddr, sizeof(servaddr)); 
  
    // assign IP, PORT 
    servaddr.sin_family = AF_INET; 
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY); 
    servaddr.sin_port = htons(PORT); 
  
    // Binding newly created socket to given IP and verification 
    if ((bind(sockfd, (SA*)&servaddr, sizeof(servaddr))) != 0) { 
        printf("socket bind failed...\n"); 
        exit(0); 
    } 
    else
        printf("Socket successfully binded on port %d\n",  PORT); 
  
    // Now server is ready to listen and verification 
    if ((listen(sockfd, 5)) != 0) { 
        printf("Listen failed...\n"); 
        exit(0); 
    } 
    else
        printf("Server listening..\n"); 
		len = sizeof(cli); 
  
	while(1){
		// Accept the data packet from client and verification 
		connfd = accept(sockfd, (SA*)&cli, &len); 
		if (connfd < 0) { 
			printf("server acccept failed...\n"); 
			exit(0); 
		} 
		else
			printf("server acccept the client...\n"); 
	  
		// Function for chatting between client and server 
		login_wrapper(connfd); 
	  
		// After chatting close the socket 
		
		}
	
	close(sockfd); 
} 