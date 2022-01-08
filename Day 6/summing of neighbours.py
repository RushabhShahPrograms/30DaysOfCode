'''
Given an array of integers of size ‘n’. Our aim is to calculate the maximum sum of ‘k’ consecutive elements in the array.
Input : n = 10
k = 4
arr[] = 1, 4, 2, 10, 23, 3, 1, 0, 20
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.
There is no subarray of size 3 as size of the whole array is 2.

Input Format

n = 10
k = 4
arr[] = 1, 4, 2, 10, 23, 3, 1, 0, 20

Constraints

k < n

0 < n < 100

Output Format

39
'''
n = int(input())
k = int(input())
arr = list(map(int,input().strip().split()))[:n]

if(n<k):
    print("error")
    
res = 0
for i in range(k):
    res += arr[i]
    
c = res
for i in range(k,n):
    c += arr[i] - arr[i-k]
    res = max(res,c)
    
print(res)
