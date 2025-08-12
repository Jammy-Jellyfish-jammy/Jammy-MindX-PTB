#Header
print("May doi thoi gian")

#input
print("nhap so giay")
s = int(input())

# calculate
hours = s // 3600
minutes = (s-(hours*3600)) // 60
seconds = s - (hours*3600) - (minutes*60)

#Output
print(str(s) + " giay bang " + str(hours) + " gio, " + str(minutes) + " phut va " + str(seconds) + " giay")