a=[]
b=[]
i=int(input())
for i in range(i):
    a.append((input()).split())
for i in range(len(a)):
    if (i+1)<len(a):
        max2=a[i]+a[i+1]
    b.append(max2)
    #max sum of 3 elements:
    if (i+2)<len(a):
        max3=a[i]+a[i+1]+a[i+2]
    b.append(max3)
sorted(b, reverse=True)
print(b[0])