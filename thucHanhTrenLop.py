def solve (n):
    s=0
    shift=1
    if n%2==0:
        for i in range (1, n, 2) :
            s+=(1/i)*shift
            shift*=-1
    else:
        if n%2==1:
            for i in range (0, n, 2):
                s+=(1/(i+1))*shift
                shift*=-1

    return s
n=int(input())
print(solve(n))