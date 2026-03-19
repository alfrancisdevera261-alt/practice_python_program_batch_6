text = input("Enter a text: ")
words = text.split()

for word in words:
    if len(word) > 0:
        title_word = word[0].upper + word[1:].lower