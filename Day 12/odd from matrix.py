'''
There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some 
increment operations on the matrix.
For each location indices[i], do both of the following:
Increment all the cells on row ri.
Increment all the cells on column ci.
Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.

Input Format
m = 2, n = 3, length of indices=2, indices = [[0,1],[1,1]]

Constraints
1 <= m, n <= 50
1 <= indices.length <= 100
0 <= ri < m
0 <= ci < n

Output Format
6
'''

m = int(input())
n = int(input())
length = int(input())
indices = list(map(int, input().split()))
ma = []
while indices != []:
    ma.append(indices[:2])
    indices = indices[2:]

x = [0]*m
y = [0]*n
for i in ma:
    x[i[0]] += 1
    y[i[1]] += 1
print(sum([1 for j in y for i in x if (j+i) % 2]))
