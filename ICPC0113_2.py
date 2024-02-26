def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def reverse_number(num):
    return int(str(num)[::-1])

def list_emirp_pairs(N):
    emirp_pairs = []
    for i in range(13, N):
        if is_prime(i):
            reversed_i = reverse_number(i)
            if i != reversed_i and is_prime(reversed_i) and reversed_i < N:
                emirp_pairs.append((i, reversed_i))
    return emirp_pairs

def print_emirp_pairs_less_than_N(N):
    emirp_pairs = list_emirp_pairs(N)
    for pair in emirp_pairs:
        print(*pair, end=' ')

# Đọc số lượng test
T = int(input())

# Đọc và in kết quả cho mỗi test
for _ in range(T):
    N = int(input())
    print_emirp_pairs_less_than_N(N)
    print()  # Xuống dòng giữa các test
