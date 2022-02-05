'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

For e.g.:

If input is nums = [0,1,0,3,12], then output will be [1,3,12,0,0].

Input Format

length = 5 nums = [0 1 0 3 12]

Constraints

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
Output Format

1 3 12 0 0

Sample Input 0

5
0 1 0 3 12
Sample Output 0

1 3 12 0 0
Sample Input 1

1
0
Sample Output 1

0
'''

class Solution(object):
    def moveZeroes(self, nums):
        insert_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_index]=nums[i]
                insert_index+=1
        for i in range(insert_index,len(nums)):
            nums[i]=0
        return nums
    
n = int(input())
nums = list(map(int, input().split()))[:n]
ob1 = Solution()
print(*ob1.moveZeroes(nums),sep=" ")
