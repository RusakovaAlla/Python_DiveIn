"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида “10.25%”.
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
"""


def dict_combine(list1: list, list2: list, list3: list):
    if len(list1) != len(list2) or len(list2) != len(list3):
        print("Преобразование невозможно - списки разной длины")
        return None
    else:
        zl = list(zip(list1, list2, list3))
        zl = {zl[i][0]: zl[i][1]*float(zl[i][2].split("%")[0])/100 for i in range(0, len(zl))}
        print(zl)
        return zl


if __name__ == '__main__':
    list_names = ["dsjkhg", "skajefd", "kasjfhn", "waleiuh"]
    list_disct = [5_000, 1_200, 535, 7_025]
    list_perc = ["10.25%", "7.25%", "20.1%", "8.6%"]
    dict_combine(list_names, list_disct, list_perc)
