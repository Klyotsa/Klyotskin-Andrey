n = int(input("Введите количество строк матрицы (n): "))
m = int(input("Введите количество столбцов матрицы (m): "))
print("Введите элементы матрицы построчно:")
matrix = []
for i in range(n):
    row = list(map(float, input(f"Строка {i + 1}: ").split()))
    matrix.append(row)
new_matrix = []
for row in matrix:
    min_element = min(row)
    transformed_row = [
        (0 if x == min_element and x % 2 == 0 else 1 if x == min_element else x)
        for x in row
    ]
    new_matrix.append(transformed_row)
print("Новая матрица:")
for row in new_matrix:
    print(" ".join(map(str, row)))


