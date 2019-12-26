# Challenge 

## Challenge 1: Find the DNA String
- Your task is to find the **DNA string of length 10** that has the **MD5 hash value "6a81c717d2a7cebdaecf766cf85687e4"**. A DNA string can be any combintion of 'A', 'T', 'C', and 'G' (e.g. 'AAAAAAAAAA', 'ATATGCTAAG', 'AAAAAAAAAT'). Find the combination that gives you the correct hash.
- Hint: Generate unique 10-nucleobase long sequences by finding a cartesian product
- Hint: If your_fav_lang == "python": use hashlib.md5(sequence.encode()).hexdigest() for each sequence you generated.

## Challenge 2: Bowling for 15
- Bowling is a very interesting game. With bowling, you get two chances to knock over all of the pins. On this second attempt, there are A LOT of different possible pin setups to attempt for a **spare**. How many different spare combinations are there for a pin setup which has 15 pins?  

Hint: Combinations and Permutations   
Hint: The case of knocking all of the pins over is not counted. But, the case of missing all of the pins is counted. 

## Pin Enumeration 
- A common feature of a website is to have a *password reset* feature, allowing the user to reset a password, in the case that they forgot their previous. However, this opens up an entirely new way to take over an account! 
- What if you found a password reset that was poorly implemented? Instead of limiting the amount of pins for an account to 1, it just kept adding them. For instance, the first requst added the code 0115 as a valid reset pin. Then, upon asking for a new pin, it gives you 4301. However, 0115 **and** 4301 are BOTH valid now. 
- Given this setup with 4 digits (XXXX), how many pins need to be attmpted in order to statically guarentee that the pin will be guessed?  
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Hint: The probability must be greater than 1 for this to be possible. 
