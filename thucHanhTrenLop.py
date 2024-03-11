def s1(n):
    s=1
    for i in range (1, n+1, 1):
        s*=i
    return s
def s2(n):
    if n==0:
        return 1
    else:
        s=1
        while (n>=1):
            s*=n
            n-=1
            if n>0:
                s2(n)
            else:
                return s
n=int(input())
print(s1(n))
print(s2(n))