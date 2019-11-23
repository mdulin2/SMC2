'''
Imagine: There is a password reset function on a website. 
However, this allows for an infinite amount of reset codes within a 10 minute time frame 
and does not expire old tokens upon request of a new token.
Given a password reset passcodes, how many attempts are needed to have a probability of 1 that the passcode has been found? 

For 10,000 (XXXX), the probability of 1 is around 141 guesses. 
By running the expirement, on 10,000, it found the passcode, on average, on 124-126 attempts (which is about 75% likely from the probability scale)
'''
import random

# Everytime the passcode pool adds 1, incresing the probability of a find for each guess 
# Calculautes a compound probability, given n possible passcodes
# Gives a probability of 1 or more!
def prob(n,p):
        
    total = 0 
    for i in range(1,n):
        new = i / (float(n-i))
        total =  total + new 
	print i, n-i
        if(total >= p):
            return i

# Simulates the passcode checking
# N is the amount of possible codes. 
def test_prob_single(n):

    iteration = 1
    passcode_lst = []
    length = len(str(n)) - 1
    while(True):
        # The newly requested code
        new_code = extend(random.randint(1,n + 1), length)
        passcode_lst.append(new_code)
        # Guesses a random number. 
        guess = extend(random.randint(1,n + 1),length)
        if(guess in passcode_lst):
            return iteration

        iteration += 1

# Runs a randomness test 
# n is the amount of possible passcodes 
# amount is the amount of runs for the test. 
def test_prob(n, amount):

    amount_lst = []
    for _ in range(amount):
        attempts = test_prob_single(n)
        amount_lst.append(attempts)
    
    print "Maximum needed attempts: ", max(amount_lst) 
    print "Minimum needed attempts: ", min(amount_lst)
    return sum(amount_lst) / float(amount)

# Extends the passcode to have 0's on the front. 
# passcode is the string being extended 
# total_len is the total length of the string. 
def extend(passcode, total_len):
    code = str(passcode)
    while(len(code) <= total_len -1):
        code = '0' + code 
    return code 


n = 10000
print "Statistical probability of 1 for attempts needed: ", str(prob(n,1))
avg = test_prob(n,10000)
print "Amount of attempts to guarentee a correct pin: ", avg
