'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
Example 1:
Input:length of nums = 4
nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Input Format
n = 4
arr = 1 2 3 4

Constraints
0 < n < 100

Output Format
1 3 6 10

Sample Input 0
4
1 2 3 4

Sample Output 0
1 3 6 10 
'''

def runningSum(listf):
    nt = len(listf)
    ans = []
    ans = [0]*len(listf)
    ans[0]=listf[0]
    for i in range(1,nt):
        ans[i] = ans[i-1] + listf[i]
    return ans

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

o = runningSum(lt)
print(*o, sep = " ")
