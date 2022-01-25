'''
Given a string s of words delimited by spaces, reverse the order of words.

Input Format
sentence = "hello there my friend"

Constraints
n ≤ 100,000 where n is the length of s

Output Format
friend my there hello

Sample Input 0
hello there my friend

Sample Output 0
friend my there hello
'''

def word(str):
    i=len(str)-1
    start=end=i+1
    result=''
    
    while i>=0:
        if str[i] == ' ':
            start = i+1
            while start != end:
                result += str[start]
                start += 1
            result += ' '
            end = i
        i -= 1
    start = 0
    while start!= end:
        result += str[start]
        start += 1
    return result

str = input()
print(word(str))
