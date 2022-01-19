'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the array in the form [x1,y1,x2,y2,...,xn,yn].
First line of input contains 2N (2N is the numbe of elements) The second line contains array on 2N elements seperated by spaces

Example 1: Input:
legth = 6 nums = [2,5,1,3,4,7], n = 3

Output:
[2,3,5,4,1,7]

Explanation:
Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
'''

def shuffle(nums, n):
    ans=[]
    for i in range(n):
        ans.append(nums[i])   
        ans.append(nums[n+i])
    return ans

n = int(input())
nums = list(map(int, input().split()))
print(*shuffle(nums,n),end=" ")
