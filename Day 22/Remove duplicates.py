'''
Given a list of integers nums, remove numbers that appear multiple times in the list, while maintaining order of the appearance in the original list.

It should use O(k) space where k is the number of unique integers.

Input Format

length = 7

nums = [1, 3, 5, 0, 3, 5, 8]

Constraints

n ≤ 100,000 where n is the length of nums
Output Format

1 0 8

Sample Input 0

7
1 3 5 0 3 5 8
Sample Output 0

1 0 8
Explanation 0

Only [1, 0, 8] are unique in the list and that's the order they appear in.

Sample Input 1

8
0 1 3 1 3 4 6 5
Sample Output 1

0 4 6 5
'''

def solve(nums):
    dict={}
    for i in nums:
        if i not in dict:
            dict[i]=0
        dict[i]=dict[i]+1
    return [k for k, v in dict.items() if v==1]

n=int(input())
nums=list(map(int, input().split()))[:n]
print(*solve(nums),end=" ")
