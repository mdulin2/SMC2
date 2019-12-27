#!/usr/bin/env python3
#
# Author: Luke Hartman
# Date: 23 December 2019
# Description:
#   Script that enumerates through all possible dna strings of length n
# Usage:
#   python3 dna.py {n}    (n is an integer > 0)
#----------------------------------------------------------------------

import sys
import time
import hashlib
from itertools import product

# TODO: remove answer
# solution = "AATGTACACT"
# solution_hash = hashlib.md5(solution.encode()).hexdigest()
solution_hash = "6a81c717d2a7cebdaecf766cf85687e4"

def more_efficient_solver():
    """Python implementation of http://phrogz.net/lazy-cartesian-product"""
    start = time.time()
    seq = ["A" for i in range(10)]

    def dive(d):
        a = "ATCG"
        if d == 9:
            for i in range(4):
                seq[d] = a[i]
                current_seq = "".join(seq)
                ans = check_hash(current_seq)
                if ans:
                    msg = "Found sequence: %s in %s sec" % (current_seq, str(time.time() - start))
                    sys.exit(msg)
        else:
            for i in range(4):
                seq[d] = a[i]
                dive(d+1)                
        seq[9] = "A"
    return dive(0)

def check_hash(seq):
    seq_hash = hashlib.md5(seq.encode()).hexdigest()
    if seq_hash == solution_hash:
        return seq
    else:
        return ""

def generate_dna_strings(n):
    """
    Finds all possible dna sequences of length n by computing 
    the Cartesian product of n sets containing ['A','T','C','G']. 

    Args:
        n: length of strings to be generated.
       
    Returns: 
        A list of all possible dna sequences of length n.
    """
    sequences = list(product('ATCG', repeat=n))
    return ["".join(seq) for seq in sequences]

def find_matching_hash(sequences):
    """Hashes each sequence till matching hash is found"""
    for seq in sequences:
        seq_hash = hashlib.md5(seq.encode()).hexdigest()
        if seq_hash == solution_hash:
            return seq
    return ""

def print_sequences(sequences):
    for seq in sequences:
        print(seq)     


def main():
    """ uncomment to generate all combinations
    try:
        n = int(sys.argv[1])
    except ValueError:
        sys.exit("Length argument should be an integer. \'%s\' is invalid" % sys.argv[1])
    
    # get all possible dna sequences of length n
    possible_sequences = generate_dna_strings(n)
    ans = find_matching_hash(possible_sequences)
    
    if ans:
        print("you found it!!!\n%s" % ans)
    else:
        print("not found... keep looking :)")
    """
    more_efficient_solver()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Incorrect number of arguments. \n\t Usage: python3 dna.py {length}")
    main()
