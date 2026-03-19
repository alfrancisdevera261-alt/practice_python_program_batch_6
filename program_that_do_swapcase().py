text = input("Enter a input: ")
result = ""

for characters in text:
    if characters.isupper():
        result += characters.lower()
    else:
        result += characters.upper()

print(result)