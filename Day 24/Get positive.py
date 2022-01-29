'''
You are given a list of integers nums. Return the minimum positive value we can append to the beginning of nums such that prefix sums of the resulting list contains numbers that are all greater than 0.

Example 1
Input
nums = [2, -5, 3, 2]
Output
4
Explanation
If we have append 4 to the list then we have [4, 2, -5, 3, 2].
The prefix sums are then [4, 6, 1, 4, 6], all of which are > 0.
Input Format

4 2 -5 3 2

Constraints

n ≤ 100,000 where n is the length of nums

Output Format

4

Sample Input 0

4
2 -5 3 2
Sample Output 0

4
Sample Input 1

1
2
Sample Output 1

1
'''

class Solution:
    def minStartValue(self, nums):
        min_n=0
        sum_n=0
        for i in nums:
            sum_n+=i
            min_n=min(sum_n,min_n)
            
            
        return 1-min_n
    
ob=Solution()
n=int(input())
nums=list(map(int, input().split()))[:n]
print(ob.minStartValue(nums))
