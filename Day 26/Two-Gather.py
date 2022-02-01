'''
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
Input Format

11 1

Constraints

1 <= a.length, b.length <= 104 a and b consist only of '0' or '1' characters. Each string does not contain leading zeros except for the zero itself.

Output Format

100

Sample Input 0

11
1
Sample Output 0

100
Sample Input 1

1010
1011
Sample Output 1

10101
'''

class Solution:
    def addBinary(self, a, b):
        a, b = list(a), list(b)
        carry = 0
        ans = ""
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            carry, remain = divmod(carry, 2)
            ans += str(remain)
        return ans[::-1]
    
a=input()
b=input()
ob=Solution()
print(ob.addBinary(a,b))
