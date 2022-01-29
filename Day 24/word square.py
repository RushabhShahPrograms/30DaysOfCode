'''
Given a sequence of words, check whether it forms a valid word square.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤k< max(numRows, numColumns).

Input Format

[
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]
Constraints

The number of words given is at least 1 and does not exceed 500.
Word length will be at least 1 and does not exceed 500.
Each word contains only lowercase English alphabet a-z.
Output Format

true

Sample Input 0

4
abcd
bnrt
crmy
dtye
Sample Output 0

true
Explanation 0

The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crmy".
The fourth row and fourth column both read "dtye".
Therefore, it is a valid word square.

Sample Input 1

4
abcd
bnrt
crm
dt
Sample Output 1

true
Explanation 1

The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crm".
The fourth row and fourth column both read "dt".
Therefore, it is a valid word square.

Sample Input 2

4
ball
area
read
lady
Sample Output 2

false
Explanation 2

The third row reads "read" while the third column reads "lead".

Therefore, it is NOT a valid word square.
'''

class Solution:
    def solve(self, words):
        for i in range(len(words)):
            for j in range(len(words[i])):
                if i != j and (j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]):
                    return False
            
        return True
    

ob=Solution()
n=int(input())
words=[]
for i in range(n):
    w=(input())
    words.append(w)
    

if(ob.solve(words)==True):
    print("true")
else:
    print("false")
