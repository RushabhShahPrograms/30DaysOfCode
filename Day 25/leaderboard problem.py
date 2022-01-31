'''
You are given a list of integers nums, representing the number of chess matches each person has won. Return a relative ranking (0-indexed) of each person.

If two players have won the same amount, their ranking should be the same.

Input Format

length = 5,
nums = [50, 30, 50, 90, 10]
Constraints

n ≤ 100,000 where n is the length of nums
Output Format

1 2 1 0 3
Sample Input 0

5
50 30 50 90 10
Sample Output 0

1 2 1 0 3
Sample Input 1

10
50 30 50 90 10 100 120 60 70 60
Sample Output 1

5 6 5 2 7 1 0 4 3 4
'''

class Solution:
    def solve(self, nums):
        d = {v: k for k, v in enumerate(reversed(sorted(list(set(nums)))))}
        return [d[v] for v in nums]

ob=Solution()
n=int(input())
nums=list(map(int, input().split()))[:n]
print(*ob.solve(nums),sep=" ")
