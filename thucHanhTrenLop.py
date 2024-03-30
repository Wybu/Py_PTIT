# l=[('Anh', 88), ('Toan', 90), ('Hoa', 85), ('Sinh', 95)]
# print(list(sorted(l, key=lambda x: x[1])))
#
from collections import Counter
import permutations
# l1=[1,2, 3, 4, 5, 6, 7, 9, 10]
# l2=[1,2, 3, 6, 8]
# print(list(filter(lambda x: x in l1, l2)))

# pronun =['A', 'E', 'I', 'O', 'U']
# names=["Elita", "Mai", "Linh", "Hoa", "Huyen", "Anh", "Huong", "Urser", "Avocad"]
# print(list(filter(lambda x: x[0] in pronun, names)))

l=['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yz', 'bacd', 'dcab', 'abcde']

l1='abcd'
print(Counter(l))

print (list(filter(lambda x: x[0] in l1, l)))