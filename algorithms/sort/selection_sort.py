def find_smallest(arr):
    smallest_value = arr[0]
    smallest_index = 0
    for i, v in enumerate(arr):
        if v < smallest_value:
            smallest_value = v
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    newArr = []
    copiedArr = list(arr)
    for _ in arr:
        smallest = find_smallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr


print(selection_sort([5, 3, 2, 1, 19, 399]))
