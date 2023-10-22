"""Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов."""

from random import randint
from collections import Counter


def result_list():
    num = None
    random_list = []
    doubles_list = []
    while num is None or num <= 0 or num > 1000:
        try:
            num = int(input("Укажите длину генерируемого списка. Не больше 1000 элементов "))
        except (TypeError, ValueError):
            print("Некорректное число, повторите ввод")
            continue
    [random_list.append(randint(0, num)) for _ in range(1, num+1)]
    print(Counter(random_list))
    for key in Counter(random_list):
        if Counter(random_list)[key] > 1:
            doubles_list.append(key)
    print(f"Удалены повторяющиеся элементы {set(doubles_list)}")

    return set(random_list)


if __name__ == '__main__':
    result_list()
