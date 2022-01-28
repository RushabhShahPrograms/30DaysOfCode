'''
Given a n x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Input Format

4 4 3 2 -1 3 2 1 -1 1 1 -1 -2 -1 -1 -2 -3

Constraints

m == grid.length n == grid[i].length 1 <= m, n <= 100 -100 <= grid[i][j] <= 100

Output Format

8

Sample Input 0

4
4 3 2 -1 
3 2 1 -1
1 1 -1 -2
-1 -1 -2 -3
Sample Output 0

8
Sample Input 1

2
3 2
1 0
Sample Output 1

0
'''

class Solution:
    def countNegatives(self, grid):
        count=0
        for i in grid:
            for j in i:
                if j<0:
                    count+=1
        return count

ob=Solution()
n=int(input())
grid=[0]*n
for i in range(n):
    grid[i]=list(map(int, input().split()))

print(ob.countNegatives(grid))
