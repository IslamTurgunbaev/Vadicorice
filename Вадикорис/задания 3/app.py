def task_1():
    print("\n--- Задание 1. Удаление части строки ---")
    word = input("Введите слово: ")
    result = word[2:-2]
    print(f"Результат: {result}\n")


def task_2():
    print("\n--- Задание 2. Перестановка частей слова ---")
    word = "информатика"
    result = word[5:] + word[:5]
    print(f"Исходное слово: {word}")
    print(f"Ожидаемый результат: {result}\n")


def task_3():
    print("\n--- Задание 3. Чётные и нечётные индексы ---")
    word = "информатика"
    even_chars = word[::2]
    odd_chars = word[1::2]
    print(f"Исходное слово: {word}")
    print(f"Чётные индексы: {even_chars}")
    print(f"Нечётные индексы: {odd_chars}\n")


def task_4():
    print("\n--- Задание 4. Замена середины звёздочками ---")
    word = input("Введите слово (не менее 6 символов): ")
    if len(word) < 6:
        print("Ошибка: длина слова должна быть не менее 6 символов!\n")
        return
    result = word[:3] + '*' * (len(word) - 6) + word[-3:]
    print(f"Результат: {result}\n")


def task_5():
    print("\n--- Задание 5. Обратный порядок части строки ---")
    word = "информатика"
    result = word[:3] + word[3:][::-1]
    print(f"Исходное слово: {word}")
    print(f"Ожидаемый результат: {result}\n")


def task_6():
    print("\n--- Задание 6. Обратный порядок первой половины ---")
    text = input("Введите строку с чётным количеством символов: ")
    if len(text) % 2 != 0:
        print("Предупреждение: количество символов нечётное!")
    
    middle = len(text) // 2
    result = text[:middle][::-1] + text[middle:]
    print(f"Результат: {result}\n")


def task_7():
    print("\n--- Задание 7. Обмен первого и последнего символов ---")
    word = input("Введите слово (не менее 2 символов): ")
    if len(word) < 2:
        print("Ошибка: слово слишком короткое!\n")
        return
    result = word[-1] + word[1:-1] + word[0]
    print(f"Результат: {result}\n")


def task_8():
    print("\n--- Задание 8. Удаление символа по индексу ---")
    text = input("Введите строку: ")
    try:
        index = int(input("Введите индекс: "))
        if 0 <= index < len(text):
            result = text[:index] + text[index+1:]
            print(f"Результат: {result}\n")
        else:
            print("Ошибка: индекс выходит за пределы строки!\n")
    except ValueError:
        print("Ошибка: введите целое число!\n")


def task_9():
    print("\n--- Задание 9. Получение фрагмента по индексам ---")
    text = input("Введите строку: ")
    try:
        start = int(input("Начальный индекс: "))
        end = int(input("Конечный индекс: "))
        result = text[start:end]
        print(f"Результат: {result}\n")
    except ValueError:
        print("Ошибка: индексы должны быть целыми числами!\n")


def task_10():
    print("\n--- Задание 10. Проверка одинаковых половин ---")
    text = input("Введите строку с чётным количеством символов: ")
    middle = len(text) // 2
    
    if text[:middle] == text[middle:]:
        print("Результат: половины одинаковые\n")
    else:
        print("Результат: половины разные\n")


def main_menu():
    tasks = {
        "1": task_1,
        "2": task_2,
        "3": task_3,
        "4": task_4,
        "5": task_5,
        "6": task_6,
        "7": task_7,
        "8": task_8,
        "9": task_9,
        "10": task_10
    }

    while True:
        print("================ МЕНЮ ЗАДАНИЙ ================")
        print("1. Удаление части строки (первые и последние 2)")
        print("2. Перестановка частей слова (после 5-го символа)")
        print("3. Чётные и нечётные индексы")
        print("4. Замена середины звёздочками")
        print("5. Обратный порядок части строки (после 3-го)")
        print("6. Обратный порядок первой половины")
        print("7. Обмен первого и последнего символов")
        print("8. Удаление символа по индексу")
        print("9. Получение фрагмента по индексам")
        print("10. Проверка одинаковых половин")
        print("0. Выход из программы")
        print("==============================================")

        choice = input("Выберите номер задания (0-10): ").strip()

        if choice == "0":
            print("\nПрограмма завершена. До свидания!")
            break
        elif choice in tasks:
            tasks[choice]()
        else:
            print("\nНеверный ввод. Пожалуйста, выберите число от 0 до 10.\n")


if __name__ == "__main__":
    main_menu()