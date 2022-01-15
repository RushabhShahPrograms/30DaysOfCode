'''
Given an integer n greater than or equal to 0, return whether it is a power of two.
for example numbers like 1,2,4,8,16,......, return true or false.

example 1

Input:
    n = 1

Output:
true
    
Explanation:
    2^0 = 1
    
Input Format
2

Constraints
0 ≤ n < 2 ** 31

Output Format
true
'''

import math
def Log2(x):
    if(x==0):
        return False
    return (math.log10(x)/math.log10(2));

def ispoweroftwo(n):
    return (math.ceil(Log2(n)) == (math.floor(Log2(n))));

n = int(input())
if(n == 0):
    print("false")
elif(ispoweroftwo(n)):
    print("true")
else:
    print("false")
