print("n?")
n = int(input())

while n<0 or n>=100:
    print("Try again!")
    n = int(input())

for i in range (n, 101):
    print(i, end="\t")

print()


    

 