diemso_list = input("Danh sach diem so: ").split()

if "10" in diemso_list:
    diem10_count = 0
    for i in diemso_list:
        if i == "10":
            diem10_count += 1

    print(f"So diem 10 la {diem10_count}")

else:
    print("Ban khong co diemm 10")