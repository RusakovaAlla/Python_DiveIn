"""
Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""
from random import randint
import time
from tqdm import tqdm
import task2

__all__ = ["generate_queens", "select_combos"]

def generate_queens():
    gen_tuple = []
    for _ in range(0, 8):
        gen_tuple.append((randint(1, 8), randint(1, 8)))
    gen_tuple = tuple(gen_tuple)

    return gen_tuple


# исходим из предположения, что заданное количество вариантов решения существует
def select_combos():
    combo_num = 1
    dict_placement = {}
    print(f"Поиск...")
    while combo_num < 5:
        queens_placement = generate_queens()
        if task2.check_board(queens_placement):
            if queens_placement not in dict_placement.values():
                for _ in tqdm(range(combo_num), desc=f"Подбор расстановки №{combo_num}..."):
                    time.sleep(0.1)
                dict_placement[combo_num] = queens_placement
                combo_num += 1
            else:
                continue
    return dict_placement


if __name__ == "__main__":
    combos = select_combos()
    print("Варианты размещения ферзей:")
    for i in combos.items():
        print(i)

