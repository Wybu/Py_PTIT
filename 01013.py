def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def sum_of_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n //= 10
    return sum_digits

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_if_gcd_sum_prime(a, b):
    greatest_common_divisor = gcd(a, b)
    sum_of_gcd_digits = sum_of_digits(greatest_common_divisor)
    if is_prime(sum_of_gcd_digits):
        return True
    else:
        return False

# Example usage:
for _ in range(int(input())):
    a, b = map(int, input().split())
    if check_if_gcd_sum_prime(a, b):
        print("YES")
    else:
        print("NO")