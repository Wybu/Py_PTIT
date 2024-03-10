def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def reverse_number(num):
    return int(str(num)[::-1])

def print_emirp_numbers(N):
    emirp_numbers = []
    for i in range(2, N):
        if is_prime(i):
            reversed_i = reverse_number(i)
            if i != reversed_i and is_prime(reversed_i):
                emirp_numbers.append(i)
    print(*emirp_numbers, sep=' ')


for _ in range(int(input())):
    N = int(input())
    print_emirp_numbers(N)
