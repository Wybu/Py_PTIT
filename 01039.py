def is_beautiful_number(n):
    # Chuyển số n thành chuỗi để dễ xử lý
    n_str = str(n)

    # Kiểm tra xem số có hai chữ số khác nhau hay không
    if len(set(n_str)) != 2:
        return False

    # Kiểm tra xem các chữ số có cách nhau 2 vị trí đều bằng nhau hay không
    for i in range(2, len(n_str)):
        if n_str[i] != n_str[i - 2]:
            return False

    # Nếu vượt qua cả hai điều kiện trên, số được coi là số đẹp
    return True


# Ví dụ sử dụng
for i in range (int(input())):
    number = int(input())
    if is_beautiful_number(number):
        print("YES")
    else:
        print("NO")