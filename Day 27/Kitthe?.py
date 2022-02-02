'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
Input Format

6 9 -1 0 3 5 9 12

Constraints

1 <= nums.length <= 104 -104 < nums[i], target < 104 All the integers in nums are unique. nums is sorted in ascending order.

Output Format

4

Sample Input 0

6
9
-1 0 3 5 9 12
Sample Output 0

4
Sample Input 1

6
2
-1 0 3 5 9 12
Sample Output 1

-1
'''

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
    
ob=Solution()
n=int(input())
target=int(input())
nums=list(map(int, input().split()))[:n]
print(ob.search(nums,target))
