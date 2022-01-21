'''
The factorial of a number n is defined as n! = n * (n - 1) * (n - 2) * ... * 1. For e.g.: If a = 6, then output will be 3 Explanation 3! = 6

Input Format
6

Constraints
0 < a < 2 ** 31

Output Format
3

Sample Input 0
6

Sample Output 0
3

Sample Input 1
10

Sample Output 1
-1
'''

def solve(a):
    count = 1
    factor = 2
    while(a > 1):
        a = a / factor
        factor += 1
        count += 1
    if(a == 1):
        return count
    else:
        return -1

n = int(input())
print(solve(n))
