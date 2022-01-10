'''
A phoenix sentence is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true

Explanation: sentence contains at least one of every letter of the English alphabet.

Input Format
string = "thequickbrownfoxjumpsoverthelazydog"

Constraints
1 <= sentence.length <= 1000
sentence consists of lowercase English letters.

Output Format
true
'''

def checkPangram(s):
    l = []
    for i in range(26):
        l.append(False)
    for c in s.lower():
        if not c == " ":
            l[ord(c) -ord('a')] = True
    
    for ch in l:
        if(ch == False):
            return False
    return True

s = input()
if(checkPangram(s)):
    print("true")
else:
    print("false")
