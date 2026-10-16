
text = input("Enter a string: ")

reverse = ""

for i in range(len(text) - 1, -1, -1):
    reverse = reverse + text[i]

if text == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")