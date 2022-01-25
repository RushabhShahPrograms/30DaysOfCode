'''
Given a string s representing a number in base 3 (consisting only of 0, 1, or 2), 
return its decimal integer equivalent. This should be implemented directly without using a built-in function.

For e.g.:
If s = "10", 
Then output will be 3.

Input Format
10

Constraints
The input will be greater than 0.

Output Format
3
'''

s = input()
ans=0
for i in s:
    ans=ans*3+int(i)
print(ans)
