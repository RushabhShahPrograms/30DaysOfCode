'''
Given a number N, check whether the number is an Phoenix number or not.
A number is called Phoenix number if and only if its square ends in the same digits as the number itself.
Input: N = 76
Output: Phoenix number
Explanation:
76^2 = 5776 which ends with 76 therefore it is an Phoenix number.
if it is not then print Not a phoenix number

Input Format
76

Constraints
0

Output Format
Phoenix number

Sample Input 0
76

Sample Output 0
Phoenix number

Sample Input 1
7

Sample Output 1
Not a phoenix number.
'''
def isphoneixnumber(n):
    s = n*n
    while(n>0):
        if(n%10!=s%10):
            return False
        n//=10
        s//=10
    return True

n = int(input())
if isphoneixnumber(n):
    print("Phoenix number")
else:
    print("Not a phoenix number.")
