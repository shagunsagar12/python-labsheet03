# Find the longest word

text = input("Enter a string: ")

words = text.split()

if len(words) == 0:
    print("No words entered.")
else:
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    print("Longest word:", longest)