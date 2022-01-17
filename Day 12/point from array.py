'''
Given a list of unique integers nums sorted in ascending order, return the minimum i such that nums[i] == i. If there's no solution, return -1.
This should be done in \mathcal{O}(log(n))O(log(n)) time.

Input Format
length = 5 

arr = -5  -2  0  3  4

Constraints
n ≤ 100,000 where n is the length of nums.

Output Format
3

Sample Input 0
5
-5 -2 0 3 4

Sample Output 0
3

Explanation 0
Both nums[3] == 3 and nums[4] == 4 but 3 is smaller.
'''

def pointofarray(arr):
    for i,v in enumerate(arr):
        if(i==v):
            return i
    return -1

n = int(input())
arr = list(map(int, input().split()))
print(pointofarray(arr))
