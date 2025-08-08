with open("3.txt", "r") as f:
    d = f.read().strip()

v = []
s = 0, 0
for m in d:
    if m == ">":
        s = (s[0] + 1, s[1])
    if m == "<":
        s = (s[0] - 1, s[1])
    if m == "^":
        s = (s[0], s[1] + 1)
    if m == "v":
        s = (s[0], s[1] - 1)
    v.append(s)


print("Part 1: ", len(set(v)))

v = []
s = 0, 0
rs = 0, 0
for i, m in enumerate(d):
    if i % 2 == 0:
        if m == ">":
            s = (s[0] + 1, s[1])
        if m == "<":
            s = (s[0] - 1, s[1])
        if m == "^":
            s = (s[0], s[1] + 1)
        if m == "v":
            s = (s[0], s[1] - 1)
        v.append(s)
    else:
        if m == ">":
            rs = (rs[0] + 1, rs[1])
        if m == "<":
            rs = (rs[0] - 1, rs[1])
        if m == "^":
            rs = (rs[0], rs[1] + 1)
        if m == "v":
            rs = (rs[0], rs[1] - 1)
        v.append(rs)


print("Part 2: ", len(set(v)))
