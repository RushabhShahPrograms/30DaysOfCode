'''
Given an integer n, return a list with each number from 1 to n, except if it's a multiple of 3 or has a 3, 6, or 9 in the number, it should be the string "clap". Note: return the number as a string.

Input Format

16

Constraints

n ≤ 100,000
Output Format

1 2 clap 4 5 clap 7 8 clap 10 11 clap clap 14 clap clap

Sample Input 0

16
Sample Output 0

1 2 clap 4 5 clap 7 8 clap 10 11 clap clap 14 clap clap
'''

n = int(input())
string = "clap"
ls = [str(i) for i in range(1,n+1)]
for i in range(len(ls)):
    if(int(ls[i])%3==0):
        ls[i]=string
    elif '3' in ls[i]:
        ls[i]=string
    elif '6' in ls[i]:
        ls[i]=string
    elif '9' in ls[i]:
        ls[i]=string
print(*ls,end=" ")
