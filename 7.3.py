print("HOÀNG VĂN LỰC")
print("MSSV:235752021610065")

# Đọc toàn bộ tệp văn bản
file_path = 'C:/Users/asus/Documents/7.2.py'  # Đường dẫn của tệp văn bản

try:
    # Mở tệp với chế độ đọc ('r')
    with open(file_path, 'r', encoding='utf-8') as file:
        # Đọc toàn bộ nội dung tệp vào biến nội_dung
        content = file.read()

    # In ra nội dung của tệp
    print(content)

except FileNotFoundError:
    print(f"Không thể tìm thấy tệp tại đường dẫn {file_path}.")
except Exception as e:
    print(f"Đã có lỗi xảy ra: {e}")
