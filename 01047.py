import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

for _ in range(int(input())):
    n = input()
    substr = n[-4:] if len(n) >= 4 else n  # Lấy 4 ký tự cuối cùng hoặc toàn bộ chuỗi nếu ít hơn 4 ký tự
    so = int(substr)  # Chuyển đổi thành số nguyên
    if is_prime(so):
        print("YES")
    else:
        print("NO")
