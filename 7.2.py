print("HOÀNG VĂN LỰC")
print("MSSV:235752021610065")

def count_file_attributes(file_path):
    try:
        # Mở file và đọc dữ liệu
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Số dòng trong file
        num_lines = len(lines)

        # Số từ và số ký tự
        num_words = 0
        num_chars = 0
        
        for line in lines:
            num_chars += len(line)  # Tính số ký tự trong dòng
            num_words += len(line.split())  # Tính số từ trong dòng

        # In kết quả
        print(f"Số dòng trong file: {num_lines}")
        print(f"Số từ trong file: {num_words}")
        print(f"Số ký tự trong file: {num_chars}")

    except FileNotFoundError:
        print("File không tồn tại.")
    except Exception as e:
        print(f"Đã có lỗi xảy ra: {e}")

# Nhập đường dẫn của file cần đọc
file_path = r'C:\Users\asus\Documents\7.2.py'  # Sử dụng chuỗi raw để tránh lỗi với dấu backslash
count_file_attributes(file_path)
