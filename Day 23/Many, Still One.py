'''
You are given a list of integers nums which contains at least one 1. Return whether all the 1s appear consecutively.

Example 1
Input
nums = [0, 1, 1, 1, 2, 3]
Output
true
Explanation
All the 1s appear consecutively here in the middle.
Example 2
Input
nums = [1, 1, 0, 1, 1]
Output
false
Explanation
There's two groups of consecutive 1s.
Input Format

6 0 1 1 1 2 3

Constraints

1 ≤ n ≤ 100,000 where n is the length of nums

Output Format

true

Sample Input 0

6
0 1 1 1 2 3
Sample Output 0

true
Sample Input 1

5
1 1 0 1 1
Sample Output 1

false
'''

class Solution:
    def solve(self, nums):
        alreadyseen = 0
        """
        0 means never seen
        1 means currently seeing
        2 means has finished seeing
        """
        for x in nums:
            if x == 1:
                if alreadyseen == 2:
                    return False
                alreadyseen = 1
            elif alreadyseen:
                alreadyseen = 2
        return True
    
ob=Solution()
n=int(input())
nums=list(map(int,input().split()))
if(ob.solve(nums)):
    print("true")
else:
    print("false")
