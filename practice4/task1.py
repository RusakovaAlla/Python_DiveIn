"""Напишите функцию для транспонирования матрицы"""
import copy


def transp_matrix(list_of_lists):
    tm = copy.deepcopy(list_of_lists)
    for i in range(len(tm)):
        for j in range(len(tm[0])):
            tm[j][i] = list_of_lists[i][j]
    return tm


if __name__ == '__main__':
    given_matrix = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    print(transp_matrix(given_matrix))
