'''
Given a list of integers nums, return whether there's an integer whose frequency in the list is same as its value.
first take the number of integers and then take the numbers seperated by space.

Example 1 :

Input :
Length = 5
nums = 7 9 3 3 3

Output:
true

Explanation:
The number 3 appears 3 times.
the output should be either true or false.
'''

n = int(input())
a = [int(n) for n in input().split()]

a.sort()
max_count=1
res=a[0]
curr_count=1

for i in range(1,n):
    if(a[i] == a[i-1]):
        curr_count += 1
    else:
        if(curr_count>max_count):
            max_count = curr_count
            res = a[i-1]
        curr_count = 1
        
if(curr_count>max_count):
    max_count = curr_count
    res = a[n-1]

if(max_count == res):
    print("true")
else:
    print("false")
