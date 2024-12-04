n = int(input("Введите количество строк матрицы (n): "))
m = int(input("Введите количество столбцов матрицы (m): "))
print("Введите элементы матрицы построчно:")
matrix = []
for i in range(n):
    row = list(map(int, input(f"Строка {i + 1}: ").split()))
    matrix.append(row)
for i in range(n):
    matrix[i] = sorted(matrix[i])
print("Отсортированная матрица:")
for row in matrix:
    print(" ".join(map(str, row)))

