"""Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление."""


def dict_from_given(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except TypeError:
            result[str(value)] = key

    return result


if __name__ == '__main__':
    print(dict_from_given(some_list=[1, 2, 3], some_list2="Name"))
