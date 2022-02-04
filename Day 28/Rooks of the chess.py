'''
Two ways are considered different if in one of the ways, some cell of the chessboard is occupied, and in the other way, the cell is not occupied. Note: two rooks are attacking each other if they are either on the same row or on the same column. For e.g.: If n = 3, then Output will be 6.

Explanation: Here are the different chessboard configurations, where X is a rook.

X O O 
O X O
O O X

X O O 
O O X
O X O

O X O
X O O
O O X

O X O
O O X
X O O

O O X
O X O
X O O

O O X
X O O
O X O
Input Format

3

Constraints

n > 0

Output Format

6

Sample Input 0

3
Sample Output 0

6
Sample Input 1

4
Sample Output 1

24
'''

import math
class Solution:
    def solve(self, n):
        return math.factorial(n)

ob = Solution()
n=int(input())
print(ob.solve(n))
