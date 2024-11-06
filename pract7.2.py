numbers = [1, 2, 2, 3, 4, 5, 5, 6, 7, 7]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Новый массив без дубликатов:", unique_numbers)

