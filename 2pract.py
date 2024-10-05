import math
def calculate_s (x, Y, z):
    first_term = math.log(y **(-math.sqrt(abs(x))))
    second_term = (x - (y / 2))
    third_term = math.sin(math.atan(z)) ** 2
    s = first_term *second_term + third_term
    return s
try:
    x = float(input("Введите значение x: "))
    y_input = input("Введите значение y: ")
    y = float(eval(y_input))
    z = float(input("Введите значение z: "))
    s_result = calculate_s (x, y, z)
    print(f"Результат: s = {s_result: .3f}")
except ValueError:
        print("Ошибка: Введите правильные значения.")
