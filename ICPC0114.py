import math

def is_prime(num):
    if int(num) < 2:
        return False
    for i in range(2, int(math.sqrt(int(num))) + 1):
        if int(num) % i == 0:
            return False
    return True

def checkNum(n):
    num = str(n)
    for i in num:
        if not is_prime(int(i)):
            return False
    return True

def checkSum(n):
    num = str(n)
    res = 0
    for i in num:
        res += int(i)
    return is_prime(res)

for _ in range(int(input())):
    n = input()
    nr = n[::-1]
    if is_prime(n) and is_prime(nr) and checkSum(n) and checkNum(n):
        print("Yes")
    else:
        print("No")
