text = input("Enter a text: ")
width = int(input("Enter the width: "))

space_needed = width - len(text)

if space_needed > 0:
    formatted_text = text + "-" * space_needed
else:
    formatted_text = text
print(formatted_text)