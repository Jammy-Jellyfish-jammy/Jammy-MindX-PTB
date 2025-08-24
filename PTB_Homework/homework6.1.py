#Homework 6.1 - Tinh tong cac so chan
#created date: 21-8-2025

n = int(input("nhap mot so nguyen duong n: "))

x = range(1, n+1)
sum = 0

for i in x:
    if i%2==0:
        sum+=i
    
print("Tong cac so chan tu 1 den", n, "la", sum)

