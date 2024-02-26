def tinh_tong(n):
    S = 0
    if n % 2 == 1:  # Nếu N là số lẻ
        for i in range(1, n + 1, 2):
            S += 1 / i
    else:  # Nếu N là số chẵn
        for i in range(2, n + 1, 2):
            S += 1 / i
    return S
for _ in range(int(input())):
    N = int(input())
    ket_qua = tinh_tong(N)
    formatted_result = "{:.6f}".format(ket_qua)
    print(f"{formatted_result}")
