'''
Given two strings s0 and s1, return whether they are phoenix strings of each other.

Phoenix strings are a word, phrase, or name formed by rearranging the letters of another,

eg. such as spar, formed from rasp.

Input Format

s0 = "listen"

s1 = "silent"

Constraints

n ≤ 100,000 where n is the length of s0
m ≤ 100,000 where m is the length of s1
Output Format

true

Sample Input 0

listen
silent
Sample Output 0

true
Sample Input 1

bedroom
classroom
Sample Output 1

false
'''

def check(s0,s1):
    list1=list(s0)
    list2=list(s1)
    
    list1.sort()
    list2.sort()
    
    position=0
    matches=True
    
    while position<len(s0) and matches:
        if list1[position]==list2[position]:
            position=position+1
        else:
            matches=False
    
    return matches
    
s0=input()
s1=input()

if check(s0,s1)==True:
    print("true")
else:
    print("false")
