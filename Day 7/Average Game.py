'''
Given a list of integers nums and an integer k, return true if you can remove exactly one element from the list to make the average equal to exactly k.

Input Format

Here n is length of nums, k is the avetage number and nums is the array.
n = 4
k = 2
nums = [1, 2, 3, 10]

Constraints
2 ≤ n ≤ 1,000 where n is length of nums
nums[i], k ≤ 1,000,000

Output Format
true
'''

n = int(input())
k = int(input())

l = []
while True:
    att = input()
    try:
        l = [int(val) for val in att.split(" ")]
        if(len(l) == n):
            break
        else:
            print("error")
    except:
        print("error")
        
s = sum(l)
t = k*(len(l)-1)
for i in l:
    if(s-i == t):
        print("true")
        break
else:
    print("false")
