'''
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in the jth bank. 
Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

Example: Input:
m = 2, n = 3,
accounts = [[1,2,3],[3,2,1]]

Output:
6

Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.

Input Format
m = 2, n = 3,
accounts = [[1,2,3],[3,2,1]]

Constraints
m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100

Output Format
6
'''

def Wealth(accounts):
    return max(map(sum, accounts)) 

m = int(input())
n = int(input())
accounts = [0]*m
for i in range(m):
    accounts[i] = list(map(int, input().split()))
print(Wealth(accounts))
