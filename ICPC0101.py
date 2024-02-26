def loai_bo_cac_cap_tong_chan(arr):
    i = 0
    while i < len(arr) - 1:
        if (arr[i] + arr[i+1]) % 2 == 0:
            arr.pop(i)
            arr.pop(i)
            i = max(0, i - 1)
        else:
            i += 1

# Đọc dữ liệu từ input
N = int(input())
A = list(map(int, input().split()))

# Gọi hàm loại bỏ cặp phần tử có tổng chẵn
loai_bo_cac_cap_tong_chan(A)

# In số lượng phần tử còn lại trong dãy A
print(len(A))
