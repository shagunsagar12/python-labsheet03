numbers = list(map(int, input("Enter numbers: ").split()))

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest element:", largest)
print("Smallest element:", smallest)