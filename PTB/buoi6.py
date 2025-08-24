print("a?")
a = int(input())

print("b")
b = int(input())

if a>=b:
    print(":(")
    print("Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.")


print("le/chan?")
user_input = input()

tong = 0

if user_input == "chan" or user_input == "Chan" or user_input=="CHAN":
    if a%2==0:
        x = range(a, b+1, 2)
        for i in x:
            tong+=i
    
    else:
        x = range(a+1, b+1, 2)
        for i in x:
            tong+=i

elif user_input == "le" or user_input == "Le" or user_input == "LE":
    if a%2==1:
        x = range(a, b+1, 2)
        for i in x:
            tong+=i
    
    else:
        x = range(a+1, b+1, 2)
        for i in x:
            tong+=i

else:
    print(":(")
    print("Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.")

print(tong)


