'''
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [0,1,1] results in [1,0,0].

Input Format
3 1 1 0 1 0 1 0 0 0

Constraints
n == image.length
n == image[i].length
1 <= n <= 20
images[i][j] is either 0 or 1.

Output Format
1 0 0 1 0 1 0 0 0

Sample Input 0
3
1 1 0
1 0 1
0 0 0

Sample Output 0
1 0 0
0 1 0
1 1 1

Explanation 0
First reverse each row: [[0,1,1],[1,0,1],[0,0,0]]. Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
'''

def upordown(arr):
    for i in arr:
        i.reverse()
    for j in range(len(arr)):
        for k in range(len(arr[j])):
            if(arr[j][k]==1):
                arr[j][k]=0
            else:
                arr[j][k]=1
    return (arr)

n = int(input())
arr = [0]*n
for i in range(n):
    arr[i] = list(map(int, input().split()))
m=upordown(arr)
#print(*upordown(arr),end=" ")

m = [[str(x) if x else "0" for x in row] for row in m]
field_length = max(len(x) for row in m for x in row)
print("\n".join(" ".join("%%%ds" % field_length % x for x in row)for row in m))
