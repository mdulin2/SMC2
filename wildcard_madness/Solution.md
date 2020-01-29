## Solution

The goal is to use non-alphabetic characters (besides 1) in order to beat this challenge. The key to solving this is wildcards. 

- '*' will call all existing. For example, ls * will print all of the files in a directory.
- '?' will call all with a specific amount. For example, ls flag.??? will list all files that start with 'flag.' and end with 3 characters.

### Solutions
In theory, this challenge is actually solvable without a single character. However, this seemed too hard. So, we allowed one character.

The solutions depend on the env heavily. This is because the binaries installed on the particular device make a very large difference. Several solution that we wrote worked locally, but not on the server with the challenges. So, we had to come up with several working solutions.

### Solution 1
This is the simplest solution that I could come up with: `/???/??t ./????.???`. This calls /bin/cat ./flag.txt. Doing this with a c (in Cat) may also work.

### Solution 2
This solution uses echo and a few interesting directives. The initial `/???/e???` is calling /bin/echo. The second part `$(<./????.???)` is setting the file flag.txt as input into echo. The full solution is `/???/e???  $(<./????.???)`

### Solution 3
This is also a really simple solution: `/???/m??? ./????.???`. This is very similar to number 1 but uses 'more' instead of cat.

## Solution 4
Okay, this one is pretty cool! This uses no alphabetic characters but uses numbers. By using the base32 binary (base64 does not work for some reason) we can pass this with NO characters! `/???/???/????32 ./????.???` turns into `/usr/bin/base32 ./flag.txt`. This data is then outputted in base32. But, once it is decoded, the flag is there! This took me (Max Dulin) about 2 hours of playing with to come up with. There's a solution out there with no alphabetic or numeric characters, but I am pretty happy with this!