# Solutions! 

## Solution 1: 
- Luke! 


## Solution 2: 
Calculating the amount of possbile spare combinations is pretty cool!   
In order to do this, we must consider 2 things:   
- Each amount of pins still up (i.e. 1 pin, 2 pins...) 
- Every location where these pins could be at.  ! - - -   - ! - -
                                                 - - -     - - -
                                                  - -       - -
                                                   -    vs   -

This is a combination, as opposed to a permutation because the order of the pins on the layout DOES NOT MATTER.   

For a single go of n total pins (i.e. 6), for i pins left (i.e. 4), this is calcuated as:   
- C(n,i) or n! / ((i!)(n - i)!) or 
- C(6,4) or 6! / ((4!)(6 - 4)!)  
However, this is for a single pin setup.   
So, iterate over a given i (amount of pins ups) from 1, n -1.   
Note: This is 1 for the starting point, and not 0. because having 0 pins left has completed a round of bowling, meaning that there is no spare attempt.  

C(6,0) + C(6,1) + C(6,2) + C(6,3) + C(6,4) + C(6,5) = 63 combinations 
  1    +    6   +    15  +   20  +    15  +     6   = 63 combinations

# Solution 3: 
- Need to verify....