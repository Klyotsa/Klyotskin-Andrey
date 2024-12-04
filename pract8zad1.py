def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def subtract_fractions(a, b, c, d):
    denominator = b * d
    numerator = a * d - c * b
    greatest_common_divisor = gcd(abs(numerator), denominator)
    numerator //= greatest_common_divisor
    denominator //= greatest_common_divisor
    return numerator, denominator
A = int(input("Введите числитель первой дроби (A): "))
B = int(input("Введите знаменатель первой дроби (B): "))
C = int(input("Введите числитель второй дроби (C): "))
D = int(input("Введите знаменатель второй дроби (D): "))
result_numerator, result_denominator = subtract_fractions(A, B, C, D)
print(f"Результат вычитания: {result_numerator}/{result_denominator}")
