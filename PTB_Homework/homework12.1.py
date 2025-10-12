def printer(content):
    printContent = ""
    for character in content:
        printContent+=character
        print(printContent)

contentInput = input("Type something here: ")
printer(contentInput)
