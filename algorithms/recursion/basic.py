def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


fact(3)


def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + recursive_sum(arr[1:])


print(recursive_sum([2, 4, 6]))
