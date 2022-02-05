'''
Given an integer array nums representing cash of each house, return the max amount of money you can rob tonight without alerting the police.

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

For e.g.:

If nums = [1,2,3,1], then output will be 4.
Explanation:
Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Input Format

length = 4
nums = [1, 2, 3, 1]
Constraints

1 <= nums.length <= 100
0 <= nums[i] <= 400
Output Format

4

Sample Input 0

4
1 2 3 1
Sample Output 0

4
Explanation 0

Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).

Total amount you can rob = 1 + 3 = 4.

Sample Input 1

5
2 7 9 3 1
Sample Output 1

12
'''

def rob(nums):
    if not nums: 
        return 0
    nums = [0]+nums
    for i in range(3,len(nums)):
        nums[i]+=max(nums[i-3],nums[i-2])
    return max(nums[-1],nums[-2])

n=int(input())
nums=list(map(int,input().split()))[:n]
print(rob(nums))
