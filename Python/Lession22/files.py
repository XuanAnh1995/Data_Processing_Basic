# r  = Read
# 'r' → Mở để đọc (mặc định, lỗi nếu file không tồn tại).

# a = Append
# 'a' → Ghi tiếp vào cuối file (tạo mới nếu không tồn tại)

# w = Write
# 'w' → Ghi đè file (tạo mới nếu không tồn tại)

# x = Create
# 'x' → Tạo file mới (lỗi nếu file đã tồn tại).

# 'b' → Mở ở chế độ nhị phân (ví dụ: ảnh, video)
# 't' → Mở ở chế độ văn bản (mặc định).
# '+' → Mở để đọc & ghi

# Read - error if it doesn't exist

# Lệnh open() trong Python được dùng để mở tệp tin và trả về một đối tượng file để thao tác với tệp đó.

# file = open(
#     file,                 Đường dẫn đến tệp cần mở hoặc file descriptor
#     mode='r',             Chế độ mở tệp.
#     buffering=-1,         Điều khiển bộ đệm:
                                # 0: Không có bộ đệm (chỉ trong chế độ nhị phân)
                                # 1: Bộ đệm theo dòng
                                # >1: Dùng bộ đệm với kích thước nhất định
#     encoding=None,        Mã hóa ký tự (UTF-8, ASCII, v.v.).
#     errors=None, 
#     newline=None,         Điều khiển cách xử lý ký tự xuống dòng (\n, \r\n)
#     closefd=True, 
#     opener=None
#     )




f = open(
    "names.txt", 
    mode="r"
    )

# print(f.read())
# print(f.read(1))

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("name_list.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()


# Append - create the file if it doesn't exist
# 'a' → Ghi tiếp vào cuối file (tạo mới nếu không tồn tại)
f = open("names.txt", mode="a")
f.write("Neil")
f.close

f = open("names.txt", mode="a")
print(f.read())
f.close