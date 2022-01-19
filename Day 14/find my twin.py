'''
You are given a list nums of length n + 1 picked from the range 1, 2, ..., n. By the pigeonhole principle, there must be a duplicate. Find and return it. 
There is guaranteed to be exactly one duplicate. Bonus: Can you do this in \mathcal{O}(n) O(n) time and \mathcal{O}(1) O(1) space?
Example 1 Input length=4 nums = [1, 2, 3, 1] Output 1

Input Format
5 4 2 1 3 2

Constraints
n ≤ 10,000

Output Format
2

Sample Input 0
4
1 2 3 1

Sample Output 0
1
'''

def solve(nums):
    s = set()
    for i in nums:
        a = i in s
        if a == True:
            return i
        else:
            s.add(i)

n = int(input())
nums = list(map(int, input().split()))
print(int(solve(nums)))
