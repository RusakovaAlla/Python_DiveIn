"""Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака."""

belongings = {
    'спички': 1,
    'розжиг': 5,
    'еда': 30,
    'сменное': 50,
    'термос': 20,
    'аптечка': 30,
    'спальник': 70,
    'котелок': 30,
    'кружка': 5,
    'изолента': 2,
    'powerbank': 8,
    'телефон': 8
}

backpack = 200


def sort_items(items_list):
    sorted_items = dict(sorted(items_list.items(), key=lambda x: x[1], reverse=True))
    print(sorted_items)
    return sorted_items

packed_weigth = 0
packed_stuff = {}

for item, weight in belongings.items():
    if packed_weigth+weight <= backpack:
        packed_weigth += weight
        packed_stuff[item] = weight
    else:
        break

print(packed_stuff)

