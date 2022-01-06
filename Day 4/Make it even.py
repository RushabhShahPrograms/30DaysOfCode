'''
Given an array nums of integers, return how many of them contain an even number of digits.
For eg:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits

Input Format
5 12 345 2 6 7896

Constraints
1 <= nums.length <= 500
1 <= nums[i] <= 105

Output Format
2

Sample Input 0
5
12 345 2 6 7896

Sample Output 0

2
'''

def countevendigits(nums):
    count=0
    for i in range(len(nums)):
        num = nums[i]
        if(len(str(num))%2==0):
            count = count + 1
    return count

n = int(input())
lt = []
while True:
    att = input()
    try:
        lt = [int(val) for val in att.split(" ")]
        if(len(lt) == n):
            break
        else:
            print("error")
    except:
        print("error")

o = countevendigits(lt)
print(o)
