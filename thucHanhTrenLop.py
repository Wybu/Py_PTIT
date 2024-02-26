words=[1,2,1,3,1,1,2]
my_set = {1, 2, 3}
my_set |= {4}
abc={}
print(my_set)  # Kết quả: {1, 2, 3, 4}

for i in range (len(words)):
    abc.add(words[i])
print(abc)