from collections import OrderedDict


def list_comprehensions(x, y, z, n):
    return [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in
            range(z + 1) if ((i + j + k) != n)]


def nested_lists(n):
    grades = {}
    for i in range(n):
        name = input()
        grades[name] = float(input())

    sorted_grades = sorted([[v, k] for k, v in grades.items()])
    minimum = sorted_grades[0][0]
    sorted_grades = [k for k in sorted_grades if k[0] != minimum]

    print(sorted_grades)
    minimum = sorted_grades[0][0]

    for k in sorted_grades:
        if k[0] == minimum:
            print(k[1])


nested_lists(4)
