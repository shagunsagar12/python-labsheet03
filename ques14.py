text = input("Enter a string: ")

result = ""

for ch in text:
    if ch.isalnum() or ch == " ":
        result += ch

print("String without punctuation:", result)