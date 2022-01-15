'''
Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.If no equilibrium index is found return -1 else return the index. consider the index starting from 0.
For example, in an array A:

**Example : **

length:7
Input: A[] = {-7, 1, 5, 2, -4, 3, 0} 
Output:

3 
Explanation

3 is an equilibrium index, because: 
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]
example:

length:3
Input: A[] = {1, 2, 3} 
Output: -1 
Input Format

6 -7 1 5 2 -4 3 0

Constraints

the array may contain negative values
Output Format

3
'''

def indexing(n,a):
    l,r=0,0
    
    for i in range(n):
        l,r=0,0
        
        for j in range(i):
            l += a[j]

        for j in range(i+1,n):
            r += a[j]
        
        if(l==r):
            return i
    
    return -1

n = int(input())
a = [int(n) for n in input().split()]
print(indexing(n,a))
