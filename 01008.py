a=str(input())
low=0
up=0
for i in range (0, len(a)):
    if a[i].islower():
        low+=1
    else: up+=1
if low>=up:
    print(a.lower())
else: print(a.upper())