s = "1113122113"

for _ in range(40):
    ns = ""
    i = 0
    while i < len(s):
        l = s[i]
        j = 0
        for c in s[i:]:
            if c == l:
                j += 1
                continue
            break
        ns += str(j) + str(l)
        i += j
    s = ns

print("Part 1: ", len(s))

s = "1113122113"

from datetime import datetime as dt

start = dt.now()

# NOTE: yikes this really doesn't scale that well. guess string concatenation
# etc is poor in Python
# handling as a list etc would be a better way and joining in the end.

for x in range(50):
    print(x, (dt.now() - start).seconds)
    ns = ""
    i = 0
    while i < len(s):
        l = s[i]
        j = 0
        for c in s[i:]:
            if c == l:
                j += 1
                continue
            break
        ns += str(j) + str(l)
        i += j
    s = ns

print("Part 2: ", len(s))
