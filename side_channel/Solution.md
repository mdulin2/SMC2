# Solution 

<p>
The goal of the challenge is to get the passcode for the server. One could use a true brute force (10 ^ 8 possibilites). However, the verification of the passcode leaks data via a **side channel**. In computer security, a side channel is information that exposing data that is not an issue with the algorithm itself but with the implemenation. Common examples of this are timing information (this challenge), power consumption, electromagnetic information or sound. https://en.wikipedia.org/wiki/Side-channel_attack
</p>

<p>
In order to solve this challenge, use the timing difference between the a correct character and an incorrect character. 
For example, ./client 00000000 will time very quickly (durring testing, we used *time ./client 00000000*). However, ./client 10000000 will return about a second later because the character 1 is the correct character for the first character in the passcode.
</p>  

<p>
The maximum amount of attempts to solve this problem has gone from 10 ^ 8 to 8 x 10, or 80! This challenge can be automated (such as the solve.py file in this repo) or done by hand during the timing differences between two calls with the *time* binary as shown above. 
</p>  

## Flag
- 12348219
