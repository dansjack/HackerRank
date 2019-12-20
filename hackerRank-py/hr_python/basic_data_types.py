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


def finding_the_percentage(n):
    d = {}
    while n > 0:
        name, math, phys, chem = input().split()
        d[name] = (float(math), float(phys), float(chem))

        n -= 1

    query = input()
    avg = 0
    for i in d[query]:
        avg += i
    avg /= len(d[query])
    print('{:0.2f}'.format(avg))


def lists(n):
    result = []
    while n > 0:
        args = input().split()
        instruction = args.pop(0)
        if instruction == 'insert':
            result.insert(int(args[0]), int(args[1]))
        elif instruction == 'remove':
            result.remove(int(args[0]))
        elif instruction == 'append':
            result.append(int(args[0]))
        elif instruction == 'pop':
            result.pop()
        elif instruction == 'sort':
            result.sort()
        elif instruction == 'reverse':
            result.reverse()
        elif instruction == 'print':
            print('{}'.format(result))
        n -= 1


def tuples(n):
    print(hash(tuple([int(i) for i in input().split()])))
