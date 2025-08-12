# Header
print("May chia keo")

# Input
print("So keo?")
n = int(input())
print("So hoc sinh?")
m = int(input())

# Tien hanh chia keo
if m > n:
    print("Thay cam " + str(n) + " vien keo mang ve")
    print("Khong em nao duoc keo :)))")

else:
    keo_hs = n // m
    keo_thay = n % m

    print("Moi em nhan duoc " + str(keo_hs) + " vien keo.")
    print("Thay cam " + str(keo_thay) + " vien keo mang ve.")

        
