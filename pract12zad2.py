def find_second_max(max1, max2):
    n = int(input("Введите число (0 для завершения): "))
    if n == 0:
        return max2
    if n > max1:
        return find_second_max(n, max1)
    elif n > max2:
        return find_second_max(max1, n)
    else:
        return find_second_max(max1, max2)
print("Введите последовательность натуральных чисел, завершив 0:")
second_max = find_second_max(0, 0)
print("Второй по величине элемент:", second_max)

