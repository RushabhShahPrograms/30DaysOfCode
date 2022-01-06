'''
Given an array arr[] of n integers. Check whether it contains a triplet that sums up to zero.
For eg:
0, -1 and 1 forms a triplet with sum equal to 0.

Input Format
n = 5,
arr[] = {0, -1, 2, -3, 1}

Constraints
1 <= n <= 104

Output Format
true

Sample Input 0
5
0 -1 2 -3 1

Sample Output 0
true
'''

def findtriplet(ar):
    found = False
    for i in range(0,len(ar)-2):
        for j in range(i+1,len(ar)-1):
            for k in range(j+1,len(arr)):
                if(ar[i]+ar[j]+ar[k] == 0):
                    found = True
    if(found == True):
        print("true")
                    
    else:
        print("false")
    
n = int(input())
arr = []
while True:
    att = input()
    try:
        arr = [int(val) for val in att.split(" ")]
        if(len(arr) == n):
            break
        else:
            print("error")
    except:
        print("error")

o = findtriplet(arr)
