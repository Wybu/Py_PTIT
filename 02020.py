A = []
n = int(input())
numbers_input = input()

# Tách chuỗi nhập thành các số
numbers_list = numbers_input.split()
sum=0
# Chuyển các số thành kiểu float và thêm vào danh sách A
for num_str in numbers_list:
    num = float(num_str)
    A.append(num)
    sum+=num
A.sort()
st=set(A)
print(st)
print(A)
avr=(sum-A[0]-A[-1])/(len(A)-2)
print(avr)
