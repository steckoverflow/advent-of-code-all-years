with open("8.txt", "rb") as f:
    b = f.readlines()

# x = ",".join(map(lambda x: str(x), list(b))).split("10,")
# bs = [len(v) for v in x]

with open("8.txt", "r") as f:
    d = f.readlines()

print(len(b[0]))
print(len(d[0]))

# print(x)

print(ord("\n"))
print(ord("n"))
