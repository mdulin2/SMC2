# Challenge 

## Challenge 1: Discover Your Inner Blue Team
- The human immune system has really complicated processes in place to fight off millions of different foreign [antigens](https://en.wikipedia.org/wiki/Antigen). [Certain immune cells](https://en.wikipedia.org/wiki/Lymphocyte#T_cells_and_B_cells) use their receptors to recognize and bind to specific antigens. A process called [V(D)J Recombination](https://en.wikipedia.org/wiki/V(D)J_recombination) ensures that you have a diverse repertoire of receptors to fight off these nasty antigens.
- Find the correct DNA sequence of length 10 that will allow a receptor to bind a specific antigen.
- The correct sequence has the md5 hash: "6a81c717d2a7cebdaecf766cf85687e4".

Hint: DNA sequences can be any combination of 'A', 'T', 'C', and 'G' (e.g. 'ATCTGTA', "AAA", "AAT")
Hint: Loop over each possible sequence to see if the md5 hash of that sequence is "6a81c717d2a7cebdaecf766cf85687e4"
Hint: If your_fav_lang == "python": use hashlib.md5(sequence.encode()).hexdigest()

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