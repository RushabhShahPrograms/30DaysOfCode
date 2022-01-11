'''
Given two arrays of integers nums and index. Your task is to create a target array under the following rules.
Initially the target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in the target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.
It is guaranteed that the insertion operations will be valid.

Input Format

5 5 0 1 2 3 4 0 1 2 2 1

Constraints

0 < nums < 1000 0 < index < 1000

Output Format

0 4 1 3 2
'''
n= int(input())
k= int(input())
s1 = input()
s2 = input()
nums = s1.split()
index = s2.split()
nums = list(map(int, nums))
index = list(map(int, index))
ans = []
for num,ind in zip(nums,index):
    ans.insert(ind,num)
print(*ans, sep=" ")
