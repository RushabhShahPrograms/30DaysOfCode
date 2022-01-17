'''
You are given a list of integers nums. Return the index of every peak in the list, sorted in ascending order. An index i is called a peak if:

nums[i] > nums[i + 1] if i = 0
nums[i] > nums[i - 1] if i = n - 1
nums[i - 1] < nums[i] > nums[i + 1] otherwise
However, a list of length 1 is not considered a peak.

Constraints
0 ≤ n ≤ 100,000 where n is the length of nums

Sample Input 0
5
1 2 3 2 4

Sample Output 0
2 4

Explanation 0
The values at index 2 and 4 are considered peaks since they are larger than their neighbors.

Sample Input 1
4
1 2 1 1

Sample Output 1
1
'''

n = int(input())
nums = list(map(int, input().split()))

ans = []
if(n==1):
    print(ans)
for i,num in enumerate(nums):
    if(i>0 and i<n-1):
        if(nums[i-1]<num>nums[i+1]):
            ans.append(i)
    if(i==0):
        if(num>nums[i+1]):
            ans.append(i)
    if(i==n-1):
        if(num>nums[i-1]):
            ans.append(i)
print(*ans,end=" ")
