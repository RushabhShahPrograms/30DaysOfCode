'''
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

For e.g.:

Input:
n = 19

Output:
true

Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Input Format
19

Constraints
1 <= n <= 231 - 1

Output Format
true
'''

def sum(n):
    sq = 0
    while(n!=0):
        d=n%10
        sq+=d*d
        n=n//10
    return sq;

def Happy(n):
    s=set()
    s.add(n)
    while(True):
        if(n==1):
            return True;
        n=sum(n)
        if n in s:
            return False
        s.add(n)
    return False;

n = int(input())
if(Happy(n)):
    print("true")
else:
    print("false")
