'''
Given a list of integers nums, find a pair i < j, such that nums[i] + nums[j] + (i - j) is maximized, and return the value.

Input Format

length = 6
nums = [5, 5, 1, 1, 1, 7]
Constraints

n ≤ 100,000 where n is the length of nums.
Output Format

9

Sample Input 0

6
5 5 1 1 1 7
Sample Output 0

9
Explanation 0

Picking the two 5 is the best since its score is 5 + 5 + 0 - 1 = 9.

If we had picked the rightmost 5 with the 7 we'd get 5 + 7 + (1 - 5) = 8

Sample Input 1

11
8 9 3 4 2 4 2 1 1 1 7
Sample Output 1

16
'''

def solve(nums):
    large = nums[0]
    maxi = 0
    for i in range(1, len(nums)):
        large -= 1
        maxi = max(large + nums[i], maxi)
        large = max(large, nums[i])
    return maxi

n=int(input())
nums=list(map(int,input().split()))[:n]
print(solve(nums))
