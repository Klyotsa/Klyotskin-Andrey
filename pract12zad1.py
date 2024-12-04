def print_digits_reverse(n):
    if n == 0:
        return
    else:
        print(n % 10, end=" ")
        print_digits_reverse(n // 10)
N = int(input("Введите натуральное число N: "))
if N > 0:
    print("Цифры числа в обратном порядке:")
    print_digits_reverse(N)
else:
    print("Введите положительное натуральное число!")



