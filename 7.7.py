print("HOÀNG VĂN LỰC")
print("MSSV:235752021610065")

def count_lines_in_file(fname):
    try:
        # Mở tệp để đọc
        with open(fname, 'r', encoding='utf-8') as file:
            # Đếm số dòng bằng cách sử dụng vòng lặp
            num_lines = sum(1 for line in file)
        
        print(f"Số dòng trong tệp: {num_lines}")
    
    except FileNotFoundError:
        print("Tệp không tồn tại.")
    except Exception as e:
        print(f"Đã có lỗi xảy ra: {e}")

# Gọi hàm với đường dẫn đến tệp
file_path = (r'C:\Users\asus\Documents\0.1.py')
count_lines_in_file(file_path)
