def checker(num):
    numStr=str(num)
    if len(numStr)%2==0:
        return False
    for i in range(len(numStr)):
        if int(numStr[i]) %2 != 0:
            return False
    return True

for _ in range (int(input())):
    n=int(input())
    for i in range(n):
        if checker(i):
            print(i)

    print()