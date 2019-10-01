## Challenge
- Explain Diffie-Hellman Key Exchange
- Ask the questions below in the solution...

## Solution: 
- Ask1: 
	- Why is it useful? 
- Want to hear: 
	- Create shared key between two parties in a secure manner.
- Ask2: 
	- What numbers are put into the open? 
- Want to hear: 
	- p and g. 
- Ask3: 
	- What are the requirements of these numbers? 
- Want to hear: 
	- Prime number(p) and primative root(g). 
- Ask4: 
	- What numbers are exchanged? What are kept secret? 
- Want to hear: 
	- Alice and Bob each have a private value. They calculate g ^ secret_val mod p, then send this to the other. 
- Ask5: 
	- What is done with the values? 
- Want to hear: 
	- key = other_secret ^ my_secert mod p. 
	
- Ask6: 
	- Why does this work? 
- Want to hear: 
	- Magic with how modulo and exponents work. 
	- By rule, any value that is (x^y)^z = x^yz. So, g^ba mod p = (g^ab) mod p
	

Feel free to guide them throughout the workings of this, drawing diagrams and so on... Especially with the last one. 


## Flag: 
- Diffie is a bad ass
	
	
	
	
	

