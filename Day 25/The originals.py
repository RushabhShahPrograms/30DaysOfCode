'''
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Input Format

6 1 2 2 1 1 3

Constraints

1 <= arr.length <= 1000 -1000 <= arr[i] <= 1000

Output Format

true

Sample Input 0

6
1 2 2 1 1 3
Sample Output 0

true
Sample Input 1

2
1 2
Sample Output 1

false
Sample Input 2

6
1 3 1 3 4 3
Sample Output 2

true
'''

from collections import Counter
def unique(arr):
    counter = Counter(arr).values()
    if(len(counter) == len(set(counter))):
        return True
    else:
        return False

n=int(input())
arr=list(map(int, input().split()))[:n]
if(unique(arr)==True):
    print("true")
else:
    print("false")
