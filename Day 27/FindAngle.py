'''
Given a clock time with hour and integer minutes, determine the smaller angle between the hour and the minute hands and floor it to the nearest integer.

Note that the hour hand moves too.

Bonus: When, during the course of a day, will the angle be zero?

Input Format

hour = 12
minutes = 22
Constraints

0 ≤ hour ≤ 23
0 ≤ minutes ≤ 59
Output Format

121

Sample Input 0

12
22
Sample Output 0

121
Explanation 0

the smaller angle between the hour and the minute hands is 121.

Sample Input 1

4
12
Sample Output 1

54
'''

class Solution:
    def solve(self, hour, minutes):
        hour = hour % 12
        hdeg = hour * 30 + minutes * 0.5
        Mdeg = minutes * 6
        angle = min(abs(hdeg - Mdeg), 360 - abs(hdeg - Mdeg))
        return int(angle)
    
ob=Solution()
hour=int(input())
minutes=int(input())
print(ob.solve(hour,minutes))
