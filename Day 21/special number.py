'''
Given an m x n matrix of distinct numbers, return all Special numbers in the matrix in any order. A Special number is an element of the matrix such that it is the minimum element in its row and maximum in its column. Return the list of Special numbers.

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only Special number since it is the minimum in its row and the maximum in its column.
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only Special number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only Special number since it is the minimum in its row and the maximum in its column.
Input Format

3
3
3 7 8
9 11 13
5 16 17

Constraints

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 105.
All elements in the matrix are distinct.
Output Format

15

Sample Input 0

3 
3
3 7 8 
9 11 13
15 16 17
Sample Output 0

15
Sample Input 1

3
4
1 10 4 2
9 3 8 7
15 16 17 12
Sample Output 1

12
Sample Input 2

3
5
3 2 1 5 2
6 5 4 4 2
9 8 7 4 2
Sample Output 2

2 2
'''

def special_number(matrix):
    min_n={min(rows) for rows in matrix}
    max_n={max(columns) for columns in zip(*matrix)}
    return list(min_n & max_n)

r=int(input())
c=int(input())
matrix=[0]*r
for i in range(r):
    matrix[i]=list(map(int, input().split()))[:c]

print(*special_number(matrix),end=" ")
