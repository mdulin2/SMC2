## Solution

<p> Encryption is the process of encoding a message or information in such a way that only authorized parties can access it and those who are not authorized cannot. 
</p>

<p>
The 'Cesar Cipher' is quite famous and well known, as it was the beginning of cryptography! 
- This cipher represents each letter as a number (A is 0, B is 1 and so on...) 
- Then, it shifts each letter over by the key. This key is the amount that the values have been shifted. 
- For example, MOM with a key of 5 would translate to 12 14 14. With the shift, this becomes 17 19 17 or rtr
- If the values is greater than 25 (0-25 are valid because there are 26 letters in the alphabet) then we mod (take the remainder) of the value. For instance, Z, with a key of 3 would go from 25 to 28. 28 % 26 would give use a key of 2. The same works but in the negative direction. 
- It is fun to play around with the cipher at https://cryptii.com/pipes/caesar-cipher. 
</p>

<p>
The challenge itself is tzu{qsgof_kog_o_usbwig}. In order to get the solution just rotate each letter by 14 (the key is 14). This will give you a proper flag, which is flg{cesar_was_a_genius}.
 
</p>