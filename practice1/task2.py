"""Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч. """

from math import sqrt, ceil

def simple_number():
    print("Проверим число!")
    number = int(input("Введите положительное число до 100 000: "))
    while number < 0 or number > 100_000:
        number = int(input("Повнимательнее. Нужно число больше 0 и не больше 100 000! Повторите ввод: "))
    if number > 2:
        for i in range(2, ceil(sqrt(number))):
            if number%i == 0:
                flag = True
                break
            else:
                flag = False
                continue
    else:
        flag = False
    if flag:
        print(f"Составное")
    else:
        print("Простое")



if __name__ == '__main__':
    simple_number()
