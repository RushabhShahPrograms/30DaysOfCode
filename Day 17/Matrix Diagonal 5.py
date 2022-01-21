'''
Given a square n x n matrix, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

Input Format
n = 3, mat = [[1,2,3], [4,5,6], [7,8,9]]

Constraints
n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100

Output Format
25

Sample Input 0
3
1 2 3
4 5 6
7 8 9

Sample Output 0
25
'''

def diagonal(arr):
    ans=0
    for i in range(len(arr)):
        ans += arr[i][i] + arr[i][~i]
    if(len(arr)%2):
        ans -= arr[int(i/2)][int(i/2)]
    return ans

n = int(input())
arr=[0]*n
for i in range(n):
    arr[i] = list(map(int, input().split()))

print(diagonal(arr))
