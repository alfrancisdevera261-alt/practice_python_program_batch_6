file_name = input("Enter a file name: ")
suffix = input("Enter a suffix to check: ")

if file_name[-len(suffix):] == suffix:
    print(f"'{file_name}' ends with '{suffix}'")
else:
    print(f"'{file_name}' does NOT end with '{suffix}'")
