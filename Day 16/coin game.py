'''
You have n coins and you want to build a staircase with these coins. 
The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
Given the integer n, return the number of complete rows of the staircase you will build.

Input Format
n = 5

Constraints
1 <= n <= 231 - 1

Output Format
2

Sample Input 0
5

Sample Output 0
2
'''

def coin(n):
    start=0
    end=n
    while(start+1<end):
        mid=start+(end-start)//2
        if(mid*(mid+1)//2<=n):
            start=mid
        else:
            end=mid
    if(end*(end+1)//2<=n):
        return end
    return start

n = int(input())
print(coin(n))
