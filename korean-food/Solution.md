# Solution 
The goal of the challenge is to become the administrative user on the site. There are two ways to go about this: 
- Poor session cookies (medium)
- UTF8 character truncation (very hard)

## Poor Session Cookies 
- Web browsers are sessionless by design. However, by using cookies as the state for a user, we have circumvented on the modern web. All that stands in the way between two users is their differing session cookies. Because of this, session cookies are supossed to be very large, random values. 
- The session cookies in the application are purposely insecure; they are just the name of the user base64 encoded. By taking the username 'admin', and base64 encoding it (YWRtaW4=), the user will have the administrators session.  

## UTF8 Character Truncation
- The character sets for MySQL UTF8 are relly messed up. The UTF8 is not true UTF, but a custom UTF8. Instead, users are supossed to use utf8mb4. What happens when an unsupported character is used? Some characters, such as 𝌆, will not work with the encoding and truncate the result (assuming strict mode is not being used). 
- The application uses a check to see if a given username exists or not. If the username does exist then it cannot be recreated. Running a query against admin𝌆aaa will result in no match. But, when the user is created, the unusable unicode character and everything after it will be THROWN out. So, a user with the username admin will be created. Now, just login with the admin user that was created when registering to win. 
- For more on this: https://cedricvb.be/post/wordpress-stored-xss-vulnerability-4-1-2/

## Winning 
- Once the application believes that the admin user is being used, it will output the flag on the next search that is done. 