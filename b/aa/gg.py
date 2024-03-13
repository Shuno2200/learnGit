#Hãy viết chương trình để tính tổng các phần tử là sô chẳn, lẻ trong danh sách.
def tong_chan_le(ds):
    tong_chan = 0
    tong_le = 0
    for so in ds:
        if so % 2 == 0:
            tong_chan += so
        else:
            tong_le += so
    return tong_chan, tong_le

# Khởi tạo một danh sách bất kỳ
ds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tính tổng các phần tử là số chẵn và số lẻ
tong_chan, tong_le = tong_chan_le(ds)
print("Tổng các phần tử chẵn trong danh sách:", tong_chan)
print("Tổng các phần tử lẻ trong danh sách:", tong_le)