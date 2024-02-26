for _ in range (int(input())):
    n=input()
    check=0
    for i in range(len(n)):
        if n[i]!='1'and n[i]!='2'and n[i]!='0':
            print("NO")
            check=1
            break
    if check==0 :
        print("YES")