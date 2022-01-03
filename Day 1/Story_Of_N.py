import itertools
def findNth(n):
    count = 0
    for c in itertools.count():
        sum = 0
        x = c
        while(x):
            sum = sum + x % 10
            x = x // 10

        if (sum == 11):
            count = count + 1

        if (count == n):
            return c
    return -1

if __name__=='__main__':
    a = int(input())
    print(findNth(a))
