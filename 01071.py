def is_python_file(filename):
    # Chuyển tất cả các ký tự trong tên file thành chữ thường
    filename_lower = filename.lower()

    # Kiểm tra xem tên file có kết thúc bằng '.py' không
    return filename_lower.endswith('.py')
filename = input()
if is_python_file(filename):
   print("yes")
else:
    print("no")
