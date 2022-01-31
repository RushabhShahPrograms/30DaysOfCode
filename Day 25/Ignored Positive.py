'''
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Input Format

length = 3
nums = [1,2,0]
Constraints

1 <= nums.length <= 5 * 3105
-231 <= nums[i] <= 231 - 1
Output Format

3

Sample Input 0

3
1 2 0
Sample Output 0

3
Sample Input 1

4
3 4 -1 1
Sample Output 1

2
Sample Input 2

5
7 8 9 11 12
Sample Output 2

1
'''

class Solution:
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while 0 <= nums[i] - 1 < len(nums) and nums[nums[i] - 1] != nums[i]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
    
ob=Solution()
n=int(input())
nums=list(map(int, input().split()))[:n]
print(ob.firstMissingPositive(nums))
