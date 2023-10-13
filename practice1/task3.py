"""Программа загадывает число от 0 до 1000.
Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
Для генерации случайного числа используйте код"""
from random import randint


def check_number(number=None, start=0):
    """
    :param number:
    :param start: номер по порядку
    :return:
    """
    while number is None or number < 0 or number > 1000:
        try:
            number = int(input(f"Попытка №{start}. Ваше число:"))
            if number < 0 or number > 1000:
                raise ValueError
        except (TypeError, ValueError) as Error:
            print(f'Айайай! Выберите число от 0 до 1000')
            continue

    return number


def guess_number(comp_number=randint(0, 1000), user_try=None, start=1):
    """
    :param comp_number: загаданное число
    :param user_try: вариант пользователя
    :param start: стадия игры
    :return:
    """
    print("Я загадал число от 0 до 1000. У вас есть 10 попыток, чтобы его угадать. Поехали!")

    print(comp_number)
    while start <= 10:
        user_try = check_number(None, start)
        if user_try > comp_number or start > 10:
            start += 1
            print("Я загадал число меньше")
        elif user_try < comp_number:
            start += 1
            print("Я загадал число больше")
        elif user_try == comp_number:
            print(f"Вы победили! Я загадал число {comp_number}. Поздравляю!")
            break
        else:
            continue
    else:
        print(f"Игра окончена. У вас больше нет попыток. Вы проиграли :(")


if __name__ == '__main__':
    guess_number()
