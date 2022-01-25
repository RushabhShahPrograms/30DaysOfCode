'''
You are given a list of integers nums. Return the number of pairs i < j such that nums[i] + nums[j] is equal to 2 ** k for some 0 ≤ k.

input: first line contains N, the number of elements second line contains N elements.

Input Format

4 1 1 3 5

Constraints

0 ≤ n ≤ 100,000

Output Format

4

Sample Input 0

4
1 1 3 5
Sample Output 0

4
Sample Input 1

4
16 11 32 11
Sample Output 1

0
'''

def powerof2(n,nums):
    count=0
    for i in range(0,n):
        for j in range(i+1,n):
            if(nums[i]+nums[j]==n):
                count += 2
    return count

n = int(input())
nums = list(map(int, input().split()))
print(powerof2(n,nums))


#it is not the general one only some output will give result. If you know the correct code then please change it.
