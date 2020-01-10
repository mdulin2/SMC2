## Solution 
Arbitrary redirects are really bad in general. They are bad in for phishing campaigns because they convince users that the site is the correct one, and may not realize a similar looking site. Additionally, arbitrary redirects can make several vulns much worse, such as OAuth bugs.   

### Thoughts 
- This program is meant to simulate the ability to redirect a user. However, it has a single restriction: no domain names. So, there are two main bypasses for this. 

### Solution 1
- The filter only blocks domain names. IP addresses are totally fine to use in this.  `http://IP:9999?page=http://18.218.89.10`

### Solution 2
- The double slash will actually just redirect a user to any site...
`http://IP:9999?page=//google.com`. Finding this no actual sites is quite common. 
