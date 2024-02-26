def is_valid_number(n):
    # Chuyển số n thành chuỗi để dễ xử lý
    n_str = str(n)

    # Tính tổng các chữ số của n
    digit_sum = sum(int(digit) for digit in n_str)

    # Kiểm tra tính chia hết cho 10
    if digit_sum % 10 != 0:
        return False

    # Kiểm tra tính chất các chữ số cạnh nhau khác nhau đúng 2 đơn vị
    for i in range(len(n_str) - 1):
        if abs(int(n_str[i]) - int(n_str[i + 1])) != 2:
            return False

    # Nếu vượt qua cả hai điều kiện trên, số được coi là hợp lệ
    return True


# Ví dụ sử dụng
for i in range (int(input())):
    number = int(input())
    if is_valid_number(number):
        print("YES")
    else:
        print("NO")