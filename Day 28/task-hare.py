'''
You are given a list of integers tasks and another list of integers people. The integer tasks[i] represents the amount of strength required to perform the ith task. people[i] represents the amount of strength the ith person has.

Return the number of tasks that can be finished if one person can perform at most one task.

Input Format

len1 = 4
len2 = 4
tasks = [3, 2, 9, 13]
people = [10, 5, 2, 1]
Constraints

n ≤ 100,000 where n is the length of tasks
m ≤ 100,000 where m is the length of people
Output Format

3

Sample Input 0

4
4
3 2 9 13
10 5 2 1
Sample Output 0

3
Explanation 0

First person can perform task 9
Second person can perform task 3
Third person can perform task 2
Fourth person can't perform any tasks
Sample Input 1

5
4
3 1 2 9 13
10 5 2 1
Sample Output 1

4
'''

class Solution:
    def solve(self, tasks, people):
        tasks.sort()
        people.sort()
        ct=0
        ind=0
        for i in range(len(people)):
            for j in range(ind,len(tasks)):
                if people[i]>=tasks[j]:
                    ct+=1
                    ind+=1
                    break
                else:
                    break
        return ct


len1 = int(input())
len2 = int(input())
tasks = list(map(int, input().split()))[:len1]
people = list(map(int, input().split()))[:len2]
ob=Solution()
print(ob.solve(tasks, people))
