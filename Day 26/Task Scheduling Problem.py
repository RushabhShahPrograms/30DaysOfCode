'''
You are given a list of integers tasks where each different integer represents a different task type, and a non-negative integer k. Each task takes one unit of time to complete and each task must be done in order, but you must have k units of time between doing two tasks of the same type. At any time, you can be doing a task or waiting.

Return the amount of time it takes to complete all the tasks.

Input Format

length = 4
k = 2
nums = [0 1 0 1]
Constraints

n ≤ 100,000 where n is the length of tasks
Output Format

5

Sample Input 0

4
2
0 1 0 1
Sample Output 0

5
Explanation 0

The tasks get run the following way: [0, 1, wait, 0, 1]. Note that before running the second 0 task we must wait one unit to have 2 units of time before running it again. We can just run the second 1 task right away since it has already been 2 units of time since we last did task 1.

Sample Input 1

4
1
0 0 1 1
Sample Output 1

6
Explanation 1

The tasks get run the following way: [0, wait, 0, 1, wait, 1].
'''

class Solution:
    def solve(self, tasks, k):
        last_times = {}
        cur_time = 0
        for j, task in enumerate(tasks):
            if task in last_times and cur_time - last_times[task] <= k:
                wait_time = k - (cur_time - last_times[task]) + 1
                cur_time += wait_time
            last_times[task] = cur_time
            cur_time += 1
        return cur_time

ob=Solution()
n=int(input())
k=int(input())
nums=list(map(int, input().split()))[:n]
print(ob.solve(nums,k))
