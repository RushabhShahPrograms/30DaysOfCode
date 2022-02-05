'''
You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
For e.g.:

If input is 
length = 3
items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], 
ruleKey = "color", ruleValue = "silver"
then output will be 1.
Explanation:

There is only one item matching the given rule, which is ["computer","silver","lenovo"].

Hint: You can use arrayList to store the input elements.

Input Format

ruleKey = "color"
ruleValue = "silver"
length = 3
items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
Constraints

1 <= items.length <= 104
1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
ruleKey is equal to either "type", "color", or "name".
All strings consist only of lowercase letters.
Output Format

1

Sample Input 0

color
silver
3
phone blue pixel
computer silver lenovo
phone gold iphone
Sample Output 0

1
Explanation 0

There is only one item matching the given rule, which is ["computer","silver","lenovo"].

Sample Input 1

type
phone
3
phone blue pixel
computer silver phone
phone gold iphone
Sample Output 1

2
Explanation 1

There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.
'''

class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        count=0
        for i in items:
            if (ruleKey == "type" and i[0] == ruleValue):
                count+=1
            elif (ruleKey == "color" and i[1] == ruleValue):
                count+=1
            elif(ruleKey == "name" and i[2] == ruleValue):
                count+= 1
        return count
    
ob=Solution()
rulekey=input()
ruleValues=input()
length=int(input())
items = [None]*length
for i in range(length):
    items[i]=list(input().split())
print(ob.countMatches(items, rulekey, ruleValues))
