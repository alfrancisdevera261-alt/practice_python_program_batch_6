text = input("Enter a text: ")
words = text.split()
title_word = []
for word in words:
    if len(word) > 0:
        format_word = word[0].upper() + word[1:].lower()
        title_word.append(format_word)
result = " ".join(title_word)
print(result)