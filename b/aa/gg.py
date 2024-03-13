def sum_chan_le(ds):
    sum_chan = 0
    sum_le = 0
    for so in ds:
        if so % 2 == 0:
            sum_chan += so
        else:
            sum_le += so
    return sum_chan, sum_le

# Khởi tạo một danh sách bất kỳ
ds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tính tổng các phần tử là số chẵn và số lẻ
sum_chan, sum_le = sum_chan_le(ds)
print("Tổng các phần tử chẵn trong danh sách:", sum_chan)
print("Tổng các phần tử lẻ trong danh sách:", sum_le)