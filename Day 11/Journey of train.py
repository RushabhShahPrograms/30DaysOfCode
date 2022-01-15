'''
There are n trains that are labeled from 1 to n.

You are given an array of train bookings as bookings, where bookings[i] = [first, last, seats] represents a booking for trains from first through last (inclusive) with no of seats seats reserved for each train in the range.

Return an array answer of length n, where answer[i] is the total number of seats reserved for train i.

Input Format

length of bookings = 3,

bookings = [[1,2,10],[2,3,20],[2,5,25]],

no of trains = 5

Constraints

1 <= n <= 2 * 104
1 <= bookings.length <= 2 * 104
bookings[i].length == 3
1 <= firsti <= lasti <= n
1 <= seatsi <= 104
Output Format

10 55 45 25 25

Sample Input 0

3
1 2 10
2 3 20
2 5 25
5
Sample Output 0

10 55 45 25 25
'''

length = int(input())
bookings = [0]*length
for i in range(length):
    bookings[i] = list(map(int, input().split()))
trains = int(input())

res = [0]*trains
for i in range(len(bookings)):
    l=bookings[i][0]
    r=bookings[i][1]
    k=bookings[i][2]
    res[l-1] += k
    
    if(r<=len(res)-1):
        res[r]=(-k)+res[r]

for i in range(1,len(res)):
    res[i] += res[i-1]

for i in range(len(res)):
    print(res[i],end=" ")
