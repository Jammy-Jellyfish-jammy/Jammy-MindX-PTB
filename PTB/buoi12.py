numList = input("Nhap day so: ").split()
oddList = []
total = 0
try:
    for i in numList:
        i = int(i)
        if i%2==1:
            oddList.append(i)

except Exception as e:
    print(e)

for j in oddList:
    total+=j

print(total)    
