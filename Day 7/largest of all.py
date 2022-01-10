'''
Given a list of integers nums, return whether the largest number is bigger than the second-largest number by more than two times.
Array can be in unsorted manner.

Input Format
n = 3 nums = [3, 9, 6]

Constraints
2 ≤ n ≤ 100,000 where n is the length of nums

Output Format
false
9 is not bigger than 2 * 6.

Sample Input 0
3
3 19 9

Sample Output 0
true

Sample Input 1
3
3 6 12

Sample Output 1
false

Explanation 1
12 is not bigger than 2 * 6, they're 
'''

n = int(input())
a = []
while True:
    att = input()
    try:
        a = [int(val) for val in att.split(" ")]
        if(len(a) == n):
            break
        else:
            print("error")
    except:
        print("error")

a.sort()
b = a[-2]*2
if(b<a[-1]):
    print("true")
else:
    print("false")
