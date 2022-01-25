'''
Given an integer array nums of length n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).' 
For e.g.: nums = [1,2,1] Then output will be [1,2,1,1,2,1] Explanation: The array ans is formed as follows: - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]] - ans = [1,2,1,1,2,1]

Input Format
1 2 1

Constraints
n == nums.length 1 <= n <= 1000 1 <= nums[i] <= 1000

Output Format
1 2 1 1 2 1

Sample Input 0
3
1 2 1

Sample Output 0
1 2 1 1 2 1 

Sample Input 1
4
1 3 2 1

Sample Output 1
1 3 2 1 1 3 2 1 
'''

n = int(input())
arr = list(map(int, input().split()))
print(*arr,*arr,end=" ")
