'''
The array-form of an integer num is an array representing its digits in left to right order.
For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

Example 1:

Input: num = [1,2,0,0], k = 34

Output: [1,2,3,4]

Explanation: 1200 + 34 = 1234

Input Format
length = 3
num = [2,1,5]
k = 806

Constraints
1 <= num.length <= 104
0 <= num[i] <= 9
num does not contain any leading zeros except for the zero itself.
1 <= k <= 104

Output Format
[1,0,2,1]
'''

n = int(input())
num = list(map(int, input().split()))
k = int(input())

value=0
for val in num:
    value = value*10 +val
sum = value+k

if(sum==0):
    print(0)

result = []

while(sum>0):
    result.insert(0,sum%10)
    sum //= 10
print(*result,end=" ")
