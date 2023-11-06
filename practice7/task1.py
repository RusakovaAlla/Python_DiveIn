"""Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например, для диапазона [3, 6]
берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
Далее счётчик файлов и расширение.
"""
import os
import re
from math import inf

__all__ = ["set_work_dir", "rename_params", "rename_dir_files"]

def set_work_dir():
    """
    получаем путь к директории и проверяем, есть ли она
    :return: список файлов директории
    """
    dir_content = None
    while dir_content is None or not os.path.isdir(dir_content):
        dir_content = input("Укажите директорию, в которой будем работать: ")
        if not os.path.isdir(dir_content):
            print(f"Директории {dir_content} не существует. Проверьте корректность введеннного пути")
    os.chdir(dir_content)


def rename_params():
    """
    задаем параметры для переименования
    :return: кортеж с параметрами для rename_dir_files()
    """
    params_dir = {"new_name": None, "ext_old": None, "ext_new": None, "num_file": None, "name_start_end": None}
    while not params_dir["new_name"]:
        try:
            params_dir["new_name"] = str(input("Введите новое имя файла: "))
        except TypeError:
            print("Ошибка. Повторите ввод")
            continue
    while not params_dir["ext_old"]:
        try:
            params_dir["ext_old"] = str(input("Укажите расширение файлов для переименования: "))
            if not re.match("^\.{1}", params_dir["ext_old"]):
                params_dir["ext_old"] = "." + params_dir["ext_old"]
        except ValueError:
            print("Ошибка. Повторите ввод")
            continue
    while not params_dir["ext_new"]:
        try:
            params_dir["ext_new"] = str(input("Укажитe, какое расширение файлов установить: "))
            if not re.match("^\.{1}", params_dir["ext_new"]):
                params_dir["ext_new"] = "." + params_dir["ext_new"]
        except ValueError:
            print("Ошибка. Повторите ввод")
            continue
    while not params_dir["num_file"]:
        try:
            params_dir["num_file"] = int(input("Укажитe количество знаков нумерации файла: "))
            if params_dir["num_file"] == 0:
                params_dir["num_file"] = 1
        except ValueError:
            print("Ошибка. Повторите ввод")
            continue
    while not params_dir["name_start_end"]:  # определим, хочет ли пользователь сохранять часть файла
        try:
            print("Укажите, какую часть имени файла оставить (начиная с 0). Не указывайте ничего, если не нужно")
            params_dir["name_start_end"] = list(map(int, input("Введите через пробел диапазон: ").split(" ")))
            if len(params_dir["name_start_end"]) != 2:
                raise TypeError
        except TypeError:
            print("Ошибка. Повторите ввод")
            continue
        except ValueError:
            params_dir["name_start_end"] = [0, +inf]

    return params_dir


def rename_dir_files(**kwargs):
    """
    :param new_name: str, желаемое конечное имя файла
    :param num_file: int, количество цифр в порядковом номере. По умолчанию равно 1, чтобы избежать дублирования
    :param ext_start: str, расширение исходного файла c ".", переименование работает только для них
    :param ext_end: str, желаемое расширение конечного файла "."
    :param name_start_end: list, (необязательно) диапазон сохраняемого оригинального имени
    :return: файлы переименованы, [False, True]
    """
    new_name = kwargs["new_name"]
    ext_old = kwargs["ext_old"]
    ext_new = kwargs["ext_new"]
    num_file = kwargs["num_file"]
    name_start_end = kwargs["name_start_end"]

    if new_name is None or ext_old is None or ext_new is None:
        print("Неверно указаны заменяемое расширение и параметры замены")
        return False
    num_end = 1
    for ent in os.listdir():
        if not os.path.isfile(ent):
            continue
        if ext_old not in ent:
            continue
        ent_name = ent.split(".")[0]
        if name_start_end[0] > len(ent_name):
            print(f"Имя оригинального файла короткое. "
                  f"Переименовываем {ent} ... "
                  f"{ent_name}_{new_name}_{num_end:{f'0{num_file}'}}{ext_new}")
            os.rename(ent, f"{ent_name}_{new_name}_{num_end:{f'0{num_file}'}}{ext_new}")
        elif name_start_end[0] <= len(ent_name) < name_start_end[1]:
            print(f"Имя оригинального файла короткое. "
                  f"Переименовываем {ent} ... "
                  f"{ent_name[name_start_end[0]:]}_{new_name}_{num_end:{f'0{num_file}'}}{ext_new}")
            os.rename(ent, f"{ent_name[name_start_end[0]:]}_{new_name}_{num_end:{f'0{num_file}'}}{ext_new}")
        elif len(ent_name) >= name_start_end[1]:
            print(f"Переименовываем {ent} ... "
                  f"{ent_name[name_start_end[0]:(name_start_end[1] + 1)]}_{new_name}_"
                  f"{num_end:{f'0{num_file}'}}{ext_new}")
            os.rename(ent,
                      f"{ent_name[name_start_end[0]:(name_start_end[1] + 1)]}_{new_name}_"
                      f"{num_end:{f'0{num_file}'}}{ext_new}")
        num_end += 1
    print("Файлы переименованы")
    return True


if __name__ == "__main__":
    set_work_dir()
    params = rename_params()
    rename_dir_files(**params)
    