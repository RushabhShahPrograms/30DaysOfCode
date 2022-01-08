'''
For each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i]. Return the answer in an array.

Input Format
n = 5
nums = 8 1 2 2 3

Constraints
2 <= nums.length <= 500 0 <= nums[i] <= 100

Output Format
4 0 1 1 3
'''

n = int(input())
arr1 = []
arr2 = []

while True:
    att = input()
    try:
        arr1 = [int(val) for val in att.split(" ")]
        if(len(arr1) == n):
            break
        else:
            print("error")
    except:
        print("error")

res = [0]*len(arr1)
temp = [0]*101
for i in range(0,len(arr1)):
    temp[arr1[i]] = temp[arr1[i]] + 1
for i in range(1,101):
    temp[i] = temp[i] + temp[i-1]
for i in range(0,len(arr1)):
    if(arr1[i]==0):
        res[i]=0
    else:
        res[i] = temp[arr1[i]-1]

print(*res,sep = " ")
