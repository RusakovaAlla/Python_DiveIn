"""Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата."""


def number_is_16number(number=None):
    while number is None or isinstance(number, int) != True:
        try:
            number = int(input(f"Введите целое число: "))
        except ValueError as Error:
            print(f'Вводите только числа')
            continue

    return number


def check_16_number1():
    number = oper_num = number_is_16number()
    check_hex = hex(number)
    system_16 = "0123456789ABCDEF"  # набор цифр для перевода числа
    decimal_2_16 = []
    while oper_num > 0:
        ost = oper_num % 16  # остаток от деления на 16
        digit_16 = system_16[ost]  # Получаем шестнадцатеричную цифру
        decimal_2_16.insert(0, digit_16)
        oper_num //= 16  # остаток от деления для определения следующей цифры
    else:
        decimal_2_16.insert(0, "0x")
    if ''.join(decimal_2_16).lower() == check_hex:
        print(f"Функция1: {number} в шестнадцатеричной системе счисления {check_hex}")
        return str(''.join(decimal_2_16))
    else:
        return "Что-то пошло не так!"


def check_16_number2():
    number = number_is_16number()
    number_16 = '0x'+str(format(number, "x"))
    print(f"Функция2: {number} в шестнадцатеричной системе счисления {number_16}")
    return number_16


if __name__ == '__main__':
    check_16_number1()
    check_16_number2()
