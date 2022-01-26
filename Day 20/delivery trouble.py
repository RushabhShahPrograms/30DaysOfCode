'''
In a list of strings, each element in orders starts with either "P" meaning pickup or "D" meaning delivery followed by the order id. For example, "P12" means pick up order 12.

Return whether orders is valid given the following rules: A delivery cannot happen for an order before pickup Every pickup must be delivered An order that's already been picked up and delivered cannot be picked up or delivered again

Example 1:

Input:
orders = ["P1", "P2", "D2", "D1"]
Output:
true
Explanation:
We first pick up orders 1 and 2 then we drop 2 and 1.
Example 2:

Input:
orders = ["P1", "P2", "P3"]
Output;
false
Explanation:
The orders were not delivered.
Hint: use sc.next() to take input in Java.

Input Format

4

P1 P2 D2 D1

Constraints

0 ≤ n ≤ 100,000 where n is the length of orders
Output Format

true

Sample Input 0

4
P1 P2 D2 D1
Sample Output 0

true
Explanation 0

We first pick up orders 1 and 2 then we drop 2 and 1.

Sample Input 1

3
P1 P2 P3
Sample Output 1

false
Sample Input 2

2
D1 P1
Sample Output 2

false
Sample Input 3

4
P1 P2 D2 D1
Sample Output 3

true
'''

def solve(orders):
    delivered = set()
    picked = set()
    for i in orders:
        if i[0] == "P" and i[1:] not in delivered:
            picked.add(i[1:])
            delivered.add(i[1:])
        elif i[0] == "D":
            try:
                picked.remove(i[1:])
            except:
                return False
        else:
            return False
    return len(picked) == 0

n = int(input())
orders = list(input().split())
if(solve(orders)==False):
    print("false")
else:
    print("true")
