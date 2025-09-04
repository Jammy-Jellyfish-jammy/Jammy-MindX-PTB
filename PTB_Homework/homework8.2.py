userInput = int(input("Thang? "))

thang31ngay = [1, 3, 5, 7, 8, 10, 12]
thang30ngay = [4, 6, 9, 11]

if userInput in thang31ngay:
    print("Thang co 31 ngay!")

elif userInput in thang30ngay:
    print("Thang co 30 ngay!")

elif userInput == 2:
    print("Thang co 28 hoac 29 ngay!")

else:
    print("Error!")