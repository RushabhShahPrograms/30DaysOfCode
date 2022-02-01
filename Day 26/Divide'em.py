'''
Given a list of positive integers nums, return the largest positive integer that divides each of the integers.

Example 1
Input
nums = [6, 12, 9]
Output
3
Explanation
3 is the largest integer that divides into 6, 12, and 9.
Example 2
Input
nums = [6, 7, 9]
Output
1
Explanation
7 is a prime number so only 1 divides into it.
Input Format

3 6 12 9

Constraints

1 ≤ n ≤ 100,000 where n is the length of nums

Output Format

6

Sample Input 0

3
6 12 9
Sample Output 0

3
Sample Input 1

3
6 7 9
Sample Output 1

1
'''

import math
class Solution:
    def solve(self, nums):
        ans = nums[0]
        for x in nums:
            ans = math.gcd(ans, x)
        return ans

ob = Solution()
n=int(input())
nums=list(map(int, input().split()))[:n]
print(ob.solve(nums))
