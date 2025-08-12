print("Hello, what is your name?")
name = input()

if name == "":
    print("Tell me your name, please.")

else:
    print("How old are you?")
    age = input()
    
    if age == "":
        print("Tell me your age, please.")

    else:
        print("What school are you in?")
        school = input()

        if school == "":
            print("What school are you in, please.")

        else:
            print("What is your favourite song")
            song = input()

            if song == "":
                print("You don't have any favourite songs, do you?")

            else:
                print("Hi " +  name + ", it's nice to meet you. You are " + age + " years old and you are study at " + school + ". You love the song " + song + ", don't you. You are my best friend. See you soon.")
 
