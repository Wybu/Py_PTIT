for i in range(int(input())):
    n=input()
    res=0
    for j in n:
        tmp=ord(j)-ord('0')
        res+=tmp
    if res%3==0:
        print("YES")
    else:
        print("NO")