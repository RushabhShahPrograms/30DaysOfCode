'''
Given a 2D integer array matrix, return the interchange of matrix.

The interchange of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Input Format

m = 3
n = 3
matrix = [[1,2,3],[4,5,6],[7,8,9]]
Constraints

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
Output Format

1 4 7 2 5 8 3 6 9

Sample Input 0

3
3
1 2 3
4 5 6
7 8 9
Sample Output 0

1 4 7
2 5 8
3 6 9
Sample Input 1

2
3
1 2 3
4 5 6
Sample Output 1

1 4
2 5
3 6
'''

m=int(input())
n=int(input())
x = [0]*m
result = [0]*m
for i in range(m):
    x[i]=list(map(int, input().split()))

result = map(list, zip(*x))

for r in result:
    for c in r:
        print(c,end = " ")
    print()
