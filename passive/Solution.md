## Solution
- The file is a pcap file, which records network traffic. The easiest way to view this file is with Wireshark. 
- The easy way to find the correct traffic is to sort by protocol. The type of traffic being sent to a website is going to HTTP traffic. 
- By clicking at the 6 HTTP requests, it is found that the /login.cgi (request no 34). There are several form items in this request, where the form item is 'login_authorization'. This form value is YWRtaW46MTIzNDU=, or admin: 12345.
- The flag is : YWRtaW46MTIzNDU=