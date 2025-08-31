n = int(input("Nhap n? "))

x = range(2, n)

for i in x:
    if n%i == 0:
        print(n, "khong phai la so nguyen to")
        break

else:
    print(n, "la so nguyen to")