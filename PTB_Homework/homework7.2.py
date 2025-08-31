#Homework 7.2 - Kiem tra password
#created date: 27-8-2025

from getpass import getpass

#Sign Up
print("Sign Up")
userName = input("Username: ")
userPass = getpass("Password: ")
userPassConfirm = getpass("Confirm Password: ")

if userPass != userPassConfirm: #Confirm the password
    print("Sorry, the confirm password you've typed didn't match the password.")

else:
    #Log In
    print("Log in")
    print("Username:", userName)
    userPassCount = 0   #Count
    while userPassCount <= 5:
        userPassInput = getpass("Password: ")
        if userPassInput == userPass:
            print("Welcome back,", userName)
            break

        else:
            print("Wrong password, please try again!")
            userPassCount+=1

    else:   #If userPassCount > 5
        print("Sorry, you can't log in to", userName, "now.")