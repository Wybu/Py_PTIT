from itertools import permutations

def generate_strings(N):
    result = set()

    # Tạo tất cả các xâu chứa A, B, C có độ dài N
    all_strings = permutations('ABC', N)

    # Lọc những xâu thỏa mãn điều kiện
    for s in all_strings:
        s = ''.join(s)
        if s.count('A') <= s.count('B') <= s.count('C'):
            result.add(s)

    return sorted(result)

# Nhập giá trị N từ người dùng
N = int(input("Nhập giá trị N: "))

# Liệt kê và in ra tất cả các xâu thỏa mãn yêu cầu
result_strings = generate_strings(N)
for string in result_strings:
    print(string)
