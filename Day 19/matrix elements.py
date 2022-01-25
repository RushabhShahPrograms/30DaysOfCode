'''
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

Input Format
length = 3
matrix = [[1,2,3],[3,1,2],[2,3,1]]

Constraints
n == matrix.length == matrix[i].length
1 <= n <= 100
1 <= matrix[i][j] <= n

Output Format
true

Sample Input 0
3
1 2 3
3 1 2
2 3 1

Sample Output 0
true
'''

def elements(matrix,n):
    new_matrix = [[None]*n for _ in range(n)]
    
    for row in matrix:
        if(len(set(row)) != n):
            return False
    
    for x in range(n):
        for y in range(n):
            new_matrix[x][y]=matrix[y][x]
               
    for row in new_matrix:
        if(len(set(row))!=n):
            return False
    return True
               
              
n = int(input())
matrix = [0]*n
for i in range(n):
    matrix[i] = list(map(int, input().split()))
if(elements(matrix,n)==True):
    print("true")
else:
    print("false")
