def absolute_value():
    number = int(input("Nhap mot so nguyen: "))
    if number < 0:
        absolute = -number
    else:
        absolute = number
    print(f"Gia tri tuyet doi cua so nguyen la {absolute}")

absolute_value()