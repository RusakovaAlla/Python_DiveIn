"""
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""


def form_triangle():
    tr_sides = []
    while len(tr_sides) < 3:
        try:
            side = float(input(f"Введите длину {len(tr_sides) + 1} стороны треугольника: "))
            if side <= 0:
                raise ValueError
            tr_sides.append(side)
        except ValueError:
            print(f"Длина стороны треугольника не может принимать такое значение. Повторите ввод")
            continue
    return check_triangle(tr_sides)


def check_triangle(some_sides: list):
    description = str()
    if some_sides[0] + some_sides[1] > some_sides[2] and \
            some_sides[0] + some_sides[2] > some_sides[1] and \
            some_sides[2] + some_sides[1] > some_sides[0]:
        description = "Tреугольник"
        flag = True
    else:
        description = f"Треугольник со сторонами {some_sides} начертить нельзя"
        flag = False
    if flag:
        if some_sides[0] == some_sides[1] == some_sides[2]:
            description += " равносторонний"
            return some_sides
        elif some_sides[0] == some_sides[1] or some_sides[0] == some_sides[2] or some_sides[1] == some_sides[2]:
            description += " равнобедренный"
            return some_sides
        else:
            description += " разносторонний"
        description += f" со сторонами {some_sides}"
    print(description)
    return some_sides


if __name__ == '__main__':
    form_triangle()
