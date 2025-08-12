#Tran Nguyen Minh Khang
#May tinh tien dien

#Input
print("Nhap so kWh")
user_input =  int(input())

#Calculate
output = 0
KWh_st = 50*1700
kWh_nd = 50*1900
kWh_rd = 100*2100

if user_input < 0:
    print("Error!")

elif user_input <= 50:
    output = user_input * 1700

elif user_input <= 100:
    output = KWh_st + (user_input - 50) * 1900

elif user_input <= 200:
    output = KWh_st + kWh_nd + (user_input - 100) * 2100

else:
    output = KWh_st + kWh_nd + kWh_rd + (user_input - 200) * 3000

#Output
print("So tien phai tra la", output, "VND")
