"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""


def parse_filepath():
    """

    :return:
    """
    path = None
    while path is None:
        try:
            path = str(input("Укажите путь к файлу: "))
            if ("\\" not in path or "/" not in path) and "." not in path:
                print("Не удалось найти файл. Проверьте указанный путь к файлу")
                # path = None
                continue
        except TypeError:
            print("Введите текстовый формат пути к файлу")
            # path = None
            continue
    if "\\" in path: #в файловой системе для указания используется обратная черта, что в Python escape-символ
        sign = "\\"
    else:
        sign = "/"
    *filepath, file = path.split(sign)
    filepath = sign.join(filepath)
    file_name, file_extention = file.split(".")
    print(f"Путь к файлу: {filepath}\n"
          f"Имя файла: {file_name}\n"
          f"Расширение файла: {file_extention}")

    return filepath, file_name, file_extention


if __name__ == '__main__':
    parse_filepath()
