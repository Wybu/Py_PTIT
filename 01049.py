def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def solve(s):
    if is_prime(len(s)):
        check=0
        for i in range(len(s)):
            if not is_prime(ord(s[i])):
                check+=1
            if check >= (len(s)-check):
                return 'NO'
        return 'YES'
    else:
        return 'NO'

for _ in range   (int(input())):
    s=input()
    print(solve(s))