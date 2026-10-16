text = input("Enter the main string: ")
substring = input("Enter the substring: ")

if substring in text:
    print("Substring exists in the string.")
else:
    print("Substring does not exist.")