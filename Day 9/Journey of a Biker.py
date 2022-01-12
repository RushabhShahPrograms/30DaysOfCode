'''
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

For e.g.:
The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

Input Format:
length of gain= 6
gain = 0 -5 -4 1 1 -6

Constraints
n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100

Output Format
1
'''
n = int(input())
gain = [int(n) for n in input().split()]

res,height = 0,0
for i in gain:
    height += i
    res = max(res,height)
print(res)
