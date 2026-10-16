text = input("Enter a string: ")

characters = list(text)
characters.sort()

result = ""

for ch in characters:
    result += ch

print("Sorted string:", result)