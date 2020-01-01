# Solutions

1.Sum the number of 1's in each string

weight(A) = weight("1101 1110") = 6

weight(B) = weight("1111 0000") = 4

weight(C) = weight("0101 1101") = 5

2. To find the max distance between strings, find the # of places where they are different.

d(A,B) = xor("1101 1110", "1111 0000") = 4

d(A,C) = xor("1101 1110", "0101 1101") = 3

**d(B,C) = xor("1111 0000", "0101 1101") = 5**

```python3
def logical_xor(x, y):
    """xor two bits"""
    return int(x, 2) ^ int(y, 2)
ds
def hamming_dist(a, b):
    """hamming distance between two bit strings"""
    assert len(a) == len(b), "strings are not equal length"
    dist = 0
    for i in range(len(a)):
        if logical_xor(a[i], b[i]):
            dist += 1
    return dist
    
if __name__ == "__main__":
    print("dist(A,B):", hamming_dist("11011110", "11110000"))
    print("dist(A,C):", hamming_dist("11011110", "01011101"))
    print("dist(B,C):", hamming_dist("11110000", "01011101"))
```
