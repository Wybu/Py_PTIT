def check(n):
   # if int(str(n)[-1] %2==0):
   num=str(n)
   if len(num)%2==0:
       return False
   if num[0]==num[1]:
       return False
   for i in range (0, len(num)-1, 2):
       if num[i] != num[i+2]:
           return False
   return True


for i in range (int(input())):
    n=input()
    if check(n):
        print("YES")
    else:
        print("NO")