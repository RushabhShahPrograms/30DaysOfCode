'''
consider a list of numbers, you will have to find product of those numbers whose product is the highest of all. Input nums = [5, 1, 7] Output 35 Explanation 35 is the largest product that can be made from 5 * 7

Input Format
5 1 7

Constraints
n<10000 where n is the length of list

Output Format
35

Sample Input 0
3
5 1 7

Sample Output 0
35
'''

num = int(input())
lit = list(map(int,input().strip().split()))[:num]
n = len(lit)
if(n<2):
    print("No greater number")
    
b = lit[1]
a = lit[0]
for i in range(0,n):
    for j in range(i+1,n):
        if(lit[i]*lit[j] > a*b):
            a = lit[i]
            b = lit[j]
print(a*b)
