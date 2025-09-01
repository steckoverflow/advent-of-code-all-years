l = [ord(v) - 96 for v in list("hepxcrrq")]

# NOTE: Just realised if I just convert it to base27 integers it
# Could probably be solved with simple addition.


def increment(ls):
    ls = ls[::-1]
    for i, v in enumerate(ls):
        if i == 0 and v <= 25:
            ls[i] = v + 1
            break
        elif i > 0 and v <= 25:
            ls[i] = v + 1
            j = i - 1
            while j >= 0:
                ls[j] = 1
                j -= 1
            break
    ls = ls[::-1]
    return ls


def three_in_line(ls):
    for i in range(len(ls) - 2):
        if ls[i] + 1 == ls[i + 1] and ls[i] + 2 == ls[i + 2]:
            return True
    return False


def no_iol(ls):
    return 9 not in ls and 15 not in ls and 12 not in ls


def contains_two_pairs(ls):
    for i in range(len(ls) - 3):
        if ls[i] == ls[i + 1]:
            j = i + 2
            while j <= len(ls) - 2:
                if ls[j] == ls[j + 1]:
                    return True
                j += 1
    return False


if __name__ == "__main__":
    x = 0
    while True:
        x += 1
        if x % 10_000 == 0:
            print(x)
        l = increment(l)
        if all([three_in_line(l), no_iol(l), contains_two_pairs(l)]):
            s = "".join([chr(v + 96) for v in l])
            print(s, l)
            break

    # Part two
    while True:
        x += 1
        if x % 10_000 == 0:
            print(x)
        l = increment(l)
        if all([three_in_line(l), no_iol(l), contains_two_pairs(l)]):
            s = "".join([chr(v + 96) for v in l])
            print(s, l)
            break
