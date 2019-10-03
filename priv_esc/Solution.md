# Solution 

## Background 

The goal is to teach the students about file permissions in Linux. 

File permissions govern **who** can access **what** on a file system. In Linux, there are three settings: owner level, group level and others.  

Within these different user types are different permissions: read, write and execute. These can be easily seen by using the 'ls -lA' command on a file.   

Besides these permissions, there are ways to make files immutable, change level upon execution and many other cool things that can be done.  

## Deeper 
A another set of powerful tools exist: setuid, setgid and sticky bits.   

- When the setuid bit is used, the behavior described above it's modified so that when an executable is launched, it does not run with the privileges of the user who launched it, but with that of the file owner instead.
- Unlike the setuid bit, the setgid bit has effect on both files and directories. In the first case, the file which has the setgid bit set, when executed, instead of running with the privileges of the group of the user who started it, runs with those of the group which owns the file: in other words, the group ID of the process will be the same of that of the file.
- The sticky bit works in a different way: while it has no effect on files, when used on a directory, all the files in said directory will be modifiable only by their owners. A typical case in which it is used, involves the /tmp directory. 

## Vulnerability 
Two of the binaries, within the running OS, have the setuid bit turned on in a dangerous fashion. Because of this, they can be used to leak the information from the flag files. 

- date: 
	- The flag -f will accept a file name. Putting the flag file returns an error upon exiting...This error leaks the flag value.  
- dd: 
	- The flag if=flag.txt will accept a file name. This will show the flag in the process of converting the file. 
	
Either of these answers are suitable; we just wanted to teach the students the dangers of the setuid bit within an OS, as well as Linux file permissions. 






A good walkthrough of all this can be found at https://www.guru99.com/file-permissions.html#targetText=Linux%20divides%20the%20file%20permissions,ownership%20of%20a%20file%2Fdirectory.
- date binary can leak information using the file's error messages. 
- dd works just the same. q