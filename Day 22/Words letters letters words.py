'''
Given a list of strings words and a string letters, return the length of longest string in words that can be made from letters in letters. If no word can be made, return 0. Note that you can't reuse letters.

Example 1

Input
words = ["the", "word", "love", "scott", "finder", "dictionary"]
letters = "fanierdow"

Output
6

Explanation
We can make the word finder out of our letters, which has the longest length of 6.

Example 2

Input
words = ["credit", "nirvana", "karma", "empathy", "hang", "aaaaaaaaa"]
letters = "afnvlfkm"

Output
0

Explanation
We can't make any of these words with the letters we have.
Input Format

fanierdow
6
the word love scott finder dictionary
Constraints

n ≤ 10,000 where n is the length of words
m ≤ 1,000 where m is the length of letters
Output Format

6

Sample Input 0

fanierdow
6
the word love scott finder dictionary
Sample Output 0

6
Explanation 0

We can make the word finder out of our letters, which has the longest length of 6.

Sample Input 1

afnvlfkm
6
credit nirvana karma empathy hang aaaaaaaaa
Sample Output 1

0
Explanation 1

We can't make any of these words with the letters we have.

Sample Input 2

fanierdow
6
the word frowned scott finder dictionary
Sample Output 2

7
'''

from collections import Counter
class Solution:
    def solve(self, letters, words):
        lc = Counter(letters)
        maxL = 0
        for w in words:
            wc = Counter(w)
            if wc == (wc & lc):
                maxL = max(maxL, len(w))
        return maxL
    
ob=Solution()
letters = input()
length = int(input())
words = list(input().split())
print(ob.solve(letters,words))
