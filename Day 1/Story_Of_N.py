'''
Raam is superstitious. He will only use a particular digit of number as a roll number if its sum of digits is 11. Find those numbers having sum 11.
Here, find the Nth number having sum 11. So, in short: Given an integer value n, find out the n-th positive integer whose sum is 11.

Input Format
2

Constraints
0 < n < 50

Output Format
38

Sample Input 0
3

Sample Output 0
47
'''

import itertools
def findNth(n):
    count = 0
    for c in itertools.count():
        sum = 0
        x = c
        while(x):
            sum = sum + x % 10
            x = x // 10

        if (sum == 11):
            count = count + 1

        if (count == n):
            return c
    return -1

if __name__=='__main__':
    a = int(input())
    print(findNth(a))
