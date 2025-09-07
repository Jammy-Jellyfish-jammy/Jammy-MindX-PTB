sum = 0

for i in range(1, 101):
    so_nguyen_to = True
    for j in range(2, i):
        if i%j==0:
            so_nguyen_to = False
    if so_nguyen_to == True:
        print(i)
        sum = sum + i

print(sum)

        