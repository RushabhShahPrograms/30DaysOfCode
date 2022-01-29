'''
Given an integer array nums where every element appears two times except for one, which appears exactly once. Find the single element and return it. You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
Input Format

4 2 2 3 2

Constraints

1 <= nums.length <= 3 * 104 -231 <= nums[i] <= 231 - 1 Each element in nums appears exactly two times except for one element which appears once.

Output Format

3

Sample Input 0

5
2 2 3 4 4
Sample Output 0

3
Sample Input 1

5
0 1 0 1 99
Sample Output 1

99
'''

from collections import Counter
def solve(n,nums):
    answer = 0
    cnt = dict(Counter(nums))
    keys = cnt.keys()
    for key in keys:
        if cnt[key] == 1:
            answer = key
    return answer


n=int(input())
nums=list(map(int,input().split()))
print(solve(n,nums))
