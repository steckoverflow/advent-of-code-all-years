# Binary search
# NOTE: Binary search takes log 2 n vs n steps

from random import choice

lst = [i + 1 for i in range(0, 1000)]

print("Generating a list of 1000 numbers (sorted)")
print("Running Binary search on random number ...")


def binary_search(arr, item):
    no_searches = 0
    low = 0
    high = len(arr) - 1
    while low <= high:
        no_searches += 1
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == item:
            print(f"Found item: {item}, at pos: {mid}. Searches: {no_searches}")
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    print(f"Didn't find item {item}")
    return None


three_random_choices = [choice(lst) for _ in range(0, 3)]

for n_choice in three_random_choices:
    sr = binary_search(lst, n_choice)
    print(f"Random choice: {n_choice}. Outcome: {sr}")
