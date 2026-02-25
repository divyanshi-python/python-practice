numbers = [10, 20, 10, 30, 40, 20, 50]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("List after removing duplicates:", unique)
