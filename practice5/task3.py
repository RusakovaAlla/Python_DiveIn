"""
Создайте функцию генератор чисел Фибоначчи
"""


def fibonachhi_nums(num: int):
    """
    Функция принимает целое количество длины генерируемой последовательности
    :param num: количество элементов возвращаемой последовательности
    :return: последовательность Фибоначчи заданной длины
    """
    if num is None or isinstance(num, int) == False or num <= 0:
        print("Невозможно создать последовательность")
        return None
    else:
        fib = []
        if num <= 2:
            print("Лучше введите число побольше, иначе будут только единицы")
            fib = [1] * num
        else:
            for i in range(1, num):
                if i == 1:
                    fib.extend((1, 1))
                else:
                    fib.append(fib[i-2] + fib[i-1])
        return fib


if __name__ == '__main__':
    try:
        result = fibonachhi_nums(4)
    except NameError:
        result = "Упс, что-то с переменной..."
    print(result)
