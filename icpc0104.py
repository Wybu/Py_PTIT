def tim_so_lon_nhat_trong_xau(s):
    max_number = float('-inf')  # Khởi tạo biến max_number với giá trị âm vô cùng lớn
    current_number = 0

    i = 0
    while i < len(s):
        if s[i].isdigit():
            current_number = int(s[i])
            i += 1
            while i < len(s) and s[i].isdigit():
                current_number = current_number * 10 + int(s[i])
                i += 1

            max_number = max(max_number, current_number)
        else:
            i += 1

    return max_number

# Test với xâu X[]="12ab29cd19"
for _ in range(int(input())):
    xau_test = input()
    ket_qua = tim_so_lon_nhat_trong_xau(xau_test)
    print(ket_qua)
