import math


def calculate_years(N, X, M):
    years = 0
    while N < M:
        N += N * (X / 100)
        years += 1
    return years


# Đọc số bộ test
num_tests = int(input())

for _ in range(num_tests):
    # Đọc giá trị N, X, M cho mỗi bộ test
    N, X, M = map(float, input().split())

    # Gọi hàm tính số năm và in ra kết quả
    result = calculate_years(N, X, M)
    print(result)
