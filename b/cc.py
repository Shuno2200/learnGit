#Hãy viết chương trình để tính tổng các phần tử bất kì trong danh sách.
def tong(ds):
    tong = 0
    for i in ds:
        tong = tong + i
    return tong

# Tạo một danh sách bất kỳ
ds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tính tổng tất cả các phần tử trong danh sách
tong_danh_sach = tong(ds)
print("Tổng tất cả các phần tử trong danh sách:", tong_danh_sach)