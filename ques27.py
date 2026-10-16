numbers = list(map(int, input("Enter numbers: ").split()))

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

if len(unique) < 2:
    print("Second largest number does not exist.")
else:
    unique.sort()
    print("Second largest number:", unique[-2])