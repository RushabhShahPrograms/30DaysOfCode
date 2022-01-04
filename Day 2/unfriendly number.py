'''
Raam is superstitious. He will only use a number as a roll number if all digits of the number are different(i.e. no digits are repeated)
Return boolean string as output, print true if all digits are different and false if there are repetitions.
Input Format
983

Constraints
0

Output Format
true

Sample Input 0
9838

Sample Output 0
The number is unlucky.

Sample Input 1
1234

Sample Output 1
The number is lucky.
'''


def lucky(str):
    for i in range(len(str)):
        for j in range(i+1,len(str)):
            if(str[i] == str[j]):
                return False;
    return True;

str = input()
if(lucky(str)):
    print("The number is lucky.")
else:
    print("The number is unlucky.")
