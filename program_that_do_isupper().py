text = input("Enter a text: ")
capitalized = True

for characters in text:
    if characters.islower():
        capitalized = False
    else:
        capitalized = True
print(capitalized)