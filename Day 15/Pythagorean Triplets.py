'''
Given a list of positive integers nums, return whether there exist integers a, b, and c such that a ** 2 + b ** 2 = c ** 2.

Explanation:
For e.g.:
nums = [5, 1, 7, 4, 3]
3, 4, 5 are in the array and 3^2 + 4^2 = 5^2.

Input Format
length = 5 nums = 5 1 7 4 3

Constraints
0 ≤ n ≤ 1,000 where n is the length of nums

Output Format
true

Sample Input 0
5
5 1 4 7 3

Sample Output 0
true

Explanation 0
3, 4, 5 are in the array and 3^2 + 4^2 = 5^2.
'''

def Triplet(n,nums):
    j=0
    for i in range(n-2):
        for k in range(j+1,n):
            for j in range(i+1,n-1):
                x=nums[i]*nums[i]
                y=nums[j]*nums[j]
                z=nums[k]*nums[k]
                if(x==y+z or y==x+z or z==x+y):
                    return 1
    return 0
    
n = int(input())
nums = list(map(int, input().split()))
if(Triplet(n,nums)):
    print("true")
else:
    print("false")
