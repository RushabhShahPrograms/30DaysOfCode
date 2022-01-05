'''
given a number check whether it contains even number of digits or odd number of digits. consider thw sample case given below.

Input Format
12

Constraints
1 <= nums.length <= 500

Output Format
Even

Sample Input 0
12

Sample Output 0
Even
'''
n = int(input())
if(n%2==0):
    print("Even")
else:
    print("Odd")
