'''
Given a number N. The task is to find the sum of N Harmonic Number. Let the nth harmonic number be Hn. The harmonic series is as follows:
H1 = 1
H2 = H1 + 1/2
H3 = H2 + 1/3
H4 = H3 + 1/4
. . .
Hn = Hn-1 + 1/n

Input Format

5

Constraints

0

Output Format

2.2833
'''



n = int(input())
sum=0
for i in range(1,n+1):
    sum += 1/i
print("Harmonic sum upto 4 decimal places:","{0:.4f}".format(sum))
