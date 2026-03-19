text = input("Enter a text: ")
result = ""

for text_case in text:
    if text_case.isupper():
        result += text_case.swapcase()
    else:
        result += text_case
print(result)