# Logging Challenge 1

## Solution.md - Logging 

Being able to analyze log files is an important aspect of the defensive side of security. So, this challenges are a way to get started with log file analysis on Windows computers. 


### Background 

How to open the files: 
- Security.xml file found at https://github.com/omerbenamram/evtx/blob/master/samples/security.evtx. 
- This is a binary file that can be converted into an XML file in several ways...:
	- python-evtx (which is what is used) 
		- python-evtz file_name > security.xml
	- Native Windows tools. 
	- Once this is done, all of the other problems can be solved...

### Solutions

Each one of the questions has an answer and a fairly easy 'how to solve it' for the two bullets:
- What OS are evtx files used for? 
	- Windows 
	- Look up the file type by googling it...
- What is the most common event number in file? 
	- 4907
	- cat security.xml | grep "EventID" -i | sort | uniq -c | sort
- How many different computer Id's are seen within the log files? 
	- 2
	- cat security.xml | grep "Computer" | sort | uniq -c | sort
- View all of the different processes that ran on the computers listed. Which file has the longest name? (full path) 
	- C:\Windows\servicing\TrustedInstaller.exe
	- cat security.xml | grep "ProcessName" | sort | uniq -c
	- Then, just look at the processes to see the longest name. 
	- It is interesting to see all of the processes that are running on this! 


# Logging Challenge 2

## solution.md - \*nix logs

### Background

The provided auth.log file is a standard sshd log for an ubuntu server linux system. This can be analyzed with a number of programs or cracked open by hand.

Hint:
You may provide the following regex if a team is super stuck: `sshd.+: (?P<result>\S+) (?P<method>\S+) for (?P<user>\S+) from (?P<ip>\S+) port (?P<port>\d+)`

Hint: GeoIP can be done a variety of ways but Maxmind provides a great resource: https://dev.maxmind.com/geoip/geoip2/geolite2/

### Solutions:

The solutions are numbers or csv submissions

1. 424
2. 418
3. 6
4. 
```
password,Failed,418
publickey,Accepted,5
password,Accepted,1
```
5. 37.204.31.33
6. 
```
China,399
Russia,20
United States,5
```