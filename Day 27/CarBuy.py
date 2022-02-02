'''
Given a list of integers prices representing prices of cars for sale, and a budget k, return the maximum number of cars you can buy.

Input Format

length = 5
k = 95
prices = [90, 30, 20, 40, 90]
Constraints

n ≤ 200,000 where n is the length of prices
Output Format

3

Sample Input 0

5
95
90 30 20 40 90
Sample Output 0

3
Explanation 0

We can buy the cars with prices 30, 20, and 40.

Sample Input 1

4
50
60 90 55 75
Sample Output 1

0
Explanation 1

We cannot afford any of these cars.
'''

class Solution:
    def solve(self, prices, k):
        count =0
        prices.sort()
        for i in range(len(prices)):
            if(prices[i]<=k):
                k = k-prices[i]
                count += 1
            else:
                break
        return count

ob = Solution()
n=int(input())
k=int(input())
prices=list(map(int, input().split()))[:n]
print(ob.solve(prices, k))
