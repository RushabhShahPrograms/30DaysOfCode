'''
Given a list of numbers nums and a number k, return whether any two elements from the list add up to k. Note: You may not use the same element twice.
Numbers can be negative or 0.

Input Format
5 35 8 18 3 22 11

Constraints
n ≤ 100,000 where n is the length of nums

Output Format
True

Sample Input 0
5
35 8 18 3 22
11

Sample Output 0
true

Explanation 0
8 + 3 = 11
'''
def sum(nums,k):
    temp = set()
    for num in nums:
        if num in temp:
            return ("true")
        temp.add(k-num)
    return ("false")

n = int(input())
nums = list(map(int, input().split()))
k = int(input())
print(sum(nums,k))
