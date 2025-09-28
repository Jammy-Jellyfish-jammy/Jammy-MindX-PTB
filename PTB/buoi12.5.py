def in_danh_sach_va_tong(danh_sach):
    print("Danh sach cac phan tu: ")
    for so in danh_sach:
        print(so)
    
    tong = sum(danh_sach)
    print(f"Tong cua danh sach la {tong}")

danh_sach = []
n = int(input("Nhap so phan tu trong danh sach: "))
for i in range(n):
    so = int(input("Nhap phan tu thu (): ".format(i + 1)))
    danh_sach.append(so)

in_danh_sach_va_tong(danh_sach)