## Solution 
- The challenge includes three files: 
- A general admin panel with options to select from (Administrator.php)
- A directory listing (?) 
- A connection tester (ping.php).   
- The **ping.php** file has a command injection vulnerability. Attacker controlled input is put directly into a PHP exec command. This looks like: `ping <input> -c 3`. 
- A potential exploit would look something like: `ping <google.com -c 1; whoami;`. 
- As this is a source code review (no actual exploitation), the hackers-in-training will need to up to the judged based upon their understandnig of the bug.- They will need to explain: 
	- What the vulnerability is (code/command injection) 
	- How they would exploit it? They do not need an exact payload. But, understanding the avenue for attacking this is interesting to hear about!
