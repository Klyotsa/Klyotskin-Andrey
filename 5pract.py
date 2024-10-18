for i in range(5):
    numbers = input(f"Введите последовательность {i + 1} (завершается числом 0): ").split()
    count = 0
    for number in numbers:
        if int(number) == 0:
            break
        count += 1
    print(f"Количество членов последовательности {i + 1}: {count}")
    if i < 4:
        continue_input = input("Хотите ввести еще одну последовательность? (да/нет): ").strip().lower()
        if continue_input != "да":
            break

