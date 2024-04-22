def is_prime(n):
    if n<2: return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0: return False
    return True

def solve(n):
    up=int(n[0]+n[1]+n[2])
    down=int(n[len(n)-3]+n[len(n)-2]+n[len(n)-1])
    if is_prime(up) and is_prime(down): return True
    else: return False

for _ in range (int(input())):
    s=input()
