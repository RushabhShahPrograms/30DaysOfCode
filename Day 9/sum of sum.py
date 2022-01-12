'''
Given a positive integer n, sum all of its digits to get a new number. Repeat this operation until the new number is less than 10 and return it.

Input :
n = 8835

Output:
6  

Explanation:
8 + 8 + 3 + 5 = 24  
2 + 4 = 6 
here 6<10 so print 6. 
'''

sum = 0
n = int(input())
while(n!=0):
    digit = int(n%10)
    sum += digit
    n /= 10
sum1 = 0


while(sum!=0):
    digit1 = int(sum%10)
    sum1 += digit1
    sum /= 10
        
print(sum1)
