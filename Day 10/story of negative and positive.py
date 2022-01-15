'''
Given a list of integers nums, return the largest integer k where k and -k both exist in nums (they can be the same integer). 
If there's no such integer, return -1. 

Example 1:
Input:
length= 6
nums = [-4, 1, 8, -5, 4, -8]

Output:
8
here 8 is the largest integer where 8 and -8 are present in array

Example 2:

Input:
length= 4
nums = [5, 6, 1, -2]

Output:
-1
here there is no whose negative and positive format exists 
'''

def story(a):
    res = -1
    table = {}
    for n in a:
        if -n in table or not n:
            res = max(res, abs(n))
        table[n] = True
    return res

n = int(input())
a = [int(n) for n in input().split()]
print(story(a))
