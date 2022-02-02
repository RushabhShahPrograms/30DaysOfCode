'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place

Input Format

m = 3
n = 3
matrix = [[1,1,1],[1,0,1],[1,1,1]]
Constraints

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
Output Format

1 0 1
0 0 0
1 0 1
Sample Input 0

3
3
1 1 1
1 0 1
1 1 1
Sample Output 0

1 0 1
0 0 0
1 0 1
Explanation 0

image

Sample Input 1

3
4
0 1 2 0
3 4 5 2
1 3 1 5
Sample Output 1

0 0 0 0
0 4 5 0
0 3 1 0
Explanation 1

image
'''

class Solution:
    def setZeroes(self, matrix):
        zero_rows = set()
        zero_columns = set()
        
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):                
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_columns.add(j)                    
                    
        
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):                
                if i in zero_rows or j in zero_columns:
                    matrix[i][j] = 0
        return matrix

ob=Solution()
m=int(input())
n=int(input())
matrix=[0]*m
for i in range(m):
    matrix[i]=list(map(int, input().split()))

result = ob.setZeroes(matrix)

for r in result:
    for c in r:
        print(c,end = " ")
    print()
