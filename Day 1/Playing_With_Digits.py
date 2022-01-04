'''
Take 'n' as the first line of input ('n' is total number of digits). Then input the number with 'n' digits in new line. Find the sum of digits and product of digits and then the difference of them.

Input Format
3
234

Constraints
0 < n < 5

Output Format
15

Sample Input 0
4
4421

Sample Output 0
21
'''
n = int(input())
sum,product,digit=0,1,0
num = int(input())
while(num>0):
    digit = num % 10
    sum = sum + digit
    product = product * digit
    num=num//10

if(product>sum):
    print(product-sum)
else:
    print(sum-product)
