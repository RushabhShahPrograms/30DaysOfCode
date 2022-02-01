'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
Input Format

4 1 2 3 4

Constraints

2 <= nums.length <= 105 -30 <= nums[i] <= 30 The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Output Format

24 12 8 6

Sample Input 0

4
1 2 3 4
Sample Output 0

24 12 8 6
Sample Input 1

6
-1  -2 -3 -4 -5 -6
Sample Output 1

-720 -360 -240 -180 -144 -120
Sample Input 2

7
3 4 -3 -4 5 -6 7
Sample Output 2

-10080 -7560 10080 7560 -6048 5040 -4320
'''

def productExceptSelf(nums):
    start, end, n = 1, 1, len(nums)
    out = [1]*n 
    for i in range(n):
        out[i] *= start
        start *= nums[i]
        out[~i] *= end
        end *= nums[~i]
    return out

length=int(input())
nums=list(map(int, input().split()))[:length]
print(*productExceptSelf(nums))
