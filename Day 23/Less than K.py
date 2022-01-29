'''
Given a list of integers nums and an integer k, return the maximum possible index i where nums[0] + nums[1] + ... + nums[i] ≤ k. Return -1 if no valid i exists.

Input Format

length = 5
k = 4
nums = [3, -5, 4, 1, 6]
Constraints

0 ≤ n ≤ 1,000 where n is the length of nums.
-1,000 ≤ nums[i] ≤ 1,000
0 ≤ k ≤ 10 ** 9
Output Format

3

Sample Input 0

5
4
3 -5 4 1 6
Sample Output 0

3
Explanation 0

The largest i here is 3, since we have nums[0] + ... + nums[3] = 3 and if we added the next number (6) the sum would no longer be less than k.

Sample Input 1

2
0
1 1
Sample Output 1

-1
'''

n = int(input())
k = int(input())
lst = list(map(int, input().split()))
item = lst[0]
cumulative_lst = []
for i in range(len(lst)):
    if i!=0:
        item+=lst[i]
        cumulative_lst.append(item)
    else:
        cumulative_lst.append(lst[i])
for i in range(len(cumulative_lst)):
    if cumulative_lst[i]<=k:
        continue
    else:
        temp = i-1
        break
print(temp)
