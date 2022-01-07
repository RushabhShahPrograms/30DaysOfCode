'''
find out the possible positions with a people in front and b people behind in a line of n people.
You are given integers n, a and b. You are standing in a line of n people. You don't know which position you're in, but you know there are at least a people in front of you and at most b people behind you.
Return the number of possible positions you could be in.
Example 1:
Input:
n = 10
a = 3
b = 4

Output:
5

Explanation
There's 10 people and at least 3 are in front and at most 4 are behind.
This means you can be in indexes [0, 1, 2, 3, 4]. For example, at index 0, 9 people are in front, 0 are behind.

Input Format
n = 10
a = 3
b = 4

Constraints
0

Output Format
5
'''
def fpo(n,a,b):
    x = n-max(a+1,n-b)+1
    print(x)
    
n = int(input())
a = int(input())
b = int(input())
fpo(n,a,b)
