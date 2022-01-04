'''
The Collatz sequence is generated sequentially where

n = n / 2 if n is even
n = 3 * n + 1 if n is odd
And the sequence ends if n = 1
N = 11;
Output: 15
Explanation:
The Collatz sequence is: [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1] and its length is 15.

Input Format
Input is simple number. Output the size of colatz sequence. 6

Constraints
0 < n < 10000

Output Format
9

Sample Input 0
6

Sample Output 0
9
'''

class Solution:
   def solve(self, num):
      if(num == 0):
         return 0
      length = 1
      while(num != 1):
         num = (num / 2) if num % 2 == 0 else (3 * num + 1)
         length += 1
      return length
ob = Solution()
a = int(input())
print(ob.solve(a))
