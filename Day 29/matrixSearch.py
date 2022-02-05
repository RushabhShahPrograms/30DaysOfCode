'''
Given a two-dimensional integer matrix, where every row and column is sorted in ascending order, find the kth (0-indexed) smallest number.

Input Format

m = 3, n = 3,
matrix = [
    [1, 3, 30],
    [2, 3, 31],
    [5, 5, 32]
],
k = 4
Constraints

n, m ≤ 250 where n and m are the number of rows and columns in matrix
Output Format

5

Sample Input 0

3
3
4
1 3 30
2 3 31
5 5 32
Sample Output 0

5
Sample Input 1

1
3
0
1 2 3
Sample Output 1

1
Sample Input 2

3
1
2
1
2
3
Sample Output 2

3
'''

m = int(input())
n = int(input())
k = int(input())
lst_of_lst = []
for i in range(m):
    lst = list(map(int, input().split()))
    lst_of_lst.extend(lst)
lst_of_lst.sort()
if k==0:
    print(lst_of_lst[0])
else:
    print(lst_of_lst[k])
