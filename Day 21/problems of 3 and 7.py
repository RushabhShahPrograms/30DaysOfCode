'''
Given a positive integer n, determine whether you can make n by summing up some non-negative multiple of 3 and some non-negative multiple of 7.

Input Format

n = 13

Constraints

n < 2 ** 31
Output Format

true

Sample Input 0

13
Sample Output 0

true
Explanation 0

We can get 13 with 1 * 7 + 2 * 3.

Sample Input 1

9
Sample Output 1

true
'''

def solve(n):
    no3=n//3
    return no3>=2*(n%3)

n=int(input())
if(solve(n)==True):
    print("true")
else:
    print("false")
