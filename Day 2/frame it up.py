'''
Given a decimal number as input, we need to write a program to convert the given decimal number into equivalent binary number.

Input Format
7

Constraints
0

Output Format
111

Sample Input 0
7

Sample Output 0
111

Sample Input 1
11

Sample Output 1
1011
'''

num = int(input())
print("{0:b}".format(int(num)))
