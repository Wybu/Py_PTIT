import math

# Hàm kiểm tra số nguyên dương có phải là số nguyên tố không
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Hàm tính số lượng ước số của một số nguyên dương
def count_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
            # Nếu i không phải là căn bậc hai của n thì n/i cũng là ước số của n
            if i != n // i:
                count += 1
    return count

# Hàm tìm số phản nguyên tố bé nhất không nhỏ hơn X
def find_next_deficient_prime(X):
    # Bắt đầu kiểm tra từ số X
    n = X
    while True:
        # Nếu số n là số phản nguyên tố, trả về n
        if count_divisors(n) > count_divisors(n - 1):
            return n
        # Ngược lại, tăng n lên 1 và tiếp tục kiểm tra
        n += 1

# Đọc số lượng test cases
T = int(input())

# Vòng lặp xử lý từng test case
for _ in range(T):
    # Đọc số nguyên dương X từ input
    X = int(input())
    # Tìm số phản nguyên tố bé nhất không nhỏ hơn X và in ra kết quả
    print(find_next_deficient_prime(X))
