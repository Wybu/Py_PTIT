def kiem_tra_tinh_chat(N):
    # Chuyển số nguyên thành chuỗi để dễ xử lý chữ số
    str_N = str(N)

    # Kiểm tra xem số có ít nhất 4 chữ số không
    if len(str_N) < 4:
        return False

    # Lấy hai chữ số đầu và hai chữ số cuối
    dau = str_N[:2]
    cuoi = str_N[-2:]

    # Kiểm tra xem hai chữ số đầu và hai chữ số cuối có giống nhau hay không
    return dau == cuoi

t=int(input())
for index in range (t) :
    # Nhập số nguyên dương N từ người dùng
    N = int(input())

    # Gọi hàm kiểm tra tính chất và in kết quả
    if kiem_tra_tinh_chat(N):
        print("YES")
    else:
        print("NO")
