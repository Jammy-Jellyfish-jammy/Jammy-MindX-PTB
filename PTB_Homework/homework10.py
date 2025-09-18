so_bai = int(input("So bai da lam? "))
diem = []
for i in range(1, so_bai+1):
    j = float(input("So diem bai "))
    diem.append(j)

diem.sort()

h = diem[0]
diem_new = []
diem_newest = []

for j in diem:
    if j != h:
        diem_new.append(j)

    if j>=8:
        diem_newest.append(j)

print(diem_new)
print(diem_newest)



