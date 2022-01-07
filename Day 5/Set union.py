'''
Given two arrays a[] and b[] of size n and m respectively. The task is to find union between these two arrays.
Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.
print the length of the new array.

Input:
5 3
1 2 3 4 5
1 2 3

Output:
5

Explanation:
1, 2, 3, 4 and 5 are the elements which comes in the union set of both arrays. So count is 5.

Input Format
n = 5 m = 3 a = 1 2 3 4 5 b = 1 2 3

Constraints
the output set must contain all elements from both set

Output Format
5

Sample Input 0
5 3
1 2 3 4 5
1 2 3

Sample Output 0
5

'''
n,m = map(int, input().split())

arr1 = []
while True:
    att = input()
    try:
        arr1 = [int(val) for val in att.split(" ")]
        if(len(arr1) == n):
            break
        else:
            print("error")
    except:
        print("error")
        
arr2 = []
while True:
    tt = input()
    try:
        arr2 = [int(val1) for val1 in tt.split(" ")]
        if(len(arr2) == m):
            break
        else:
            print("error")
    except:
        print("error")   

unionarr = list(set(arr1 + arr2))
print(len(unionarr))
