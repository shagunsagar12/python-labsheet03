# Replace spaces with underscores

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch == " ":
        result += "_"
    else:
        result += ch

print("Result:", result)