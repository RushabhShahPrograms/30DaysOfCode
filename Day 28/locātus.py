'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Input Format

6 8 5 7 7 8 8 10

Constraints

0 <= nums.length <= 105 -109 <= nums[i] <= 109 nums is a non-decreasing array. -109 <= target <= 109

Output Format

3 4

Sample Input 0

6
8
5 7 7 8 8 10
Sample Output 0

3 4
Sample Input 1

6
6
5 7 7 8 8 10
Sample Output 1

-1 -1
'''

def findFirstAndLast(arr, n, x) :
    first = -1
    last = -1
    for i in range(0, n) :
        if (x != arr[i]) :
            continue
        if (first == -1) :
            first = i
        last = i
     
    if (first != -1) :
        print(first, last)
    else :
        print("-1", "-1")

n = int(input())
x = int(input())
arr = list(map(int, input().split()))[:n]
findFirstAndLast(arr, n, x)
