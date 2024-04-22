def solve(n):
    tong=0
    tich=1
    a=[]
    a=n.split()
    for i in range (len(a)):
        if i%2!=0:
            tong+=int(a[i])
        else:
            if int(a[i]) ==0 :
                a[i]=1
            tich*=int(a[i])
    print(tich,tong)
for _ in range (int(input())):
    n=input()
    solve(n)