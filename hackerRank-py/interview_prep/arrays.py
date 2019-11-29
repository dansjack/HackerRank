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


