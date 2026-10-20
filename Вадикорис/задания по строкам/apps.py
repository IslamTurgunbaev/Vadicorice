import string


# ==========================================
# Задание 1. Подсчёт частоты слов
# ==========================================
def task_1_word_frequency():
  print("\n--- Задание 1: Подсчёт частоты слов ---")
  text = input("Введите предложение: ")
  for p in string.punctuation:
    text = text.replace(p, "")

  words = text.lower().split()
  freq = {}
  for word in words:
    freq[word] = freq.get(word, 0) + 1

  result = [f"{word} — {count}" for word, count in freq.items()]
  print("Вывод:", "; ".join(result))


# ==========================================
# Задание 2. Самый частый символ
# ==========================================
def task_2_most_frequent_char():
  print("\n--- Задание 2: Самый частый символ ---")
  text = input("Введите строку: ").replace(" ", "")
  if not text:
    print("Вывод: Строка пуста")
    return

  counts = {}
  for char in text:
    counts[char] = counts.get(char, 0) + 1

  max_char = text[0]
  max_count = counts[max_char]
  for char in text:
    if counts[char] > max_count:
      max_count = counts[char]
      max_char = char

  print(f"Вывод: {max_char} — {max_count}")


# ==========================================
# Задание 3. Нормализация предложения
# ==========================================
def task_3_normalize_sentence():
  print("\n--- Задание 3: Нормализация предложения ---")
  text = input("Введите предложение: ")
  words = text.strip().split()
  if not words:
    print("Вывод: .")
    return

  cleaned_text = " ".join(words)
  normalized = cleaned_text[0].upper() + cleaned_text[1:].lower()
  if not normalized.endswith("."):
    normalized += "."

  print("Вывод:", normalized)


# ==========================================
# Задание 4. Удаление соседних повторов
# ==========================================
def task_4_remove_adjacent_duplicates():
  print("\n--- Задание 4: Удаление соседних повторов ---")
  text = input("Введите предложение: ")
  words = text.split()
  if not words:
    print("Вывод:")
    return

  result = [words[0]]
  for word in words[1:]:
    if word.lower() != result[-1].lower():
      result.append(word)

  print("Вывод:", " ".join(result))


# ==========================================
# Задание 5. Проверка адреса электронной почты
# ==========================================
def task_5_validate_email():
  print("\n--- Задание 5: Проверка почты ---")
  email = input("Введите адрес электронной почты: ")
  if email.count("@") != 1:
    print("Вывод: Некорректный адрес")
    return

  username, domain = email.split("@")
  if not username or not domain:
    print("Вывод: Некорректный адрес")
    return

  if domain.startswith(".") or domain.endswith(".") or "." not in domain:
    print("Вывод: Некорректный адрес")
    return

  print("Вывод: Корректный адрес")


# ==========================================
# Задание 6. Шифр Цезаря
# ==========================================
def task_6_caesar_cipher():
  print("\n--- Задание 6: Шифр Цезаря ---")
  text = input("Введите строку (латинские буквы): ")
  shift = int(input("Введите число сдвига: "))

  result = []
  for char in text:
    if "a" <= char <= "z":
      new_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
      result.append(new_char)
    elif "A" <= char <= "Z":
      new_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
      result.append(new_char)
    else:
      result.append(char)

  print("Вывод:", "".join(result))


# ==========================================
# Задание 7. Сумма чисел в тексте
# ==========================================
def task_7_sum_numbers_in_text():
  print("\n--- Задание 7: Сумма чисел в тексте ---")
  text = input("Введите строку: ")
  total_sum = 0
  current_num = ""

  for char in text:
    if char.isdigit():
      current_num += char
    else:
      if current_num:
        total_sum += int(current_num)
        current_num = ""

  if current_num:
    total_sum += int(current_num)

  print("Вывод:", total_sum)


# ==========================================
# Задание 8. Чередование регистра
# ==========================================
def task_8_alternate_case():
  print("\n--- Задание 8: Чередование регистра ---")
  text = input("Введите строку: ")
  result = []
  upper_case = True

  for char in text:
    if char.isalpha():
      result.append(char.upper() if upper_case else char.lower())
      upper_case = not upper_case
    else:
      result.append(char)

  print("Вывод:", "".join(result))


