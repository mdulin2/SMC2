# Logging Challenge 1

## Challenge - EVTX Logging 
- Although most of the challenges are on the offensive side of information security, an important part of it is the defense! 
- This set of challenges involves gaining valuable information from log files (evtx files). 

- Given: 
	- security.evtx 

Hint: 
	- Figure out how to open it first :) 
	

## Questions: 
- What OS are evtx files used for? 
- What is the most common event number in file? 
- How many different computer Id's are seen within the log files? 
- View all of the different processes that ran on the computers listed. Which file has the longest name? (full path for be in the flag ) 


# Logging Challenge 2

## Challenge - \*nix auth logs

Here are some authentication logs from a system that is suspected to have been compromised in April, 2019. The threat hunting team has a hypothesis that the attackers were able to obtain access through the ssh daemon. Your task is to test that hypothesis and answer some questions for a report. 

## Questions:
1. How many entries are there for this time period?
2. How many failed entries are there for this time period?
3. How many successful logins occurred during this period?
4. Provide a csv of login methods and their result. Provide as format method,result,count (no header). Example:

```
password,Accepted,3
publickey,Failed,2
```

5. If you confirm the hypothesis, what is the IP address of the attacker?

6. Provide a csv of all login attemps (successful or not) using geolocation of IP addresses. Provide as format CountryCode,count (no header). Example:
    
```
US,472
RU,182
EL,98
```