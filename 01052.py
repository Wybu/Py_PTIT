import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
def total_prime(n):
    num=str(n)
    res=0
    for i in num:
        res+= int (i)

    if is_prime(res):
        return True
    else:
        return False


for t in range (int(input())):
    n= int(input())
    if total_prime(n):
        print("YES")
    else:
        print("NO")
