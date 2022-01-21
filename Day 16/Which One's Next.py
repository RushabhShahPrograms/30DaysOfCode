'''
Given a list of integers nums, return the number of elements x there are such that x + 1 exists as well.
Explanation:

For e.g.:

nums = [3, 1, 2, 2, 7], 
We can take
1. 1 since 1 + 1 exists in the list.
2. 2 since 2 + 1 exists in the list.
3. Another 2.
So total output is 3.

Input Format
length = 5,
nums = [3, 1, 2, 2, 7]

Constraints
n ≤ 100,000 where n is the length of nums

Output Format
3

Sample Input 0
5
3 1 2 2 7

Sample Output 0
3

Explanation 0

We can take

1 since 1 + 1 exists in the list.
2 since 2 + 1 exists in the list.
Another 2.
So total output is 3.
'''

def count(n,arr):
    mp=dict()
    for i in range(n):
        mp[arr[i]] = mp.get(arr[i],0)+1
    answer=0
    for i in mp:
        if i+1 in mp:
            answer += mp[i]
    return answer

n = int(input())
arr = list(map(int, input().split()))
print(count(n,arr))
