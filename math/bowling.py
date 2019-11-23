'''
Calculating the amount of possbile spare combinations is pretty cool! 
In order to do this, we must consider 2 things: 
- Each amount of pins still up (i.e. 1 pin, 2 pins...) 
- Every location where these pins could be at.  ! - - -   - ! - -
                                                 - - -     - - -
                                                  - -       - -
                                                   -    vs   -

This is a combination, as opposed to a permutation because the order of the pins on the layout DOES NOT MATTER.

For a single go of n total pins (i.e. 6), for i pins left (i.e. 4), this is calcuated as: 
  C(n,i) or n! / ((i!)(n - i)!) or 
  C(6,4) or 6! / ((4!)(6 - 4)!)

However, this is for a single pin setup. 
So, iterate over a given i (amount of pins ups) from 1, n -1. 
Note: This is 1 for the starting point, and not 0. because having 0 pins left has completed a round of bowling, meaning that there is no spare attempt.

C(6,0) + C(6,1) + C(6,2) + C(6,3) + C(6,4) + C(6,5) = 63 combinations
  1    +    6   +    15  +   20  +    15   +   6    = 63 combinations
'''
# Calculates the factorial of a number 
def fact(n):
    if n <= 1:
        return 1 
    
    total = 1
    for i in range(1,n+1):
        total = i * total 
    return total 

# Calculates the combination possbilities. 
def comb(n,r):
    return fact(n) / (fact(r) * (fact(n-r)))

# Calculates the amount of possible spare combinations, given the amount of pins.
def bowling_ball(n):
    # Calculate n choose i. 
    # This will find combinations of pins the n locations avaiable with i pins. 
    # Finds each combination, given the amount of pins knocked over. 
    total = 0 
    for i in range(0,n):
        amount = comb(n,i) 
        total = total + amount 
    return total


# Note: A strike (zero pins) does not count for this calculation.
print "Amount of different pin combinations in bowling for a spare setup..."
print "03 pins: ", bowling_ball(3)
print "06 pins: ", bowling_ball(6)
print "10 pins: ", bowling_ball(10)
print "15 pins: ", bowling_ball(15)
print "21 pins: ", bowling_ball(21)
print "28 pins: ", bowling_ball(28)
print "36 pins: ", bowling_ball(36)
print "45 pins: ", bowling_ball(45)
print "55 pins: ", bowling_ball(55)
print "66 pins: ", bowling_ball(66)
