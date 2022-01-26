'''
Note: Except for multiples of 3 use “Fizz” instead of the integer and for the multiples of 5 use “Buzz”. For integers which are multiples of both 3 and 5 use “FizzBuzz”.
For e.g.: n = 15 Then output will be: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
Input Format
15
Constraints
0 ≤ n ≤ 100,000
Output Format
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz
Sample Input 0
15
Sample Output 0
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz
Sample Input 1
23
Sample Output 1
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 
'''

def fizzBuzz(n):
    result = []
    for i in range(1,n+1):
        if i% 3== 0 and i%5==0:
            result.append("FizzBuzz")
        elif i %3==0:
            result.append("Fizz")
        elif i% 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

n = int(input())
print(*fizzBuzz(n),end=" ")
