a = int(input("a? "))
b = int(input("b? "))

#ucln = uoc chung lon nhat
for ucln in range (a, 0, -1):
    if a%ucln==0:
        if b%ucln==0:
            break

else:   #when a=0
    ucln = 1

#bcnn = boi chung nho nhat
bcnn = a*b/ucln
print("Boi chung nho nhat la", int(bcnn))

#rut gon phan so
a_rutgon = a/ucln
b_rutgon = b/ucln
print("Phan so rut gon cua", a, "/", b, "la", int(a_rutgon), "/", int(b_rutgon))

