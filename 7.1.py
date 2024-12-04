print("HOÀNG VĂN LỰC")
print("MSSV:235752021610065")

# Mở file với mã hóa utf-8
with open('C:/Users/asus/Documents/7.1.py', 'r', encoding='utf-8') as input_file:
    # Đọc từng dòng trong file
    for line in input_file:
        # Đảo ngược thứ tự các ký tự trong dòng
        reversed_line = line[::-1]
        # In ra dòng đã đảo ngược
        print(reversed_line)
