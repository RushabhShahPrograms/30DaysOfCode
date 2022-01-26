'''
Given an integer n, return the maximum number you can make by inserting 5 anywhere in the number.

For e.g.:

If n = 923, 
Then ouput will be 9523 as it will be the maximum number when 5 is added into the       given 3 digits.
Input Format

923

Constraints

-100000 < n < 100000

Output Format

9523

Sample Input 0

923
Sample Output 0

9523
Sample Input 1

-234
Sample Output 1

-2345
'''

def solve(n):
    k = 1
    maxVal = float("-inf")
    minVal = float("inf")
    negative = n < 0
    n = abs(n)

    while k <= n * 10:
        a, b = (n // k) * (k * 10), (5 * k) + n % k
        k = k * 10
            
        maxVal = max(maxVal, a + b)
        minVal = min(minVal, a + b)

    return -1 * minVal if negative else maxVal

n = int(input())
print(solve(n))
