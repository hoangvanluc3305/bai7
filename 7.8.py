print("HOÀNG VĂN LỰC")
print("MSSV:235752021610065")

def write_list_to_file(fname, data_list):
    try:
        # Mở tệp theo chế độ ghi (write mode). Nếu tệp không tồn tại, nó sẽ được tạo mới.
        with open(fname, 'w', encoding='utf-8') as file:
            # Ghi mỗi phần tử trong danh sách vào tệp, mỗi phần tử sẽ được ghi trên một dòng
            for item in data_list:
                file.write(str(item) + '\n')  # Chuyển phần tử thành chuỗi và thêm dấu xuống dòng
            
        print(f"Nội dung danh sách đã được ghi vào tệp {fname}.")
    
    except Exception as e:
        print(f"Đã có lỗi xảy ra: {e}")

# Danh sách dữ liệu cần ghi vào tệp
data_list = ["hello",
             "day la vd",
             "python rat thu vi."]

# Gọi hàm với tên tệp bạn muốn ghi vào
file_name = (r'C:\Users\asus\Documents\0.1.py')
write_list_to_file(file_name,data_list)
