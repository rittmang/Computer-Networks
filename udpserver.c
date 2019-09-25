#include<stdio.h>
#include<unistd.h>
#include <netdb.h> 
#include <netinet/in.h> 
#include <stdlib.h> 
#include <string.h> 
#include <sys/socket.h> 
#include <sys/types.h> 
#include<string.h>
#define MAX 1000 
#define PORT 5000 

int main()
{
    char buffer[100];
    char* msg="Hello";
    int listenfd=socket(AF_INET, SOCK_DGRAM,0);
    int len;
    struct sockaddr_in servaddr, cliaddr;
    bzero(&servaddr,sizeof(servaddr));
    listenfd = socket(AF_INET,SOCK_DGRAM,0);
    servaddr.sin_addr.s_addr=htonl(INADDR_ANY);
    servaddr.sin_port=htons(PORT); 
    servaddr.sin_family = AF_INET;  
   
    // bind server address to socket descriptor 
    bind(listenfd, (struct sockaddr*)&servaddr, sizeof(servaddr)); 
       
    //receive the datagram 
    len = sizeof(cliaddr); 
    int n = recvfrom(listenfd, buffer, sizeof(buffer), 0, (struct sockaddr*)&cliaddr,&len); //receive msg from server 
    buffer[n] = '\0';
     
    //puts(strupr(buffer));
    for(int i=0;i<n;i++)
    {
        buffer[i]=toupper(buffer[i]);
    }
    puts(buffer); 
           
    // send the response 
    sendto(listenfd, msg, MAX, 0,(struct sockaddr*)&cliaddr, sizeof(cliaddr)); 
 
} 

