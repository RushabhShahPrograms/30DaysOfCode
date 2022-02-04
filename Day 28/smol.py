'''
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target. Note that the letters wrap around. For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.

Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"

Example 3:
Input: letters = ["c","f","j"], target = "d"
Output: "f"
Input Format

target = a
len = 3
array = [c f j]
Constraints

2 <= letters.length <= 104 letters[i] is a lowercase English letter. letters is sorted in non-decreasing order. letters contains at least two different characters. target is a lowercase English letter.

Output Format

c

Sample Input 0

a
3
cfj
Sample Output 0

c
Sample Input 1

c
3
cfj
Sample Output 1

f
Sample Input 2

d
3
cfj
Sample Output 2

f
'''

def solve(letters, target):
    l = 0
    r = len(letters) - 1
    while l <= r:
        mid = (l + r)//2
        if letters[mid] > target:
            r = mid -1
        else:
            l = mid + 1
    return letters[l % len(letters)]

target = input()
n = int(input())
letters = list(input())
print(solve(letters, target))
