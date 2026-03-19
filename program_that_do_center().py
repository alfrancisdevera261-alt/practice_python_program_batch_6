text = input("Enter a text: ")
width = int(input("Enter the width: "))

total_width = len(text) + width
left_width = total_width // 2
right_width = total_width - left_width

centered_text = " " * left_width + text + " " * right_width
print(centered_text)