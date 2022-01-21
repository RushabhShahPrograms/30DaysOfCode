'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Input Format
length = 4
nums = [1, 3, 5, 6]
target = 5

Constraints
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

Output Format
2

Sample Input 0
6
1 3 5 6 13 64
13

Sample Output 0
4
'''

def find_index(n,arr,target):

    start = 0
    end = n - 1
    
    while start<= end:
        mid =(start + end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid-1
    return end + 1

n = int(input())
arr = list(map(int, input().split()))
target = int(input())
print(find_index(n,arr,target))
