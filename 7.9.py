print("HOÀNG VĂN LỰC")
print("MSSV:23575202161006")

def copy_file_contents(src_file, dest_file):
    try:
        # Mở tệp nguồn để đọc
        with open(src_file, 'r', encoding='utf-8') as src:
            # Đọc toàn bộ nội dung của tệp nguồn
            content = src.read()
        
        # Mở tệp đích để ghi nội dung vào
        with open(dest_file, 'w', encoding='utf-8') as dest:
            # Ghi nội dung vào tệp đích
            dest.write(content)
        
        print(f"Nội dung đã được sao chép từ {src_file} sang {dest_file}.")
    
    except FileNotFoundError:
        print(f"Tệp nguồn {src_file} không tồn tại.")
    except Exception as e:
        print(f"Đã có lỗi xảy ra: {e}")

# Nhập tên tệp nguồn và tệp đích
source_file = (r'C:\Users\asus\Documents\0.2.py')
destination_file = (r'C:\Users\asus\Documents\0.1.py')

# Sao chép nội dung từ tệp nguồn sang tệp đích
copy_file_contents(source_file, destination_file)
