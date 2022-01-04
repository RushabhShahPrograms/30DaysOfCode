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
