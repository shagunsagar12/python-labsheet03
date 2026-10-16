text = input("Enter a string: ")

found = False

for ch in text:
    count = 0

    for x in text:
        if ch == x:
            count += 1

    if count == 1:
        print("First non-repeated character:", ch)
        found = True
        break

if not found:
    print("No non-repeated character found.")