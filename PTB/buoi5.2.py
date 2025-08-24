# Header
print("XEP LOAI HOC SINH")

#Input
print("Diem so? (please use '.' instead)")
user_input = float(input())

#Output
if user_input > 10 or user_input < 0:
    print(":(")
    print("Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.")

elif user_input >= 8:
    print("Gioi")

elif user_input >= 6.5:
    print("Kha")

elif user_input >= 5:
    print("Trung Binh")

else:
    print("Yeu")

