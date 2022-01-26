'''
You are given a list of integers nums of length n representing the current score of swimmers in a competition. There is one more round to swim and the first place winner for this round gets n points, second place n-1 points, etc. and the last place gets 1 point. Return the number of swimmers that can still win the competition after the last round. If you tie for first in points, this still counts as winning.

Example 1
Input
nums = [8, 7, 10, 11]
Output
3
Explanation
The swimmers that currently have 8, 10 and 11 points can all win if final score is [12, 10, 12, 12]. That is, the 8 point swimmer gets first place, 7 point swimmer swimmer gets second, 10 point swimmer gets third, and 11 point swimmer gets last place.

Even if the 7 point swimmer gets first place and has final score of 11 points, 8 point swimmer gets second, the third place person would still get 2 points so the last two swimmers would still get at least 12 points. So the 7 point swimmer cannot win the competition.
Input Format

4 8 7 10 11

Constraints

n ≤ 100,000 where n is the length of nums

Output Format

3

Sample Input 0

4
8 7 10 11
Sample Output 0

3
Sample Input 1

4
9 6 11 12
Sample Output 1

3
'''

def solve(nums):
    if not nums:
        return 0
    n = len(nums)
    ans = 0
    nums.sort()
    a = 0
    for i in range(n - 1, -1, -1):
        cand = nums[i] + n - i
        if cand > a:
            a = cand
    for x in nums:
        if x + n >= a:
            ans += 1
    return ans

z = int(input())
nums = list(map(int, input().split()))[:z]
print(solve(nums))
