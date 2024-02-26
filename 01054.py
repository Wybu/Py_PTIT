for i in range (int(input())):
    n=input()
    result=1
    for j in n:
        temp=ord(j)-ord('0')
        if temp>0 :
            result*=temp

    print(result)

