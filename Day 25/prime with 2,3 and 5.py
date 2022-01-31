'''
Given an integer n, return whether its prime factors only include 2, 3 or 5.

Input Format

n = 10

Constraints

0 ≤ n < 2 ** 31
Output Format

true

Sample Input 0

10
Sample Output 0

true
Explanation 0

10's prime factors are 2 and 5.

Sample Input 1

14
Sample Output 1

false
Explanation 1

14's prime factors include 7.
'''

class Solution:
    def solve(self, n):
        if n < 0:
            return False
        factor = [2,3,5]
        for i in factor:
            while n%i ==0:
                n/=i
        return n==1

ob = Solution()
n=int(input())
if(ob.solve(n)==True):
    print("true")
else:
    print("false")
