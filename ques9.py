# Count number of words

text = input("Enter a string: ")

count = 0
inside_word = False

for ch in text:
    if ch != " ":
        if not inside_word:
            count += 1
            inside_word = True
    else:
        inside_word = False

print("Number of words:", count)