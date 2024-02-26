import math

def check(n):
    num = str(n)
    for j in range(0, len(num), 2):
        if int(num[j]) % 2 != 0:
            return False

    for j in range(1, len(num), 2):
        if int(num[j]) % 2 == 0:
            return False

    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def total_prime(n):
    num_str = str(n)
    total = sum(int(digit) for digit in num_str)
    return is_prime(total)

for _ in range(int(input())):
    num = int(input())
    if check(num) and total_prime(num):
        print("YES")
    else:
        print("NO")
