def ip_check(n):
    a=n.split('.')
    if len(a)!=4:
        return False
    for i in a:
        if not i.isdigit():
            return False
        if int(i)<0 or int(i)>255:
            return False
    return True

for _ in range(int(input())):
        n=input()
        if ip_check(n):
            print('YES')
        else:
            print('NO')