'''
For e.g.: n = 0 Output will be 0 as no. of 1's in its binary i.e 0 are 0. n = 3 Output will be 2 as no. of 1's in its binary i.e 11 are 2.

Input Format

2

Constraints

0 ≤ n < 2 ** 31

Output Format

1
'''

n = int(input())
c0,c1 = 0,0
while(n!=0):
    if(n%2==0):
        c0 += 1
    else:
        c1 += 1
    n //= 2
print(c1)
