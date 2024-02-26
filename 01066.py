def reve(s1):
    s2=s1[::-1]
    return s2
def equal_strings(s1, s2):
    for i in range(1, len(s1)):
        absolute_diff_s1 = abs(ord(s1[i]) - ord(s1[i - 1]))
        absolute_diff_s2 = abs(ord(s2[i]) - ord(s2[i - 1]))

        if absolute_diff_s1 != absolute_diff_s2:
            return False  # Nếu có ít nhất một vị trí không thoả mãn điều kiện, trả về False

    return True
for i in range (int(input())):
    s=input()
    s1=reve(s)
    if equal_strings(s, s1):
        print("YES")
    else: print("NO")
