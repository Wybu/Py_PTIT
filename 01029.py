def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def reverse (a):
    return a[::-1]
for _ in range (int(input())):
    a=input()
    b=reverse(a)
    if gcd(int(a),int(b))==1:
        print("YES")
    else:
        print("NO")