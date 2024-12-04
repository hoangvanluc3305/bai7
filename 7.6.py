print("HOÀNG VĂN LỰC")
print("MSSV:235752021610065")


import os

def file_read_from_tail(fname, lines):
    bufsize = 8192
    fsize = os.stat(fname).st_size
    data = []
    try:
        with open(fname, 'r', encoding='utf-8', errors='ignore') as f:  # Use utf-8 encoding
            if bufsize > fsize:
                bufsize = fsize - 1

            while True:
                f.seek(fsize - bufsize)
                data.extend(f.readlines())
                if len(data) >= lines or f.tell() == 0:
                    print(''.join(data[-lines:]))
                    break
                fsize -= bufsize
    except UnicodeDecodeError as e:
        print(f"Error reading the file: {e}")

file_read_from_tail(r'C:\Users\DELL\Documents\0.1.py', 2)
