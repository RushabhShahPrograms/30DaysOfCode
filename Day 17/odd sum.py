'''
Given an integer n, return the sum of the first n positive odd integers.
Example 1 Input n = 5 Output 25 Explanation The first 5 odd integers are [1, 3, 5, 7, 9] and its sum is 25.

Input Format
5

Constraints
n ≤ 1,000

Output Format
25

Sample Input 0
5

Sample Output 0
25
'''

def oddSum(n) :
    sum = 0
    curr = 1
    i = 0
    while(i < n):
        sum = sum + curr
        curr = curr + 2
        i = i + 1
    return sum
 
n = int(input())
print (oddSum(n))
