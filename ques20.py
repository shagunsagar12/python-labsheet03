text = input("Enter a sentence: ")

words = text.lower().split()

most_word = ""
highest = 0

for word in words:
    count = 0

    for w in words:
        if word == w:
            count += 1

    if count > highest:
        highest = count
        most_word = word

print("Most repeated word:", most_word)
print("Frequency:", highest)