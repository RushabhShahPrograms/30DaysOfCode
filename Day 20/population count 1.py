'''
You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.

Return the earliest year with the maximum population.

Example 1:

Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
Explanation: The maximum population is 1, and 1993 is the earliest year with this       population.
Input Format

length 2

logs = [[1993,1999],[2000,2010]]

Constraints

1 <= logs.length <= 100
1950 <= birthi < deathi <= 2050
Output Format

1993

Sample Input 0

2
1993 1999
2000 2010
Sample Output 0

1993
Explanation 0

The maximum population is 1, and 1993 is the earliest year with this population.

Sample Input 1

3
1950 1961
1960 1971
1970 1981
Sample Output 1

1960
'''

from collections import defaultdict
def solve(matrix):
    d=defaultdict(int)
    res=[2051,0]
    for YOB, YOD in matrix:
        for year in range(YOB, YOD):
            d[year] += 1
            if d[year] >= res[1]:
                if d[year] > res[1]:
                    res = [year,d[year]]
                else:
                    res = [min(year,res[0]),res[1]]
    return res[0]

n=int(input())
matrix = [0]*n
for i in range(n):
    matrix[i] = list(map(int, input().split()))
    
print(solve(matrix))
