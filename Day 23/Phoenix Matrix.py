'''
Given a two-dimensional matrix of integers matrix, determine whether it's a Phoenix matrix. A Phoenix is one where every diagonal descending from left to right has the same value.

Input Format

m = 4
n = 3
matrix = [
    [0, 1, 2],
    [3, 0, 1],
    [4, 3, 0],
    [5, 4, 3]
]
Constraints

n, m ≤ 250 where n and m are the number of rows and columns in matrix
Output Format

true

Sample Input 0

3
4
1 2 3 4
5 1 2 3
9 5 1 2
Sample Output 0

true
'''

def isToeplitz(matrix):
    row = len(matrix)
    col = len(matrix[0])
     
    map = {}
    for i in range(row):
        for j in range(col):
            key = i-j
            
            if (key in map):
                 
                if (map[key] != matrix[i][j]):
                    return False
             
            else:
                map[key] = matrix[i][j]
    return True
 

if __name__ == "__main__":
    m=int(input())
    n=int(input())
    matrix = [0]*m
    for i in range(m):
        matrix[i]=list(map(int, input().split()))
     
    # Function call
    if (isToeplitz(matrix)):
        print("true")
    else:
        print("false")
