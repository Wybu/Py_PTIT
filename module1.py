def count(n):
    a=0
    for i in range (len(n)):
        if n[i]==' ':
            a+=1
    return len(n)-a
def test(sub, n):
    return sub in n