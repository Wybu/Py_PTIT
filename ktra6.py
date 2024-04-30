n=int(input())
for i in range(n):
    m=int(input())
    a=[]
    for i in range(m):
        a.append(list(map(int,input().split())))
    a.sort(key=lambda x:x[1])
    count=0
    end=a[0][1]
    for i in range(1,m):
        if a[i][0]>end:
            count+=1
            end=a[i][1]
    print(count+1)