'''
You are given a list of integer rooms and an integer target. Return the first integer in rooms that's target or larger. If there is no solution, return -1. Example 1: Input:

length=5
rooms = [15, 10, 30, 50, 25]
target = 20
Output:

30
Explanation:

30 is the first room that's at least as large as 20.
Input Format

5
15 10 30 50 25
20

Constraints

0 ≤ n ≤ 100,000 where n is the length of room

Output Format

30
'''
n = int(input())
a = [int(n) for n in input().split()]
k = int(input())

print(next((x for x in a if x >= k), -1))
