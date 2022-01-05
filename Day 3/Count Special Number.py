'''
The task is to count the number of elements that occurs exactly floor(N/K) times in the array.

Input:
5 2
1 4 1 2 4

Output:
2

Explanation:
In the given array, 1 and 4 occurs floor(5/2) = 2 times. So count is 2.
First line contains 2 integers N and K seperated by spaces. Second line contains N array elements seperated by spaces.

Input Format
5 2
1 4 1 2 4

Constraints
1 <= N <= 103 1 <= Ai <= 103

Output Format
2

Sample Input 0
5 2
1 4 1 2 4

Sample Output 0
2
'''
from array import *
N,K = map(int, input().split())
a =  list(map(int, input().strip().split()))
freq = []
freq = [-1 for i in range(len(a))]
count2=0
floor = N//K
for i in range(0,len(a)):
    count = 1
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            count = count + 1
            freq[j] = 0
    if(freq[i]!=0):
        freq[i]=count
    if(count == floor and freq[i] == floor):
        count2 = count2 + 1
print(count2)
