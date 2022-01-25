'''
Given a two-dimensional n x n integer matrix, return the total number of integers whose value is the largest in its row and in its column.

Input Format

n = 3,

matrix = [ [1, 3, 2], [6, 6, 5], [1, 5, 7] ]

Constraints

n ≤ 250 where n is the number of rows and columns in matrix
Output Format

3

Sample Input 0

3
1 3 2
6 6 5
1 5 7
Sample Output 0

3
Explanation 0

The 3 big numbers are 6, 6, and 7.

Sample Input 1

4
1 2 3 2
3 2 3 2
1 2 2 3
1 1 1 1
Sample Output 1

4
'''
# below given two solutions are not accurate they will give output for some specific output only. If you know the correct one then please edit it.
# 1st option

n = int(input())
m = [0]*n
for i in range(n):
    m[i] = list(map(int, input().split()))

r=len(m)
c=len(m[0])
l=[]
for i in range(r): 
    max1=0
    for j in range(c): 
        if m[i][j] >= max1:
            max1= m[i][j]
    l.append(max1)
m2 = list(zip(*m))
l2=[]
for i in range(r): 
    max1=0
    for j in range(c): 
        if m[i][j] >= max1: 
            max1 = m[i][j]
    l2.append(max1)
a=[]
for r in range(len(m)):
    for c in range(len(m2)):
        b = m[r][c]
        if (l[r], l2[c]) == (b, b):
            a.append(b)
print(len(a))

# 2nd option
'''
c=0
ma=[0]*n
r=len(m)
c=len(m[0])
for i in range(r):
    max1=0
    for j in range(c):
        if m[i][j] > max1:
            max1=m[i][j]
    ma=max1
print(ma)
'''
