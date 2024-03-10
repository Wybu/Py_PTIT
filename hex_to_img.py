with open('binary_file') as file:
    data = file.read()

data = bytes.fromhex(data[2:])

with open('image.png', 'wb') as file:
    file.write(data)