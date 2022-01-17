'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
and an integer n(number of flowers to b planted), return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1

Output:
true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2

Output: false

Input Format
5
1 0 0 0 1
2

Constraints
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

Output Format
false
'''

def flower(flowerbed,n):
    if(n==0):
        return True
    flowerbed = [0] + flowerbed + [0]
    size = len(flowerbed)
    for i in range(1,size-1):
        if(flowerbed[i]):
            continue
        elif(flowerbed[i-1] == flowerbed[i+1] == 0):
            n -= 1
            flowerbed[i] = 1
            if(n==0):
                return True
    return False

length = int(input())
flowerbed = list(map(int, input().split()))
n = int(input())

if(flower(flowerbed,n)==True):
    print("true")
else:
    print("false")
