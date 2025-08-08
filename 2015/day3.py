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
