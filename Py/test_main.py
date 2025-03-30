from main import (factorial, is_prime, unique_sorted, group_words_by_length)
def test_factorial():
    assert(factorial(0) == 1)  # Факториал нуля.
    assert(factorial(1) == 1)  # Факториал единицы.
    assert(factorial(2) == 2)  # Факториал двойки.
    assert(factorial(3) == 6)  # Факториал тройки.
    assert(factorial(4) == 24)  # Факториал четверки.
    assert(factorial(5) == 120)  # Факториал пятерки.
    assert(factorial(6) == 720)  # Факториал шестерки.
    assert(factorial(10) == 3628800)  # Факториал десяти.
    assert(factorial(-1) == "Ошибка: факториал для отрицательных чисел не определен.")  # Отрицательное число.
    assert(factorial(-5) == "Ошибка: факториал для отрицательных чисел не определен.")  # Еще одно отрицательное число.

# Запуск тестов
test_factorial()
print("(Факториал) тесты пройдены успешно!")


def test_is_prime():
    assert(is_prime(2) is True)  # 2 - простое число.
    assert(is_prime(3) is True)  # 3 - простое число.
    assert(is_prime(4) == 4)      # 4 - составное число.
    assert(is_prime(5) is True)  # 5 - простое число.
    assert(is_prime(9) == 9)      # 9 - составное число.
    assert(is_prime(11) is True)  # 11 - простое число.
    assert(is_prime(15) == 15)     # 15 - составное число.
    assert(is_prime(1) is False)  # 1 - не является простым.
    assert(is_prime(0) is False)  # 0 - не является простым.
    assert(is_prime(-5) is False) # Отрицательное число - не является простым.


test_is_prime()
print("(Простое число) тесты  пройдены успешно!")


def test_unique_sorted():
    assert unique_sorted([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5] # Все уникальные элементы.
    assert unique_sorted([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5] # Обратный порядок.
    assert unique_sorted([1, 1, 2, 2, 3, 3]) == [1, 2, 3] # Повторяющиеся элементы.
    assert unique_sorted([]) == [] # Пустой список.
    assert unique_sorted(["apple", "banana", "apple"]) == ["apple", "banana"] # Строки.
    assert unique_sorted([3.1, 2.2, 3.1, 4.4]) == [2.2, 3.1, 4.4] # Числа с плавающей запятой.
    assert unique_sorted(["2", "1", "1", "3"]) == ["1", "2", "3"]  # Строки.
    assert unique_sorted([True, False, True]) == [False, True] # Логические значения.
    assert unique_sorted([None, None]) == [None]  # Все элементы - None.
    assert unique_sorted(["Hello", "hello", "HELLO"]) == ["HELLO", "Hello", "hello"] # Разные регистры.


test_unique_sorted()
print("(Список уникальных элементов) тесты пройдены успешно!")


def test_group_words_by_length():
    # Пустой список.
    assert group_words_by_length([]) == {}

    # Список с одним словом.
    assert group_words_by_length(["hello"]) == {5: ["hello"]}

    # Список с несколькими словами разной длины.
    assert group_words_by_length(["hi", "hello", "a", "world"]) == {2: ["hi"], 5: ["hello", "world"], 1: ["a"]}

    # Слова одинаковой длины.
    assert group_words_by_length(["cat", "dog", "bat"]) == {3: ["cat", "dog", "bat"]}

    # Слова разной длины и с повторениями.
    assert group_words_by_length(["apple", "banana", "pear", "kiwi", "fig", "grape"]) == {3: ["fig"], 4: ["pear", "kiwi"], 5: ["apple", "grape"], 6: ["banana"]}

    # Слова с пробелами.
    assert group_words_by_length(["hello world", "hi", "python", "code"]) == {11: ["hello world"], 2: ["hi"], 6: ["python"], 4: ["code"]}

    # Слова с цифрами.
    assert group_words_by_length(["word1", "word2", "123", "4567"]) == {5: ["word1", "word2"], 3: ["123"], 4: ["4567"]}

    # Смешанные символы.
    assert group_words_by_length(["^&*!@", "abc", "12345", "hello!"]) == {5: ["^&*!@", "12345"], 3: ["abc"], 6: ["hello!"]}

    # Слова с разными регистрами.
    assert group_words_by_length(["Python", "python", "PYTHON"]) == {6: ["Python", "python", "PYTHON"]}

    # Слова с пробелами и смешанными символами.
    assert group_words_by_length(["Hello World!", "Test 123", "Python3"]) == {12: ["Hello World!"], 8: ["Test 123"], 7: ["Python3"]}

test_group_words_by_length()
print("(Группировка слов) тесты пройдены успешно!")