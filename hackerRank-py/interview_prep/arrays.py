def hourglass_sum(arr):
    """
    :returns integer, the maximum hourglass sum in the array.
    an hourglass is a subset of values of the form: a b c
                                                      d
                                                    e f g
    """
    hourglasses = []
    for i in range(4):
        mid = 1
        for j in range(4):
            hourglasses.append(
                sum(arr[i][j:j + 3] + arr[i + 2][j:j + 3]) + arr[i + 1][mid])
            mid += 1
    return max(hourglasses)


def minimum_bribes(q):
    total = 0
    local_total = 0

    for i in range(len(q), -1, -1):
        for j in range(i, len(q)):
            if q[i] > q[j]:
                local_total += 1
        if local_total > 2:
            break
        total += local_total
        local_total = 0

    if local_total > 2:
        print('Too chaotic')
    else:
        print(total)


minimum_bribes([2, 1, 5, 3, 4])
# minimum_bribes([2, 5, 1, 3, 4])
minimum_bribes([1, 2, 5, 3, 7, 8, 6, 4])
minimum_bribes([5, 1, 2, 3, 7, 8, 6, 4])



