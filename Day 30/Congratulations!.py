'''
You are given an integer array nums. Return true if you can reach the last index, or false otherwise.

You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

For e.g.:

If nums = [2,3,1,1,4], then output will be true.
Explanation:
Jump 1 step from index 0 to 1, then 3 steps to the last index.

If nums = [3,2,1,0,4], then output will be false.
Explanation: 
You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
Input Format

5
2 3 1 1 4
Constraints

1 <= nums.length <= 104
0 <= nums[i] <= 105
Output Format

true

Sample Input 0

5
2 3 1 1 4
Sample Output 0

true
Sample Input 1

5
3 2 1 0 4
Sample Output 1

false
'''

class Solution:
    def canJump(self, nums):
        jump = nums[0]
        for i in range(1,len(nums)):
            if jump == 0:
                return False
            jump -= 1
            jump = max(jump,nums[i])
        return True
    
ob=Solution()
n=int(input())
nums=list(map(int, input().split()))
if(ob.canJump(nums)==True):
    print("true")
else:
    print("false")
