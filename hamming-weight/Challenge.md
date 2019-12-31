# Hamming Weight
Hamming distance and hamming weight are related concepts often relied upon in different applications of cryptography, information theory, coding theory, and more! 

## Definitions
- Hamming Distance: # of positions between two strings where a symbol differs
- Hamming Weight (for a binary string): # of 1's in the string, the distance from an all-zero binary string of the same length.

## Examples
Suppose A = "1001 0110", B = "1010 1010".
- dist(A, B) = # of positions where the symbol is different = 4; notice this is equivalent to performing binary addition w/o a carry which is also equivalent to XOR(A,B).
- weight(A) = hamming distance from "0000 0000" = # of 1's = 4
- weight(B) = 4 

## Questions
Suppose A = "1101 1110", B = "1111 0000", C = "0101 1101"
1. Find weight(A), weight(B), and weight(C).
2. Which two strings have the greatest distance?
