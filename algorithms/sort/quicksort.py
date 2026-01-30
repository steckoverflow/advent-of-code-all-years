def quicksort(arr):
    if len(arr) < 2:
        return arr
    p = arr[0]
    s = []
    b = []
    for v in arr[1:]:
        if v <= p:
            s.append(v)
        else:
            b.append(v)
    return quicksort(s) + [p] + quicksort(b)


print(quicksort([33, 10, 15, 7]))
