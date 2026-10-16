# Extract uppercase characters

text = input("Enter a string: ")

uppercase = ""

for ch in text:
    if ch.isupper():
        uppercase += ch

print("Uppercase characters:", uppercase)