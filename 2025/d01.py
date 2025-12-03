# example = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

with open("./2025/d01.txt") as f:
    data = f.read().strip().split("\n")

clicks = 0
rotation_clicks = 0
ts = 50


def psi(i, s, c, rc):
    """process input(input, sum, clicks, rotation_clicks)"""
    d, v = i[:1], int(i[1:])
    v = v * (-1 if d == "L" else 1)
    rc += abs((s + v) // 100)
    s = (s + v) % 100
    if s == 0:
        c += 1
    print(v, c, rc, s)
    return s, c, rc


for e in data:
    ts, clicks, rotation_clicks = psi(e, ts, clicks, rotation_clicks)

print("part 1: ", clicks)
print("part 2: ", rotation_clicks)
