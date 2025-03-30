def factorial(n):
    # Возвращает факториал числа n. Для n = 0 возвращает 1.
    if n < 0:
        return "Ошибка: факториал для отрицательных чисел не определен."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def is_prime(n):
    # Проверяет, является ли число простым.
    # Если число не простое, возвращает n / 1 (то есть n).
    if n <= 1:
        return False  # Числа <= 1 не являются простыми
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return n  # Если число не простое, возвращаем его
    return True  # Если число простое, возвращаем True

def unique_sorted(lst):
    # Возвращает отсортированный список уникальных элементов из входного списка.
    # :param lst: Список любых элементов.
    # :return: Отсортированный список уникальных элементов.
    # Преобразуем список в множество для получения уникальных элементов, затем сортируем.
    return sorted(set(lst))

def group_words_by_length(words):
    # Создаем обычный словарь.
    grouped_words = {}

    # Проходим по каждому слову в списке.
    for word in words:
        # Получаем длину слова.
        length = len(word)
        # Добавление слова в список по длине.
        grouped_words.setdefault(length, []).append(word)

    return grouped_words