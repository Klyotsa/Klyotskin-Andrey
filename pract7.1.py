numbers = [3, -2, -5, 7, -8, -4, 0, 6, -3, -1]
for i in range(len(numbers) - 1):
    if numbers[i] < 0 and numbers[i + 1] < 0:
        print(f"Пара отрицательных чисел: {numbers[i]} и {numbers[i + 1]}")
