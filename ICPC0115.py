def tinh_giai_thua_de_quy(n):
    if n == 0:
        return 1
    return n * tinh_giai_thua_de_quy(n - 1)

def kiem_tra_krishnamurthy(n):
    tong_giai_thua = sum(tinh_giai_thua_de_quy(int(chu_so)) for chu_so in n)
    if tong_giai_thua == int(n):
        return "Yes"
    else:
        return "No"

for _ in range(int(input())):
    print(kiem_tra_krishnamurthy(input()))
