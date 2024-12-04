print("HOÀNG VĂN LỰC")
print("MSSV:235752021610065")

import os

def file_write_and_read(fname):
    # Kiểm tra nếu tệp đã tồn tại trước khi viết
    if os.path.exists(fname):
        # Mở tệp để ghi nội dung vào cuối tệp (append mode)
        with open(fname, "a", encoding="utf-8") as myfile:
            myfile.write("chuc lam tot\n")
            myfile.write("happy\n")
        
        # Mở tệp để đọc và hiển thị nội dung
        with open(fname, "r", encoding="utf-8") as txt:
            print(txt.read())  # Đọc toàn bộ nội dung của tệp và in ra
    else:
        print(f"File {fname} does not exist!")

# Gọi hàm và sử dụng tệp 'abc.txt'
file_write_and_read(r'C:\Users\asus\Documents\0.1.py')  # Ensure this file path is correct
