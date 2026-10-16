text = input("Enter a string: ")

result = ""

for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            result += ch.upper()
        else:
            result += ch.lower()
    else:
        result += ch

print("Result:", result)