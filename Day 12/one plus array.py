'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Input Format
length = 3
array = [1, 2, 3]

Constraints
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

Output Format
1 2 4

Sample Input 0
3
1 2 3

Sample Output 0
1 2 4

Explanation 0
Input: digits = [1,2,3] Output: [1,2,4] Explanation: The array represents the integer 123. Incrementing by one gives 123 + 1 = 124. Thus, the result should be [1,2,4].
'''

n = int(input())
arr = list(map(int, input().split()))

num=int(''.join([str(arr) for arr in arr]))+1
mylist = [int(d) for d in list(str(num))]
print(*mylist,end=" ")
