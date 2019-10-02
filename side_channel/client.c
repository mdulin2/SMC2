// Modifed from https://www.geeksforgeeks.org/tcp-server-client-implementation-in-c/ 
// gcc client.c -o client 
#include <netdb.h> 
#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <sys/socket.h> 
#define MAX 80 
#define SA struct sockaddr 


void send_data(int sockfd, char *password) 
{ 
    char buff[MAX]; 
    int n; 
	
	bzero(buff, sizeof(buff)); 
	
	//send to the user
	write(sockfd, password, sizeof(password));
	
	// Receieve the result from the server 
	read(sockfd, buff, sizeof(buff));
	printf("Result: %s\n", buff);
	
} 
  
//\\\//\\\ Ignore this! //\\//\\//
int setup_sock(char* IP, int PORT){
    int sockfd, connfd; 
    struct sockaddr_in servaddr, cli; 
  
    // socket create and varification 
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
    servaddr.sin_addr.s_addr = inet_addr(IP); 
    servaddr.sin_port = htons(PORT); 
  
    // connect the client socket to server socket 
    if (connect(sockfd, (SA*)&servaddr, sizeof(servaddr)) != 0) { 
        printf("connection with the server failed...\n"); 
        exit(0); 
    } 
    else
        printf("connected to the server..\n"); 
  
    // function for chat 
    return sockfd; 	
}

//\\\//\\\ Ignore this! //\\//\\//
int main(int argc, char* argv[] ) 
{ 
	// Parameter 1: IP address 
	// Parameter 2: PORT number 
	// Parameter 3: Passcode attempt
	int sockfd = setup_sock(argv[1], atoi(argv[2]));
	
	send_data(sockfd, argv[3]); 
    // close the socket 
    close(sockfd); 
} 