# ==========================================
# Задание 9. Проверка анаграмм
# ==========================================
def task_9_check_anagrams():
  print("\n--- Задание 9: Проверка анаграмм ---")
  str1 = input("Введите первую строку: ")
  str2 = input("Введите вторую строку: ")

  def clean_and_sort(s):
    filtered = [c.lower() for c in s if c.isalpha()]
    return sorted(filtered)

  if clean_and_sort(str1) == clean_and_sort(str2):
    print("Вывод: Это анаграммы")
  else:
    print("Вывод: Это не анаграммы")


# ==========================================
# Задание 10. Форматирование номера телефона
# ==========================================
def task_10_format_phone_number():
  print("\n--- Задание 10: Форматирование номера телефона ---")
  phone = input("Введите номер телефона: ")
  digits = "".join([c for c in phone if c.isdigit()])

  if len(digits) == 11:
    if digits[0] == "8":
      digits = "7" + digits[1:]
    if digits[0] == "7":
      formatted = f"+7 ({digits[1:4]}) {digits[4:7]}-{digits[7:9]}-{digits[9:]}"
      print("Вывод:", formatted)
      return

  print("Вывод: Некорректный номер")


# ==========================================
# Задание 11. Общий префикс слов
# ==========================================
def task_11_longest_common_prefix():
  print("\n--- Задание 11: Общий префикс слов ---")
  text = input("Введите несколько слов через пробел: ")
  words = text.split()
  if not words:
    print("Вывод: Нет общего префикса")
    return

  prefix = words[0]
  for word in words[1:]:
    while not word.startswith(prefix):
      prefix = prefix[:-1]
      if not prefix:
        break
    if not prefix:
      break

  if prefix:
    print("Вывод:", prefix)
  else:
    print("Вывод: Нет общего префикса")


# ==========================================
# Задание 12. Статистика текста
# ==========================================
def task_12_text_statistics():
  print("\n--- Задание 12: Статистика текста ---")
  text = input("Введите строку: ")
  words_count = len(text.split())
  letters_count = sum(1 for c in text if c.isalpha())
  digits_count = sum(1 for c in text if c.isdigit())
  punct_count = sum(1 for c in text if c in string.punctuation)

  print(
      f"Вывод: Слов: {words_count}; букв: {letters_count}; цифр:"
      f" {digits_count}; знаков препинания: {punct_count}"
  )


# ==========================================
# Главное меню программы
# ==========================================
def main():
  while True:
    print("\n" + "=" * 50)
    print("ПРАКТИЧЕСКАЯ РАБОТА: ЗАДАНИЯ ПО СТРОКАМ В PYTHON")
    print("=" * 50)
    print("1. Подсчёт частоты слов")
    print("2. Самый частый символ")
    print("3. Нормализация предложения")
    print("4. Удаление соседних повторов")
    print("5. Проверка адреса электронной почты")
    print("6. Шифр Цезаря")
    print("7. Сумма чисел в тексте")
    print("8. Чередование регистра")
    print("9. Проверка анаграмм")
    print("10. Форматирование номера телефона")
    print("11. Общий префикс слов")
    print("12. Статистика текста")
    print("0. Выход из программы")
    print("=" * 50)

    choice = input("Выберите номер задания (0-12): ").strip()

    if choice == "1":
      task_1_word_frequency()
    elif choice == "2":
      task_2_most_frequent_char()
    elif choice == "3":
      task_3_normalize_sentence()
    elif choice == "4":
      task_4_remove_adjacent_duplicates()
    elif choice == "5":
      task_5_validate_email()
    elif choice == "6":
      task_6_caesar_cipher()
    elif choice == "7":
      task_7_sum_numbers_in_text()
    elif choice == "8":
      task_8_alternate_case()
    elif choice == "9":
      task_9_check_anagrams()
    elif choice == "10":
      task_10_format_phone_number()
    elif choice == "11":
      task_11_longest_common_prefix()
    elif choice == "12":
      task_12_text_statistics()
    elif choice == "0":
      print("\nРабота завершена. Успехов в учёбе!")
      break
    else:
      print("\nНеверный ввод! Пожалуйста, введите число от 0 до 12.")


if __name__ == "__main__":
  main()