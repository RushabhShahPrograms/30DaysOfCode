'''
Phoenix Numbers are the numbers whose sum of factorial of digits is equal to the original number. Given a number, check if it is a Phoenix Number or not. Print Yes or No
Sum of digit factorials = 1! + 4! + 5! = 145

Input Format
145

Constraints
0

Output Format
Yes

Sample Input 0
145

Sample Output 0
Yes
'''

num = int(input())
temp = num
sum = 0
while(num>0):
    digit = num%10
    fact=1
    for i in range(1,digit+1):
        fact = fact * i
    sum = sum + fact
    num = num//10
    
if(sum == temp):
    print("Yes")
else:
    print("No")
