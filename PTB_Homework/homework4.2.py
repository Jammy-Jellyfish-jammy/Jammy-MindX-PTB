# Homework 4.2 - S  So sanh chieu cao
# Created 07-08-2025

# Header
print("So sanh chieu cao")

# Input
print("Nhap chieu cao cua An (cm)")
an =  float(input())

print("Nhap chieu cao cua Minh (cm)")
minh = float(input())

print("Nhap chieu cao cua Lan (cm)")
lan = float(input())

# Output
if an <= 0 or minh <= 0 or lan <= 0:
    print("Error! Try again")

if an > minh and an > lan:
    print("Lan cao nhat")

elif minh > an and minh > lan:
    print("Minh cao nhat")

elif lan > an and lan > minh:
    print("Lan cao nhat")

else:
    print("Maybe it's a tie")

#   !!! IMPORTANT !!!
#   This script can have some issue when print the output (else()).
