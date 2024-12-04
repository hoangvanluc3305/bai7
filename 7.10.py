print("HOÀNG VĂN LỰC")
print("MSSV:235752021610065")

def find_longest_words(text):
    # Tách văn bản thành các từ bằng cách dùng phương thức split() và loại bỏ các ký tự không cần thiết (dấu câu)
    words = text.split()
    
    # Xóa dấu câu và chuyển các từ về chữ thường (để không bị phân biệt hoa thường)
    cleaned_words = [word.strip('.,!?()[]{}":;') for word in words]
    
    # Tìm độ dài của từ dài nhất
    max_length = max(len(word) for word in cleaned_words)
    
    # Tìm tất cả các từ có độ dài bằng với từ dài nhất
    longest_words = [word for word in cleaned_words if len(word) == max_length]
    
    return longest_words

# Nhập văn bản từ bàn phím hoặc từ tệp
text = input("Nhập văn bản: ")

# Tìm và in các từ dài nhất
longest_words = find_longest_words(text)
print(f"Các từ dài nhất trong văn bản: {', '.join(longest_words)}")
