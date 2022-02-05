'''
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that : - i != j - 0 <= i, j < arr.length - arr[i] == 2 * arr[j]

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
Input Format

length = 4
arr = [10,2,5,3]
Constraints

2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3
Output Format

true

Sample Input 0

4
10 2 5 3
Sample Output 0

true
Explanation 0

N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Sample Input 1

4
3 1 7 11
Sample Output 1

false
Explanation 1

In this case does not exist N and M, such that N = 2 * M.
'''

class DoubleExist:
    def checkIfExist(self, arr):
        for i in range(len(arr)):
            for j in (arr[:i]+arr[i+1:]):
                if 2*arr[i] == j:
                    return True
        return False

ob=DoubleExist()
n=int(input())
arr=list(map(int,input().split()))[:n]
if(ob.checkIfExist(arr)==True):
    print("true")
else:
    print('false')
