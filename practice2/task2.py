"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions
"""

import fractions


def check_fractal(number: list = []):
    while number is None or len(number) < 2:
        try:
            number = list(map(int, input(f"Введите дробь формата a/b: ").split("/")))
            if number[0] == 0 or number[1] == 0:
                number = None
                raise ZeroDivisionError
        except ValueError:
            print(f'Вводите только числа')
            number = None
            continue
        except IndexError:
            print(f'Вы не закончили ввод числа. Попробуйте еще раз')
            number = None
            continue
        except ZeroDivisionError:
            print(f'Делитель не может быть равен 0, а с числителем считать нечего. Повторите ввод')
            continue
    print(number)

    return number


def eq_res(fracs: list = []):
    """
    cocтавляем список частей дроби для операций
    :param fracs: список из двух списков - числитель и знаменатель дроби
    :return: значение суммы и произведения дробей
    """
    while len(fracs) < 2 or fracs is None:
        fracs.append(check_fractal())
    print(fracs)

    return fracs


def nod(fracs):
    """
    для операции сложения, необходимо найти значение наименьшего общего делителя
    :param fracs: список списков числителя и знаменателя двух дробей
    :return: значение наименьшего общего делителя
    """
    nod_frac = None
    for i in range(min(fracs[0], fracs[1]), 0, -1):
        if fracs[0] % i == 0 and fracs[1] % i == 0:
            nod_frac = i
            break

    return nod_frac


def sum_mult_fracs():
    """
    :return:
    """
    frac_list = eq_res()
    sum_frac = [frac_list[0][0] * frac_list[1][1] + frac_list[1][0] * frac_list[0][1],
                frac_list[0][1] * frac_list[1][1]]
    mult_frac = [frac_list[0][0] * frac_list[1][0], frac_list[0][1] * frac_list[1][1]]
    n_o_d = nod(sum_frac)
    while n_o_d != 1:
        n_o_d = nod(sum_frac)
        sum_frac = [i // n_o_d for i in sum_frac]
    n_o_d = nod(mult_frac)
    while n_o_d != 1:
        n_o_d = nod(mult_frac)
        mult_frac = [i // n_o_d for i in mult_frac]
    print(f"Сумма {frac_list[0][0]}/{frac_list[0][1]} и {frac_list[1][0]}/{frac_list[1][1]} равна {sum_frac[0]}/"
          f"{sum_frac[1]}")
    print(
        f"Произведение {frac_list[0][0]}/{frac_list[0][1]} и {frac_list[1][0]}/{frac_list[1][1]} равна "
        f"{mult_frac[0]}/{mult_frac[1]}")

    return sum_frac, mult_frac


if __name__ == '__main__':
    sum_mult_fracs()
