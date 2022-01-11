'''
Given a list of integers prices representing the stock prices of a company in chronological order, return the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

Note: You are not required to buy or sell the stock. example: Input Length of prices = 6 prices = [9, 11, 8, 5, 7, 10] Output 5 Explanation You can buy at 5 and sell at 10. As 5 is the minimum price of the stock we may buy at 5 and sell at 10 as it is increasing. our profit might have been zero if the price would have decreased.

Input Format

6 9 11 8 5 7 10

Constraints

n ≤ 100,000 where n is the length of prices

Output Format

5
'''


n = int(input())
l = [int(n) for n in input().split()]
mp =0
minsofar = l[0]
for i in range(0,len(l)):
    minsofar = min(minsofar,l[i])
    profit = l[i] - minsofar
    mp = max(mp,profit)
print(mp)
