from collections import Counter, defaultdict


def collections_counter():
    x = int(input())
    sizes = Counter(input().split())
    n = int(input())
    total = 0
    while n > 0:
        cust_size, price = input().split()
        if sizes[cust_size] > 0:
            total += int(price)
            sizes[cust_size] -= 1
        n -= 1
    print(total)


def default_dict():
    # https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
    n, m = input().split()
    n, m = int(n), int(m)
    dd = defaultdict(list)
    for i in range(1, n + 1):
        a_word = input()
        dd[a_word].append(i)

    result = []
    for j in range(1, m + 1):
        b_word = input()
        if b_word in dd:
            result.append(dd[b_word])
        else:
            result.append(-1)

    for k in range(len(result)):
        if isinstance(result[k], list):
            print(*result[k], sep=' ')
        else:
            print(-1)
