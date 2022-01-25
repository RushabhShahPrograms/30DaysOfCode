'''
Given an integer n, return its base 3 representation as a string. Example:

Input n = 11

Output 102

Input Format

7

Constraints

0 ≤ n < 2 ** 31

Output Format

21

Sample Input 0

7
Sample Output 0

21
Sample Input 1

11
Sample Output 1

102
'''

def solve(n):
    r=""
    while(n>=3):
        r=str(n%3)+r
        n=n//3
    r=str(n)+r
    return r

n = int(input())
print(solve(n))
