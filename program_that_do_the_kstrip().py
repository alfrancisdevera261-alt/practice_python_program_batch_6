name = input("Enter your name: ")
spaces = ""
for character in name:
    if character == " ":
        spaces += " "
    else:
        break
result = name.removeprefix(spaces)
print(result)