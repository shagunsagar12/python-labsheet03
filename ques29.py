list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

difference = []

for item in list1:
    if item not in list2:
        difference.append(item)

print("Difference of first list from second list:", difference)