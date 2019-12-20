from collections import Counter


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
