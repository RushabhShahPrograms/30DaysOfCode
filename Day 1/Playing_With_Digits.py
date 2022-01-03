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
