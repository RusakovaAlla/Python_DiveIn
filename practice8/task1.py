"""
2. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
файлов и директорий.
"""

import os
import json
import csv
import pickle

__all__ = ['input_dir', 'get_dir_size', 'write_every_series', 'path_descr', 'measure_directory']


def input_dir():
    """
    получаем путь к директории и проверяем, есть ли она
    :return: список файлов директории
    """
    some_dir = None
    while some_dir is None or not os.path.isdir(some_dir):
        some_dir = input("Укажите директорию, в которой будем работать: ")
        if not os.path.isdir(some_dir):
            print(f"Директории {some_dir} не существует. Проверьте корректность введенного пути")

    return some_dir


def get_dir_size(some_dir):
    """
    считаем размер директории по вложенным файлам
    :param some_dir: любая директория
    :return:
    """
    total_size = 0
    for dirpath, _, filenames in os.walk(some_dir):
        for some_file in filenames:
            file_path = os.path.join(dirpath, some_file)
            if not os.path.islink(file_path):
                total_size += os.path.getsize(file_path)
    return total_size


def write_every_series(some_dict: dict):
    """
    pfgbcsdftv
    :param some_dict: словарь
    :return:
    """
    with open('dir_file.json', 'w', encoding='utf-8') as json_file:
        json.dump(some_dict, json_file, indent=4, separators=(',', ':'))
    # write_CSV
    data = [["Dir", "Files"]]
    for key, value in some_dict.items():
        data.append([key, value])
    with open('dir_file.csv', 'w', encoding='utf-8') as csv_f:
        write_csv = csv.writer(csv_f, dialect='excel', delimiter=',')
        write_csv.writerows(data)
    # write PICKLE
    with open('dir_file.pickle', 'wb') as pickle_file:
        pickle.dump(some_dict, pickle_file)


def path_descr(path):
    descr_dict = {"name": os.path.basename(path)}
    if os.path.isdir(path):
        descr_dict["type"] = "directory"
        descr_dict["size"] = f"{get_dir_size(path)} bytes"
        descr_dict["parent"] = f"{os.path.dirname(path)}"
        descr_dict["children"] = [path_descr(os.path.join(path, x)) for x in os.listdir(path)]
    else:
        descr_dict["type"] = "file"
        descr_dict["size"] = f"{os.stat(path).st_size} bytes"
        descr_dict["parent"] = f"{os.path.dirname(path)}"
    return descr_dict


def measure_directory():
    result = path_descr(input_dir())
    write_every_series(result)
    print(f"Данные сохранены в рабочей директории {os.getcwd()}")


if __name__ == "__main__":
    measure_directory()
