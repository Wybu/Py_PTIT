n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
tichmax3 = max(a[0]*a[1]*a[2], a[0]*a[1]*a[-1])
tichmax2= max(a[0]*a[1], a[0]*a[-1])
print(max(tichmax2, tichmax3))